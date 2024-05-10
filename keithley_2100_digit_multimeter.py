import pyvisa
import time
import numpy as np
# path to folder to save text file measurement data
path_to_folder = 'd:/programs_work/Python/keithley_2100_digit_multimeter/text_file_test/'
# path to text file to save data
path_to_file = path_to_folder + 'keithley_2100_voltage_meas.txt'
# start pyVISA Resource manager
rm = pyvisa.ResourceManager()
print(rm)
# acquire and print possible connections
rm.list_resources()
print(rm.list_resources())
# open USB connection to the Keithley 2100 Digit Multimeter
keithley_inst = rm.open_resource('USB0::0x05E6::0x2100::1408068::INSTR')
# ask identification of Keithley 2100
print(keithley_inst.query("*IDN?"))
# print current voltage with range of 10 Volts and resolution 1 microVolts
##value = keithley_inst.query_ascii_values('MEASure:VOLTage:DC? 10, 0.000001')
##print(value)
# create buffer to store measurement data as numpy array
buffer = np.array([], dtype=float)
# wait time between voltage measurememts in seconds
wait_time = 1.0
# create counter to count measurement
counter = 1
while True:
    # acquire voltage measurements with range 10 Volts and resolution 1 microVolts
    volt_value = keithley_inst.query('MEASure:VOLTage:DC? 1, 0.000001')
    # print type of volt_value, it should be string
    #print(type(volt_value))
    print(float(volt_value))
    if counter == 0:
        # append measurement data to buffer numpy array
        buffer = np.append(buffer, [float(1.0)*wait_time, float(volt_value)])
    else:
        # append measurement data to buffer numpy array
        buffer = np.append(buffer, [float(counter)*wait_time, float(volt_value)])
    #print(buffer)
    # wayt certain amount of time
    time.sleep(wait_time)
    # increase counter
    counter += 1
    # size of buffer numpy array
    buffer_size = np.size(buffer)
    # print buffer size
    #print(buffer_size)
    no_rows =  int(buffer_size / 2)
    # reshape buffer numpy array
    buffer_reshaped = np.reshape(buffer, (no_rows, 2))
    # save reshaped buffer numpy array
    np.savetxt(path_to_file, buffer_reshaped, delimiter='\t')

    
    

