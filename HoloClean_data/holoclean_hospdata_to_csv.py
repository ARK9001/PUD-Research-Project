import pandas as pd

df = pd.read_csv('hospital_clean.csv')

entry = df.loc[df['tid'] == 1]
entry_trans = entry.transpose()
row = entry_trans.loc['attr_val'].tolist()
attr_names = entry_trans.loc['attr_name'].tolist()

hosp_table = pd.DataFrame(columns=attr_names)
hosp_table.loc[0] = row

for n in range(2,1001):
	entry = df.loc[df['tid'] == n]
	entry_trans = entry.transpose()
	row = entry_trans.loc['attr_val'].tolist()
	index = n-1
	hosp_table.loc[index] = row

hosp_table.to_csv('hospital_clean_datatable.csv')