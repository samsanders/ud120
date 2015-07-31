#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "number of names:", len(enron_data.keys())

enron_data_vals = enron_data.values()
print "number of features:", len(enron_data_vals[0])

num_pois = 0
for name in enron_data:
	if enron_data[name]["poi"] == True:
		num_pois = num_pois + 1

print "number of pois in data:", num_pois

names_file = open("../final_project/poi_names.txt", "rU")
names_file_text = names_file.read()

pois_list = re.findall(r'\) (\w+,\s\w+)', names_file_text)
print "number of pois total:", len(pois_list)

james_prentice_name=''
for name in enron_data:
	if name.find("PRENTICE JAMES")>=0:
		james_prentice_name = name

print "value of stock for james prentice:", enron_data[james_prentice_name]["total_stock_value"]

wesley_colwell_name=''
for name in enron_data:
	if name.find("COLWELL WESLEY")>=0:
		wesley_colwell_name = name

print "number of emails from wesley colwell to poi:", enron_data[wesley_colwell_name]["from_this_person_to_poi"]

jeffrey_skilling_name=''
for name in enron_data:
	if name.find("SKILLING JEFFREY")>=0:
		jeffrey_skilling_name = name

print "exercised stock options for jeffrey skilling:", enron_data[jeffrey_skilling_name]["exercised_stock_options"]

kenneth_lay_name=''
for name in enron_data:
	if name.find("LAY KENNETH")>=0:
		kenneth_lay_name = name

andrew_fastow_name=''
for name in enron_data:
	if name.find("FASTOW ANDREW")>=0:
		andrew_fastow_name = name

jeffrey_skilling_payments = enron_data[jeffrey_skilling_name]["total_payments"]
kenneth_lay_payments = enron_data[kenneth_lay_name]["total_payments"]
andrew_fastow_payments = enron_data[andrew_fastow_name]["total_payments"]
print "skilling:", jeffrey_skilling_payments, "lay:", kenneth_lay_payments, "fastow:", andrew_fastow_payments

num_w_salary = 0
num_w_email = 0
num_w_total_payments =0
num_pois_w_total_payments = 0
for name in enron_data:
	if enron_data[name]["salary"] != "NaN":
		num_w_salary = num_w_salary + 1
	if enron_data[name]["email_address"] != "NaN":
		num_w_email = num_w_email + 1
	if enron_data[name]["total_payments"] != "NaN":
		num_w_total_payments = num_w_total_payments + 1
	if enron_data[name]["poi"] == True and enron_data[name]["total_payments"] != "NaN":
		num_pois_w_total_payments = num_pois_w_total_payments + 1


print "number with salary:", num_w_salary, "number with email:", num_w_email

pct_w_total_payments = float(num_w_total_payments)/float(len(enron_data.keys()))

print "number with total payments:", num_w_total_payments, "percent with total payments:", pct_w_total_payments

pct_pois_w_total_payments = float(num_pois_w_total_payments)/float(num_pois)

print "number pois with total payments:", num_pois_w_total_payments, "percent pois with total payments:", pct_pois_w_total_payments