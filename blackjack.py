# File: Blackjack.py

# Description: Program that allows the user to play blackjack

# Student's Name: Vinayak Sahal

# Student's UT EID: vs9736

# Course Name: CS 313E

# Unique Number: 50725

# Date Created: 2/24/19

# Date Last Modified: 2/25/2019

import random

# Card class from Poker with some changes
class Card():
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
  SUITS = ('C', 'D', 'H', 'S')

  def __init__(self, rank=12, suit='S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__(self):
    if (self.rank == 1):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str(self.rank)

    return (rank + self.suit)

  def __eq__(self, other):
    return (self.rank == other.rank)

  def __ne__(self, other):
    return (self.rank != other.rank)

  def __lt__(self, other):
    return (self.rank < other.rank)

  def __le__(self, other):
    return (self.rank <= other.rank)

  def __gt__(self, other):
    return (self.rank > other.rank)

  def __ge__(self, other):
    return (self.rank >= other.rank)

# Deck class
class Deck():
  def __init__(self, num_decks=1):
    self.deck = []
    for i in range(num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card(rank, suit)
          self.deck.append(card)

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

# Player class from Poker with some changes
class Player():
  def __init__(self, cards):
    self.cards = cards

  def hit(self, card):
    self.cards.append(card)

  def get_points(self):
    count = 0
    for card in self.cards:
      if (card.rank > 9):
        count += 10
      elif (card.rank == 1):
        count += 11
      else:
        count += card.rank

    for card in self.cards:
      if (count <= 21):
        break
      elif (card.rank == 1):
        count = count - 10

    return count

  # checks if there is blackjack
  def has_blackjack(self):
    return (len(self.cards) == 2) and (self.get_points() == 21)

  def __str__(self):
    hand = ''
    points = self.get_points()
    for card in self.cards:
      hand = hand + str(card) + ' '

    pointStr = '- ' + str(points) + ' points'

    return (hand + pointStr)


# Dealer class inherits Player class
class Dealer(Player):
  def __init__(self, cards):
    Player.__init__(self, cards)
    self.show_one_card = True

  def hit(self, deck):
    self.show_one_card = False
    while (self.get_points() < 17):
      self.cards.append(deck.deal())

  def __str__(self):
    if (self.show_one_card):
      return str(self.cards[0])
    else:
      return Player.__str__(self)

# Blackjack class checks if players have blackjack
class Blackjack():
  def __init__(self, num_players=1):
    self.deck = Deck()
    self.deck.shuffle()

    self.num_players = num_players
    self.player_list = []

    for i in range(self.num_players):
      player = Player([self.deck.deal(), self.deck.deal()])
      self.player_list.append(player)

    self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

  def play(self):
    print()
    for i in range(self.num_players):
      print('Player ' + str(i + 1) + ' : ' + str(self.player_list[i]))

    print('Dealer : ' + str(self.dealer))

    # goes through all the players and checks for blackjack and asks to hit
    player_points = []
    for i in range(self.num_players):
      print()
      while True:
        choice = input('Player ' + str(i + 1) + ', do you want to hit? [y / n]: ')
        if choice in ('y', 'Y'):
          (self.player_list[i]).hit(self.deck.deal())
          points = (self.player_list[i]).get_points()
          print('Player ' + str(i + 1) + ' : ' + str(self.player_list[i]))
          if (points >= 21):
            break
            print()
        else:
          break
          print()
      player_points.append((self.player_list[i]).get_points())

    self.dealer.hit(self.deck)
    dealer_points = self.dealer.get_points()
    print()
    # print('Dealer : ' + str(self.dealer) + ' - ' + str(dealer_points))
    print('Dealer :' + str(self.dealer), '\n')
    print()

    # checks to see who won
    for i in range(self.num_players):
      if (player_points[i] > 21):
        print('Player ' + str(i + 1) + ' loses')
      elif (self.player_list[i].has_blackjack() or dealer_points > 21):
        print('Player ' + str(i + 1) + ' wins')
      elif (self.dealer.has_blackjack()):
        print('Player ' + str(i + 1) + ' loses')
      elif (dealer_points <= 21) and (dealer_points > player_points[i]):
        print('Player ' + str(i + 1) + ' loses')
      elif (dealer_points < player_points[i] and player_points[i] <= 21):
        print('Player ' + str(i + 1) + ' wins')
      elif (dealer_points == player_points[i]):
        print('Player ' + str(i + 1) + ' ties')


def main():
  num_players = int(input('Enter number of players: '))
  while ((num_players < 1) or (num_players > 6)):
    num_players = int(input('Enter number of players: '))

  game = Blackjack(num_players)

  game.play()


main()
