import pandas as pd

# df = pd.read_json('/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/Data frames com Pandas/dados.json')

# print(df.groupby('Pulse').mean())


data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409.1,
        "1": 479.0,
        "2": 340.0,
        "3": 282.4,
        "4": 406.0,
        "5": 300.5
    }
}

df = pd.DataFrame(data)

print(df)
