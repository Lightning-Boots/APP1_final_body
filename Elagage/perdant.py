
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

def trouver_le_pire_coup(allumettes, Coup_max, alpha, beta):
    pire_coup=None
    pire_score = float('inf')
    alpha = float('-inf')
    beta = float('inf')

    for prise in range(1, max(Coup_max + 1, allumettes + 1)):
        score = albet(allumettes - prise, False, alpha, beta)  
        if score > pire_score:
            pire_score = score
            pire_coup = prise
    return pire_coup



        
