#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:25:53 2020

@author: israel
"""

class Card():
    def __init__(self, tuple):
        self.value = tuple[0:-1]
        self.suit = tuple[-1]
        #print(f'value: {tuple[0:-1]} suit: {tuple[-1]}')

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if value == 'J':
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
        print(f'suma: {suma} s: {s}')
        return (suma == s and self.same_suit())
        
        
    # All cards are consecutive values of same suit
    def is_straight_flush(self):
        values = self.get_values()
        values.sort()
        print(f'values: {values}')
        for i in range(0,4):
            if values[i] != values[i+1]-1:
                return False
        return self.same_suit()
    
    # Four cards of the same value
    def is_four_of_a_kind(self):
        values = self.get_values()
        values.sort()
        if values[0] == values[1] and values[1] == values[2] and \
            values[2] == values[3]:
            #print(f'Poker de {values[0]}')
            return values[0]
        if values[1] == values[2] and values[2] == values[3] and \
            values[3] == values[4]:
            #print(f'Poker de {values[1]}')
            return values[1]
        return False
    
    def is_full_house():
        return 'highest'
    
    def is_flush():
        return 'highest'
    
    def is_straight():
        return 'highest'
    
    def is_three_of_a_kind():
        return 'highest'
    
    def is_two_pairs():
        return 'highest'
    
    def is_one_pair():
        return 'highest'
    
    def is_high_card():
        return 'highest'
    
    def get_hand():
        return 0