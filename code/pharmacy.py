#!/usr/bin/python
# -*- coding: utf-8 -*-

class pharmacy:
    def __init__(self):
        self.idx       =''
        self.commercial=''
        self.social    =''
        self.addresse  =''
        self.postalcode=''
        self.city      =''
        self.telephone =''
        self.fax       =''

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

    def escape (self, data):
        import MySQLdb
        return MySQLdb.escape_string(str(data))

    @staticmethod
    def fromCsv(line):
        res = pharmacy()
        csv = line.split('|')
        res.idx       =  csv[0].replace('None','')
        res.social    =  csv[1].replace('None','')
        res.commercial=  csv[2].replace('None','')
        res.addresse  =  csv[3].replace('None','')
        res.postalcode=  csv[4].replace('None','')
        res.city      =  csv[5].replace('None','')
        res.telephone =  csv[6].replace('None','')
        res.fax       =  csv[7].replace('None','')
        return res

    def sql(self):
        self.clean()
        res = "INSERT INTO `Pharma` ("\
              +  "`pharma_id`, "\
              +  "`pharma_title`, "\
              +  "`pharma_empl`, "\
              +  "`pharma_desc`, "\
              +  "`pharma_hours`, "\
              +  "`pharma_adress`, "\
              +  "`pharma_lat`, "\
              +  "`pharma_long`, "\
              +  "`pharma_contact_mail`, "\
              +  "`pharma_contact_tel`, "\
              +  "`pharma_validated`"\
              +") VALUES ("\
              +       str(self.idx)       +","\
              +  "'" +self.escape(self.social    )+ "',"\
              +  "'" +self.escape(self.commercial)+ "',"\
              +  "'',"\
              +  "'',"\
              +  "'" +self.escape(self.addresse + ", " + self.postalcode + ", " + self.city) + "',"\
              +  "0,"\
              +  "0,"\
              +  "'',"\
              +  "'" +self.escape(self.telephone) + "',"\
              +  "0"\
              +  ");"
        return res




