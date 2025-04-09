import pandas as pd
import numpy as npy

def seriesNros():
    nros = pd.Series([32, 24, 69, 87, 0, 1, 33, 14, 28, 32])
    ## print(nros)
    print("Sumar los elementos de la serie")
    print(f"Suma de todos los numeros: {sum(nros)}")
    print(f"Numero Mayor: {max(nros)}")
    print(f"Numero Menor: {min(nros)}")
    print("Ordenar la serie menor a mayor")
    ## print(nros.sort_values(ascending=True))
    print("Ordenar la serie mayor a menor")
    ## print(nros.sort_values(ascending=False))
    print("Condicionales")
    print(f"Numero mayor a 30:")
    print(nros[nros >30])
    print("Promedio")
    print(f"El promedio de Panda: {npy.mean(nros)}")


if __name__ == '__main__':
    seriesNros()