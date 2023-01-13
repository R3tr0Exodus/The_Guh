navnet = input('Skriv navn: ')
print('Dit navn er', navnet,'?','Ad...')

while True:
    etTal = input("Gib Number: ")
    try:
        val = int(etTal)
        break;
    except ValueError:
        print('det er ikke et nummber din kejle')

while True:
    etGodTal = input('Gib Another Number: ')
    try:
        val = int(etGodTal)
        break;
    except ValueError:
        print('Det er ikke et nummber din kejle')

summer = int(etTal)+int(etGodTal)


print('Summen af ', etTal, 'og ', etGodTal, 'tilsammen giver', summer, '. Du er så dum', navnet)

