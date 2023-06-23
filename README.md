# Bruker_GSTC
Here is a guide on how to check the output of Bruker Gradient System Temperature Control (GSTC) through the National Instrument (NI) Data Acquisition (DAQ) board using my Python scripts on Linux (CentOS 7).

Before starting, we need to install NI Linux kernel driver 17.5.1 as the driver that comes with NI DAQmx Base 15 cannot be compiled. You can download it from https://www.ni.com/en-us/support/downloads/drivers/download.ni-kal.html. After that, install NI DAQmx Base 15 from https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx-base.html. Please note that the latest NI DAQmx does not support CentOS 7 and USB-based DAQ.

CentOS 7 has Python 2.7 installed by default, but we need to install Python 3.6 (python3) for this project. Additionally, we need to install PyDAQmx https://pythonhosted.org/PyDAQmx/ and NumPy https://numpy.org/. For GUI, we also need Tkinter (python3-tkinter).
