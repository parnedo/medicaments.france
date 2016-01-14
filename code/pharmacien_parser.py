#!/usr/bin/python
# -*- coding: utf-8 -*-

from pharmacien import pharmacien
import xml.etree.ElementTree as ET
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import HTMLParser
import re
class pharmacien_parser:
    def __init__(self, data):
        self.removeHTMLTags = re.compile(r'<.*?>')
        self.mTree = BeautifulSoup (data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        self.mHtml_parser = HTMLParser.HTMLParser()


    def procLine(self, line):
        l = str(line.encode('utf-8').strip())
        return ' '.join(l.split())

    def parse(self):
        p = pharmacien()

        for s in self.mTree.findAll('strong'):
            if s is not None:
                print s, [s.nextSibling]
                if "Prénom" in str(s):
                    try:
                        p.name = s.nextSibling
                    except (AttributeError, TypeError):
                        pass
                if "Nom" in str(s):
                    try:
                        p.familyname = s.nextSibling
                    except (AttributeError, TypeError):
                        pass
                if "Titre" in str(s):
                    try:
                        p.title = s.nextSibling.replace('\n','')
                    except (AttributeError, TypeError):
                        pass
                if "Numéro RPPS" in str(s):
                    try:
                        p.nRPPS = s.nextSibling.replace('\n','')
                    except (AttributeError, TypeError):
                        pass

        #try:
        #    m.mGenericGroup = self.procLine(self.mTree.find('a',attrs={'title':unicode(u'Ouvrir la page de détail sur ce groupe générique')}).text)
        #except (AttributeError, TypeError):
        #    pass

        #try:
        #    m.mTherapy = self.procLine(self.mTree.find('p', attrs={'class':'AmmCorpsTexte'}).text)
        #    m.mTherapy += ' '.join([self.procLine(a.text) for a in self.mTree.findAll('p', attrs={'class':re.compile("^AmmListePuces")})])
        #except (AttributeError, TypeError):
        #    pass

        #try:
        #    m.mComposition = self.procLine(self.mTree.find('li', attrs={'class':'element'}).text)
        #    m.mComposition += self.procLine(self.mTree.find('li', attrs={'class':'composant'}).text)
        #except (AttributeError, TypeError):
        #    pass

        #try:
        #    m.mPresentation = self.mTree.find('h2', attrs={'class':'titrePresentation'}).text.encode('utf-8').strip()
        #except (AttributeError, TypeError):
        #    pass

        #for br in self.mTree.findAll('br'):
        #    if br.previousSibling is not None:
        #        if "CIP" in br.previousSibling:
        #            try:
        #                m.mCodeCIP13 = re.search('Code CIP : .*? ou (.*)', str(br.previousSibling)).groups()[0].replace(' ','')
        #            except:
        #                m.mCodeCIP13 = re.search('Code CIP : (.*)', str(br.previousSibling)).groups()[0].replace(' ','')


        #try:
        #    htmlSMR = self.mTree.find('table', attrs={'summary':unicode(u'Liste des avis de SMR rendus par la commission de la transparence')})
        #    m.mSMR =  ' '.join([a.text.encode('utf-8').strip() for a in htmlSMR.findAll('td', attrs={'class':re.compile("^ligne")})])
        #except (AttributeError, TypeError):
        #    pass

        #try:
        #    htmlASMR = self.mTree.find('table', attrs={'summary':unicode(u'Liste des avis d\'ASMR rendus par la commission de la transparence')})
        #    m.mASMR = ' '.join([self.procLine(a.text) for a in htmlASMR.findAll('td', attrs={'class':re.compile("^ligne")})])
        #except (AttributeError, TypeError):
        #    pass

        #try:
        #    htmlOther = self.mTree.find('div', attrs={'id':'autreInfo'})
        #    m.mOther = ' '.join([self.procLine(a.text) for a in htmlOther.findAll('li')])
        #except (AttributeError, TypeError):
        #    pass

        return p

if __name__ == "__main__":
    import sys
    with open (sys.argv[1], "r") as myfile:
        data=myfile.read()
    print pharmacien_parser(data).parse()

