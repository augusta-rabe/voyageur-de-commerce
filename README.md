# Optimisation du Voyageur de Commerce (TSP) avec Algorithme Génétique

Ce projet implémente une solution au problème du Voyageur de Commerce (TSP - Traveling Salesman Problem) en utilisant un algorithme génétique. L'interface graphique permet de visualiser l'évolution de la solution en temps réel.

## 🚀 Fonctionnalités

- Interface graphique interactive
- Visualisation en temps réel de l'évolution de la solution
- Export des résultats (graphique et données)
- Paramètres ajustables pour l'algorithme génétique

## 📋 Prérequis

```bash
pip install -r requirements.txt
```

## 🎮 Utilisation

1. Lancez le programme :
```bash
python tsp_genetic_gui.py
```

2. Ajustez les paramètres selon vos besoins :
   - **Nombre de villes** : Nombre de points à visiter
   - **Taille de population** : Nombre de solutions candidates
   - **Nombre de générations** : Nombre d'itérations de l'algorithme
   - **Taux de mutation** : Probabilité de modification aléatoire

3. Cliquez sur "Lancer la simulation"

## 📊 Concepts Clés

### Population
La population représente un ensemble de solutions candidates au problème TSP. Chaque individu de la population est une permutation des villes, représentant un trajet possible. Une population plus grande offre plus de diversité mais augmente le temps de calcul.

### Générations
Les générations sont les itérations successives de l'algorithme. À chaque génération :
1. Les meilleures solutions sont sélectionnées
2. De nouvelles solutions sont créées par croisement
3. Des mutations aléatoires sont appliquées
4. La population évolue vers de meilleures solutions

### Taux de Mutation
Le taux de mutation (entre 0 et 1) détermine la probabilité qu'une solution soit modifiée aléatoirement. Un taux trop faible peut mener à une convergence prématurée, tandis qu'un taux trop élevé peut empêcher la convergence vers une bonne solution.

## 📈 Résultats

Les résultats sont sauvegardés dans le dossier `resultats/` :
- `trajet_optimal.png` : Visualisation du meilleur trajet trouvé
- `trajet_optimal.csv` : Données détaillées du trajet (ordre des villes, coordonnées)

## 🔧 Paramètres Recommandés

- **Petit problème** (10-20 villes) :
  - Population : 50-100
  - Générations : 100-200
  - Mutation : 0.01-0.05

- **Problème moyen** (20-50 villes) :
  - Population : 100-200
  - Générations : 200-500
  - Mutation : 0.005-0.02

- **Grand problème** (50+ villes) :
  - Population : 200-500
  - Générations : 500-1000
  - Mutation : 0.001-0.01

## 📝 Notes

- L'algorithme génétique ne garantit pas la solution optimale, mais trouve généralement une bonne approximation
- Les temps de calcul augmentent avec la taille du problème
- La visualisation en temps réel permet de suivre l'amélioration de la solution

## 🛠️ Technologies Utilisées

- Python 3.x
- Tkinter (interface graphique)
- Matplotlib (visualisation)
- NumPy (calculs) 