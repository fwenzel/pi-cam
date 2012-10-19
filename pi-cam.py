#!/usr/bin/env python
import subprocess

import browserid
from flask import Flask, abort, jsonify, render_template, request, session

import settings


app = Flask(__name__)
Flask.secret_key = settings.SECRET_KEY

@app.route('/')
def home():
    return render_template('index.html', settings=settings, running=running())


@app.route('/vcontrol', methods=['POST'])
def vcontrol():
    """AJAX action: video controls."""
    controls = {
        'on': server_on,
        'off': server_off,
        'restart': server_restart,
    }
    if request.form['action'] in controls:
        success = controls[request.form['action']]()
        return 'ok' if success else abort(500)
    else:
        abort(400)


@app.route('/authenticate', methods=['POST'])
def authenticate():
    """Authenticate user with Persona."""
    import sys
    sys.stderr.write(settings.SITE_URL)
    data = browserid.verify(request.form['assertion'],
                            settings.SITE_URL)

    # Check against allowed users list
    if data['email'] in settings.ALLOWED_USERS:
        session['email'] = data['email']
        response = jsonify({'message': 'login successful'})
        response.status_code = 200
        return response
    else:
        abort(403)


@app.route('/logout', methods=['POST'])
def logout():
    """Log user out of app."""
    session.pop('email', None)
    response = jsonify({'message': 'logout successful'})
    response.status_code = 200
    return response


# Server controls
def server_on():
    subprocess.Popen(settings.START_SERVER, shell=True)
    return running()

def server_off():
    subprocess.Popen(settings.STOP_SERVER, shell=True)
    return not running()

def server_restart():
    server_off()
    return server_on()

def running():
    """Is server running?"""
    s = subprocess.call(settings.CHECK_SERVER, shell=True)
    return s == 0


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)