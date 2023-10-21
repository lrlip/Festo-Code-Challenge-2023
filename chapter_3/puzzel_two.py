from brokendevice import BrokenDevice

device = BrokenDevice(filename='static/32_broken_final.txt',
                      input1_switch=[2, 3],
                      input2_switch=[1, 2])

log_output = device.get_log_output()
print(log_output)




