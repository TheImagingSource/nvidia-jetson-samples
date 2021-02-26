
# Working with TIS embedded cameras on NVIDIA® Jetson platform

## Overview
This introduction is intended to get an overview of the interaction of the different software components involved in working with our embedded camera modules on the Jetson platform.

## Kernel driver
The Imaging Source offers kernel mode drivers for the Jetson platform that provide access to the the embedded cameras through the Jetson camera infrastructure. The drivers can be downloaded [here](https://www.theimagingsource.com/support/downloads-for-linux/device-drivers/mipicameradriverjetson45/). Due to limitations within the L4T-kernel (Linux4Tegra), the video device provided by the driver only offers basic properties like exposure and gain. 

## Video4Linux (v4l2)
Video4Linux (v4l2) is the standard API for video capturing on Linux systems. It is used for controlling camera devices as well as streaming data from them. General information regarding v4l2 (Video4Linux2) can be found [here](https://linuxtv.org/downloads/v4l-dvb-apis/). Information on the specifics of NVIDIAs v4l2 extension can be found [here](https://docs.nvidia.com/jetson/l4t-multimedia/group__ee__extensions__group.html). Setting the raw exposure time of TIS embedded cameras can thus be done through the v4l2 API, or e.g. from a console with the command `v4l2-ctl -c exposure=10000`, see also [here](https://manpages.debian.org/stretch/v4l-utils/v4l2-ctl.1).

## GStreamer
GStreamer is an open-source multimedia framework widely available on Linux systems. NVIDIA heavily relies and builds upon GStreamer on the Jetson platform. General information on GStreamer can be found [here](https://gstreamer.freedesktop.org/). GStreamer provides many ready-to-use elements encapsulating other APIs. They can be easily combined to so-called *pipelines*, like the examples below. Pipelines can be started for instance from a terminal using `gst-launch1.0`.

### Accelerated GStreamer
NVIDIA provides a broad set of GStreamer modules specifically designed to exploit the hardware of the Jetson platform; detailed information can be found [here](https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/accelerated_gstreamer.html). The most relevant one in this context is `nvarguscamerasrc` , as it allows for streaming from the embedded cameras and processing the image data in the ISP, see also [here](https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/accelerated_gstreamer.html#wwpID0E0LR0HA). A basic GStreamer pipeline displaying the camera stream in a window would be `nvarguscamerasrc ! nv3dsink`.

#### Working with mono sensors
The ISP built into the Jetson is specifically designed for bayer sensors. As a consequence,  mono sensors are not naturally supported by the ISP. However, there is a simple workaround for this limitation. The debayering of mono data (not containing a bayer pattern) involuntarily leads to unwanted color artifacts, which can be virtually removed by setting the saturation to 0. An example pipeline would be `nvarguscamerasrc saturation=0 ! nv3dsink`