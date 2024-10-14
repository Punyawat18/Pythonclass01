import sympy
from sympy.abc import x, y
import sympy.functions

def main():
    func = int(input("which func u want 1,2,3,4: "))
    if func == 1:
        first_func()
    elif func == 2:
        second_func()
    elif func == 3:
        third_func()
    elif func == 4:
        forth_func()


def first_func():
    x = float(input("x: "))
    a = float(input("step: "))
    count = 0
    print("count =", count, "x =", x)
    while True:
        x = x - (a * cal_for_first_func(x))
        count = count + 1
        print("count =", count, "x =", x)
        if x == x - (a * cal_for_first_func(x)):
            print("Done")
            quit()

def second_func():
    func = input("function : ")
    deri_function = find_deri_onevar(func)
    x = float(input("x: "))
    a = float(input("step: "))
    count = 0
    print("count =", count, "x =", x)
    while True:
        x = x - (a * cal_for_second(deri_function, x))
        count = count + 1
        print("count =", count, "x =", x)
        if x == x - (a * cal_for_second(deri_function, x)):
            print("Done")
            quit()

def third_func():
    x = float(input("x: "))
    y = float(input("y: "))
    a = float(input("step: "))
    xy = cal_for_third_func(x, y)
    count = 0
    print("count =", count, xy)
    while True:
        xy['x'] = xy['x'] - (a * cal_for_third_func(xy['x'], xy['y'])['x'])
        xy['y'] = xy['y'] - (a * cal_for_third_func(xy['x'], xy['y'])['y'])
        count = count + 1
        print("count =", count, xy)
        if xy['x'] == xy['x'] - (a * cal_for_third_func(xy['x'], xy['y'])['x']) and xy['y'] == xy['y'] - (a * cal_for_third_func(xy['x'], xy['y'])['y']):
            print("Done")
            quit()
            
def cal_for_first_func(x):
    result = (2 * x) + 1
    return result

def cal_for_second(func, y):
    new_func = sympy.lambdify(x, func)
    result = float(new_func(y))
    return result

def cal_for_third_func(x, y):
    result = {'x' : (2 * (x - 2)), 'y' : (4 * (y - 3))}
    return result


def find_deri_onevar(func):
    x = sympy.symbols('x')
    result = sympy.Derivative(func, x, evaluate=True)
    return str(result)

def forth_func():
    func_input = input("Enter a function of x and y (e.g., x**2 + y**2): ")
    func = sympy.sympify(func_input)

    deri_x = find_derivative(func, x)
    deri_y = find_derivative(func, y)

    x_val = float(input("Initial x: "))
    y_val = float(input("Initial y: "))
    step_size = float(input("Step size: "))
    
    count = 0
    threshold = 1e-6

    while True:
        grad_x = cal_for_gradient(deri_x, x_val, y_val)
        grad_y = cal_for_gradient(deri_y, x_val, y_val)
        
        new_x = x_val - step_size * grad_x
        new_y = y_val - step_size * grad_y
        
        print(f"Iteration {count}: x = {new_x}, y = {new_y}, grad_x = {grad_x}, grad_y = {grad_y}")

        if abs(new_x - x_val) < threshold and abs(new_y - y_val) < threshold:
            print("Converged!")
            break
        
        x_val, y_val = new_x, new_y
        count += 1

def cal_for_gradient(derivative, x_val, y_val):
    func = sympy.lambdify((x, y), derivative)
    return func(x_val, y_val)

def find_derivative(func, var):
    return sympy.Derivative(func, var, evaluate=True)

main()