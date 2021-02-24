import traceback
import sys

import gi 
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

Gst.init(sys.argv)

# Pipeline to stream the video from camera
pipeline = Gst.parse_launch("nvarguscamerasrc sensor-id=0 ! nv3dsink")
pipeline.set_state(Gst.State.PLAYING)

# Init GObject loop to handle Gstreamer Bus Events 
loop = GObject.MainLoop() 
try: 
    loop.run()
except:
    # Pipeline can be stopped by Ctrl+c
    loop.quit()

pipeline.set_state(Gst.State.NULL)

# Pipeline to save one frame in a jpeg file
pipeline = Gst.parse_launch("nvarguscamerasrc num-buffers=1 ! nvjpegenc ! filesink location=./image.jpg")
pipeline.set_state(Gst.State.PLAYING)

# Init GObject loop to handle Gstreamer Bus Events 
loop = GObject.MainLoop() 
try: 
    loop.run()
except:
    # Pipeline can be stopped by Ctrl+c
    loop.quit()

pipeline.set_state(Gst.State.NULL)
