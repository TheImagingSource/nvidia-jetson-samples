#!/usr/bin/env bash
xfce4-terminal -e 'bash -c "echo h264 streaming can be stopped with Ctrl+C;echo Start streaming by pressing ENTER;read;gst-launch-1.0 -v nvarguscamerasrc ! nvv4l2h264enc ! h264parse config-interval=-1 ! rtph264pay ! udpsink host=239.0.0.1 port=5000; bash"'
