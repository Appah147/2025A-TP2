"""
TP2 - Exercice 2 : File d'attente des commandes
"""

def calculer_priorite(commande):
    """
    Calcule la priorité d'une commande selon l'algorithme défini.
    
    Args:
        commande (dict): Dictionnaire contenant:
            - 'temps_attente': temps d'attente en minutes
            - 'nombre_items': nombre d'items dans la commande
            - 'client_vip': booléen, True si client VIP
    
    Returns:
        int: Score de priorité
    """
    score = 0
    
    # TODO: Implémenter l'algorithme de priorité
    # Score = (temps_attente × 2) + (nombre_items × 1) + (client_vip × 10)
    
    vip = 1 if commande.get("client_vip", 0) == True else 0
    score = (commande.get('temps_attente', 0) * 2) + (commande.get('nombre_items')) + (vip)*10
    
    return score


def trier_commandes(liste_commandes):
    """
    Trie les commandes par ordre de priorité décroissante.
    Utilise l'algorithme de tri à bulles adapté.
    
    Args:
        liste_commandes (list): Liste de dictionnaires de commandes
    
    Returns:
        list: Liste triée par priorité décroissante
    """
    # TODO: Implémenter un algorithme de tri (suggestion: tri à bulles)
    # Les commandes avec le score le plus élevé doivent être en premier

    n = len(liste_commandes)
    commandesTriees = liste_commandes.copy()

    for i in range(n):
        
        for j in range(0, n - i - 1):
            priorite1 = calculer_priorite(commandesTriees[j])
            priorite2 = calculer_priorite(commandesTriees[j + 1])

            if priorite1 < priorite2:
                commandesTriees[j], commandesTriees[j + 1] = commandesTriees[j + 1], commandesTriees[j]
            
    return commandesTriees


def estimer_temps_total(liste_commandes_triee):
    """
    Estime le temps total pour traiter toutes les commandes.
    
    Args:
        liste_commandes_triee (list): Liste triée de commandes
    
    Returns:
        dict: Temps total et temps moyen par commande
    """
    temps_stats = {}
    
    # TODO: Calculer le temps total et moyen
    # Chaque item prend en moyenne 3 minutes à préparer

    tempsTotal = 0

    for commande in liste_commandes_triee:
        nbItems = commande.get('nombre_items', 0)
        tempsTotal += nbItems * 3
    
    tempsMoyen = tempsTotal/len(liste_commandes_triee) if liste_commandes_triee else 0

    temps_stats = {
        'temps_total': tempsTotal,
        'temps_moyen': tempsMoyen
    }
    
    return temps_stats


def identifier_commandes_urgentes(liste_commandes, seuil_attente=30):
    """
    Identifie les commandes urgentes (attente > seuil).
    
    Args:
        liste_commandes (list): Liste de commandes
        seuil_attente (int): Seuil d'attente en minutes
    
    Returns:
        list: Liste des numéros de commandes urgentes
    """
    commandes_urgentes = []
    
    # TODO: Identifier les commandes avec temps_attente > seuil

    for commande in liste_commandes:
        if commande.get('temps_attente', 0) > seuil_attente:
            commandes_urgentes.append(commande['numero'])
    
    return commandes_urgentes


if __name__ == '__main__':
    # Test des fonctions
    commandes_test = [
        {'numero': 1, 'temps_attente': 10, 'nombre_items': 3, 'client_vip': False},
        {'numero': 2, 'temps_attente': 25, 'nombre_items': 2, 'client_vip': True},
        {'numero': 3, 'temps_attente': 5, 'nombre_items': 5, 'client_vip': False},
        {'numero': 4, 'temps_attente': 35, 'nombre_items': 1, 'client_vip': False},
        {'numero': 5, 'temps_attente': 15, 'nombre_items': 4, 'client_vip': True},
    ]
    
    # Test de calcul de priorité
    print("Priorités des commandes:")
    for cmd in commandes_test:
        priorite = calculer_priorite(cmd)
        print(f"  Commande {cmd['numero']}: priorité = {priorite}")
    
    # Test du tri
    commandes_triees = trier_commandes(commandes_test.copy())
    print("\nCommandes triées par priorité:")
    for cmd in commandes_triees:
        print(f"  Commande {cmd['numero']} (priorité: {calculer_priorite(cmd)})")
    
    # Test estimation temps
    temps_stats = estimer_temps_total(commandes_triees)
    print(f"\nTemps de traitement estimé:")
    print(f"  Total: {temps_stats.get('temps_total', 0)} minutes")
    print(f"  Moyen: {temps_stats.get('temps_moyen', 0):.1f} minutes/commande")
    
    # Test commandes urgentes
    urgentes = identifier_commandes_urgentes(commandes_test)
    print(f"\nCommandes urgentes (>30 min): {urgentes}")
