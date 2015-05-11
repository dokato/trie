#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
from trie import Trie

t = Trie()

def command_parse(arg):
    global t
    if len(arg)==1:
        ins=arg[0]
    if len(arg)==2:
        (ins,var) = arg
    if ins=='i':
        t.add_word(var)
    elif ins=='r':
        t.remove(var)
    elif ins=='f':
        print t.find_by_word(var)
    elif ins=='n':
        print t.find_by_number(int(var))
    elif ins=='p':
        print t.find_by_pref(var)
    elif ins=='a':
        for i in t.printasc():
            print i
    elif ins=='d':
        for i in t.printdesc():
            print i        
    else:
        print 'bad command'

if __name__ == "__main__":
    l=True
    while l:
        l = sys.stdin.readline()
        arg=l.split()
        if len(arg)==0:
            continue
        if len(arg)==1:
            if arg[0]=='k':
                sys.exit() 
        if len(arg)<=2:
            command_parse(arg)
