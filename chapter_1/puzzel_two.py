from cosmo_plaza.brokendevice import BrokenDevice

device = BrokenDevice(filename='cosmo_plaza/12_first_input.txt')

log_output = device.get_log_output()

input_log_lines = {0: {
    'input1': 'YXXXXYXY',
    'input2': 'XXXXXYXY',
    'math_rule': 'G',
    'output_type': 'Q',
},
    1: {
    'input1': 'YXXXYXYX',
    'input2': 'YYYXXXXX',
    'math_rule': 'L',
    'output_type': 'Q',
}
}
print(log_output)
device = BrokenDevice(logs_dict=input_log_lines)
log_output = device.get_log_output()
print(log_output)
