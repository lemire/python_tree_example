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

## Références

- Lemire et al., [La science des données: Théorie et applications avec R et Python](https://www.amazon.ca/science-donn%C3%A9es-Th%C3%A9orie-applications-Python/dp/B0D53QXGKM)
- Robert Godin et Daniel Lemire, [Programmation avec Python: des jeux au Web](https://www.amazon.ca/Programmation-avec-Python-jeux-Web/dp/B0CVX9296P)




