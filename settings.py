import socket


# Commands to start and stop mjpg streaming server.
START_SERVER = '/usr/bin/mjpg_streamer -i "input_uvc.so --yuv -d /dev/video0  -r 640x480 -f 2" -o "output_http.so -p 8090 -w /dev/null"'
STOP_SERVER = 'killall mjpg_streamer'
CHECK_SERVER = 'ps x | grep mjpg_streamer | grep -v grep'  # Exit code 0 if on, >0 otherwise.

# URL of MJPG stream
CAM_SRC = 'http://%s:8090/?action=stream' % socket.gethostname()