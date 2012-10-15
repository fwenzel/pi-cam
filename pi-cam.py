#!/usr/bin/env python
import subprocess

from flask import Flask, abort, render_template, request

import settings


app = Flask(__name__)


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