#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:25:53 2020

@author: israel
"""

class Card():
    def __init__(self, tuple):
        self.value = tuple[0]
        self.suit = tuple[1]
        #self.value = tuple[0:-1]
        #self.suit = tuple[-1]
        #print(f'value: {tuple[0:-1]} suit: {tuple[-1]}')

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if value == 'T':
            self.__value = 10
        elif value == 'J':
            self.__value = 11
        elif value == 'Q':
            self.__value = 12
        elif value == 'K':
            self.__value = 13
        elif value == 'A':
            self.__value = 14
        else:
            self.__value = int(value)
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit):
        self.__suit = suit
    
    def __str__(self):
        return (str(self.value) + self.suit)
    

class Hand():
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        output = ''
        for c in self.__cards:
            output += str(c)
            output += ' '
        return output
    
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards):
        self.__cards = cards
    
    # Devuelve array con todos los palos
    def get_suits(self):
        suits = []
        for c in self.cards:
            suits.append(c.suit)
        return suits
    # Devuelve array con todos los valores
    def get_values(self):
        values = []
        for c in self.cards:
            values.append(c.value)
        return values
    # Comprueba si todas las cartas son del mismo palo
    def same_suit(self):
        suits = self.get_suits()
        return suits[0] == suits[1] and suits[1] == suits[2] and \
            suits[2] == suits[3] and suits[3] == suits[4]

    
    # Ten, Jack, Queen, King, Ace, in same suit
    def is_royal_flush(self):
        suma = 14+13+12+11+10
        s = 0
        for i in self.cards:
            s += i.value
        return (suma == s and self.same_suit())
        
    # All cards are consecutive values of same suit
    def is_straight_flush(self):
        values = self.get_values()
        values.sort()
        for i in range(0,4):
            if values[i] != values[i+1]-1:
                return 0
        if self.same_suit():
            return values[4]
        return 0
    
    # Four cards of the same value
    def is_four_of_a_kind(self):
        values = self.get_values()
        values.sort()
        if values[0] == values[1] and values[1] == values[2] and \
            values[2] == values[3]:
            return values[0]
        if values[1] == values[2] and values[2] == values[3] and \
            values[3] == values[4]:
            return values[1]
        return 0
    
    # Three of a kind and a pair
    def is_full_house(self):
        values = self.get_values()
        values.sort()
        if values.count(values[0]) == 3 and values.count(values[4]) == 2:
            return values[0]
        if values.count(values[0]) == 2 and values.count(values[4]) == 3:
            return values[4]
        return 0
    
    # All cards of the same suit
    def is_flush(self):
        suits = self.get_suits()
        values = self.get_values()
        values.sort(reverse=True)
        if suits[0] == suits[1] and suits[1] == suits[2] and \
            suits[2] == suits[3] and suits[3] == suits[4]:
                return values
        return 0
        
    # All cards are consecutive values
    def is_straight(self):
        values = self.get_values()
        values.sort()
        for i in range(0,4):
            if values[i] != values[i+1]-1:
                return 0
        return values[4]
    
    # Three cards of the same value
    def is_three_of_a_kind(self):
        values = self.get_values()
        for v in values:
            if values.count(v) == 3:
                return v
        return 0
    
    # Two different pairs
    def is_two_pairs(self):
        values = self.get_values()
        values.sort(reverse=True)
        pairs = []
        for v in values:
            if values.count(v) == 2 and v not in pairs:
                pairs.append(v)
        if len(pairs) == 2:
            return pairs
        else:
            return 0
    
    # Two cards of the same value
    def is_one_pair(self):
        values = self.get_values()
        for v in values:
            if values.count(v) == 2:
                return v
        return 0
    
    # Highest value card
    def is_high_card(self):
        values = self.get_values()
        values.sort(reverse=True)
        return values

    # 1: gana jugador 1
    # 2: gana jugador 2
    # 0: ninguno tiene esa mano
    # -1: empate    
    def compare_royal_flush(self, h2):
        h2_rf = h2.is_royal_flush()
        if self.is_royal_flush():
            if h2_rf:
                return -1
            return 1
        if h2_rf:
            return 2
        return 0
    
    def compare_straight_flush(self, h2):
        h1_sf = self.is_straight_flush()
        h2_sf = h2.is_straight_flush()
        if h1_sf == 0 and h2_sf == 0:
            return 0
        if h1_sf > h2_sf:
            return 1
        if h2_sf > h1_sf:
            return 2
        return self.compare_high_card(h2)
            
    def compare_four_kind(self, h2):
        h1_fk = self.is_four_of_a_kind()
        h2_fk = h2.is_four_of_a_kind()
        if h1_fk == 0 and h2_fk == 0:
            return 0
        if h1_fk > h2_fk:
            return 1
        if h2_fk > h1_fk:
            return 2
        return self.compare_high_card(h2)
        
    def compare_full_house(self, h2):
        h1_fh = self.is_full_house()
        h2_fh = h2.is_full_house()
        print(f'h1: {h1_fh}  h2: {h2_fh}')
        if h1_fh == 0 and h2_fh == 0:
            return 0
        if h1_fh > h2_fh:
            return 1
        if h1_fh < h2_fh:
            return 2
        
    def compare_flush(self, h2):
        h1_fl = self.is_flush()
        h2_fl = h2.is_flush()
        if h1_fl == 0 and h2_fl == 0:
            return 0
        if h1_fl == 0 and h2_fl != 0:
            return 2
        if h1_fl != 0 and h2_fl == 0:
            return 1
        for i in range(0,len(h1_fl)):
            if h1_fl[i] > h2_fl[i]:
                return 1
            if h1_fl[i] < h2_fl[i]:
                return 2
        return -1
    
    def compare_straight(self, h2):
        h1_st = self.is_straight()
        h2_st = h2.is_straight()
        if h1_st == 0 and h2_st == 0:
            return 0
        if h1_st > h2_st:
            return 1
        if h1_st < h2_st:
            return 2
        return -1
    
    def compare_three_kind(self, h2):
        h1_tk = self.is_three_of_a_kind()
        h2_tk = h2.is_three_of_a_kind()
        if h1_tk == 0 and h2_tk == 0:
            return 0
        if h1_tk > h2_tk:
            return 1
        if h1_tk < h2_tk:
            return 2
        return -1
        
    def compare_two_pairs(self, h2):
        h1_tp = self.is_two_pairs()
        h2_tp = h2.is_two_pairs()
        if h1_tp == 0 and h2_tp == 0:
            return 0
        if h1_tp == 0:
            return 2
        if h2_tp == 0:
            return 1
        for i in range(0,len(h1_tp)):
            if h1_tp[i] > h2_tp[i]:
                return 1
            if h1_tp[i] < h2_tp[i]:
                return 2
        return self.compare_high_card(h2)
            
    def compare_one_pair(self, h2):
        h1_op = self.is_one_pair()
        h2_op = h2.is_one_pair()
        if h1_op == 0 and h2_op == 0:
            return 0
        if h1_op > h2_op:
            return 1
        if h1_op < h2_op:
            return 2
        return self.compare_high_card(h2)
    
    def compare_high_card(self, h2):
        h1_hc = self.is_high_card()
        h2_hc = h2.is_high_card()
        for i in range(0,len(h1_hc)):
            if h1_hc[i] > h2_hc[i]:
                return 1
            if h1_hc[i] < h2_hc[i]:
                return 2
        return -1
        