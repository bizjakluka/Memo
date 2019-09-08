import random

STEVILO_DOVOLJENIH_NAPAK = 6
PRAVILNA_BARVA_MESTO = 'B'
# B - black(črna)
PRAVILNA_BARVA = 'W'
# W - white(bela)
NAPACEN_UGIB = ' '
ZMAGA = 'Z'
PORAZ = 'P'



class Igra:
    def __init__ (self, nakljucna_izbira, kako_kaze = None, ugibane_kombinacije = None):
        self.nakljucna_izbira = nakljucna_izbira.upper()
        print(self.nakljucna_izbira)
        self.kako_kaze = [] if kako_kaze == None else kako_kaze
        self.ugibane_kombinacije = [] if ugibane_kombinacije == None else ugibane_kombinacije
    
    def ugibaj(self, kombinacija):
        kombinacija = kombinacija.upper()
        if kombinacija == self.ugibane_kombinacije:
            self.kako_kaze = self.primerjava(kombinacija)
            return print('PONOVLJENA KOMBINACIJA')
        else:
            self.ugibane_kombinacije.append(kombinacija)
            if kombinacija != self.nakljucna_izbira:
                if self.poraz():
                    return PORAZ
                else:
                    self.ugibane_kombinacije = self.napacni_ugibi(kombinacija)
                    self.kako_kaze = self.primerjava(kombinacija)
                    return print('NAPACNA KOMBINACIJA')
            if self.zmaga(kombinacija):
                return ZMAGA
            else: 
                return print('nekje je napaka')

    def zmaga(self, kombinacija):
        if self.nakljucna_izbira == kombinacija:
            return True
        else:
            return False
    
    def poraz(self):
        if len(self.ugibane_kombinacije) >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False
    
    def napacni_ugibi(self, kombinacija):
        if kombinacija == None:
            return self.ugibane_kombinacije
        if kombinacija not in self.ugibane_kombinacije:
            self.ugibane_kombinacije.append(kombinacija)
        return self.ugibane_kombinacije

    def primerjava(self, kombinacija):
        if kombinacija == None:
            return self.kako_kaze
        self.kako_kaze = []
        for i in range(0, 4):
            if self.nakljucna_izbira[i] == kombinacija[i]:
                self.kako_kaze.append('B')
            elif kombinacija[i] in self.nakljucna_izbira:
                self.kako_kaze.append('W')
            else:
                self.kako_kaze.append(' ')      
        return self.kako_kaze



    

def nova_igra():
    mozne_izbire = ['Y', 'O', 'R', 'B', 'G', 'V']
    nakljucna_izbira = []
    prvi = random.choice(mozne_izbire)
    nakljucna_izbira.append(prvi)
#   mozne_izbire.remove(prvi)
    drugi = random.choice(mozne_izbire)
#   mozne_izbire.remove(drugi)
    nakljucna_izbira.append(drugi)
    tretji = random.choice(mozne_izbire)
#   mozne_izbire.remove(tretji)
    nakljucna_izbira.append(tretji)
    cetrti = random.choice(mozne_izbire)
    nakljucna_izbira.append(cetrti)
    nakljucna_izbira = ''.join(nakljucna_izbira)
    return Igra(nakljucna_izbira)
#z odstranitvijo '#' se igralne barve ne ponavljajo več



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
    
    def ugibaj(self, id_igre, kombinacija):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(kombinacija)
        self.igre[id_igre] = (igra, poskus)
        return id_igre
