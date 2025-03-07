
def alphabeta(plateau, profondeur, alpha, beta, est_maximisant):
    if est_fin_du_jeu(plateau):
        return évaluer_plateau(plateau)

    if est_maximisant:
        meilleur_score = float('-inf')
        for mouvement in générer_mouvements(plateau):
            jouer_mouvement(plateau, mouvement, 'X')
            score = alphabeta(plateau, profondeur + 1, alpha, beta, False)
            annuler_mouvement(plateau, mouvement)
            meilleur_score = max(meilleur_score, score)
            alpha = max(alpha, meilleur_score)
            if beta <= alpha:
                break
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for mouvement in générer_mouvements(plateau):
            jouer_mouvement(plateau, mouvement, 'O')
            score = alphabeta(plateau, profondeur + 1, alpha, beta, True)
            annuler_mouvement(plateau, mouvement)
            meilleur_score = min(meilleur_score, score)
            beta = min(beta, meilleur_score)
            if beta <= alpha:
                break
        return meilleur_score


def jouer_contre_ordinateur():
    plateau = initialiser_plateau()
    joueur = 'X'

    while not est_fin_du_jeu(plateau):
        if joueur == 'X':
            mouvement = utilisateur_choisir_mouvement(plateau)
        else:
            _, mouvement = minimax(plateau, 0, joueur == 'X')
        jouer_mouvement(plateau, mouvement, joueur)
        joueur = 'O' if joueur == 'X' else 'X'

    afficher_resultat(plateau)