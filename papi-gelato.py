print('welkom bij Papi Gelato')
aantalBollen = 0
hoorntjes = 0
bakjes = 0
slagroom = 0
sprinkles = 0
caramelSaus = 0
caramelPrijs = 0.60
aantalLiter = 0


def bolletjes():
    global aantalBollen
    global hoorntjes
    global bakjes
    global caramelPrijs

    aantal = input('hoeveel bolletjes wilt u? ')
    aantalBollen += int(aantal)
    fout = 'sorry dit begrijp ik niet'
    klaar = 'bedankt en tot ziens!'
    nummer = 0
    
    if aantal.isdigit():
        aantal = int(aantal)
        if aantal <= 3:

            for c in range(aantal):
                nummer += 1
                smaak = input('welke smaak wilt u voor bolletje {} A) aardbei C) chocolade M) munt of V) vanille? '.format(nummer))
                if smaak == 'a' or smaak == 'A' or smaak == 'c' or smaak == 'C' or smaak == 'm' or smaak == 'M' or smaak == 'v' or smaak == 'V':
                    pass
                else:
                    print(fout)

                    return bolletjes()

            keuze1 = input('wilt u deze {} bolletjes in A) een hoorntje of B) een bakje? '.format(aantal))
            
            if keuze1 == 'a' or keuze1 == 'A':
                a = 'hoorntje'
                hoorntjes += 1
                topping()
                keuze2 = input('Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N) '.format(a, aantal))
                if keuze2 == 'y' or keuze2 == 'Y':
                    return bolletjes()
                elif keuze2 == 'n' or keuze2 == 'N':
                    bon()
                    print(klaar)
                    exit()
                else:
                    print(fout)
                    return bolletjes()

            elif keuze1 == 'b' or keuze1 == 'B':
                caramelPrijs = 0.90
                b = 'bakje'
                bakjes += 1
                topping()
                keuze3 = input('Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N) '.format(b, aantal))
                if keuze3 == 'y' or keuze3 == 'Y':
                    return bolletjes()
                elif keuze3 == 'n' or keuze3 == 'N':
                    bon()
                    print(klaar)
                    exit()
                else:
                    print(fout)
                    return bolletjes()

            else:
                print(fout)
                return bolletjes()

        elif 4 <= aantal <= 8:
            caramelPrijs = 0.90
            bakjes += 1
            topping()
            for c in range(aantal):
                nummer += 1
                smaak = input('welke smaak wilt u voor bolletje {} A) aardbei C) chocolade M) munt of V) vanille? '.format(nummer))

            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
            keuze4 = input('wilt u nog meer bestellen? (Y/N) ')
            if keuze4 == 'y' or keuze4 == 'Y':
                return bolletjes()
            elif keuze4 == 'n' or keuze4 == 'N':
                bon()
                print(klaar)
                exit()
            else:
                print(fout)
                return bolletjes()

        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
            return bolletjes()
    else:
        print(fout)
        return bolletjes()

def bon():
    global caramelPrijs
    slagroomPrijs = 0.50
    sprinkelsPrijs = 0.30
    totaal = aantalBollen * 1.10 + hoorntjes * 1.25 + bakjes * 0.75 + slagroom * slagroomPrijs + sprinkles * sprinkelsPrijs + caramelSaus * caramelPrijs
    print('   -----"papi gelato"-----')
    print('bolletjes     {} x 1.10   = €'.format(aantalBollen) + '{:.2f}'.format(aantalBollen * 1.10))
    print('hoorntjes     {} x 1.25   = €'.format(hoorntjes) + '{:.2f}'.format(hoorntjes * 1.25))
    print('bakje         {} x 0.75   = €'.format(bakjes) + '{:.2f}'.format(bakjes * 0.75))
    print('topping                   = € {}'.format(slagroom * slagroomPrijs + sprinkles * sprinkelsPrijs + caramelSaus * caramelPrijs))
    print('                         ----------- +')
    print('totaal                   = €{:.2f}'.format(totaal))

def topping():
    global slagroom
    global sprinkles
    global caramelSaus
    vraag = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
    if vraag == 'a' or vraag == 'a':
        slagroom += 0
        sprinkles += 0
        caramelSaus += 0
    elif vraag == 'b' or vraag == 'B':
        slagroom += 1
    elif vraag == 'c' or vraag == 'C':
        sprinkles += 1
    elif vraag == 'd' or vraag == 'D':
        caramelSaus += 1
    else:
        print('sorry dit begrijp ik niet')
        return topping()

def zakelijk():
    nummer = 0
    vraag = input('bent u A) particulier of B) zakelijk ')
    if vraag == 'a' or vraag == 'A':
        return bolletjes()
    elif vraag == 'b' or vraag == 'B':
        amount = int(input('hoeveel liter ijs wilt u kopen '))
    else:
        print('sorry dat begrijp ik niet')
    
    if amount:
        global aantalLiter
        aantalLiter += int(amount)
        for i in range(amount):
            nummer += 1
            smaak = input('welke smaak wilt u voor liter {} A) aardbei C) chocolade M) munt of V) vanille? '.format(nummer))
        vraag2 = input('wilt u nog meer bestellen? Y/N ')
        if vraag2 == 'Y' or vraag2 == 'y':
            return zakelijk
        elif vraag2 == 'N' or vraag2 == 'n':
            return zakelijkBon()
        
    pass

def zakelijkBon():
    prijs = aantalLiter * 9.80
    print('   -----"papi gelato"-----')
    print('liter        {} x €9.80  = €{} '.format(aantalLiter, aantalLiter * 9.80))
    print('totaal                   = €{} '.format(aantalLiter * 9.80))
    print('btw (9%)                 = €{} '.format(prijs / 100 * 9))
    
zakelijk()
bolletjes()