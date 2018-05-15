import pandas

df = pandas.read_csv("holo_hosp_data_dirty_from_mysql.csv")
num_entries = input()
file_name = "holo_pracmln_datasets_2/hc_data_pracmln_" + str(num_entries) + ".db" 
f = open(file_name, "w+") 

 
count = 0 
for index, row in df.iterrows():
	#ProviderA
	tup = "ProviderA(" + str(row['ProviderNumber']) + ", " + row['HospitalName'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#ProviderB
	tup = "ProviderB(" + str(row['ProviderNumber']) + ", " + str(row['PhoneNumber']) + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#ProviderC
	tup = "ProviderC(" + str(row['ProviderNumber']) + ", " + str(row['ZipCode']) + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#ProviderD
	tup = "ProviderD(" + str(row['ProviderNumber']) + ", " + row['City'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#ProviderE
	tup = "ProviderE(" + str(row['ProviderNumber']) + ", " + row['CountyName'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#ProviderF
	tup = "ProviderF(" + str(row['ProviderNumber']) + ", " + row['State'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	f.write("\n")

	count = count + 1
	if count >= num_entries:  
		break

f.write("\n")
count = 0
for index, row in df.iterrows():
	#MeasureA
	meascode = str(row['MeasureCode']) #).replace("-","")
	measname = (row['MeasureName']).replace("(","")
	measname = measname.replace(")","")
	measname = measname.replace("/","")
	measname = measname.replace("\\","")
	tup = "MeasureA(" + meascode + ", " + measname + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	f.write("\n")

	count = count + 1
	if count >= num_entries:
		break

f.write("\n")
count = 0
for index, row in df.iterrows():
	#StateA
	tup = "StateA(" + str(row['pd_index']) + ", " + str(row['ZipCode']) + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#StateB
	tup = "StateB(" + str(row['pd_index']) + ", " + row['City'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#StateC
	tup = "StateC(" + str(row['pd_index']) + ", " + row['State'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	f.write("\n")

	count = count + 1
	if count >= num_entries:
		break

f.write("\n")
count = 0
for index, row in df.iterrows():
	#CountyA
	tup = "CountyA(" + str(row['pd_index']) + ", " + str(row['ZipCode']) + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#CountyB
	tup = "CountyB(" + str(row['pd_index']) + ", " + row['City'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#CountyC
	tup = "CountyC(" + str(row['pd_index']) + ", " + row['State'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	#CountyD
	tup = "CountyD(" + str(row['pd_index']) + ", " + row['CountyName'] + ")"
	print tup
	tup = tup.replace(" ", "")
	tup = tup + "\n"
	f.write(tup)
	f.write("\n")

	count = count + 1
	if count >= num_entries:
		break

f.close()
	


