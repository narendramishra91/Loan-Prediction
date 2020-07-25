import pandas as pd

def dataFunction():
    data = pd.read_csv("loan_dataset.csv")
    data.dropna(subset=['Credit_History','Married', 'Gender', 'LoanAmount', 'Dependents' ], axis=0, inplace = True)
    data['Loan_Amount_Term'].fillna(360, inplace = True)
    data['Self_Employed'].fillna('No', inplace = True)
    data.drop(['Loan_ID'], axis = 1, inplace = True)
    return data

def Accuracy(_matrix):
    accu = (_matrix[0][0]+ _matrix[1][1])/(_matrix[0][0]+ _matrix[1][1] + _matrix[1][0]+ _matrix[0][1])
    return accu

