navnet = input('Skriv navn: ')
print('Dit navn er', navnet,'?','Ad...')


while True: #loop indtil du giver int
    etTal = input("Gib Number: ") #dit input
    try:
        val = int(etTal) #Er dit value input et nummer/int?
        break;
    except ValueError:
        print('det er ikke et nummer din kejle') #It's not an int

while True: #Same before
    etGodTal = input('Gib Another Number: ') #dit andet input
    try:
        val = int(etGodTal) #er dit andet input et nummer/int?
        break;
    except ValueError:
        print('Det er ikke et nummer din kejle') #it's not an input... Do you not learn from your mistakes?

summer = int(etTal)+int(etGodTal #Lave ens input om til int så de kan plusses sammen


print('Summen af ', etTal, 'og ', etGodTal, 'tilsammen giver', summer, '. Du er så dum', navnet) #print svar og end

