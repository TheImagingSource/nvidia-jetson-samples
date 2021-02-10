#!/usr/bin/env bash
xfce4-terminal -e 'bash -c "echo Live image can be stopped with Ctrl+C;echo Start live view by pressing ENTER;read;gst-launch-1.0 nvarguscamerasrc sensor-id=0 ! queue ! nv3dsink; bash"'
