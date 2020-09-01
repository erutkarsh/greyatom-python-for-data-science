# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
numerical_var=bank.select_dtypes(include='number')
print(categorical_var.shape)
print(numerical_var.shape)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$")

banks=bank.drop(columns='Loan_ID')
print(banks.isnull().sum())


bank_mode = banks.mode().iloc[0]
print('Bank mode is : \n', bank_mode)


banks.fillna(bank_mode, inplace=True)
#for x in bank.columns:
        #bank[x]=bank[x].fillna(value=bank_mode[x].iloc[0])

print(banks.isnull().sum())
print(banks.shape)
print(banks.isnull().sum().values.sum())
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#Code starts here
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])

percentage_se = (loan_approved_se * 100)/614
percentage_nse = (loan_approved_nse * 100)/614
print(percentage_nse)
print(percentage_se)
print("$4444444444444444444")

loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))

big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome','Credit_History']
mean_values=loan_groupby.mean()






































