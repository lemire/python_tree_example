import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from io import StringIO

# Création d'un jeu de données réaliste
data = {
    'Type_Produit': ['Fragile', 'Non_Fragile', 'Fragile', 'Non_Fragile', 'Fragile', 'Non_Fragile', 'Fragile', 'Non_Fragile'],
    'Distance': ['Proche', 'Lointaine', 'Proche', 'Proche', 'Lointaine', 'Proche', 'Lointaine', 'Lointaine'],
    'Saison': ['Basse', 'Haute', 'Haute', 'Basse', 'Basse', 'Basse', 'Haute', 'Haute'],
    'Livraison_A_Temps': ['Oui', 'Non', 'Oui', 'Oui', 'Non', 'Oui', 'Non', 'Non']
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# Encodage des variables catégoriques
df_encoded = pd.get_dummies(df[['Type_Produit', 'Distance', 'Saison']], drop_first=True)
X = df_encoded
y = df['Livraison_A_Temps']

# Création et entraînement de l'arbre de décision
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Exemple d'application : prédiction pour une nouvelle commande
nouvelle_commande = pd.DataFrame({
    'Type_Produit_Non_Fragile': [1],  # Non_Fragile
    'Distance_Proche': [1],          # Proche
    'Saison_Haute': [0]              # Basse
})
prediction = clf.predict(nouvelle_commande)
print(f"Prédiction pour la nouvelle commande : {prediction[0]}")