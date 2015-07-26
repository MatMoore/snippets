"""
Plot of the probability of winning the UK lottery jackpot at least once with
multiple tickets, either entering the same draw multiple times, or entering
multiple draws once.

To win the jackpot you need all 6 picks to match the numbers drawn, at odds of
1:13,983,816.

(Source: https://www.national-lottery.co.uk/games/lotto/game-procedures#int_win)

This comparison does not take into account expected winnings, which may include
winning from lesser prize categories.
"""
from matplotlib import pyplot
from numpy import logspace

n = logspace(0, 6)
p = 1 / 13983817.0
spread_chance = 1 - (1 - p) **n
single_chance = p * n
pyplot.xkcd()
pyplot.xlabel('Number of tickets')
pyplot.ylabel('Probability of jackpot')
pyplot.plot(n, single_chance, 'r-', n, spread_chance, 'b-')
pyplot.legend(['Same draw = p*n', 'Different draws = 1-(1-p)^n'])
pyplot.show()
