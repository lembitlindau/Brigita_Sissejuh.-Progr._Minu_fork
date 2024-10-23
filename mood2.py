# Kasutajalt küsitakse ettevõtte nime ja salvestatakse see muutuja nimi alla.
nimi = input('Sisesta firma nimi: ')

# Kasutajalt küsitakse toote nimetus ja salvestatakse see muutuja toode alla.
toode = input('Sisesta toote nimetus: ')

# Sõnastik laoseis hoiab kolme toote nimetust (kleit, särk, püksid) ja nende vastavat laoseisu (kogust laos).
laoseis = {
    'kleit': 5,
    'särk': 1,
    'püksid': 0
}

# Muutuja minimaalne_laoseis hoiab endas väärtust 3.
minimaalne_laoseis = 3

# Funktsioon kontrolli_laoseisu võtab argumendiks toote ja koguse ning kontrollib, kas kogus on 0, väiksem kui minimaalne_laoseis või suurem või võrdne minimaalse laoseisuga.
def kontrolli_laoseisu (toode, kogus):
    if kogus == 0:
        print(f"{toode}: Laost otsas! Telli kohe juurde.")
    elif kogus < minimaalne_laoseis:
        print(f"{toode}: Lähiajal vaja juurde tellida. Laoseis: {kogus}")
    else:
        print(f"{toode}: Laoseis on piisav. Laoseis: {kogus}")

# Tsükkel läbib iga elemendi sõnastikust laoseis, eraldades toote ja selle koguse. Iga toote kohta kutsutakse välja funktsioon kontrolli_laoseisu, et vaadata, kas laoseis on piisav.
for toode, kogus in laoseis.items():
    kontrolli_laoseisu(toode, kogus)

# Prinditakse tervitus koos kasutaja sisestatud firma nime ja toote infoga. Kui kasutaja sisestatud toote nimetus on laoseis sõnastikus olemas, kuvatakse selle laoseis. Kui toodet ei ole laoseisus, kuvatakse tekst "Toode ei ole laoseisus".
print(f'Tere, {nimi}. Teie laoseis tootele {toode} on {laoseis.get(toode, "Toode ei ole laoseisus")}.')