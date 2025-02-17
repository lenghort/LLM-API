import matplotlib.pyplot as plt
import numpy as np
import re

def parse_input(user_input):
    """Extracts function type and interval from user input."""
    match = re.search(r'(sin|cos|x\^2|x) on (-?\d+) to (-?\d+)', user_input)
    if match:
        function, x_min, x_max = match.groups()
        return function, int(x_min), int(x_max)
    return None, None, None

def plot_function(function, x_min, x_max):
    """Plots the requested function."""
    x = np.linspace(x_min, x_max, 400)
    
    if function == 'x':
        y = x
    elif function == 'x^2':
        y = x**2
    elif function == 'sin':
        y = np.sin(x)
    elif function == 'cos':
        y = np.cos(x)
    else:
        print("Unsupported function.")
        return
    
    plt.plot(x, y)
    plt.title(f"Plot of {function} from {x_min} to {x_max}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

def main():
    while True:
        user_input = input("Enter your graph request (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you – that’s it for today, bye!")
            break
        
        function, x_min, x_max = parse_input(user_input)
        if function:
            plot_function(function, x_min, x_max)
        else:
            print("Sorry, I didn't understand. Try something like: 'Plot sin on -5 to 5'.")

if __name__ == "__main__":
    main()
