import math
import matplotlib.pyplot as plt

def expected_value(dic):
    expected_value = 0
    for k, v in dic.items():
        expected_value += k * v
    return expected_value


def squared_difference(dic, ev):
    squared_diff = 0
    for k, v in dic.items():
        squared_diff += (k - ev) ** 2 * v
        # squared_diff += math.pow((k - ev), 2) * v
    return squared_diff


def plot(dic, expected_val, standard_dev):
    # Discrete random variables diagram
    prob = tuple(dic.values())
    award = tuple(dic.keys())

    fig, ax = plt.subplots(1, 1)
    ax.plot(award, prob, 'ro', ms=12, mec='blue')
    ax.vlines(award, 0, prob, colors='blue', lw=4)
    plt.ylabel("Winning probability")
    plt.xlabel("Dollars")
    plt.plot(expected_val, 0, 'ro')
    # Show DISPERSION on the chart
    ax.hlines(y=-0.005, xmin=expected_val - standard_dev, xmax=expected_val + standard_dev, linewidth=2, color='b')
    plt.show()


if __name__ == '__main__':
    # Roulette game. key is award in $ value is probability to win award
    dic = {0: 0.5, 1: 0.125, 2: 0.25, 10: 0.125}

    ev = expected_value(dic)
    #     r = (0 - 1.875) ** 2 * 0.5 + (1 - 1.875) ** 2 * 0.125 + (10 - 1.875) ** 2 * 0.125 + (2 - 1.875) ** 2 * 0.25
    squared_diff = squared_difference(dic, ev)
    # Standard deviation or "dispersion"
    standard_deviation = math.sqrt(squared_diff)

    print('expected value', ev)
    print('square difference', squared_diff)
    print('Standard deviation or "dispersion"', standard_deviation)

    plot(dic, ev, standard_deviation)
