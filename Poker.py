#  File: Poker.py

#  Description: Program plays Poker (5 card hand)

#  Student's Name: Vinayak Sahal

#  Student's UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/17/19

#  Date Last Modified:

import random


class Card():
  RANKS = (2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14)
  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__(self, rank=12, suit='S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__(self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str(self.rank)

    return rank + self.suit

  # equality tests
  def __eq__(self, other):
    return self.rank == other.rank

  def __ne__(self, other):
    return self.rank != other.rank

  def __lt__(self, other):
    return self.rank < other.rank

  def __le__(self, other):
    return self.rank <= other.rank

  def __gt__(self, other):
    return self.rank > other.rank

  def __ge__(self, other):
    return self.rank >= other.rank


class Deck():

  # constructor
  def __init__(self, num_decks=1):
    self.deck = []
    for i in range(num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card(rank, suit)
          self.deck.append(card)

  # shuffles deck
  def shuffle(self):
    random.shuffle(self.deck)

  # deals cards
  def deal(self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)


class Poker():

  # constructor
  def __init__(self, num_players=2, num_card=5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deals cards to players
    for i in range(num_players):
      hand = []
      for j in range(self.numCards_in_Hand):
        hand.append(self.deck.deal())
      self.all_hands.append(hand)

  # plays poker
  def play(self):
    for i in range(len(self.all_hands)):
      sorted_hand = sorted(self.all_hands[i], reverse=True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str(card) + ''
      print("Player " + str(i + 1) + ' : ' + hand_str)

    # determine hand and print
    hand_type = []
    hand_points = []

    # determine winner

  # checks if hand is royal flush
  def is_royal(self, hand):
    same_suit = True
    for i in range(len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    else:
      # calculates total points
      points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    return points, 'Royal Flush'

  # checks if hand straight flush
  def is_straight_flush(self, hand):
    same_suit = True
    for i in range(len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (same_suit == False):
      return 0, ''

    rank_order = True
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[i + 1].rank)

    if (rank_order == False):
      return 0, ''

    else:
      points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    return points, 'Straight Flush'

  # checks if hand is 4 of a kind
  def is_four_kind(self, hand):
    four_cards = False
    if ((hand[0].rank) == (hand[1].rank) == (hand[2].rank) == (hand[3].rank)):
      four_cards = True

    elif ((hand[1].rank) == (hand[2].rank) == (hand[3].rank) == (hand[4].rank)):
      four_cards = True

    if four_cards == False:
      return 0, ''

    if ((hand[0].rank) == (hand[1].rank) == (hand[2].rank) == (hand[3].rank)):
      points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    elif ((hand[1].rank) == (hand[2].rank) == (hand[3].rank) == (hand[4].rank)):
      points = 8 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
      points = points + (hand[1].rank)

    return points, 'Four of a Kind'

  # checks if hand is a full house CHECK AGAIN TO MAKE SURE IT WORKS LOGIC
  def is_full_house(self, hand):
    full_house = False
    if ((hand[0].rank) == (hand[1].rank) == (hand[2].rank) and (hand[3].rank) == (hand[4].rank)) or ((hand[2].rank) == (hand[3].rank) == (hand[4].rank) and (hand[0].rank) == (hand[1].rank)):
      full_house = True

    else:
      full_house = False
      return 0, ''

    if full_house == True:
      if ((hand[0].rank) == (hand[1].rank) == (hand[2].rank) and (hand[3].rank) == (hand[4].rank)):
        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Full House'

      elif ((hand[2].rank) == (hand[3].rank) == (hand[4].rank) and (hand[0].rank) == (hand[1].rank)):
        points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Full House'

  # checks if hand is a flush
  def is_flush(self, hand):
    same_suit = False
    for i in range(len(hand) - 1):
      if ((hand[i].suit) == (hand[i + 1].suit)):
        same_suit = True

    if same_suit == False:
      return 0, ''

    else:
      points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Straight Flush'

  # checks if hand a straight
  def is_straight(self, hand):
    rank_order = False
    for i in range(len(hand) - 1):
      if ((hand[i].rank) + 1 == (hand[i + 1].rank)):
        rank_order = True

    if (rank_order == True):
      points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Straight'

    else:
      return 0, ''

  # checks if hard is three of a kind
  def is_three_kind(self, hand):
    if ((hand[0].rank) == (hand[2].rank)):
      points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Three of a kind'

    elif ((hand[1].rank) == (hand[3].rank)):
      points = 4 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Three of a kind'

    elif ((hand[2].rank) == (hand[4].rank)):
      points = 4 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)

      return points, 'Three of a kind'

    else:
      return 0, ''

  # checks if hand is a two pair
  def is_two_pair(self, hand):
    pass

   # checks if hand is a one pair
  def is_one_pair(self, hand):
    one_pair = False
    for i in range(len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        break

    if (one_pair == False):
      return 0, ''

    else:
      # calculates total points
      points = 2 * 15 ** 5 + (hand[0].rank) * 15 * 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'One Pair'

  # checks if hand only has a high card
  def is_high_card(self, hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 * 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

# main calls functions


def main():
  num_players = int(input('Enter the number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int(input('Enter number of players: '))

  game = Poker(num_players)

  game.play()


# calls main
main()
