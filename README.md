# Interactive_Art_v1
 Project of interactive visual and sonor experiences loosely based on deep learning.

 ## The goal
 My goal in this project is to create a number of "experiences" where sound and image vary following what is seen by a webcam. 

 I am creating a bunch of modules that can easily be combined to create new experiences. Some of those are based on deep learning algorithm like Yolo_v3 that I took from existing repos on Github.

## The experiences
 Right now we have:
  - The default experience from which all the other inherit
  - Basic_Experience (A blanck experience used as a reference when creating other ones) 
  - Sweet Arpegio
  - Sweet Dawn
  - SweetVCV (This one outputs midi data and I use VCV Rack to make music out of it)
  - Joconde (Try stuff with Haar Cascades)


## The modules
 Right now we have:
  - The base treaded module from which all the other should inherit 
  - Midi output module
  - speech recgnition module 
  - Tracking module
  - Haar cascade module to detect face element (it's so bad its good)
  - Yolo v3 (I will redo it myself soon because now its just a copy of somemone elses implementation) 


## Requierements
If you want all the modules to work thi should do: 
 - python 3.7.4
 - Tensorflow 1.15.0
 - Keras 2.3.1
 - numpy
 - cv2
 - PIL
 - mido
 - simpleaudio

 - PyAudio
 - speech_recognition 






