import pandas as pd
data = {'A': [1, 2, 3, 5],
'B': ['apple', 'banana', 'apple','apple']}
df = pd.DataFrame(data)
print(df)
datas =df[df.duplicated(subset='B',keep=False)]
print(df.duplicated(subset='B',keep=False))
df = datas.value_counts(subset='B')
print(datas)



data = {'A': [1, 2, 3, 5],'B': ['apple', 'banana', 'apple','apple']}
data = pd.DataFrame(data)
df = data.drop_duplicates(subset='B')
print(df)