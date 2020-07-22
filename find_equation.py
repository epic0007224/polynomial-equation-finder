import sympy as sp

def get_matrix_points():
    matrix_points = []

    for i in range(len(x_values)):
        matrix_points.append([])
        for j in range(len(x_values)-1, -1, -1):
            matrix_points[-1].append(x_values[i]**j)
        matrix_points[-1].append(y_values[i])

    return matrix_points

def get_constants(matrix):
    rref = list(matrix.rref()[0])
    constants = [rref[i] for i in range(len(x_values), len(rref), len(x_values)+1)]

    return constants

def create_answer(constants):
    answer = ''
    for i in range(len(x_values)-1, -1, -1):
        num = constants[len(x_values)-1-i]
        if num != 0:
            if i == 0:
                answer += f'{constants[-1]}'
            else:
                answer += f'({num})x^{i} + '

    return answer

def find_polynomial():
    matrix = sp.Matrix(get_matrix_points())

    constants = get_constants(matrix)
    answer = create_answer(constants)

    return answer

if __name__ == '__main__':
    global x_values
    global y_values
    x_values = list(map(int, input('Enter the x values: ').split(' ')))
    y_values = list(map(int, input('Enter the y values: ').split(' ')))
    
    answer = find_polynomial()
    print(answer)
