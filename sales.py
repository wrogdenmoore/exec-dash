# monthly_sales.py


import matplotlib.pyplot as plt
# TODO: write some Python code here to produce the desired functionality...


#https://python-graph-gallery.com/1-basic-barplot/

 


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

 
# Create bars
plt.barh(products, sales)

# Show graphic
plt.show()