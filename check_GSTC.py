#!/usr/bin/env python3

# Python script to check Bruker GSTC for the gradient coil's temperature

# Cecil Chern-Chyi Yen @ NINDS/NIH
# CentOS 7 & Python 3.6

# 6/13/'23 Initial version
# 6/14/'23 Simplfied

from PyDAQmx import *
from numpy import zeros

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

print(round(data[0]*100,2), "degree C")
