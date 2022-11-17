import pandas as pd

df = pd.DataFrame({'X': [0, 1, 2, 3, 4, 5, 6], 'Y': [7, 8, 9, 10, 11, 12, 13]}, index=['店名', '住所', 'TEL', '営業時間', '定休日', 'HP', 'Email'])

print(df.T)

transposed = df.T
transposed.to_csv('transposed.csv')