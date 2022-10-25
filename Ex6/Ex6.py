import pandas as pd

df = pd.read_csv("diamonds.csv")

cutReplaces = {
    "Ideal": 1,
    "Premium" : 2,
    "Very Good" : 3,
    "Good": 4,
    "Fair": 5
}
df['cut'].replace(cutReplaces, inplace=True)

colorReplaces = {
    "D": 1,
    "E": 2,
    "F": 3,
    "G": 4,
    "H": 5,
    "I": 6,
    "J": 7
}
df['color'].replace(colorReplaces, inplace=True)

clarityReplaces = {
    "IF": 1,
    "VVS1": 2,
    "VVS2": 3,
    "VS1": 4,
    "VS2": 5,
    "SI1": 6,
    "SI2": 7,
    "I1": 8
}
df['clarity'].replace(clarityReplaces, inplace=True)


df_X = df[["carat","cut","color","clarity"]]

df_Y = df[["price"]]

from sklearn.model_selection import train_test_split

X_treinamento, X_testes, Y_treinamento, Y_testes = train_test_split(df_X, df_Y, test_size=0.2)

from sklearn import linear_model
reg = linear_model.LinearRegression()

reg.fit(X_treinamento, Y_treinamento)
reg.coef_

Y_pred = reg.predict(X_testes)

from sklearn.metrics import r2_score

r2 = r2_score(Y_testes, Y_pred)

r2*100

print(r2)