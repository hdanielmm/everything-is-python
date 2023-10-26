import pandas as pd

archivo = input("Procesar archivo: ")
df = pd.read_csv(archivo + ".csv")

name = df["variable"].str.split("=", expand=True)

print(name.info())

if len(name.axes[1]) == 2:
    name.columns = ["Variable", "Valor"]
elif len(name.axes[1]) == 3:    
    name.columns = ["Variable", "Valor", "Valor2"]

df = pd.DataFrame(name)
df["Valor"] = df["Valor"].str.strip()
df["Variable"] = df["Variable"].str.strip()

print(df)

new_test_csv = df.to_csv(archivo + "_" + "procesado.csv")


