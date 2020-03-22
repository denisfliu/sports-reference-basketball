#!/usr/bin/env python
import g

if __name__ == '__main__':
    while True:
        print('Enter url: ')
        dateurl = input()
        with open("data.csv", 'a') as csvfile:
            g.get_goods(dateurl, csvfile)