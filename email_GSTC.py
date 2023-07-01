#!/usr/bin/env python3

# Python script to check Bruker GSTC for the gradient coil's temperature
# For crontab, one must set XAUTHORITY=~/.Xauthority DISPLAY=:0

# Cecil Chern-Chyi Yen @ NINDS/NIH
# CentOS 7 & Python 3.6

# 6/13/'23 Initial version
# 6/14/'23 Simplfied the code
# 6/15/'23 Added checking recoStage process
# 6/16/'23 Added reporting overheating
# 6/20/'23 Added email reporting
# 6/21/'23 Added logging temperature
# 6/22/'23 Used tkinter to show dialog
# 6/23/'23 Added closing dialog after 15sec

from os import system
if system("pidof acq_out > /dev/null") != 0: #exist status 0 = At least one program was found with the requested name.
	exit()

from PyDAQmx import *
from numpy import zeros
from datetime import datetime

nsample=1
rate=10.0 #in Hertz
timeout=1.0 #in seconds -1=DAQmx_Val_WaitInfinitely 0=nowait

analog_input = Task()
data = zeros(nsample)

# DAQmx Configure Code
analog_input.CreateAIVoltageChan(b'Dev1/ai0',None,DAQmx_Val_Cfg_Default,0.0,10.0,DAQmx_Val_Volts,None)
analog_input.CfgSampClkTiming(None,rate,DAQmx_Val_Rising,DAQmx_Val_FiniteSamps,nsample)

# DAQmx Start Code
analog_input.StartTask()

# DAQmx Read Code
analog_input.ReadAnalogF64(DAQmx_Val_Auto,timeout,DAQmx_Val_GroupByChannel,data,nsample,int32(),None)

with open('~/GSTC.log', 'a') as f:
	f.write(f'{datetime.now().strftime("%y%m%d%H%M")} {round(data[0]*100,2)}\n')

if data[0]*100 > 40:
	from tkinter import messagebox, Tk
	root = Tk()
	root.withdraw()
	root.after(15000, root.destroy)

	if data[0]*100 > 60:
		from smtplib import SMTP
		try:
			t = SMTP("localhost",25)
			from_email = "nmrsu@localhost"
			to_email = "xxx@xx.xxx"
		except:
			t = SMTP("xxx.xxx.xxx",25)
			from_email = "xxx@xxx.xxx"
			to_email = "xxx2@xxx.xxx"
		t.sendmail(from_email,to_email,'Subject:[Gradient] Overheating\n')
		t.quit()
		try:
			messagebox.showerror("Error", "Gradient temperature is higher than 60C. A report was emailed to xxx. Please stop the scan now!")
		except:
			pass
	else:
		try:
			messagebox.showwarning("Warning", "Gradient temperature is higher than 40C.")
		except:
			pass
