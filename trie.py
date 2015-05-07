#!/usr/bin/env python
# -*- coding: utf-8 -*- #

class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def add_word(self, word):
        self.root.add_word(word)
        
    def remove(self,word):
        self.root.remove(word)
        
    def find_by_word(self,word):
        return self.root.find_by_word(word)

    @property
    def children(self):
        return self.root.children
    
    def __repr__(self):
        return 'Root<%s>'%(self.root.children)

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
    
    def _add(self):
        self.__count += 1

    def _pop(self):
        self.__count -= 1
        if self.__count <=0:
            return False
        else:
            return True

    def add_child(self,value,early_child=False):
        if early_child:
            tmpt = TrieNode(value)
            tmpt.__count -= 1
            self.__children.append(tmpt)
        else:
            self.__children.append(TrieNode(value))
        self.__children.sort()
    
    def add_word(self,word):
        if len(word)>1:
            s = word[0]
            word = word[1:]
            for c in self.children:
                if c.has_value(s):
                    c._add()
                    c.add_word(word)
                    break
            else:
                self.add_child(s,True)
                self.add_word(s+word)
        else:
            s = word
            for c in self.children:
                if c.has_value(s):
                    c._add()
                    break
            else:
                self.add_child(s)

    def has_value(self,letter):
        return self.__value == letter

    def remove(self,word):
        if len(word)>1:
            s = word[0]
            word = word[1:]
            for c in self.children:
                if c.has_value(s):
                    if c.remove(word):
                        if not c._pop():
                            self.__children.remove(c)
                        return True
            else:
                return False
        else:
            s = word
            for c in self.children:
                if c.has_value(s):
                    if not c._pop():
                        self.__children.remove(c)
                    return True
            else:
                return False

    def find_by_word(self,word):
        nbr = 0
        node = self
        while nbr!=None:
            try:
                s = word[0]
            except IndexError:
                nbr=None
                break
            word = word[1:]
            for c in node.children:
                nbr+=c.count
                if c.has_value(s):
                    nbr-=c.count
                    node=c
                    break
            else:
                nbr=None
            if len(node.children)<=0:
                break
        return nbr
        
    def __repr__(self):
        return 'Trie<%s (%i)>'%(self.__value,self.__count)

    def __gt__(self, node2):
        return self.__value > node2.value
    
if __name__ == '__main__':
    t=Trie()
    t.add_word('money')
    t.add_word('power')
    t.add_word('mouse')
    t.add_word('paris')
    t.add_word('kawa')
    t.remove('madrid')
    print t.find_by_word('powe')
