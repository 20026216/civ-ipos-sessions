# Remember you file paths when you attempt use this file reader
# import the csv library
import csv


# Function to read data from CSV file
def read_sales_data(filename):
# Task 1: Read data from CSV file
    two_dim_list = []
    with open(filename,"r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Units Sold"] = int(row["Units Sold"])
            row["Units Price"] = float(row["Unit Price"])
            row["Total Revenue"] = float(row["Total Revenue"])
            two_dim_list.append(row)
    return two_dim_list


sales_data = read_sales_data('./sales_data.csv')
print(sales_data)

# Task 2: Calculate total revenue for each product
def get_revenue_for_products(sales_data):
    product_revenue = {}
    for sale in sales_data:
        product = sale['Product']
        revenue = sale['Total Revenue']
        product_revenue[product] = product_revenue.get(product,0) + revenue

    return product_revenue

product_revenue = get_revenue_for_products(sales_data)
print(product_revenue)

# # Task 3: Identify the product that generated the maximum revenue
max_revenue_product = max(product_revenue, key=product_revenue.get)
print(max_revenue_product)

# Task 4: Calculate total revenue for each day
# date_revenue = {}
def get_revenue_per_day(sales_data):
    revenue_per_day = {}
    for sale in sales_data:
        day = sale['Date']
        revenue = sale['Total Revenue']
        revenue_per_day[day] = revenue_per_day.get(day,0) + revenue

    return revenue_per_day

revenue_per_day = get_revenue_per_day(sales_data)
print(revenue_per_day)

# Task 5: Identify the day with the highest total revenue
max_revenue_date = max(revenue_per_day, key=revenue_per_day.get)
print(max_revenue_date)
# Task 6: Calculate total units sold for each date
# product_units_sold = {}


# Task 7: Identify the product with the highest total units sold
# max_units_sold_product = max(product_units_sold, key=product_units_sold.get)

# Task 8: Calculate average unit price for each product - watch out for division by zero
# print("\nAverage unit price for each product:")
# product_unit_price = {}


# Display results
# print("Total revenue for each product:")
# code here

# print("\nThe product that generated the maximum revenue:")
# print(max_revenue_product)

# print("\nTotal revenue for each day:")
# code here

# print("\nThe day with the highest total revenue:")
# print(max_revenue_date)
#
# print("\nTotal units sold for each product:")
# code here

# print("\nThe product with the highest total units sold:")
# print(max_units_sold_product)
#
# print("\nAverage unit price for each product:")
# code here

### TODO how to deal with zero division