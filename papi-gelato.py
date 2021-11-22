def bolletjes():
    aantal = input('hoeveel bolletjes wilt u? ')
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
                keuze2 = input('Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N) '.format(a, aantal))
                if keuze2 == 'y' or keuze2 == 'Y':
                    return bolletjes()
                elif keuze2 == 'n' or keuze2 == 'N':
                    print(klaar)
                    exit()
                else:
                    print(fout)
                    return bolletjes()

            elif keuze1 == 'b' or keuze1 == 'B':
                b = 'bakje'
                keuze3 = input('Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N) '.format(b, aantal))
                if keuze3 == 'y' or keuze3 == 'Y':
                    return bolletjes()
                elif keuze3 == 'n' or keuze3 == 'N':
                    print(klaar)
                    exit()
                else:
                    print(fout)
                    return bolletjes()

            else:
                print(fout)
                return bolletjes()

        elif 4 <= aantal <= 8:
            for c in range(aantal):
                nummer += 1
                smaak = input('welke smaak wilt u voor bolletje {} A) aardbei C) chocolade M) munt of V) vanille? '.format(nummer))

            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
            keuze4 = input('wilt u nog meer bestellen? (Y/N) ')
            if keuze4 == 'y' or keuze4 == 'Y':
                return bolletjes()
            elif keuze4 == 'n' or keuze4 == 'N':
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
    

bolletjes()