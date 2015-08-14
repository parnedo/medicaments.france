#!/usr/bin/python
# -*- coding: utf-8 -*-

class main:
    def __init__(self):
        self.mMedicament_list = []
        self.mBaseUrl = 'base-donnees-publique.medicaments.gouv.fr'

    def fetchMedicaments(self, filename):
        from parser import medicament_parser
        for upperCase in map(chr, range(ord('A'), ord('Z')+1)):
            for med in self.getMedURL_List(self.fetchURL(upperCase)):
                print med
                medData = self.getMedData(med)
                medicament = medicament_parser(self.getMedData(med)).parse()
                self.mMedicament_list += [medicament]
                f = open(filename, 'a')
                f.write(str(medicament)+'\n')
                f.close()
        print self.mMedicament_list

    def getMedData(self, url):
        import urllib2
        return urllib2.urlopen('http://'+self.mBaseUrl+'/'+url).read()

    def fetchURL(self, key):
        import httplib, urllib
        params = urllib.urlencode({
            'page':'1',
            'affliste':'0',
            'affNumero':'0',
            'isAlphabet':'1',
            'inClauseSubst':'0',
            'nomSubstances':'',
            'typeRecherche':'0',
            'choixRecherche':'medicament',
            'txtCaracteres':key,
            'radLibelle':'2',
            'txtCaracteresSub':'',
            'radLibelleSub':'4'
            })
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection(self.mBaseUrl + ":80")
        conn.request("POST", "/index.php", params, headers)
        response = conn.getresponse()
        print key, response.status, response.reason
        data = response.read()
        conn.close()
        return data

    def getMedURL_List(self, html):
        from BeautifulSoup import BeautifulSoup
        import re
        site = BeautifulSoup(html)
        return [x['href'] for x in site.findAll('a',attrs={'class':'standart'})]

if __name__ == "__main__":
    main().fetchMedicaments("med.txt")

