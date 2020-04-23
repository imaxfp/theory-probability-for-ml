import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Continues random variables diagram
    # Range can be from "-infinity" to "+infinity", Can be select any float point from the range
    x_cords = range(-500, 500)
    y_cords = [x * x for x in x_cords]

    plt.scatter(x_cords, y_cords)
    plt.show()

    # Discrete random variables diagram
    pk = (2, 4, 8)
    fig, ax = plt.subplots(1, 1)
    ax.plot(np.arange(3), pk, 'ro', ms=12, mec='blue')
    ax.vlines(np.arange(3), 0, pk, colors='blue', lw=4)
    plt.show()