####################################
def albet(allumettes, est_maximisant, alpha, beta):
    if allumettes == 0:
        return +1 if est_maximisant else -1  # -1 perdu, +1 gagné

    if est_maximisant:
        meilleur_score = float('-inf')
        for coup in range(1, min(4, allumettes + 1)):
            score = albet(allumettes - coup, False, alpha, beta)
            meilleur_score = max(meilleur_score, score)
            alpha = max(alpha, score)
            
            
            if beta <= alpha:
                break  
            
            
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for coup in range(1, min(4, allumettes + 1)):
            score = albet(allumettes - coup, True, alpha, beta)
            meilleur_score = min(meilleur_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  
        return meilleur_score

def trouver_meilleur_coup(allumettes):
    meilleur_coup = None
    meilleur_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    
    for prise in range(1, min(4, allumettes + 1)):
        score = albet(allumettes - prise, False, alpha, beta)  
        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = prise
    
    return meilleur_coup

def jouer_nim():
    allumettes = 13  
    est_tour_joueur = True  # Le joueur commence
    
    while allumettes > 0:
        print(f"Allumettes restantes : {allumettes}")
        
        if est_tour_joueur:
            coup = int(input("Combien d'allumettes ? (1, 2 ou 3) : "))
            while coup < 1 or coup > 3 or coup > allumettes:
                coup = int(input("Coup invalide. Prenez entre 1 et 3 allumettes : "))
        else:
            coup = trouver_meilleur_coup(allumettes)
            print(f"L'IA prend {coup} allumettes.")
        
        allumettes -= coup  # Mise à jour des coups
        est_tour_joueur = not est_tour_joueur  # Changement de joueur
    
    if est_tour_joueur:
        print("Le joueur gagne")
    else:
        print("L'IA gagne")

# Lancement du jeu    
jouer_nim()
