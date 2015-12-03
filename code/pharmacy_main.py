#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
class main:
    def __init__(self):
        self.mPharmacy_list = []
        self.mBaseUrl = 'http://www.ordre.pharmacien.fr/annuaire/etablissement'

    def fetchFarmacies(self, filename):
        from pharmacy_parser import pharmacy_parser
        import urlparse
        for page in range(1,15000):
            for farmacy in self.getFarmacyList(page):
                r = requests.get(self.mBaseUrl+'/'+farmacy)
                pharmacy = pharmacy_parser(r.text).parse()
                pharmacy.idx = urlparse.parse_qs(farmacy)['sid'][0]
                print pharmacy
                self.mPharmacy_list += [pharmacy]
                f = open(filename, 'a')
                f.write(str(pharmacy)+'\n')
                f.close()
        #print self.mPharmacy_list


    def getFarmacyList(self, page):
        payload = {'type': 'P', 'page': str(page)}
        r = requests.get(self.mBaseUrl, params=payload)
        from BeautifulSoup import BeautifulSoup
        import re
        site = BeautifulSoup(r.text)
        return [x.attrMap['href'] for x in site.findAll('a',attrs={'href':re.compile (".*type.*sid.*")})]

if __name__ == "__main__":
    main().fetchFarmacies("pharma.txt")

