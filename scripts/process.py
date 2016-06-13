#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib

source = 'http://www.nber.org/data/chat/FinalCHAT_72909.csv'

def retrieve(source):
    '''Downloades csv data to data directory
    
    '''
    urllib.urlretrieve(source,'data/historical-adoption-of-technology.csv')

if __name__ == '__main__':
    retrieve(source)