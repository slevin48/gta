import pyvjoy

#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on
j.set_button(15,1)

#Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.


#turn button 15 off again
j.set_button(15,0)

#Set X axis to fully left
j.set_axis(pyvjoy.HID_USAGE_X, 0x1)

#Set X axis to fully right
j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)

#Also implemented:

j.reset()
j.reset_buttons()
j.reset_povs()