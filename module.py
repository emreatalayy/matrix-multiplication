import numpy as np

def solve_from_input():
    num_variables = int(input("Kaç tane değişken var? "))
    A = np.zeros((num_variables, num_variables))
    b = np.zeros(num_variables)
    for i in range(num_variables):
        row = list(map(float, input(f"{i+1}. denklem için katsayıları girin(örnek x1 x2... xn y: ").split()))
        b[i] = row.pop() 
        A[i] = row
    x = solve_system(A, b)
    print("Sonuç:", x)

def solve_from_file(file_name):
    with open(file_name, "r") as f:
        num_variables = int(f.readline())
        A = np.zeros((num_variables, num_variables))
        b = np.zeros(num_variables)
        for i in range(num_variables):
            row = list(map(float, f.readline().split()))
            b[i] = row.pop() 
            A[i] = row
    x = solve_system(A, b)
    print("Sonuç:", x)

def solve_system(A, b):
    x = np.linalg.solve(A, b)
    return x
