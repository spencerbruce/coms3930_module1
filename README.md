# COMS 3930: Creative Embedded Systems
## Module 1 (Generative Art)
## Spencer Bruce (sgb2145)

I have uploaded, along with this README, a Processing program and a Python program.
I ran these programs on a Rapsberry Pi 4 Model B with a 8-NeoPixel LED ring attached.
To control the Raspberry Pi, I used VNC Viewer Remote Desktop to use my iPad as a remote display.
The art was on display in my bedroom window facing the inner shaft/courtyard of my building, of which I can only get an outside view from my kitchen window due to COVID.

My generative tracks the movement of the sun and moon, with the NeoPixel LED ring
displaying your location's sun/moon, and the iPad/display showing what the opposite side
of the world may see. When the moon is up, the sun may be setting in across the Earth from
you.

The installation on display can be seen here: https://youtu.be/c8yHNITInxo

# Running Processing on Boot
Thanks to help and suggestions from the course Discord, I was able to find the
Rapsbian `autostart` file at `/etc/xdg/lxsession/LXDE-pi/autostart`. I was able to
add the following line to the end of this file to get my Processing program to start
when the Pi boots up: `/usr/local/bin/processing-java --sketch=/home/pi/Desktop/embedded-systems/sunrise --run`

# Running Python Script on Boot
To get my Python program to run from start, I modified  the `rc.local` file at `/etc/rc.local`. By adding the following line directing Raspbian to my Python script,
the NeoPixels light up on boot: `sudo python2 /home/pi/Desktop/embedded-systems/neopixels.py`. These paths can be adjusted based on your setup's needs!

# Dependencies
In order to run my program, one needs Processing, a Raspberry Pi, and an external
monitor and keyboard. I chose to use VNC Viewer (www.realvnc.com) for both an external monitor and keyboard. VNC Viewer is a multi-platform remote desktop that allows me to remotely control the Pi from any device.

This project requires Processing for Raspberry Pi to run (https://pi.processing.org/download/). For my Python script, I used the Sunrise-Sunset web API (https://sunrise-sunset.org/api) to collect the current latitude and longitude's sunrise, sunset, and day
length for the LED lights. For Processing, I referenced the following sites to learn
how to create gradient circles from scratch:

- https://behreajj.medium.com/color-gradients-in-processing-v-2-0-e5c0b87cdfd2
- https://www.openprocessing.org/sketch/106094
- https://processing.org/examples/lineargradient.html
