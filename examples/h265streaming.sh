#!/usr/bin/env bash
xfce4-terminal -e 'bash -c "echo h265 streaming can be stopped with Ctrl+C;echo Start streaming by pressing ENTER;read;gst-launch-1.0 -v nvarguscamerasrc ! nvv4l2h265enc ! h265parse config-interval=-1 ! rtph265pay ! udpsink host=239.0.0.1 port=5000; bash"'
