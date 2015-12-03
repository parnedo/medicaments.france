#!/usr/bin/python
# -*- coding: utf-8 -*-

from pharmacy import pharmacy
import xml.etree.ElementTree as ET
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import HTMLParser
import re
class pharmacy_parser:
    def __init__(self, data):
        self.removeHTMLTags = re.compile(r'<.*?>')
        self.mTree = BeautifulSoup (data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        self.mHtml_parser = HTMLParser.HTMLParser()

    def parse(self):
        p = pharmacy()
        for s in self.mTree.findAll('strong'):
            if s is not None:
                #print s, [s.nextSibling]
                if "Dén. commerciale" in str(s):
                    try:
                        p.commercial = s.nextSibling
                    except (AttributeError, TypeError):
                        pass
                if "Raison sociale" in str(s):
                    try:
                        p.social= s.nextSibling
                    except (AttributeError, TypeError):
                        pass
                if "Adresse" in str(s):
                    try:
                        p.addresse = s.nextSibling
                    except (AttributeError, TypeError):
                        pass
                if "Code postal - ville :" in str(s):
                    try:
                        (p.postalcode,p.city) =  re.search('(\d+)[\n*](.*)', str(s.nextSibling)).groups()
                    except (AttributeError, TypeError):
                        pass
                if "Téléphone" in str(s):
                    try:
                        (p.telephone,)= re.search('(\d+)', str(s.nextSibling)).groups()
                    except (AttributeError, TypeError):
                        pass
                if "Télécopie" in str(s):
                    try:
                        (p.fax,)= re.search('(\d+)', str(s.nextSibling)).groups()
                    except (AttributeError, TypeError):
                        pass

        return p

if __name__ == "__main__":
    import sys
    with open (sys.argv[1], "r") as myfile:
        data=myfile.read()
    print [pharmacy_parser(data).parse()]

