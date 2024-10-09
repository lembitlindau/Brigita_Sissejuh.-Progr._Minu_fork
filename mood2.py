nimi = input('Sisesta firma nimi: ')
toode = input('Sisesta toote nimetus: ')

laoseis = {
    'kleit': 5,
    'särk': 1,
    'püksid': 0
}

minimaalne_laoseis = 3

def kontrolli_laoseisu (toode, kogus):
    if kogus == 0:
        print(f"{toode}: Laost otsas! Telli kohe juurde.")
    elif kogus < minimaalne_laoseis:
        print(f"{toode}: Lähiajal vaja juurde tellida. Laoseis: {kogus}")
    else:
        print(f"{toode}: Laoseis on piisav. Laoseis: {kogus}")

for toode, kogus in laoseis.items():
    kontrolli_laoseisu(toode, kogus)

print(f'Tere, {nimi}. Teie laoseis tootele {toode} on {laoseis.get(toode, "Toode ei ole laoseisus")}.')