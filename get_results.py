from pracmln.utils.project import mlnpath
import pandas as pd 
import numpy as np 

pd.options.mode.chained_assignment = None

result_file_name = "test5_query_out_2.txt" #raw_input() 

df_clean = pd.read_csv("hospital_clean_datatable.csv")
df_dirty = pd.read_csv("holo_hosp_data_dirty_from_mysql.csv")
df_mln_clean = df_dirty.copy()

path = '/home/seismic/PUD-Research-Project/examples/test_mln5.pracmln:' + result_file_name
p = mlnpath(path)
content = p.content

print content

""" 
	  #to make above code work 
      #added code to line 489 of /home/seismic/.local/lib/python2.7/site-packages/pracmln/utils/project.py
            elif fileext == 'txt':   
                res = proj.results.get(self.file)
                if res is None: raise Exception('Project %s does not contain results named %s' % (self.project, self.file))
                return res

"""
 
line1 = content.split("\n")
print line1[0]

entry1 = line1[0].split("%") 
sub1 = entry1[0]
ind1 = sub1.find("]") + 1
percent_str = sub1[ind1:].strip()
percent_num = float(percent_str) 
print "Percentage: " + percent_str

if (percent_num >= 50.0): #case when value in db needs to change 
	
	db_size = raw_input("Enter db subset size: ")
	db_size = int(db_size) 
	df_clean_sub = df_clean.head(n=db_size)
	df_dirty_sub = df_dirty.head(n=db_size)

	df_clean_sub['HospitalName'] = df_clean_sub['HospitalName'].str.replace(" ","")
	df_dirty_sub['HospitalName'] = df_dirty_sub['HospitalName'].str.replace(" ","")

	df_clean_sub['City'] = df_clean_sub['City'].str.replace(" ","")
	df_dirty_sub['City'] = df_dirty_sub['City'].str.replace(" ","")

	df_clean_sub['State'] = df_clean_sub['State'].str.replace(" ","")
	df_dirty_sub['State'] = df_dirty_sub['State'].str.replace(" ","")

	df_clean_sub['CountyName'] = df_clean_sub['CountyName'].str.replace(" ","")
	df_dirty_sub['CountyName'] = df_dirty_sub['CountyName'].str.replace(" ","")

	df_clean_sub['MeasureCode'] = df_clean_sub['MeasureCode'].str.replace(" ","")
	df_dirty_sub['MeasureCode'] = df_dirty_sub['MeasureCode'].str.replace(" ","")

	df_clean_sub['MeasureName'] = df_clean_sub['MeasureName'].str.replace(" ","").str.replace("(","").str.replace(")","").str.replace("/","").str.replace("\\","")
	df_dirty_sub['MeasureName'] = df_dirty_sub['MeasureName'].str.replace(" ","").str.replace("(","").str.replace(")","").str.replace("/","").str.replace("\\","")

	df_mln_clean_sub = df_dirty_sub.copy()


	print "-------------------------------BEFORE-------------------------------"
	print df_mln_clean_sub

	sub2 = entry1[1].strip()
	ind2 = sub2.find("(")

#The below indexing depends on the format of the predicates written in the mln file
#The format is as follows: PredicateX(db_row_val, db_mln_cell_val) where X is single letter, utilized by the nested conditional statement block below


#NOTE: make sure to change the cell values across all dataframes to the same TYPE before comparing 

	pred_name = sub2[:ind2]  
	pred_main = pred_name[:-1]
	pred_letter = pred_name[-1]

	pred_content_list = sub2[(ind2+1):-1].split(",")
	db_row_val = pred_content_list[0]
	print "DB Row Value: " + db_row_val
	db_mln_cell_val = pred_content_list[1]
	print "MLN Generated Value: " + db_mln_cell_val

	if pred_main == "Provider":
		if pred_letter == 'A':
			print 'hospname'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'HospitalName'] = db_mln_cell_val

		elif pred_letter == 'B':
			print 'phonenum'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'PhoneNumber'] = db_mln_cell_val
		
		elif pred_letter == 'C':
			print 'zip'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'ZipCode'] = db_mln_cell_val

		elif pred_letter == 'D':
			print 'city'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'City'] = db_mln_cell_val

		elif pred_letter == 'E':
			print 'county'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'CountyName'] = db_mln_cell_val

		elif pred_letter == 'F':
			print 'state'
			df_mln_clean_sub.loc[df_mln_clean_sub['ProviderNumber'] == int(db_row_val),'State'] = db_mln_cell_val

	elif pred_main == "Measure":
		if pred_letter == 'A':
			print 'measurename'
			df_mln_clean_sub.loc[df_mln_clean_sub['MeasureCode'] == db_row_val,'MeasureName'] = db_mln_cell_val

	elif pred_main == "State":
		if pred_letter == 'A':
			print 'zip'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'ZipCode'] = db_mln_cell_val

		elif pred_letter == 'B':
			print 'city'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'City'] = db_mln_cell_val
 
		elif pred_letter == 'C':
			print 'state'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'State'] = db_mln_cell_val

	elif pred_main == "County":
		if pred_letter == 'A': 
			print 'zip'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'ZipCode'] = db_mln_cell_val

		elif pred_letter == 'B':
			print 'city'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'City'] = db_mln_cell_val

		elif pred_letter == 'C':
			print 'state'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'State'] = db_mln_cell_val
		
		elif pred_letter == 'D':
			print 'county'
			df_mln_clean_sub.loc[df_mln_clean_sub['pd_index'] == int(db_row_val),'CountyName'] = db_mln_cell_val

#for i in df['col1']:
#	i.replace("(","")

	print "-------------------------------AFTER-------------------------------"
	print df_mln_clean_sub

	print "--------------------------FINAL CHANGES----------------------------"

	diff_location = np.where(df_dirty_sub['HospitalName'] != df_mln_clean_sub['HospitalName'])
	change_from = df_dirty_sub['HospitalName'].values[diff_location]
	change_to = df_mln_clean_sub['HospitalName'].values[diff_location]
	change = pd.DataFrame({'pd_index':diff_location, 'from':change_from, 'to':change_to})
	change = change[['pd_index','from','to']]
	print change
