'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''
import csv
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import matplotlib.patches as mpatches


#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts) √
file = open("power_data.csv", "r")

# Putting the file in a list
power_data = []
reader = csv.reader(file, delimiter = ',')
for line in reader:
    power_data.append(line)

# Taking the labels off of the front of list to make the numbers easier to work with.
headers = power_data[0]
powdat = power_data[1:]
print("\nHeaders list: ",end="")
print(headers, "\n")

print(powdat[:5])
print()

for i in range(len(powdat)):
    if powdat[i][0] == "60614" and powdat[i][4] == "Bundled":
        print("Average bundled residential rate for 60614 =" , powdat[i][-1], "\n")


#2 What is the MEDIAN (floor division) rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)
import statistics
# sort by rate
il_list = []

# len index floor two and look at the rate at that position
for i in range(len(powdat)):
    if powdat[i][3] == "IL" and powdat[i][4] == "Bundled":
        il_list.append(powdat[i][8])

il_list.sort()
#print("SORTED:", end= "")
#print(il_list)

#do a float conversion
for i in range(len(il_list)):
    il_list[i] = float(il_list[i])

bundled_rates = []
for i in range(len(powdat)):
    if powdat[i][4] == "Bundled" and powdat[i][3] == "IL":
        bundled_rates.append(power_data[i][8])

medbundledrates = statistics.median(bundled_rates)

print("The median bundled residential rate in Illinois is", medbundledrates)
print()

#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one.
# Then you will need to reference the zipcode dataset to get the city.  (15pts)
res_rates = []
for i in range(len(powdat)):
    if powdat[i][4] == "Bundled" and powdat[i][3] == "IL":
        res_rates.append(powdat[i][-1])
print("Residential rates IL:" ,res_rates)

# SORT, then find the lowest rate and its zipcode, find which city that zipcode is in
'''
res_rates.sort()
# float conversion
for i in range(len(res_rates)):
    res_rates[i] = float(res_rates[i])
'''

for i in range(len(powdat)):
    powdat[i][-1] = float(powdat[i][-1])
powdat.sort(key=itemgetter(-1))


print("\nSorted res rates: ")

#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.

#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)

