import socket

# URL of this installation.
SITE_URL = 'http://localhost:5000'

## Auth
SECRET_KEY = 'CHANGEME!'  # Fill this in for sessions to work

# Ghetto auth method: List of allowed user emails.
# Auth provided by Persona, so all we need to know is what emails we like.
ALLOWED_USERS = ('johndoe@example.com',)

# Commands to start and stop mjpg streaming server.
START_SERVER = '/usr/bin/mjpg_streamer -i "input_uvc.so --yuv -d /dev/video0  -r 640x480 -f 2" -o "output_http.so -p 8090 -w /dev/null"'
STOP_SERVER = '/usr/bin/killall mjpg_streamer'
CHECK_SERVER = '/bin/ps x | /bin/grep mjpg_streamer | /bin/grep -v grep'  # Exit code 0 if on, >0 otherwise.

# URL of MJPG stream (the image we'll show!)
CAM_SRC = 'http://%s:8090/?action=stream' % socket.gethostname()


# Import local settings file.
try:
	from local_settings import *
except ImportError:
	pass