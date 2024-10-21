from pyspark.sql import SparkSession # type: ignore
from pyspark import * # type: ignore
import pandas as pd
import matplotlib.pyplot as plt

# Initialiser la SparkSession
spark = SparkSession.builder.appName("Protocol Count").getOrCreate()

# Lire le fichier CSV dans un DataFrame
df = spark.read.csv("network_capture.csv", header=True, inferSchema=True)

# Convertir le DataFrame en RDD pour travailler avec des opérations comme map, reduce, etc.
rdd = df.rdd

# Utiliser mapToPair pour transformer les données en paires (Time, Protocol) -> 1
rdd_mapped = rdd.map(lambda row: ((row["Time"], row["Protocol"]), 1))

# Utiliser reduceByKey pour compter le nombre de paquets par (Time, Protocol)
rdd_reduced = rdd_mapped.reduceByKey(lambda a, b: a + b)

result = rdd_reduced.collect()

# Afficher les résultats
for (time_protocol, count) in result:
    print(f"Time: {time_protocol[0]}, Protocol: {time_protocol[1]}, Count: {count}")


# Convertir les résultats en DataFrame Pandas pour la visualisation
df_pandas = pd.DataFrame(result, columns=["Time_Protocol", "Count"])
df_pandas["Time"] = df_pandas["Time_Protocol"].apply(lambda x: x[0])
df_pandas["Protocol"] = df_pandas["Time_Protocol"].apply(lambda x: x[1])

# Créer un pivot pour avoir une colonne par protocole
df_pivot = df_pandas.pivot(index="Time", columns="Protocol", values="Count").fillna(0)


# Tracer les courbes pour chaque protocole
plt.plot(df_pivot.index, df_pivot["TCP"], label="TCP")
plt.plot(df_pivot.index, df_pivot["UDP"], label="UDP")
plt.plot(df_pivot.index, df_pivot["OTHER"], label="OTHER")

# Ajouter des légendes et des titres
plt.xlabel("Time (seconds)")
plt.ylabel("Number of Packets")
plt.title("Packets by Protocol over Time")
plt.legend()

# Afficher le graphique
plt.show()
