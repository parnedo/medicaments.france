#!/usr/bin/python
# -*- coding: utf-8 -*-

class pharmacy:
    def __init__(self):
        self.idx       = None
        self.commercial= None
        self.social    = None
        self.addresse  = None
        self.postalcode= None
        self.city      = None
        self.telephone = None
        self.fax       = None

    def clean(self):
        import re
        self.commercial= re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.commercial)))))
        self.social    = re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.social)))))
        self.addresse  = re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.addresse  )))))
        self.postalcode= re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.postalcode)))))
        self.city      = re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.city      )))))
        self.telephone = re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.telephone )))))
        self.fax       = re.sub(' +',' ',re.sub('\n*','',re.sub('\s*$','',re.sub('^\s*','',str(self.fax       )))))

    def __str__(self):
        self.clean()
        return str(self.idx       ) + "|" +\
               str(self.social    ) + "|" +\
               str(self.commercial) + "|" +\
               str(self.addresse  ) + "|" +\
               str(self.postalcode) + "|" +\
               str(self.city      ) + "|" +\
               str(self.telephone ) + "|" +\
               str(self.fax       )

    def __repr__(self):
        return self.__str__()
