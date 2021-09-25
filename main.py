import random
import numpy as np

ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["D", "H", "C", "S"]
cards = []

for r, s in [(r, s) for s in suits for r in ranks]:
    cards.append(r+s)
print(cards)

deck = cards
random.shuffle(deck)

print(deck)


no_players = int(input("how many players are there?"))
players = []
for i in range(no_players):
    players.append([])
print(players)


def deal(n, who):
    for a, b in [(a, b)for a in range(n) for b in who]:
        players[b].append(deck.pop(0))


deal(7, [0, 1])
print(players)
print(deck)
