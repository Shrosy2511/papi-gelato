def bolletjes():
    aantal = str(input('hoeveel bolletjes wilt u? '))
    fout = 'sorry dit begrijp ik niet'
    klaar = 'bedankt en tot ziens!'
    
    if aantal.isdigit():
        aantal = int(aantal)
        if aantal <= 3:

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

        elif aantal >= 4 and aantal <= 8:
            print('dan krijgt u van mij een bakje met {} bolletjes'.format(aantal))
            keuze4 = input('wilt u nog meer bestellen? (Y/N) ')
            if keuze4 == 'y' or keuze4 == 'Y':
                return bolletjes()
            elif keuze4 == 'n' or keuze4 == 'N':
                print(klaar)
                exit()

        elif aantal >= 9:
            print('sorry, zulke grote bakken hebben we niet')
    else:
        print(fout)
        return bolletjes()
    

bolletjes()