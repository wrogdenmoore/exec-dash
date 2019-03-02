

# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

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


# monthly_sales.py

import os
import pandas

# utility function to convert float or integer to usd-formatted string (for printing)
# ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INPUTS
#

csv_filename = "sales-201803.csv" # TODO: allow user to specify

# reference a file in the "data" directory
# ... adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# read csv file into a pandas dataframe object
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

top_sellers = [
    {"name": "Button-Down Shirt", "monthly_sales": 6960.34},
    {"name": "Super Soft Hoodie", "monthly_sales": 1875.0},
    {"name": "Khaki Pants", "monthly_sales": 1602.0},
    {"name": "Vintage Logo Tee", "monthly_sales": 941.05},
    {"name": "Brown Boots", "monthly_sales": 250.0},
    {"name": "Sticker Pack", "monthly_sales": 216.0},
    {"name": "Baseball Cap", "monthly_sales": 156.31}
] # TODO: get from CSV data instead
#
