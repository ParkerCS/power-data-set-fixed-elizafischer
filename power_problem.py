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
print(headers)

for i in range(len(powdat)):
    if powdat[i][0] == "60614" and powdat[i][4] == "Bundled":
        print("Problem #1: The average bundled residential rate for 60614 =" , powdat[i][-1], "\n")


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

print("Problem #2: The median bundled residential rate in Illinois is", medbundledrates)
print()

#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one.
# Then you will need to reference the zipcode dataset to get the city.  (15pts)

res_rates = []
for i in range(len(powdat)):
    if powdat[i][4] == "Bundled" and powdat[i][3] == "IL":
        res_rates.append(powdat[i])

# float conversion
for i in range(len(res_rates)):
    res_rates[i][8] = float(res_rates[i][8])

# Sorting the items in the list by the residential rate
res_rates = sorted(res_rates, key=lambda x: x[8])

# Finding what zip code the highest and lowest rates are in
lowest_rate_zip = res_rates[0][0]
highest_rate_zip = res_rates[len(res_rates)-1][0]

print("Lowest rate's zip code:", lowest_rate_zip, "and Highest rate's zip code:" , highest_rate_zip)

# Bringing in the data from the zipcode database
file = open("free-zipcode-database-Primary.csv", "r")
zip_list = []
reader = csv.reader(file, delimiter=',')
for line in reader:
    zip_list.append(line)

# Cutting the headers off of the list
headers2 = zip_list[0]
#print(headers2)
zip_list = zip_list[1:]

# Making a list of only cities in Illinois
il_zip_list = []
for i in range(len(zip_list)):
    if zip_list[i][3] == "IL":
        il_zip_list.append(zip_list[i])

# Zipcodes are key 0 and cities are key 2

# Creating a binary search function to find the city names
def binary_search(input_key, list):
    upper_bound = len(list) - 1
    lower_bound = 0
    key = input_key.upper()
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        if list[middle_pos][0] < key:
            lower_bound = middle_pos + 1
        elif list[middle_pos][0] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    return middle_pos

lowest_rate_city =(il_zip_list[binary_search(lowest_rate_zip, il_zip_list)][2])
highest_rate_city =(il_zip_list[binary_search(highest_rate_zip, il_zip_list)][2])


print()
print("Problem #3:",res_rates[0][-1], "is the lowest residential rate in Illinois, in", lowest_rate_city)
print(res_rates[len(res_rates)-1][-1], "is the highest residential rate in Illinois, in", highest_rate_city)


#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.
# Make the marker size vary depending on the population contained in that zip code.
# Add an alpha value to the marker so that you can see overlapping markers.

# latitude index is 6 longitude index is 5
latitude = []
longitude = []
set_size = []

for i in range(len(zip_list)):
    if zip_list[i][3] == "IL":
        if zip_list[i][10]:
            latitude.append(float(zip_list[i][6]))
            longitude.append(float(zip_list[i][5]))
            set_size.append(float(zip_list[i][10])/25)

plt.figure(1, tight_layout=True, figsize=(6,8))
plt.scatter(latitude, longitude, set_size, color="red", alpha=.5)



# Labels
plt.title("Graph of Illinois zipcodes by population")
plt.xlabel("Latitude")
plt.ylabel("Longiturde")

plt.show()