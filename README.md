pi-cam
======

A little frontend for mjpg-streamer to turn my Raspberry Pi into a remote webcam.
Written with Flask.


Requirements
------------
* [MJPG-streamer](http://sourceforge.net/projects/mjpg-streamer/) connected to
  a webcam.
* [Flask](http://flask.pocoo.org/)


Settings
--------
Take a look at ``settings.py`` for a list. You can override all settings by
adding a file named ``local_settings.py`` and adding the values in there that
you would like to override.