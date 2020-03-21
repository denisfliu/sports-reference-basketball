#!/usr/bin/env python
import g

if __name__ == '__main__':
    print('Enter url: ')
    dateurl = input()
    with open("data.csv", 'a') as csvfile:
        csvfile.write('\n')
        g.get_goods(dateurl, csvfile)