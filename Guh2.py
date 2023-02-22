Limit = 1000000

navnet = input('Skriv navn: ')
print('Dit navn er', navnet,'?','Ad... Anyways, lad os ligge 2 tal sammen')


def godTal():
    etTal = input("Gib Number:\n") #dit input
    try:
        if int(etTal) <= Limit: #checker for om dit input val er mindre en det tal skrevet ind
            return int(etTal)
        else:
            print('For mange tal. Max input er', Limit)
            return godTal()
    except ValueError:
            print('Det er ikke et nummer din kejle') #It's not an int
            return godTal()


def bedreTal():
    etGodTal = input('Gib Another Number:\n') #dit andet input
    try:
        if int(etGodTal) >= Limit: #checker for om dit input val er mindre en det tal skrevet ind
            print('For mange tal. Max input er', Limit)
            return bedreTal()
        else:
            return int(etGodTal)
    except ValueError:
        print('Det er ikke et nummer din kejle') #it's not an input... Do you not learn from your mistakes?
        return bedreTal()

first = godTal()
second = bedreTal()
summer = int(first)+int(second)#Lave ens input om til int så de kan plusses sammen


print('Summen af ', first, 'og ', second, 'tilsammen giver', summer, '. Du er så dum', navnet) #print svar og end

