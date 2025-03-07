#simulation des parties
def minimax(allumettes, est_maximisant):
    # Condition d'arrêt 
    if allumettes == 0:
        return +1 if est_maximisant else -1#-1 perdu, +1 gagné

    scores = []
    for coup in range(1, min(4, allumettes + 1)):
        # simulation de la partie 
        score = minimax(allumettes - coup, not est_maximisant)
        scores.append(score)

    return max(scores) if est_maximisant else min(scores)

#choisis le meilleure coup
def trouver_meilleur_coup(allumettes):
    meilleur_coup = None
    # ajout chat gpt
    meilleur_score = float('-inf')

    for prise in range(1, min(4, allumettes + 1)):
        score = minimax(allumettes - prise, False)# L'adversaire joue après ce coup
        if score > meilleur_score:
            # meilleur coup déterminer
            meilleur_score = score
            meilleur_coup = prise
    return meilleur_coup


#création partie 
def jouer_nim():
    allumettes = 13  
    est_tour_joueur = True  # le joueur commence
    while allumettes > 0:
        print(f"Allumettes restantes : {allumettes}")
        if est_tour_joueur:
            coup = int(input("Combien d'allumettes ? (1, 2 ou 3) : "))
            while coup < 1 or coup > 3 or coup > allumettes:
                coup = int(input("Coup invalide. Prenez entre 1 et 3 allumettes : "))
        else:
            coup = trouver_meilleur_coup(allumettes)
            print(f"L'IA prend {coup} allumettes.")
        allumettes -= coup # mise à jour des coups
        est_tour_joueur = not est_tour_joueur  # changement de joueur
    if est_tour_joueur:
        print("Le joueur gagne")
    else:
        print("L'IA' gagne ")
        
#lancement du jeu
jouer_nim()