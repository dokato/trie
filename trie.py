#!/usr/bin/env python
# -*- coding: utf-8 -*- #

class Trie(object):
    def __init__(self):
        self.root = TrieNode(None,0)

    def add_word(self, word):
        """add word to tree"""
        self.root.add_word(word)
        self.root._add()
        
    def remove(self,word):
        """remove word from tree"""
        rem = self.root.remove(word)
        if rem: self.root._pop()
        return rem
        
    def find_by_word(self,word):
        """find given *word* in tree, if not occures None is returned"""
        return self.root.find_by_word(word)

    def printasc(self):
        """print all keys from tree in ascending order"""
        return self.root.printasc()
    
    def find_by_pref(self,pref):
        """find number of words with given prefix *pref*"""
        return self.root.find_by_pref(pref)

    def printdesc(self):
        """print all keys from tree in descending order"""
        return self.root.printasc()[::-1]
    
    def find_by_number(self,k):
        return self.root.find_by_number(k)

    @property
    def children(self):
        return self.root.children
    
    def __repr__(self):
        return 'Root<%s>'%(self.root.children)

class TrieNode(object):
    def __init__(self, val, cnt = 1):
        self.__value = val
        self.__children = []
        self.__count = cnt
    
    @property
    def value(self):
        return self.__value

    @property
    def count(self):
        return self.__count
    
    @property
    def children(self):
        "returns list of childrens"
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
        "add child and sort list of them"
        if early_child:
            tmpt = TrieNode(value)
            tmpt.__count -= 1
            self.__children.append(tmpt)
        else:
            self.__children.append(TrieNode(value))
        self.__children.sort()
    
    def add_word(self,word):
        "add word to node"
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
        "check if value occures"
        return self.__value == letter

    def remove(self,word):
        "remove from node"
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
                    if len(c.children)==0 and not c._pop():
                        self.__children.remove(c)
                    else:
                        if c.count==sum([x.count for x in c.children]):
                            return False
                        else:
                            self.__children.remove(c)
                    return True
            else:
                return False

    def find_by_word(self,word):
        "find *word* in node"
        nbr = 0
        node = self
        while nbr!=None:
            try:
                s = word[0]
            except IndexError:
                print 'zxcvbnm'
                if node.count==sum([n.count for n in node.children]):
                    nbr=None
                break
            word = word[1:]
            for c in node.children:
                nbr+=c.count
                if c.has_value(s):
                    #print ' >>> ', c, c.children
                    #print c.count , sum([n.count for n in c.children])
                    sumleft = sum([n.count for n in c.children])
                    if c.count!=sumleft:
                        nbr+= c.count-sumleft
                    nbr -= c.count
                    node = c
                    break
            else:
                nbr=None
            if len(node.children)<=0:
                break
        if nbr!=None and len(word)>0:
            nbr=None
        return nbr

    def find_by_number(self,k):
        "find lexicographic number of the word"
        if k>0:
            if len(self.__children)==0:
                return self.__value 
            l = [0]
            ix=0
            sumch = sum([n.count for n in self.__children])
            if self.__count!=sumch:
                l.append(l[-1]+1)
                ix=-1
            for c in self.children:
                l.append(c.count+l[-1])
            for k1,k2 in zip(l[:-1],l[1:]):
                if k1 < k <= k2:
                    vl = self.__value
                    if self.__value==None: vl = ''
                    if k<2 and self.__count!=sum([n.count for n in self.__children]):
                        return vl
                    word= vl + self.children[ix].find_by_number(k-k1)
                    return word 
                ix+=1
            else:
                return None 
        else:
            return self.__value
        return word

    def find_by_pref(self,pref):
        "number of keys starting with prefix *pref* in node"
        node = self
        prefidx = 0
        while len(pref)>0:
            s = pref[0]
            pref = pref[1:]
            for c in node.children:
                if c.has_value(s):
                    prefidx = c.count
                    node=c
                    break
            else:
                return 0 
            if len(node.children)<=0:
                break
        if prefidx!=0 and len(pref)>0:
            prefidx=0
        return prefidx 

    def printasc(self):
        "print all words from node in ascending order"
        lst = []
        val = self.__value
        if val == None: val=''
        for c in self.__children:
            lst.extend(c.printasc())        
        lst = [val+x for x in lst]
        lstp = [val]*(self.__count-sum([n.count for n in self.children]))
        return lstp+lst 
        
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
    t.add_word('pari')
    t.add_word('kawa')
    t.remove('madrid')
    print t.find_by_word('kawa')
    print t.find_by_word('money')
    print t.find_by_word('mouse')
    print t.find_by_word('pari')
    print t.find_by_word('paris')
    print t.find_by_word('power')
    print t.root.find_by_pref('p')
    print t.find_by_number(7)
    print '*'*10
    print t.printdesc()
