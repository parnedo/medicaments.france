#!/usr/bin/python
# -*- coding: utf-8 -*-

class medicament :
    def __init__(self):
        self.mTitle         = None
        self.mCodeCIS       = None
        self.mCodeCIP13     = None
        self.mTherapy       = None
        self.mGenericGroup  = None
        self.mComposition   = None
        self.mPresentation  = None
        self.mSMR           = None # Service Medical rendu
        self.mASMR          = None
        self.mOther         = None

    def __str__(self):
        return str(self.mTitle       ) + "|" +\
               str(self.mCodeCIS     ) + "|" +\
               str(self.mCodeCIP13   ) + "|" +\
               str(self.getType()    ) + "|" +\
               str(self.mTherapy     ) + "|" +\
               str(self.mGenericGroup) + "|" +\
               str(self.mComposition ) + "|" +\
               str(self.mPresentation) + "|" +\
               str(self.mSMR         ) + "|" +\
               str(self.mASMR        ) + "|" +\
               str(self.mOther       )

    def __repr__(self):
        return self.__str__()

    def getType(self):
         if self.mComposition is None: return 0
         if "Compartiment"    in self.mComposition: return 10
         if "émulsion"        in self.mComposition: return 10
         if "Liquide"         in self.mComposition: return 10
         if "Petit"           in self.mComposition: return 10
         if "Poudre"          in self.mComposition: return 10
         if "Sirop"           in self.mComposition: return 10
         if "Solution"        in self.mComposition: return 10
         if "Suspension"      in self.mComposition: return 10
         if "Gomme"           in self.mComposition: return 12
         if "Crème"           in self.mComposition: return 13
         if "Gel"             in self.mComposition: return 13
         if "Granules"        in self.mComposition: return 13
         if "Lotion"          in self.mComposition: return 13
         if "Pâte"            in self.mComposition: return 13
         if "Pommade"         in self.mComposition: return 13
         if "Bain"            in self.mComposition: return 14
         if "Bâton"           in self.mComposition: return 14
         if "Capsule"         in self.mComposition: return 14
         if "Cartouche"       in self.mComposition: return 14
         if "Compartiment"    in self.mComposition: return 14
         if "Compresse"       in self.mComposition: return 14
         if "Dispersion"      in self.mComposition: return 14
         if "Dispositif"      in self.mComposition: return 14
         if "éluat"           in self.mComposition: return 14
         if "Emplâtre"        in self.mComposition: return 14
         if "émulsion"        in self.mComposition: return 14
         if "éponge"          in self.mComposition: return 14
         if "Film"            in self.mComposition: return 14
         if "Gaz"             in self.mComposition: return 14
         if "Gelée"           in self.mComposition: return 14
         if "Graines"         in self.mComposition: return 14
         if "Implant"         in self.mComposition: return 14
         if "Insert"          in self.mComposition: return 14
         if "Lyophilisat"     in self.mComposition: return 14
         if "Mélange"         in self.mComposition: return 14
         if "Microsphère"     in self.mComposition: return 14
         if "Mousse"          in self.mComposition: return 14
         if "Ovule"           in self.mComposition: return 14
         if "Pansement"       in self.mComposition: return 14
         if "Pastille"        in self.mComposition: return 14
         if "Plante"          in self.mComposition: return 14
         if "Poudre"          in self.mComposition: return 14
         if "Shampooing"      in self.mComposition: return 14
         if "Solide"          in self.mComposition: return 14
         if "Solution"        in self.mComposition: return 14
         if "Solvant"         in self.mComposition: return 14
         if "Suppositoire"    in self.mComposition: return 14
         if "Système"         in self.mComposition: return 14
         if "Tampon"          in self.mComposition: return 14
         if "Vernis"          in self.mComposition: return 14
         if "Collutoire"      in self.mComposition: return 1
         if "Collyre"         in self.mComposition: return 3
         if "Gélule"          in self.mComposition: return 5
         if "Comprimé"        in self.mComposition: return 7
         if "Pilule"          in self.mComposition: return 7
         if "Comprimé"        in self.mComposition: return 9
         if "Flacon"          in self.mComposition: return 9
         if "Gélule"          in self.mComposition: return 9
         if "Granules"        in self.mComposition: return 9
         if "Granulés"        in self.mComposition: return 9
         if "Lyophilisat"     in self.mComposition: return 9
         if "Microgranule"    in self.mComposition: return 9
         if "Poche"           in self.mComposition: return 9
         if "Poudre"          in self.mComposition: return 9
         if "Sachet"          in self.mComposition: return 9
         if "Solvant"         in self.mComposition: return 9
