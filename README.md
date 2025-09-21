# TP2: Simulateur de Restaurant "Python Bistro" 🍳

#### :alarm_clock: Date de remise : Dimanche 19 octobre 2025 à 23h59

## Objectif
Ce TP vous permettra d'apprendre la programmation Python à travers la création d'un simulateur de gestion de restaurant. Vous allez découvrir et maîtriser :
- Les structures de contrôle (boucles, conditions)
- Les structures de données (listes, dictionnaires, tuples)
- Les algorithmes de base (tri, recherche, optimisation)
- La manipulation de données complexes

## Introduction
Félicitations ! Vous venez d'hériter du restaurant familial "Python Bistro". Pour moderniser l'établissement, vous devez créer un système de gestion informatisé qui permettra de :
- Gérer les commandes des clients
- Optimiser l'inventaire des ingrédients
- Calculer les profits
- Créer un système de réservation
- Gérer la satisfaction client

## Structure du TP
Le TP est divisé en 5 exercices indépendants qui simulent différents aspects de la gestion du restaurant.

## Exercice 1: Gestion du Menu (3 points)
Vous devez créer un système pour gérer le menu du restaurant. Le menu est représenté par un dictionnaire où les clés sont les noms des plats et les valeurs sont des tuples contenant (prix, temps_preparation, popularité).

Complétez la fonction `analyser_menu` qui :
- Trouve le plat le plus rentable (rapport popularité/temps_preparation le plus élevé)
- Calcule le prix moyen du menu
- Retourne un dictionnaire avec ces statistiques

**Exemple :**
```python
menu = {
    'Pizza Margherita': (12.50, 15, 8),  # (prix, temps en min, popularité sur 10)
    'Pâtes Carbonara': (14.00, 12, 9),
    'Salade César': (9.50, 5, 6),
    'Tiramisu': (6.00, 3, 10)
}
# Résultat attendu:
# {'plat_plus_rentable': 'Tiramisu', 'prix_moyen': 10.50}
```

## Exercice 2: File d'attente des commandes (3 points)
Les commandes arrivent dans votre cuisine et doivent être traitées selon un algorithme de priorité. Implémentez un système de file d'attente qui trie les commandes selon leur urgence.

**L'algorithme de priorité :**
- Score = (temps_attente × 2) + (nombre_items × 1) + (client_vip × 10)
- Les commandes avec le score le plus élevé sont traitées en premier

Complétez la fonction `trier_commandes` qui implémente cet algorithme de tri.

## Exercice 3: Optimisation de l'inventaire (4 points)
Vous devez gérer l'inventaire des ingrédients. Créez un système qui :
1. Vérifie si vous avez assez d'ingrédients pour une commande
2. Met à jour l'inventaire après chaque commande
3. Génère des alertes pour les ingrédients en rupture de stock (< 10 unités)

**Format des données :**
```python
inventaire = {'tomates': 50, 'fromage': 30, 'pâtes': 100}
recette = {'tomates': 5, 'fromage': 3}  # Ingrédients nécessaires
```

## Exercice 4: Système de réservation (5 points)
Créez un système de réservation de tables pour votre restaurant avec les fonctionnalités suivantes :

### Partie 1: Initialisation (2 points)
Créez une grille représentant la salle du restaurant où :
- `O` = table occupée
- `L` = table libre  
- `R` = table réservée
- `X` = espace non disponible (couloir, cuisine)

### Partie 2: Recherche de table (3 points)
Implémentez un algorithme qui trouve la meilleure table disponible selon :
- La taille du groupe (petites tables pour 2, grandes pour 4+)
- La position (près de la fenêtre = bonus)
- L'état de disponibilité

## Exercice 5: Analyse de la satisfaction client (5 points)
Analysez les commentaires clients pour améliorer votre service. 

Créez un système qui :
1. Analyse les mots-clés dans les commentaires
2. Calcule un score de satisfaction (0-10)
3. Identifie les points à améliorer
4. Génère un rapport de synthèse

**Mots-clés et scores :**
- Positifs : "excellent"(+3), "délicieux"(+2), "rapide"(+1)
- Négatifs : "froid"(-2), "lent"(-3), "décevant"(-2)

## Bonus: Mini-jeu de service (2 points)
Créez un mini-jeu en mode console où le serveur doit :
- Se déplacer dans le restaurant (grille 5x5)
- Prendre les commandes aux tables
- Les apporter à la cuisine
- Servir les plats
- Le tout avec un système de score basé sur la rapidité

