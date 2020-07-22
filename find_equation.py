import sympy as sp

class FindPolynomial:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        
    def get_matrix_points(self):
        matrix_points = []

        for i in range(len(self.x_values)):
            matrix_points.append([])
            for j in range(len(self.x_values)-1, -1, -1):
                matrix_points[-1].append(self.x_values[i]**j)
            matrix_points[-1].append(self.y_values[i])

        return matrix_points

    def get_constants(self, matrix):
        rref = list(matrix.rref()[0])
        constants = [rref[i] for i in range(len(self.x_values), len(rref), len(self.x_values)+1)]

        return constants

    def create_answer(self, constants):
        answer = ''
        for i in range(len(self.x_values)-1, -1, -1):
            num = constants[len(self.x_values)-1-i]
            if num != 0:
                if i == 0:
                    answer += f'{constants[-1]}'
                else:
                    answer += f'({num})x^{i} + '

        return answer

    def find(self):
        matrix = sp.Matrix(self.get_matrix_points())

        constants = self.get_constants(matrix)
        answer = self.create_answer(constants)

        return answer

if __name__ == '__main__':
    x_values = list(map(int, input('Enter the x values: ').split(' ')))
    y_values = list(map(int, input('Enter the y values: ').split(' ')))
    
    answer = FindPolynomial(x_values, y_values).find()
    print(answer)
