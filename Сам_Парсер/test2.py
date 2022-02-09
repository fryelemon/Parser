import pandas as pd

def to_xlsx():
    return 0

index = [1,2,3]
data = {'data': [1,2,3]}

vector = pd.DataFrame(index = index,data = data)

print(vector)
print(vector*2)

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])

df1.to_excel("output.xlsx")