import os

print("\n================ Bienvenue sur le Jeu du Pendu ================\n")
print("\tVous avez 10 tentatives pour trouver l'integralité du mot\n")

while True:

    word = []
    word_reveale = []
    list_letters = []
    attempt = 0

    player1_word = input("\t\tSaisir votre mot de minimum 3 lettres: ")
    while player1_word.isdigit() == True or player1_word.isalpha() == False or len(player1_word) <= 3:
        player1_word = input("\n\tCe n'est pas un mot valide !\nSaisir votre mot de mincd imum 3 lettres: ")

    clear = lambda: os.system('cls')
    clear()

    for i in range(len(player1_word)):
        word_reveale.append("*")

    word_reveale_join = " ".join(word_reveale)
    print(f"Le mot fait {len(player1_word)} lettres: \n\n" + word_reveale_join)

    word.append(list(player1_word.lower()))
    word_join = " ".join(word[0])

    while attempt < 10:
        attempt += 1

        player_attempt = input("\nProposer une lettre: ")
        while player_attempt.isdigit() == True or player_attempt.isalpha() == False or len(player_attempt) > 1 or len(player_attempt) < 1:
            player_attempt = input("\nCe n'est pas une valeur valide !\nProposer une lettre: ")

        while player_attempt in list_letters:
            player_attempt = input(f"\nVous avez deja entrer cette lettre.\n\n{list_letters_join}.\n\nProposer une autre lettre: \n")
        else:
            list_letters.append(player_attempt)
            list_letters_join = " ".join(list_letters)
            print(f"\nListe des lettres:\n\n{list_letters_join}\n")

        if player_attempt in word[0]:
            for i in range(len(player1_word)):
                if word[0][i] == player_attempt:
                    word_reveale[i] = player_attempt
                    word_reveale_join = " ".join(word_reveale)

            print(f"Vous avez trouvé la lettre '{player_attempt}'.")
            print("\n" + word_reveale_join)

        else:
            print(f"La lettre '{player_attempt}' n'est pas dans le mot.")
            print("\n" + word_reveale_join)

        if "*" not in word_reveale:
            print(f"\nVous avez gagné !\nVous avez découvert le mot '{player1_word}'.")
            break
    else:
        last_attempt = input("\n\nIl ne vous reste plus aucune tentative.\n\nVoulez vous tenter le mot en entier ?\n\nOui: 0\nNon: 1\nVotre saisie: ")
        while last_attempt.isdigit() == False or int(last_attempt) != 0 and int(last_attempt) != 1:
            last_attempt = input("\nCe n'est pas une valeur valide !\nVoulez vous recommencer une partie ?\n\nOui: 0\nNon: 1\nVotre saisie: ")

        if int(last_attempt) == 0:
            last_attempt_word = input("Entrer votre dernière tentative: ")
            while last_attempt_word.isdigit() == True or last_attempt_word.isalpha() == False or len(last_attempt_word) <= 3:
                last_attempt_word = input("\nValeur non valide !\nEntrer votre dernière tentative: ")

            if last_attempt_word == player1_word:
                print(f"\nVous avez gagné !\nVous avez découvert le mot '{player1_word}'.\n")
            else:
                print(f"\nVous avez perdu... Le mot était {player1_word}.\n")

    repeat = input("\nVoulez vous recommencer une partie ?\n\nOui: 0\nNon: 1\nVotre saisie: \n")
    while repeat.isdigit() == False or int(repeat) != 0 and int(repeat) != 1:
        repeat = input("\nCe n'est pas une valeur valide !\nVoulez vous recommencer une partie ?\n\nOui: 0\nNon: 1\nVotre saisie: ")

    if int(repeat) == 0:
        continue
    else:
        print(exit())

