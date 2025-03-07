def initialiser_plateau():
    """Crée un plateau de Tic-Tac-Toe vide."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def est_fin_du_jeu(plateau):
    """Vérifie si le jeu est terminé (victoire ou match nul)."""
    # Vérifier les lignes et colonnes
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != ' ':
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != ' ':
            return True

    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True

    # Vérifier si le plateau est rempli
    for ligne in plateau:
        for case in ligne:
            if case == ' ':
                return False  # Il reste des coups possibles

    return True  # Match nul

def evaluer_plateau(plateau):
    """Évalue l'état du plateau : 1 si 'X' gagne, -1 si 'O' gagne, 0 sinon."""
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2]:
            if plateau[i][0] == 'X':
                return 1
            elif plateau[i][0] == 'O':
                return -1
        if plateau[0][i] == plateau[1][i] == plateau[2][i]:
            if plateau[0][i] == 'X':
                return 1
            elif plateau[0][i] == 'O':
                return -1

    if plateau[0][0] == plateau[1][1] == plateau[2][2]:
        if plateau[0][0] == 'X':
            return 1
        elif plateau[0][0] == 'O':
            return -1
    if plateau[0][2] == plateau[1][1] == plateau[2][0]:
        if plateau[0][2] == 'X':
            return 1
        elif plateau[0][2] == 'O':
            return -1

    return 0  # Pas de gagnant

def générer_mouvements(plateau):
    """Retourne une liste des cases vides où un coup peut être joué."""
    mouvements = []
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                mouvements.append((i, j))
    return mouvements

def jouer_mouvement(plateau, mouvement, joueur):
    """Joue un mouvement sur le plateau."""
    i, j = mouvement
    plateau[i][j] = joueur

def annuler_mouvement(plateau, mouvement):
    """Annule un mouvement pour revenir à l'état précédent."""
    i, j = mouvement
    plateau[i][j] = ' '

def minimax(plateau, profondeur, est_maximisant):
    """Implémente l'algorithme Minimax."""
    if est_fin_du_jeu(plateau):
        return evaluer_plateau(plateau)

    if est_maximisant:
        meilleur_score = float('-inf')
        for mouvement in générer_mouvements(plateau):
            jouer_mouvement(plateau, mouvement, 'X')
            score = minimax(plateau, profondeur + 1, False)
            annuler_mouvement(plateau, mouvement)
            meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float('inf')
        for mouvement in générer_mouvements(plateau):
            jouer_mouvement(plateau, mouvement, 'O')
            score = minimax(plateau, profondeur + 1, True)
            annuler_mouvement(plateau, mouvement)
            meilleur_score = min(meilleur_score, score)
        return meilleur_score
    