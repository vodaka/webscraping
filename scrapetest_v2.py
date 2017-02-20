#!/usr/bin/env python3

# coding:utf-8 # This is not required in Python3.

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("https://docs.openstack.org/newton/install-guide-rdo/")

#print(type(html))

#content = html.read()

bs0bj = BeautifulSoup(html,'html.parser')
contents = bs0bj.p

print(contents.get_text())
