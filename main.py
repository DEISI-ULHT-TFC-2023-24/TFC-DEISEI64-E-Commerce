import pandas as pd

datasetRetail = pd.read_excel('Online_retail.xlsx')

# Group the dataset by CustomerID
customers_grouped = datasetRetail.groupby('CustomerID')
print(customers_grouped)

# Creates an empty dictionary to store the items bought by each customer
customer_items = {}

# Iterates through each customer
for customer_id, group_data in customers_grouped:

    # Checks if customer_id is already in dictionary
    if not (customer_id in customer_items.keys()):
        customer_items[customer_id] = []

    # For each costumer_id, it adds the product to that costumer
    for i in range(len(group_data["Country"].values)):
        dataset_values = {"Country": group_data["Country"].values[i],
                          "StockCode": group_data["StockCode"].values[i],
                          "Description": group_data["Description"].values[i],
                          "Quantity": group_data["Quantity"].values[i],
                          "InvoiceDate": group_data["InvoiceDate"].values[i],
                          "UnitPrice": group_data["UnitPrice"].values[i],
                          "InvoiceNo": group_data["InvoiceNo"].values[i]}

        customer_items[customer_id].append(dataset_values)

print(customer_items)