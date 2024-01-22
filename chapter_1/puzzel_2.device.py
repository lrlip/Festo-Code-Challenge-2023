from utils.brokendevice import BrokenDevice

test_file = 'static/12_first_input.txt'
device = BrokenDevice(filename=test_file)
test_output = device.get_log_output()
print('Test output:', test_output)

second_test_file = 'static/12_second_input.txt'
second_test_device = BrokenDevice(filename=second_test_file)
second_output = second_test_device.get_log_output()
print('seond teset output:', second_output)


final_lines = {0: {
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

final = BrokenDevice(logs_dict=final_lines)

final_output = final.get_log_output()
print('Checkpoint output:', final_output)
