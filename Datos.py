import pandas as pd


def analisis():
    df = pd.read_csv('Estudiantes.csv')
    #print(df)
    print(f'Suma Notas: {df["Nota"].sum()}')
    print(f'Promedio Notas: {df["Nota"].mean()}')
    print(f'Total Notas: {df["Nota"].count()}')
    print(f'Nota mas alta: {df["Nota"].max()}')
    print(f'Nota mas baja: {df["Nota"].min()}')
    #aprobados y desaprobados
    print(f'Cantidad de aprobados: {(df["Nota"]>3.0).sum()}')
    print(f'Cantidad de desaprobados: {(df["Nota"]<3.0).sum()}')
    #Cantidad de personas
    print(f"Total de Hombres: {(df['Genero'] == 'Male').sum()}")
    print(f"Total de Mujeres: {(df['Genero'] == 'Female').sum()}")
    print(f"Total de Confundidos: {(df['Genero'] == 'Beyblade').sum()}")
    #Curso
    print(f"Total de gente en frontend: {(df['Asignatura'] == 'Frontend').sum()}")
    print(f"Total de gente en Backend: {(df['Asignatura'] == 'Backend').sum()}")
    print(f"Total de gente Full-Stack: {(df['Asignatura'] == 'Full-Stack').sum()}")
    #Edades
    print(f"Promedio de edad: {df['Edad'].mean()}")
    print(f"Mas viejo: {df['Edad'].max()}")
    print(f"Mas joven: {df['Edad'].min()}")



if __name__ == '__main__':
    analisis()