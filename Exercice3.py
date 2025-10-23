"""
TP2 - Exercice 3 : Optimisation de l'inventaire
"""

def verifier_disponibilite(inventaire, recette):
    """
    Vérifie si on a assez d'ingrédients pour préparer une recette.
    
    Args:
        inventaire (dict): Stock actuel {ingredient: quantité}
        recette (dict): Ingrédients nécessaires {ingredient: quantité}
    
    Returns:
        tuple: (bool, list) - (Peut préparer?, Liste des ingrédients manquants)
    """
    peut_preparer = True
    ingredients_manquants = []
    
    # TODO: Vérifier pour chaque ingrédient de la recette
    # s'il est disponible en quantité suffisante dans l'inventaire

    for ingredient, quantiteNecessaire in recette.items():
        quantiteStock = inventaire.get(ingredient, 0)
        
        if quantiteStock < quantiteNecessaire:
            peut_preparer = False
            manquant = quantiteNecessaire - quantiteStock
            ingredients_manquants.append((ingredient, manquant))
    
    return peut_preparer, ingredients_manquants


def mettre_a_jour_inventaire(inventaire, recette, quantite=1):
    """
    Met à jour l'inventaire après la préparation d'une recette.
    
    Args:
        inventaire (dict): Stock actuel
        recette (dict): Ingrédients utilisés
        quantite (int): Nombre de fois que la recette est préparée
    
    Returns:
        dict: Inventaire mis à jour
    """
    nouvel_inventaire = inventaire.copy()
    
    # TODO: Soustraire les ingrédients utilisés de l'inventaire
    # Multiplier par la quantité si plusieurs portions

    for ingredient, quantiteUtilisee in recette.items():
        if ingredient in nouvel_inventaire:
            nouvel_inventaire[ingredient] -= quantiteUtilisee * quantite
  
            if nouvel_inventaire[ingredient] < 0:
                nouvel_inventaire[ingredient] = 0
    
    return nouvel_inventaire


def generer_alertes_stock(inventaire, seuil=10):
    """
    Génère des alertes pour les ingrédients en rupture de stock.
    
    Args:
        inventaire (dict): Stock actuel
        seuil (int): Seuil minimal avant alerte
    
    Returns:
        dict: {ingredient: (quantité_actuelle, quantité_à_commander)}
    """
    alertes = {}
    quantite_standard = 50  # Quantité standard à commander
    
    # TODO: Identifier les ingrédients avec stock < seuil
    # Suggérer une quantité à commander (ex: 50 unités - stock_actuel)

    for ingredient, quantite_actuelle in inventaire.items():
        if quantite_actuelle < seuil:
            quantite_a_commander = quantite_standard - quantite_actuelle

            if quantite_a_commander > 0:
                alertes[ingredient] = (quantite_actuelle, quantite_a_commander)
    
    return alertes


def calculer_commandes_possibles(inventaire, menu_recettes):
    """
    Calcule combien de fois chaque plat peut être préparé avec l'inventaire actuel.
    
    Args:
        inventaire (dict): Stock actuel
        menu_recettes (dict): {nom_plat: {ingredient: quantité}}
    
    Returns:
        dict: {nom_plat: nombre_portions_possibles}
    """
    commandes_possibles = {}
    # initiation vers l'infini
    nb_portions = 10000000
    temp = 0
    nomCommande = ""
    
    # TODO: Pour chaque plat, calculer combien de portions peuvent être faites
    # Le minimum est déterminé par l'ingrédient le plus limitant (on pourra initialiser une variable nb_portions = infini dans un premier temps)
    for plats, recette in menu_recettes.items():
        nomCommande = plats
        for ingredients, quantite in recette.items():
            temp = inventaire[ingredients] // quantite
            if temp < nb_portions:
                nb_portions = temp

        commandes_possibles[nomCommande] = nb_portions
        nb_portions = 10000000

    return commandes_possibles


