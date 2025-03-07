"""Code du mode de jeu gagnant de l'IA"""

def minimax(allumettes, est_maximisant, Coup_max):
    # Condition d'arrêt 
    if allumettes == 0:
        return +1 if est_maximisant else -1#-1 perdu, +1 gagné

    scores = []
    for coup in range(1, min(Coup_max +1 , allumettes + 1)):
        # simulation de la partie 
        score = minimax(allumettes - coup, not est_maximisant, Coup_max)
        scores.append(score)

    return max(scores) if est_maximisant else min(scores)

#choisit le meilleur coup
def trouver_meilleur_coup(allumettes, Coup_max):
    meilleur_coup = None
    # ajout chat gpt
    meilleur_score = float('-inf')

    for prise in range(1, min(Coup_max + 1, allumettes + 1)):
        score = minimax(allumettes - prise, False, Coup_max)# L'adversaire joue après ce coup
        if score > meilleur_score:
            # meilleur coup déterminer
            meilleur_score = score
            meilleur_coup = prise
    return meilleur_coup



