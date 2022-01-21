import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

def main():
    x = np.arange(-5, 5, 0.5)
    f = lambda x:1 + np.sin(x)**2
    a = -1*np.pi/2
    b = np.pi/2 - 1;

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 4

    int_f_a_b = trapezoidal(f, a, b, n)

def trapezoidal(f, a, b, n):
    # Trapezoidal Rule
    h = (b - a)/n
    x = np.linspace(a, b, n+1)
    int_apx = (h/2)*(f(x[0]) + np.sum(2*f(x[1:-1])) + f(x[-1]))

    #  plotting
    xv = np.linspace(a, b, 100)
    plt.scatter(x, f(x), c="red", zorder=2.5)
    plt.plot(xv, f(xv))
    ax = plt.gca();
    for i in range(n):
        xi = [x[i], x[i], x[i+1], x[i+1]]
        yi = [0 , f(x[i]), f(x[i+1]), 0]
        ax.add_patch(patches.Polygon(xy=list(zip(xi,yi)), facecolor="lightgray", edgecolor="black"))
    plt.axis("scaled")

    print(f"Integral of f(x) with x from {a} to {b}:\n{int_apx}\n")
    plt.show()

    return int_apx
    

if __name__ == "__main__":
    main()