def optimiser_achats(inventaire, menu_recettes, previsions_ventes, budget):
    """
    Optimise les achats d'ingrédients selon les prévisions de ventes.
    
    Args:
        inventaire (dict): Stock actuel
        menu_recettes (dict): Recettes des plats
        previsions_ventes (dict): {nom_plat: nombre_previsions}
        budget (float): Budget disponible pour les achats
    
    Returns:
        dict: Liste d'achats optimisée {ingredient: quantité_à_acheter}
    """
    liste_achats = {}
    cout_ingredients = {'tomates': 0.5, 'fromage': 2.0, 'pâtes': 1.0, 'sauce': 1.5, 'pain': 0.8}
    
    # TODO: Calculer les besoins totaux selon les prévisions
    # Soustraire l'inventaire actuel
    # Optimiser selon le budget disponible (prioriser les ingrédients critiques)
        
    for plats, quantite in previsions_ventes.items():
        for ingredient, qteParPlat in menu_recettes[plats].items():
            besoin = qteParPlat * quantite
            stock = inventaire.get(ingredient, 0)
            if besoin > stock:
                liste_achats[ingredient] = liste_achats.get(ingredient, 0) + (besoin - stock)
    
    coutIngredients = 0
    for ing, qte in liste_achats.items():
        coutIngredients += qte * cout_ingredients[ing]
    
    if coutIngredients > budget:
        importance = {}
        for plat in previsions_ventes:
            for ing in menu_recettes[plat]:
                importance[ing] = importance.get(ing, 0) + 1
        
        newAchats = {}
        budget_restant = budget

        for ing in liste_achats:
            qte = liste_achats[ing]
            cout = qte * cout_ingredients[ing]

            if cout <= budget_restant:
                newAchats[ing] = qte
                budget_restant -= cout
            else:
                newAchats[ing] = int(budget_restant / cout_ingredients[ing])
                break

        liste_achats = newAchats
    
    return liste_achats


if __name__ == '__main__':
    # Test de l'inventaire
    inventaire_test = {
        'tomates': 50,
        'fromage': 30,
        'pâtes': 100,
        'sauce': 25,
        'pain': 40
    }
    
    recettes_test = {
        'Pizza': {'tomates': 5, 'fromage': 3, 'pain': 2},
        'Pâtes': {'pâtes': 10, 'sauce': 2, 'fromage': 1},
        'Sandwich': {'pain': 2, 'tomates': 2, 'fromage': 1}
    }
    
    # Test vérification disponibilité
    print("Test de disponibilité:")
    for plat, recette in recettes_test.items():
        dispo, manquants = verifier_disponibilite(inventaire_test, recette)
        status = "✓ Disponible" if dispo else f"✗ Manque: {manquants}"
        print(f"  {plat}: {status}")
    
    # Test mise à jour inventaire
    print("\nMise à jour après commande de 3 Pizzas:")
    nouvel_inventaire = mettre_a_jour_inventaire(inventaire_test, recettes_test['Pizza'], 3)
    for ingredient in ['tomates', 'fromage', 'pain']:
        print(f"  {ingredient}: {inventaire_test[ingredient]} → {nouvel_inventaire.get(ingredient, 0)}")
    
    # Test alertes
    alertes = generer_alertes_stock(nouvel_inventaire, seuil=20)
    if alertes:
        print("\n⚠️ Alertes de stock:")
        for ingredient, (actuel, a_commander) in alertes.items():
            print(f"  {ingredient}: {actuel} unités (commander {a_commander})")
    
    # Test commandes possibles
    possibles = calculer_commandes_possibles(inventaire_test, recettes_test)
    print("\nNombre de portions possibles:")
    for plat, nb in possibles.items():
        print(f"  {plat}: {nb} portions")
    
    # Test optimisation achats
    previsions = {'Pizza': 20, 'Pâtes': 15, 'Sandwich': 10}
    budget = 100.0
    achats = optimiser_achats(inventaire_test, recettes_test, previsions, budget)
    if achats:
        print(f"\nPlan d'achats optimisé (budget: {budget}€):")
        for ingredient, quantite in achats.items():
            print(f"  {ingredient}: {quantite} unités")
