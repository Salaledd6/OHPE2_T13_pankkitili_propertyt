class Pankkitili: #luokan määrittely
    tilinumero = 1000001 #luokkakohtainen muuttuja. Kaikilla oliolla pääsy tähän
    def __init__(self, nimi:str): # luokan konstruktori. Tähän tullaan kun luokasta tehdään olio
        self.__nimi = nimi # __nimi on luokan yksityinen muuttuja- ei näy ulos
        self.__saldo = 0
        self.__tilinumero = Pankkitili.tilinumero
        Pankkitili.tilinumero += 1

    def nosto(self, summa:float): # nosto-metodi
        if self.__saldo > summa and summa > 0:
            self.__saldo -= summa
    
    def talletus(self, summa:float): # talletus-metodi
        if summa > 0:
            self.__saldo += summa

    @property # tehdään property. ensin määritellään get eli arvon palautus
    def saldo(self): # tämän "metodin" nimestä tulee propertyn nimi
        return self.__saldo
    
    @saldo.setter # parina edelliselle arvon asetus property
    def saldo(self, arvo:float):
        if arvo >=0:
            self.__saldo = arvo

    def __str__(self):
        return f"{self.__tilinumero}: {self.__nimi}: {self.__saldo}"
    

def main():
    tilit = []
    t1 = Pankkitili("Masa")
    tilit.append(t1)

    tilit.append(Pankkitili("Hilkka"))
    tilit.append(Pankkitili("Pertsa"))

    #palkkapäivä
    for tili in tilit:
        tili.talletus(2000)

    for tili in tilit:
        print(tili)

    tilit[0].nosto(500)

    tilit[0].saldo -= 500

    for tili in tilit:
        print(tili)

    
''' suoritus alkaa tästä '''
if __name__ == "__main__":
    main()