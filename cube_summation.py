from operation import Operation
from matrix_utils import MatrixUtils


class CubeSummation(object):
    def __init__(self, input_file):
        self.table_dictionary = {}
        self.input_file = input_file
        self.test_cases_number = int(input_file.readline())

    def calculate(self):
        for i in range(self.test_cases_number):
            matrix_size, operations_number = map(int, self.input_file.readline().split())
            self.table_dictionary.clear()
            for j in range(operations_number):
                line = self.input_file.readline().split()
                current_operation = line[0]
                if Operation.QUERY.value in current_operation:
                    result_query = MatrixUtils.execute_query(line[1:], self.table_dictionary)
                    print(result_query)
                elif Operation.UPDATE.value in current_operation:
                    MatrixUtils.execute_update(line[1:], self.table_dictionary, matrix_size)