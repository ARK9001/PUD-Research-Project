import pandas

df = pandas.read_csv("holo_hosp_data_dirty_from_mysql.csv")
f = open("holo_hosp_data_pracmln_db.txt", "w+")
num_entries = 1005

count = 0
for index, row in df.iterrows():
	tup = "ProviderFD(" + str(row['ProviderNumber']) + ", " + row['HospitalName'] + ", " + str(row['PhoneNumber']) + ", " + str(row['ZipCode']) + ", " + row['City'] + ", " + row['CountyName'] + ", " + row['State'] + ")"
	print tup
	tup = tup + "\n"
	f.write(tup)
	
	count = count + 1
	if count >= num_entries:
		break

f.write("\n")
count = 0
for index, row in df.iterrows():
	tup = "MeasureFD(" + str(row['MeasureCode']) + ", " + row['MeasureName'] + ")"
	print tup
	tup = tup + "\n"
	f.write(tup)
	
	count = count + 1
	if count >= num_entries:
		break

f.write("\n")
count = 0
for index, row in df.iterrows():
	tup = "StateFD(" + str(row['pd_index']) + ", " + str(row['ZipCode']) + ", " + row['City'] + ", " + row['State'] + ")"
	print tup
	tup = tup + "\n"
	f.write(tup)
	
	count = count + 1
	if count >= num_entries:
		break

count = 0
for index, row in df.iterrows():
	tup = "CountyFD(" + str(row['pd_index']) + ", " + str(row['ZipCode']) + ", " + row['City'] + ", " + row['State'] + "," + row['CountyName'] + ")"
	print tup
	tup = tup + "\n"
	f.write(tup)
	
	count = count + 1
	if count >= num_entries:
		break

f.close()
	


