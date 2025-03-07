#simulation des parties

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

#choisis le meilleure coup
def trouver_le_pire_coup(allumettes, Coup_max):
    pire_coup = None
    
    pire_score = float('inf')

    for prise in range(1, max(Coup_max + 1, allumettes + 1)):
        score = minimax(allumettes - prise, False, Coup_max)# L'adversaire joue après ce coup
        if score < pire_score:
            # meilleur coup déterminer
            pire_score = score
            pire_coup = prise
    return pire_coup



        
