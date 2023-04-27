def compter_mots(chaine):

#Gérer l'entrée de chaîne vide
    if not chaine:
        return 0

#Supprimer les espaces de début et de fin
    input_str = chaine.strip()

    nb_mots = 1

    for char in input_str:

        if char == ' ':

            nb_mots += 1

    return nb_mots