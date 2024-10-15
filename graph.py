import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV généré par main.py
df = pd.read_csv('network_capture.csv')

# Créer un pivot des données en fonction du protocole et du temps
# On cumul le nombre de paquets dans chaque intervalle de temps
df['Count'] = 1  # Ajouter une colonne "Count" pour chaque paquet
df_cumsum = df.pivot_table(index='Time', columns='Protocol', values='Count', aggfunc='sum').fillna(0).cumsum()

# Tracer une courbe pour chaque protocole
df_cumsum.plot()

# Titre et légendes
plt.title("Évolution du nombre de paquets par protocole au fil du temps")
plt.xlabel("Temps (secondes)")
plt.ylabel("Nombre de paquets")
plt.legend(title="Protocole")
plt.grid(True)
plt.show()
