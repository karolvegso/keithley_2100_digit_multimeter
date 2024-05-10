# keithley_2100_digit_multimeter
This simple code opens communication with Keithley 2100 digit multimeter using pyVISA and continuously reads voltage values. 

This simple program opens communication with the Keithely 2100 digital multimeter using pyVISA. My example code includes a USB interface. I use a continuous while loop to query for voltage values using the 'MEASure:VOLTage:DC? 1, 0.000001' command. I continuously save measured voltage values to the text file.
