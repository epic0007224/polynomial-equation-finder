import sympy as sp

def get_matrix_points(y_values):
    matrix_points = []

    for i, y in enumerate(y_values):
        matrix_points.append([])
        for j in range(len(y_values)-1, -1, -1):
            matrix_points[-1].append((i+1)**j)
        matrix_points[-1].append(y)

    return matrix_points

def get_constants(matrix):
    rref = list(matrix.rref()[0])
    constants = [rref[i] for i in range(len(y_values), len(rref), len(y_values)+1)]

    return constants

def create_answer(constants):
    answer = ''
    for i in range(len(y_values)-1, -1, -1):
        num = constants[len(y_values)-1-i]
        if num != 0:
            if i == 0:
                answer += f'{constants[-1]}'
            else:
                answer += f'({num})x^{i} + '

    return answer

if __name__ == '__main__':
    y_values = list(map(int, input('Enter the points: ').split(' ')))
    
    matrix = sp.Matrix(get_matrix_points(y_values))

    constants = get_constants(matrix)
    answer = create_answer(constants)
    print(answer)