**Commandes :**
- `z` : haut
- `s` : bas
- `q` : gauche  
- `d` : droite
- `p` : prendre commande/plat
- `l` : livrer

## Consignes importantes
- Ne modifiez que les sections marquées `TODO`
- N'importez pas de librairies supplémentaires
- Testez votre code avec les exemples fournis
- Respectez les formats de sortie demandés

# Barème de correction

Le barème de correction est le suivant :  

| Partie | Tâche | Points |
|--------|-------|--------|
| **Exercice 1 : Gestion du menu** | | **/3** |
| 1.1 | Calcul correct du plat le plus rentable (ratio popularité/temps, gérer temps = 0) (`analyser_menu`) | 1.0 |
| 1.2 | Calcul du prix moyen du menu (`analyser_menu`) | 0.5 |
| 1.3 | Calcul du temps de préparation moyen (`analyser_menu`) | 0.5 |
| 1.4 | Filtrage du menu par catégorie (`filtrer_menu_par_categorie`) — structure correcte | 0.5 |
| 1.5 | Calcul du profit journalier correct (`calculer_profit`) | 0.5 |
| **Exercice 2 : File d'attente des commandes** | | **/4** |
| 2.1 | Calcul correct du score de priorité (`calculer_priorite`) | 1.0 |
| 2.2 | Tri par priorité décroissante (algorithme fonctionnel, stabilité appréciée) (`trier_commandes`) | 1.0 |
| 2.3 | Estimation du temps total et temps moyen (3 min / item) (`estimer_temps_total`) | 0.75 |
| 2.4 | Identification correcte des commandes urgentes (seuil) (`identifier_commandes_urgentes`) | 0.75 |
| 2.5 | Implémentation robuste du tri (gestion des copies, pas d'effets de bord) | 0.5 |
| **Exercice 3 : Optimisation de l'inventaire** | | **/4** |
| 3.1 | Vérification correcte de la disponibilité d'une recette (`verifier_disponibilite`) | 1.0 |
| 3.2 | Mise à jour de l'inventaire après préparation (multiplie par `quantite`) (`mettre_a_jour_inventaire`) | 1.0 |
| 3.3 | Génération d'alertes de stock (< seuil) et suggestion de quantité à commander (`generer_alertes_stock`) | 0.75 |
| 3.4 | Calcul du nombre de portions possibles par plat (ingrédient limitant) (`calculer_commandes_possibles`) | 0.75 |
| 3.5 | Optimisation des achats selon prévisions et budget (priorisation raisonnable) (`optimiser_achats`) | 0.5 |
| **Exercice 4 : Système de réservation** | | **/4** |
| 4.1 | Initialisation correcte de la salle (grille `X` + placement des tables) (`initialiser_salle`) | 1.0 |
| 4.2 | Marquage des réservations (R2/R4) sans altérer les autres cases (`marquer_reservation`) | 0.5 |
| 4.3 | Calcul du score de table conforme aux règles (gaspillage, fenêtre, entrée) (`calculer_score_table`) | 0.75 |
| 4.4 | Recherche de la meilleure table libre (parcours + comparaison de score) (`trouver_meilleure_table`) | 0.75 |
| 4.5 | Rapport d'occupation correct (comptages et taux d'occupation) (`generer_rapport_occupation`) | 1.0 |
| **Exercice 5 : Analyse de la satisfaction client** | | **/5** |
| 5.1 | Analyse d'un commentaire : détection mots-clés, somme des scores, borne 0–10 (`analyser_commentaire`) | 1.0 |
| 5.2 | Catégorisation correcte des commentaires (positifs ≥7, neutres 4–6, négatifs <4) (`categoriser_commentaires`) | 1.0 |
| 5.3 | Identification des problèmes récurrents dans les commentaires négatifs (`identifier_problemes`) | 1.0 |
| 5.4 | Génération de rapport : satisfaction moyenne + distribution + points d'amélioration (`generer_rapport_satisfaction`) | 1.0 |
| 5.5 | Détection correcte de la tendance à partir d'un historique (`calculer_tendance`) | 1.0 |
| **BONUS (optionnel)** | | **/2** |
| B.1 | Mini-jeu : initialisation correcte de la grille et position cuisine (`initialiser_restaurant`) | 0.5 |
| B.2 | Déplacement serveur valide et borné (`deplacer_serveur`) | 0.5 |
| B.3 | Prendre/livrer commandes fonctionnel (points associés) (`prendre_commande`, `livrer_commande`) | 1.0 |
| **Total** |  | **/20 (+ /2 bonus)** |

Bonne chance et bon appétit ! 🍽️
