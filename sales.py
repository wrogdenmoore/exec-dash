# monthly_sales.py

import csv
import matplotlib.pyplot as plt
# TODO: write some Python code here to produce the desired functionality...


#https://python-graph-gallery.com/1-basic-barplot/


#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/csv.md

rows = []#each item in csv file
products = []
sales = []

csv_file_path = "data/sales-201803.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for next_row in reader:
        rows.append(dict(next_row))
        #print(row["date"], row["product"])\
        sales.append(float(next_row["sales price"]))
        products.append(next_row["product"])

SalesSum=sum(sales)
print(SalesSum)

print(products)
print(len(products))

#remove duplicates--datatypes
unique_products = list(set(products))
print(unique_products)
#try to make unique_products = 
#total sales per product, filtering: list comprehension or if statement
#salesreporting and filtering list notes: list comprehension
#filtering lists notes

# products=['product'].unique()
# products.sort()
# print(products)    
breakpoint()

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

# Make a fake dataset:
sales = [6900, 1800, 1600, 900, 250, 200, 150]
products = ['shirt', 'hoodie', 'pants', 'T', 'Boots', 'stickers', 'hat']
sales.reverse()
products.reverse()

salesSum = sum(sales)
print(salesSum)



# # Create bars
plt.barh(products, sales)

 # Show graphic
plt.show()