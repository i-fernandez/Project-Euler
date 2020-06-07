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
       
# Devuelve el jugador que gana (-1 = empate)
def compare_hand(h1: Hand, h2: Hand):
    # Royal Flush
    rf = h1.compare_royal_flush(h2)
    if rf != 0:
        print('royal flush')
        return rf
    # Straight Flush
    sf = h1.compare_straight_flush(h2)
    if sf != 0:
        print('straight flush')
        return sf
    # Four of a kind
    fk = h1.compare_four_kind(h2)
    if fk != 0:
        print('four of a kind')
        return fk
    # Full house
    fh = h1.compare_full_house(h2)
    if fh != 0:
        print('full house')
        return fh
    # Flush
    fl = h1.compare_flush(h2)
    if fl != 0:
        print('flush')
        return fl
    # Straight
    st = h1.compare_straight(h2)
    if st != 0:
        print('straight')
        return st
    # Three of a kind
    tk = h1.compare_three_kind(h2)
    if tk != 0:
        print('three of a kind')
        return tk
    # Two pairs
    tp = h1.compare_two_pairs(h2)
    if tp != 0:
        print('two pairs')
        return tp
    # One pair
    op = h1.compare_one_pair(h2)
    if op != 0:
        print('one pair')
        return op
    # High card
    print('high card')
    return h1.compare_high_card(h2)
    
def read_data(file_name):
    game = []
    with open(file_name) as f:
        line = f.readline()
        while line:
            all_cards = line.split(' ')
            hand = []
            cards_1 = []
            cards_2 = []
            for i in range(0,5):
                c = Card(all_cards[i])
                cards_1.append(c)
            for i in range(5,10):
                c = Card(all_cards[i])
                cards_2.append(c)
            hand.append(Hand(cards_1))
            hand.append(Hand(cards_2))
            game.append(hand)
            line = f.readline()
    return game


suits = ['H', 'S', 'D', 'C']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']




file_name = 'p054_poker.txt'

win_1 = 0
win_2 = 0
tie = 0
game = read_data(file_name)


for hand in game:
    #print(f'{hand[0]} vs {hand[1]}')
    r = compare_hand(hand[0],hand[1])
    #print(f'Winner: {r}')
    if r == 1:
        win_1 += 1
    elif r == 2:
        win_2 += 1
    elif r == -1:
        tie += 1
        
print(f'Player 1 wins: {win_1}')
print(f'Player 2 wins: {win_2}')
print(f'Ties: {tie}')

    
