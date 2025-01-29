def skaitit_vardus(teksts):
    """
    Funkcija, kas skaita vārdus dotajā tekstā.
    :param teksts: Ievades teksts
    :return: Vārdu skaits
    """
    # Sadalīt tekstu vārdos, izmantojot atstarpes kā atdalītāju
    vardi = teksts.split()
    # Atgriezt vārdu skaitu
    return len(vardi)

def skaitit_simbolus(teksts):
    """
    Funkcija, kas skaita simbolus dotajā tekstā.
    :param teksts: Ievades teksts
    :return: Simbolu skaits
    """
    return len(teksts)

# Lietotāja ievade
teksts = input("Ievadiet tekstu: ")

# Aprēķināt vārdu un simbolu skaitu dotajā tekstā
vardu_skaits = skaitit_vardus(teksts)
simbolu_skaits = skaitit_simbolus(teksts)

# Izvadīt oriģinālo tekstu, vārdu un simbolu skaitu
print("Ievadītais teksts:", teksts)
print("Vārdu skaits tekstā:", vardu_skaits)
print("Simbolu skaits tekstā:", simbolu_skaits)
