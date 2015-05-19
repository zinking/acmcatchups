#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys;

def parse_authorbook( line ):
    author_book = line.split(' (')
    authorline = author_book[0]
    book = '('+author_book[1]
    authors = authorline.split( '., ')
    for i in range( len(authors)-1 ):
	authors[i] = authors[i]+"."
    authors[-1] = authors[-1].replace('& ','')
    return book,authors

def find_erdo( author, erdoset):
    for i in range(len(erdoset)):
	if author in erdoset[i]:
	    return i
    return -1

def find_authors_erdo( authors, erdoset ):
    authorset = set(authors)
    for i in range(len(erdoset)):
	erdos = erdoset[i]
	inter = erdos.intersection(authorset)
	if( len(inter) > 0 ): return i;
    return -1
	

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    line1 = lines[0]
    mn = line1.split(' ')
    n = int(mn[0])
    m = int(mn[1])
    booklines = lines[1:]
    authorlines = lines[1+n:]
    erdosSet = [ set(['Erdös, P.']), set([]),set([]),set([]),set([]),set([])]
    for i in range(n):
	book,authors = parse_authorbook( booklines[i])
	#print book,authors
	ei = find_authors_erdo( authors, erdosSet)
	if ei != -1:
	    author_set = set(authors)
	    nauthors = author_set - erdosSet[ei]
	    #print ei, authors, nauthors, "#####"
	    erdosSet[ei+1]=erdosSet[ei+1].union(nauthors)
    print erdosSet
    for i in range(m):
	author = authorlines[i].strip()
	ae = find_erdo(author,erdosSet)
	print author, ae
