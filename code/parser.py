#!/usr/bin/python
# -*- coding: utf-8 -*-

from medicament import medicament
import xml.etree.ElementTree as ET
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import HTMLParser
import re
class medicament_parser:
    def __init__(self, data):
        self.removeHTMLTags = re.compile(r'<.*?>')
        self.mTree = BeautifulSoup (data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        self.mHtml_parser = HTMLParser.HTMLParser()

    def procLine(self, line):
        l = str(line.encode('utf-8').strip())
        return ' '.join(l.split())

    def parse(self):
        m = medicament()

        try:
            m.mTitle = self.procLine(self.mTree.find('h1', attrs={'class':'textedeno'}).text)
        except (AttributeError, TypeError):
            pass

        try:
            m.mGenericGroup = self.procLine(self.mTree.find('a',attrs={'title':unicode(u'Ouvrir la page de détail sur ce groupe générique')}).text)
        except (AttributeError, TypeError):
            pass

        try:
            m.mTherapy = self.procLine(self.mTree.find('p', attrs={'class':'AmmCorpsTexte'}).text)
            m.mTherapy += ' '.join([self.procLine(a.text) for a in self.mTree.findAll('p', attrs={'class':re.compile("^AmmListePuces")})])
        except (AttributeError, TypeError):
            pass

        try:
            m.mComposition = self.procLine(self.mTree.find('li', attrs={'class':'element'}).text)
            m.mComposition += self.procLine(self.mTree.find('li', attrs={'class':'composant'}).text)
        except (AttributeError, TypeError):
            pass

        try:
            m.mPresentation = self.mTree.find('h2', attrs={'class':'titrePresentation'}).text.encode('utf-8').strip()
        except (AttributeError, TypeError):
            pass


        try:
            htmlSMR = self.mTree.find('table', attrs={'summary':unicode(u'Liste des avis de SMR rendus par la commission de la transparence')})
            m.mSMR =  ' '.join([a.text.encode('utf-8').strip() for a in htmlSMR.findAll('td', attrs={'class':re.compile("^ligne")})])
        except (AttributeError, TypeError):
            pass

        try:
            htmlASMR = self.mTree.find('table', attrs={'summary':unicode(u'Liste des avis d\'ASMR rendus par la commission de la transparence')})
            m.mASMR = ' '.join([self.procLine(a.text) for a in htmlASMR.findAll('td', attrs={'class':re.compile("^ligne")})])
        except (AttributeError, TypeError):
            pass

        try:
            htmlOther = self.mTree.find('div', attrs={'id':'autreInfo'})
            m.mOther = ' '.join([self.procLine(a.text) for a in htmlOther.findAll('li')])
        except (AttributeError, TypeError):
            pass

        return m

if __name__ == "__main__":
    with open ("sample.html", "r") as myfile:
        data=myfile.read()
    m = medicament_parser(data).parse()
    print m

