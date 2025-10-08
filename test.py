import numpy as np
import pandas as pd

arr = np.array([5,5,5,5])

print(arr)

# --- test 1: lage en liten DataFrame ---
data = {
    "name": ["Jørgen", "Sigma", "Bro"],
    "age": [22, 24, 25],
    "power": [9000, 12000, 11000]
}

df = pd.DataFrame(data)

print("✅ DataFrame loaded:")
print(df)

# --- test 2: basic stats ---
print("\n📊 Stats:")
print(df.describe())

# --- test 3: filtrering ---
print("\n⚙️ Filter (power > 10000):")
print(df[df["power"] > 10000])
