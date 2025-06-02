

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Chargement des données depuis le fichier CSV
data = pd.read_csv("data.csv")
X = data[["x"]].values.astype(np.float32)  # forme (N,1)
y = data["y"].values.astype(np.float32)    # forme (N,)


print("Aperçu des données :")
print(data.head(), "\n")
# 2. Définition du modèle à un seul neurone
model = keras.Sequential(
    [
        layers.Dense(
            units=1,
            input_shape=(1,),
            kernel_initializer="random_normal",
            bias_initializer="zeros",
            name="mon_neurone"
        )
    ]
)

# 3. Compilation du modèle

model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.01),
    loss="mean_squared_error",
    metrics=["mean_absolute_error"]
)

# 4. Entraînement

history = model.fit(
    X,
    y,
    epochs=200,
    batch_size=4,
    verbose=1,     # 1 pour voir une barre de progression
    validation_split=0.2  # 20% des données utilisées pour valider
)

# 5. Évaluation et prédiction

loss, mae = model.evaluate(X, y, verbose=0)
print(f"\n--> Perte finale (MSE)     : {loss:.4f}")
print(f"--> Erreur absolue moyenne : {mae:.4f}\n")

# 6. Affichagee de poids (w) et biais (b) appris
#   y_pred = w * x + b
poids, biais = model.layers[0].get_weights()
print(f"Poids appris (w) : {poids.flatten()[0]:.4f}")
print(f"Biais appris (b) : {biais[0]:.4f}\n")

# 7. Quelques prédictions pour vérifier
X_test = np.array([[12.0], [15.0], [20.0]], dtype=np.float32)
preds = model.predict(X_test)
for i, x_val in enumerate(X_test.flatten()):
    print(f"Pour x = {x_val:.1f}  → prédiction y = {preds[i,0]:.2f}")


