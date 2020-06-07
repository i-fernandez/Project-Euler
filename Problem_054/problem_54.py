#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:17:18 2020

@author: israel

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


"""

        
from classes import *
    

        

suits = ['H', 'S', 'D', 'C']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
hand1 = Hand([Card('5H'), Card('AS'), Card('5D'), Card('5C'), Card('5S')])
hand2 = ['2C', '3S', '8S', '8D', 'TD']
cards_1 = [Card('5H'), Card('5C'), Card('6S'), Card('7S'), Card('KD')]
hand3 = Hand(cards_1)
print(hand1)
print(hand1.is_royal_flush())
print(hand1.is_straight_flush())
print(hand1.is_four_of_a_kind())