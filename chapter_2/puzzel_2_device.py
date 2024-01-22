from utils.brokendevice import BrokenDevice

device = BrokenDevice(filename='static/22_broken_device_2.txt',
                      input1_switch=[2, 3],
                      input2_switch=[1, 2])

log_output = device.get_log_output()


input_log_lines = {0: {
    'input1': 'YXXYXXYY',
    'input2': 'YXYXXXYX',
    'math_rule': 'G',
    'output_type': 'E',
},
    1: {
    'input1': 'YXYXYXYX',
    'input2': 'YXYXXXYY',
    'math_rule': 'W',
    'output_type': 'E',
}
}

device = BrokenDevice(logs_dict=input_log_lines)
log_output = device.get_log_output()
print(f'The result for puzzel 2 : {log_output}')
