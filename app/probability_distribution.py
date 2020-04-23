import itertools
import matplotlib.pyplot as plt


def plot(dict):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    sample_outcomes = dict.keys()
    probabilities = dict.values()
    ax.bar(sample_outcomes, probabilities)
    plt.ylabel('Probability')
    plt.xlabel('Event outcomes')
    plt.show()


if __name__ == '__main__':

    # all combinations for 3 coin flips
    # ('H', 'H', 'H'),
    # ('H', 'H', 'T'),
    # ('H', 'T', 'H'),
    # ('H', 'T', 'T'),
    # ('T', 'H', 'H'),
    # ('T', 'H', 'T'),
    # ('T', 'T', 'H'),
    # ('T', 'T', 'T')
    coin_flips = list(itertools.product("HT", repeat=3))

    h0, h1, h2, h3 = 0, 0, 0, 0
    for i in coin_flips:
        if i.count('H') == 0: h0 += 1
        if i.count('H') == 1: h1 += 1
        if i.count('H') == 2: h2 += 1
        if i.count('H') == 3: h3 += 1

    h0_p, h1_p, h2_p, h3_p = h0 / len(coin_flips), h1 / len(coin_flips), h2 / len(coin_flips), h3 / len(coin_flips)

    dict = {'Zero H': h0_p, 'H': h1_p, 'HH': h2_p, 'HHH': h3_p}
    print(dict)
    plot(dict)
