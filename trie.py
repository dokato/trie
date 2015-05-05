#!/usr/bin/env python
# -*- coding: utf-8 -*- #

class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def add_word(self, word):
        if len(word)>1:
            s = word[0]
            word = word[1:]
            for c in self.root.children:
                if c.has_value(s):
                    c.add()
                    c.add_word(word)
                    break
            else:
                self.root.add_child(s)
                self.root.children[-1].add_word(word)

class TrieNode(object):
    def __init__(self, val):
        self.__value = val
        self.__children = []
        self.__count = 1
    
    @property
    def value(self):
        return self.__value

    @property
    def count(self):
        return self.__count
    
    @property
    def children(self):
        return [x for x in self.__children]
    
    def add(self):
        self.__count += 1

    def add_child(self,value):
        self.__children.append(TrieNode(value))
    
    def add_word(self,word):
        if len(word)>1:
            s = word[0]
            word = word[1:]
            for c in self.children:
                if c.has_value(s):
                    c.add()
                    c.add_word(word)
                    break
            else:
                self.add_child(s)
                self.children[-1].add_word(word)
        else:
            s = word
            for c in self.children:
                if c.has_value(s):
                    c.add()
                    break
            else:
                self.add_child(s)
            

    def has_value(self,letter):
        return self.__value == letter
        
    def __repr__(self):
        return 'Trie<%s (%i)>'%(self.__value,self.__count)

