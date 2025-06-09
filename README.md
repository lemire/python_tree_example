# Exemple d'arbre de décision en Python

Ce projet propose un pipeline ETL (Extraction, Transformation, Chargement) simple en Python. Il utilise un arbre de décision pour prédire si une livraison sera effectuée à temps, à partir de caractéristiques de commandes (type de produit, distance, saison). Les données sont simulées dans le script.

## Prérequis

Avant de procéder, assurez-vous d'installer Python 3.7 ou une version ultérieure sur votre machine.

- **Pour Windows** :
  1. Téléchargez l'installateur depuis https://www.python.org/downloads/windows/
  2. Lancez l'installateur et cochez l'option "Add Python to PATH" avant de cliquer sur "Install Now".
  3. Ouvrez l'invite de commandes :
     - Cliquez sur le menu Démarrer (icône Windows en bas à gauche), tapez "Invite de commandes" ou "cmd", puis cliquez sur l'application correspondante.
  4. Vérifiez l'installation en tapant :
     ```
     python --version
     ```
     ou
     ```
     python3 --version
     ```

- **Pour macOS** :
  1. Ouvrez le Terminal.
  2. Installez Homebrew si ce n'est pas déjà fait :
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  3. Installez Python 3 avec Homebrew :
     ```
     brew install python
     ```
  4. Vérifiez l'installation :
     ```
     python3 --version
     ```

Le nom de l'interpréteur Python sur votre système peut être `python` ou `python3` selon votre système. Nous allons supposer qu'il s'agit de `python3`.

## Installation des dépendances (environnement virtuel recommandé)

1. Créez un environnement virtuel dans le dossier du projet :
   ```
   python3 -m venv venv
   ```
2. Activez l'environnement virtuel :
   - **Sur macOS et Linux** :
     ```
     source venv/bin/activate
     ```
   - **Sur Windows** :
     ```
     venv\Scripts\activate
     ```
3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel avec :
```
deactivate
```

## Obtention des fichiers du projet

Pour obtenir les fichiers du projet, vous pouvez télécharger une archive ZIP depuis GitHub :

1. Rendez-vous sur la page du projet : https://github.com/lemire/python_tree_example
2. Cliquez sur le bouton vert « Code » puis sur « Download ZIP ».
3. Décompressez l’archive téléchargée sur votre ordinateur.
4. Ouvrez le dossier extrait dans votre terminal ou explorateur de fichiers pour suivre les instructions d’installation ci-dessus.

## Utilisation

Lancez le script principal :

```
python3 solution.py
```

Le script affiche la prédiction de livraison à temps pour une nouvelle commande simulée.

## Exemple de résultat
Après exécution, vous verrez dans le terminal une sortie du type :

```
Prédiction pour la nouvelle commande : Oui
```

## Structure du code
- `solution.py` : script principal qui orchestre la simulation, l'entraînement et la prédiction avec un arbre de décision
- `requirements.txt` : dépendances Python nécessaires (`pandas`, `scikit-learn`)


## Explication du code

Voici une explication détaillée du code Python fourni, qui utilise un arbre de décision pour prédire si une livraison sera à temps, formatée en Markdown.

### 1. Importation des bibliothèques
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
```
- `pandas` : bibliothèque pour manipuler les données sous forme de DataFrame.
- `DecisionTreeClassifier` : modèle d'apprentissage automatique pour créer un arbre de décision.

### 2. Création des données
```python
data = {
    'Type_Produit': ['Fragile', 'Non_Fragile', ...],
    'Distance': ['Proche', 'Lointaine', ...],
    'Saison': ['Basse', 'Haute', ...],
    'Livraison_A_Temps': ['Oui', 'Non', ...]
}
```
- Un dictionnaire définit un jeu de données avec quatre colonnes : type de produit, distance, saison et résultat (livraison à temps).
- Huit exemples sont fournis, représentant différentes combinaisons de ces variables.

### 3. Conversion en DataFrame
```python
df = pd.DataFrame(data)
```
- Le dictionnaire est transformé en un DataFrame pandas pour faciliter la manipulation des données.

### 4. Encodage des variables catégoriques
```python
df_encoded = pd.get_dummies(df[['Type_Produit', 'Distance', 'Saison']], drop_first=True)
X = df_encoded
y = df['Livraison_A_Temps']
```
- `pd.get_dummies` convertit les variables catégoriques (ex. : "Fragile"/"Non_Fragile") en variables binaires (0 ou 1).
- `drop_first=True` supprime une catégorie par variable pour éviter la redondance (ex. : `Type_Produit_Fragile` est omis, car `Type_Produit_Non_Fragile = 0` l'implique).
- `X` contient les variables d'entrée : `Type_Produit_Non_Fragile`, `Distance_Proche`, `Saison_Haute`.
- `y` contient la variable cible : `Livraison_A_Temps` ("Oui" ou "Non").

### 5. Affichage des données
```python
print("Données initiales :")
print(data)
print("Données d'entraînement :")
print(X)
print(y)
```
- Affiche les données brutes et transformées pour vérification.

### 6. Entraînement du modèle
```python
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)
```
- Crée un arbre de décision avec une profondeur maximale de 3 pour limiter la complexité du modèle.
- `random_state=42` garantit la reproductibilité des résultats.
- `fit(X, y)` entraîne le modèle sur les caractéristiques (`X`) et la cible (`y`).

### 7. Prédiction pour une nouvelle commande
```python
nouvelle_commande = pd.DataFrame({
    'Type_Produit_Non_Fragile': [1],  # Non_Fragile
    'Distance_Proche': [1],          # Proche
    'Saison_Haute': [0]              # Basse
})
prediction = clf.predict(nouvelle_commande)
print(f"Prédiction pour la nouvelle commande : {prediction[0]}")
```
- Une nouvelle commande est définie avec des caractéristiques encodées : produit non fragile, distance proche, saison basse.
- `predict` utilise l'arbre entraîné pour prédire si la livraison sera à temps ("Oui" ou "Non").
- Le résultat est affiché (par exemple, "Oui").

### Résumé
Ce code construit un modèle d'arbre de décision pour prédire si une livraison sera à temps en fonction du type de produit, de la distance et de la saison. Les variables catégoriques sont encodées en variables binaires, le modèle est entraîné sur un petit jeu de données, puis utilisé pour prédire une nouvelle commande. L'arbre de décision apprend des règles simples (ex. : "si produit non fragile et distance proche, alors livraison à temps") à partir des données fournies.

## Références

- Lemire et al., [La science des données: Théorie et applications avec R et Python](https://www.amazon.ca/science-donn%C3%A9es-Th%C3%A9orie-applications-Python/dp/B0D53QXGKM)
- Robert Godin et Daniel Lemire, [Programmation avec Python: des jeux au Web](https://www.amazon.ca/Programmation-avec-Python-jeux-Web/dp/B0CVX9296P)




