#!/usr/bin/python
# -*- coding: utf-8 -*-

class pharmacien:
    def __init__(self):
        self.name     = None
        self.familyname= None
        self.title = None
        self.nRPPS       = None
    def __str__(self):
        return str(self.name) + "|" +\
               str(self.familyname) + "|" +\
               str(self.title) + "|" +\
               str(self.nRPPS)
    def __repr__(self):
        return self.__str__()
