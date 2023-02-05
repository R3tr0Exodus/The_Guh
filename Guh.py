Limit = 1000000

navnet = input('Skriv navn: ')
print('Dit navn er', navnet,'?','Ad... Anyways, lad os ligge 2 tal sammen')


while True: #loop indtil du giver int
    etTal = input("Gib Number:\n") #dit input
    try:
        val = int(etTal) #Er dit value input et nummer/int?
        if val <= Limit: #checker for om dit input val er mindre en det tal skrevet ind
            break
        else:
            print('For mange tal. Max input er', Limit)
    except ValueError:
            print('Det er ikke et nummer din kejle') #It's not an int


while True: #Same before
    etGodTal = input('Gib Another Number:\n') #dit andet input
    try:
        val = int(etGodTal) #er dit andet input et nummer/int?
        if val <= Limit: #checker for om dit input val er mindre en det tal skrevet ind
            break
        else:
            print('For mange tal. Max input er', Limit)
    except ValueError:
        print('Det er ikke et nummer din kejle') #it's not an input... Do you not learn from your mistakes?

summer = int(etTal)+int(etGodTal) #Lave ens input om til int så de kan plusses sammen


print('Summen af ', etTal, 'og ', etGodTal, 'tilsammen giver', summer, '. Du er så dum', navnet) #print svar og end

