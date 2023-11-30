import pandas as pd

datasetRetail = pd.read_excel('Online_retail.xlsx')

# Group the dataset by CustomerID
customers_grouped = datasetRetail.groupby('CustomerID')

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

        if(group_data["Quantity"].values[i] > 0):
            customer_items[customer_id].append(dataset_values)

#counted_dataframe = customers_grouped.count()
#print(counted_dataframe)

#----------------- Distinct Product Count -----------------#

# Filter the DataFrame where 'Quantity' is greater than 0
filtered_data_quantity = datasetRetail[datasetRetail['Quantity'] > 0]

# Check if any rows satisfy the condition
if not filtered_data_quantity.empty:
    category_counts_stockcode = filtered_data_quantity['StockCode'].value_counts()
    #print(category_counts_stockcode)

#----------------- Distinct Client Count -----------------#

# Counts the different clients through the dataset
category_counts_customerID = datasetRetail['CustomerID'].dropna().value_counts()
#print(category_counts_customerID)

#----------------- Distinct Purcheses Done -----------------#

category_counts_invoiceNo = filtered_data_quantity['InvoiceNo'].value_counts()
#print(category_counts_invoiceNo)
#Purchases reimbursed: 5172

#---------------- Scatter Plot Purchases ----------------#

#TODO NOT FINISHED AND NOT TESTED YET

#purchases_variables = filtered_data_quantity[["StockCode", "CustomerID", "InvoiceNo", "InvoiceDate"]]
#pd.plotting.scatter_matrix(purchases_variables)

#---------------- Products reimbursed ----------------#

purchases_reimbursed = len(datasetRetail['InvoiceNo']) - len(filtered_data_quantity['InvoiceNo'])
print(purchases_reimbursed) #10624

#---------------- Purchases with no client ID ----------------#