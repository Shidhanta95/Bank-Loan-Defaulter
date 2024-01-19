import numpy as np
from loadingdata import loading_data

def data_preprocess():
    data = loading_data()
    data =  data.drop(['ID', 'Payment Plan', 'Accounts Delinquent','Batch Enrolled','Employment Duration', ], axis = 1)
    print(data.columns)
    data['Funded Amount Investor'] = data['Funded Amount Investor'].astype('int')
    data['Interest Rate	'] = data['Interest Rate'].astype('int')
    print("----------------------data_preprocess------------------",data)
    return data

data_preprocess()