GeoCar - PSoC Tracker
===========
![Alt text](/ext/GeocarLogo.jpg?raw=true)

Plotting data from psoc and gps into a map

Simple Django project to plot data collected by a microcontroller in a car.
The microcontroller records GPS and accelerometer data every 5 seconds into a local SDCard. 
Then that data is pulled out of the SDCard via bluetooth and posted to this project.

A few python scripts are used to connect bluetooth to the board (Serial Connection) and pulls data.
Data is parsed and posted by using a Restfull service.

Project on element14: GeoCar.
