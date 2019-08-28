import random

STEVILO_DOVOLJENIH_NAPAK = 6
PRAVILNA_BARVA_MESTO = 'B'
# B - black(črna)
PRAVILNA_BARVA = 'W'
# W - white(bela)
NAPACEN_UGIB = ' '
ZMAGA = 'Z'
PORAZ = 'P'


def nova_igra():
    mozne_izbire = [Y, O, R, B, G, V]
    nakljucna_izbira = []
    prvi = random.choice(mozne_izbire)
    mozne_izbire = mozne_izbire - [prvi]
    nakljucna_izbira.append(prvi)
    drugi = random.choice(mozne_izbire)
    mozne_izbire = mozne_izbire - [drugi]
    nakljucna_izbira.append(drugi)
    tretji = random.choice(mozne_izbire)
    mozne_izbire = mozne_izbire - [tretji]
    nakljucna_izbira.append(tretji)
    cetrti = random.choice(mozne_izbire)
    nakljucna_izbira.append(cetrti)
    return Igra(nakljucna_izbira)



def primerjava(nakljucna_izbira, ugibana_kombinacija):
    if nakljucna_izbira == ugibana_kombinacija:
        return ZMAGA
    kako_kaze = []
    for i in range(0, 3):
        if nakljucna_izbira[i] == ugibana_kombinacija[i]:
            kako_kaze.append('B')
        elif ugibana_kombinacija[i] in nakljucna_izbira == True:
            kako_kaze.append('W')
        else:
            kako_kaze.append(' ')
    return kako_kaze

class Igra:
    def __init__ (self, nakljucna_izbira, kombinacije = None):
        self.nakljucna_izbira = nakljucna_izbira.upper()
        print(self.nakljucna_izbira)
        self.kombinacije = [] if kombinacije == None else kombinacije
    
    def napacni_ugibi(self):
        ugibane_kombinacije = []
        for kombinacija in self.kombinacije:
            if kombinacija not in self.kombinacije:
                ugibane_kombinacije.append(kombinacija)
        return ugibane_kombinacije
    
    def stevilo_napak(self):
        napake = len(self.uginane_kombinacije())
        return napake
       
    def zmaga(self):
        for kombinacija in self.kombinacije:
            if kombinacija not in self.kombinacije:
                return False
        else:
            return True

    def poraz(self):
        if len(self.ugibane_kombinacije()) >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    
    def primerjava(self, nakljucna_izbira, ugibana_kombinacija):
        if nakljucna_izbira == ugibana_kombinacija:
            return ZMAGA
        kako_kaze = []
        for i in range(0, 3):
            if nakljucna_izbira[i] == ugibana_kombinacija[i]:
                kako_kaze.append('B')
            elif ugibana_kombinacija[i] in nakljucna_izbira == True:
                kako_kaze.append('W')
            else:
                kako_kaze.append(' ')
        return kako_kaze

    def nepravilne_kombinacije(self):
        niz_nepravilnih_kombinacij = ''
        for kombinacija in self.kombinacije:
            if kombinacija in self.napacni_ugibi():
                niz_nepravilnih_kombinacij += kombinacija + " "
        return niz_nepravilnih_kombinacij

    def ugibaj(self, kombinacija):
        kombinacija = kombinacija.upper()
        if kombinacija == self.kombinacije:
            return PONOVLJENA_KOMBINACIJA
        else:
            self.kombinacije.append(kombinacija)
            if kombinacija != self.nakljucna_izbira:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_KOMBINACIJA
            if self.zmaga():
                return ZMAGA
            else: 
                return print('nekje je napaka')




ZACETEK = 'A'
class Memo:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1
        
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre
    
    def ugibaj(self, id_igre, vpisan_ugib):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(vpisan_ugib)
        self.igre[id_igre] = (igra, poskus)
        return id_igre
