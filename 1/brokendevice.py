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

    def __init__(self, filename: str = None,
                 logs_dict: dict = None) -> None:
        self.filename = filename
        self.logs_dict = logs_dict
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
                                   'output_type:': rule_log[3],
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
        bin_out = self.int_to_bin(int_module)
        return bin_out

    def get_log_output(self) -> list:
        log_output = []
        for key in self.logs_dict:
            log = self.logs_dict[key]
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
