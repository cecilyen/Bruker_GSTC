# Bruker_GSTC
Here is a guide on how to check the output of Bruker Gradient System Temperature Control (GSTC) through the National Instrument (NI) Data Acquisition (DAQ) board using my Python scripts on Linux (CentOS 7).

Before starting, we need to install NI Linux kernel driver 17.5.1 as the driver that comes with NI DAQmx Base 15 cannot be compiled. You can download it from https://www.ni.com/en-us/support/downloads/drivers/download.ni-kal.html. After that, install NI DAQmx Base 15 from https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx-base.html. Please note that the latest NI DAQmx does not support CentOS 7 and USB-based DAQ.

CentOS 7 has Python 2.7 installed by default, but we need to install Python 3.6 (python3) for this project. Additionally, we need to install PyDAQmx https://pythonhosted.org/PyDAQmx/ and NumPy https://numpy.org/. For popping up warning dialogue, we also need Tkinter (python3-tkinter).

It's important to note that the output voltage of the GTSTC is scaled to 1 volt/degree C. Therefore, under normal operation, the voltage may exceed NI's input range, which is from -10V to +10V. To address this, we will need to use a voltage divider to lower the output to 1/10 before connecting it to the input port of the NI DAQ.
