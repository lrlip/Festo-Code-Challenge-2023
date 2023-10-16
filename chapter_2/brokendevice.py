OUTPUT_EXPR_CODE = {'Q': 'binary',
                    'E': 'number'}


MATH_EXPR_CODE = {'G': 'add',
                  'L': 'substract',
                  'W': 'multiply',
                  }


class BrokenDevice(object):

    output_expr = {'binary', 'out_binary'}

    math_exprs = {
        "add": lambda x, y: x + y,
        'substract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y
    }

    def __init__(self,
                 filename: str = None,
                 input1_switch: list = None,
                 input2_switch: list = None,
                 logs_dict: dict = None) -> None:
        self.filename = filename
        self.logs_dict = logs_dict
        self.input1_switch = input1_switch
        self.input2_switch = input2_switch
        if self.filename != None:
            self.logs_dict = self.import_rules()

    def import_rules(self) -> list:
        """Import the trap balanced"""

        rules_list = {}
        with open(self.filename, 'r') as f:
            for idx, line in enumerate(f):
                remove_in_output = line.replace(
                    'input: ', '').replace('output: ', '').strip()
                rule_log = remove_in_output.split('; ')
                rules_list[idx] = {'input1': rule_log[0],
                                   'input2': rule_log[1],
                                   'math_rule': rule_log[2],
                                   'output_type': rule_log[3],
                                   'output': rule_log[4],
                                   }

        return rules_list

    def decode_log_line(self, log: dict) -> str:
        """Decode a single log line

        Args:
            log (dict): dict containing the log

        Returns:
            str: output of the logline
        """
        bin1 = self.txt_to_bin(log['input1'])
        bin2 = self.txt_to_bin(log['input2'])

        int1 = self.bin_to_int(bin1)
        int2 = self.bin_to_int(bin2)

        # based on the math rule get the output in int
        int_out = self.math_exprs[MATH_EXPR_CODE[log['math_rule']]](int1, int2)

        int_module = self.get_modulus(int_out)
        # Change the output to binary
        if log['output_type'] == 'Q':
            output = self.int_to_bin(int_module)
        elif log['output_type'] == 'E':
            output = int_module
        else:
            output = None
        return output

    def get_log_output(self) -> list:
        log_output = []
        for key in self.logs_dict:
            log = self.logs_dict[key]
            # self.switch_input_2(log['input_1'], 0, 2)
            if self.input1_switch:
                log['input1'] = self.switch_input(
                    log['input1'],
                    self.input1_switch[0],
                    self.input1_switch[1]
                )
            if self.input2_switch:
                log['input2'] = self.switch_input(
                    log['input2'],
                    self.input2_switch[0],
                    self.input2_switch[1]
                )
            decode_line = self.decode_log_line(log)
            log_output.append(decode_line)
        return log_output

    @staticmethod
    def txt_to_bin(string):
        binary = string.replace('X', '0').replace('Y', '1')
        return binary

    @staticmethod
    def bin_to_int(binary: str) -> int:
        return int(binary, 2)

    @staticmethod
    def int_to_bin(integer: int) -> bin:
        return format(integer, 'b')

    @staticmethod
    def get_modulus(integer):
        return integer % 256

    @staticmethod
    def switch_input(input: str,
                     cable_1: int,
                     cable_2: int) -> str:
        value_1 = input[cable_1]
        value_2 = input[cable_2]
        input2 = input[:cable_1] + value_2 + input[cable_1+1:]
        input3 = input2[:cable_2] + value_1 + input2[cable_2+1:]
        return input3
