print('welkom bij Papi Gelato')
aantalBollen = 0
hoorntjes = 0
bakjes = 0


def bolletjes():
    global aantalBollen
    global hoorntjes
    global bakjes

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
                b = 'bakje'
                bakjes += 1
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
            bakjes += 1
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
    totaal = aantalBollen * 1.10 + hoorntjes * 1.25 + bakjes * 0.75
    print('   -----"papi gelato"-----')
    print('bolletjes     {} x 1.10   = '.format(aantalBollen) + '{:.2f}'.format(aantalBollen * 1.10))
    print('hoorntjes     {} x 1.25   = '.format(hoorntjes) + '{:.2f}'.format(hoorntjes * 1.25))
    print('bakje         {} x 0.75   = '.format(bakjes) + '{:.2f}'.format(bakjes * 0.75))
    print('                         ----------- +')
    print('totaal                   = ', '€', totaal)
    

bolletjes()