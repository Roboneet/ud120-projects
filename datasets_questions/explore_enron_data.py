#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

##################
# finding out how many pois do I have in my dataset
##################

file = open("../final_project/poi_names.txt").read().split('\n')
lines = file[2:-1]
# print "\n".join(lines).upper()
last_names =[]
first_names = []
for a in lines:
	k = re.search('\([yn]\) (\w+), (\w+)', a)
	# print k.group(1,2)
	last_names.append(k.group(1).upper())
	first_names.append(k.group(2))

# print last_names
pois =[]
count_salary = 0
count_email_id = 0
for key in enron_data:
	if enron_data[key]['poi'] == 1 :
		l = key.split(" ")
		# print (l[0] in last_names)
		if l[0] in last_names:
			# print key
			pass
	if enron_data[key]['total_payments'] != 'NaN':
		count_salary+=1
	if enron_data[key]['email_address'] != 'NaN':
		count_email_id+=1
print (1 - float(count_salary)/len(enron_data.keys()))

# print(pois)

# print(enron_data["SKILLING JEFFREY K"]['total_payments'])
# print(enron_data["LAY KENNETH L"]['total_payments'])
# print(enron_data["FASTOW ANDREW S"]['total_payments'])

print count_salary
print count_email_id

######