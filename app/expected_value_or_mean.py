import matplotlib.pyplot as plt

if __name__ == '__main__':
    '''
    Expected Value 
    '''
    # Roulette game. key is award in $ value is probability to win award
    dic = {0: 0.5, 1: 0.125, 2: 0.25, 10: 0.125}
    play_game_cost = 1
    expected_value = 0
    for k, v in dic.items():
        expected_value += k * v

    prob = tuple(dic.values())
    award = tuple(dic.keys())

    fig, ax = plt.subplots(1, 1)
    ax.plot(award, prob, 'ro', ms=12, mec='blue')
    ax.vlines(award, 0, prob, colors='blue', lw=4)
    plt.plot(expected_value, 0, 'ro')
    plt.ylabel("Winning probability")
    plt.xlabel("Dollars")
    plt.plot(expected_value, 0, 'ro')
    plt.show()

    print("expected value or mean - ", expected_value)
    print("probability award for the each game - ", expected_value - play_game_cost)
