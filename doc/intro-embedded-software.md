# Working with TIS embedded cameras on NVIDIA® Jetson platform

## Overview
This introduction is intended to get an overview of the interaction of the different software components involved in working with The Imaging Source embedded camera modules on the Jetson platform.

This document covers the following topics:

 * Device drivers provided by The Imaging Source
 * Application Programming Interfaces (API) used to control the camera modules
 * Application frameworks optimized for the NVIDIA® Jetson platform
 * Getting started with machine vision programming on the NVIDIA® Jetson platform


### The Imaging Source Sensor and Interface Drivers

The sensor modules require device drivers to funktion. You can download precompiled drivers for different NVIDIA® JetPack versions from the [The Imaging Source Website](https://www.theimagingsource.com/support/downloads-for-linux/). Interface drivers required to utilize The Imaging Source FPD-Link-III interfaces are also part of the same driver package.

The precompiled drivers are delivered in the Debian package format and could be installed easily with the package manager, for example by double clicking the downloaded package in the file manager.

### Application Programming Interfaces for The Imaging Source Embedded Sensor Modules

The Imaging Source sensor modules integrate into the software infrastructure provided by NVIDIA® with the NVIDIA® JetPack SDK. This SDK controls the sensor modules via different programming interfaces:

 * [Video-4-Linux-2 (v4l2)](https://linuxtv.org/downloads/v4l-dvb-apis/driver-api/v4l2-core.html) for low-level interaction with the sensor module, like setting the exposure time and sensor gain values directly or capturing unprocessed raw video data from the imager. The v4l2 API is provided by the Linux kernel as an interface for the 'C' programming language.

 * [Jetson Multimedia API](https://docs.nvidia.com/jetson/l4t-multimedia/index.html) for low level application development utilizing Tegra hardware components to accelerate vision and image processing procedures. The Jetson Multimedia API is provided as an interface for the 'C++' programming language.

 * [GStreamer](https://gstreamer.freedesktop.org/) is a library for high level application development. The components provided by NVIDIA® for JetPack build upon the Jetson Multimedia API to utilize the hardware accellerated components provided by the Tegra platform. GStreamer provides bindings for most common programming languages.


### Application frameworks optimized for the NVIDIA® Jetson platform

NVIDIA® provides several frameworks optimized for the NVIDIA® Jetson platform to aid resourceful development. These frameworks are installed along with the latest NVIDIA® JetPack SDK:

 * [VisionWorks](https://developer.nvidia.com/embedded/visionworks) is a software development package for Computer Vision (CV) and image processing.

 * [VPI (Vision Programing Interface)](https://developer.nvidia.com/embedded/vpi), a software library that provides Computer Vision / Image Processing algorithms implemented on PVA2 (Programmable Vision Accelerator), GPU and CPU. *PVA is available only on Jetson AGX Xavier series and Jetson Xavier NX*

 * [DeepStream SDK](https://developer.nvidia.com/deepstream-sdk) delivers a complete streaming analytics toolkit for AI-based multi-sensor processing, video, audio and image understanding.

## Getting started with machine vision programming on the NVIDIA® Jetson platform

The Imaging Source provides programming examples to help you getting started with your application development. The examples could be found on this [public GitHub repository](https://github.com/TheImagingSource/nvidia-jetson-samples/tree/master/examples).

To help achieving the best possible performance out of the NVIDIA® Jetson platform, NVIDIA® has created the [Accelerated GStreamer Guide](https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/accelerated_gstreamer.html).

