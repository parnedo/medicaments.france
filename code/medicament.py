class medicament :
    def __init__(self):
        self.mTitle         = None
        self.mCode          = None
        self.mType          = None
        self.mTherapy       = None
        self.mGenericGroup  = None
        self.mComposition   = None
        self.mPresentation  = None
        self.mSMR           = None # Service Medical rendu
        self.mASMR          = None
        self.mOther         = None

    def __str__(self):
        return str(self.mTitle       ) + "|" +\
               str(self.mCode        ) + "|" +\
               str(self.mType        ) + "|" +\
               str(self.mTherapy     ) + "|" +\
               str(self.mGenericGroup) + "|" +\
               str(self.mComposition ) + "|" +\
               str(self.mPresentation) + "|" +\
               str(self.mSMR         ) + "|" +\
               str(self.mASMR        ) + "|" +\
               str(self.mOther       )

    def __repr__(self):
        return self.__str__()

