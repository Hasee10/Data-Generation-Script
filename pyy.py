# Re-importing and regenerating the Excel dataset with 1 million rows for Power BI use

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Constants
num_rows = 1_000_000
countries = ['USA', 'Germany', 'India', 'China', 'Brazil', 'UK', 'UAE', 'Australia', 'Canada', 'South Africa']
transport_modes = ['Air', 'Sea', 'Road', 'Rail']
statuses = ['In Transit', 'Delivered', 'Pending', 'Delayed', 'Cancelled']
clients = [f'Client_{i}' for i in range(1, 501)]
products = [f'Product_{i}' for i in range(1, 1001)]
warehouses = [f'WH_{i}' for i in range(1, 21)]

# Generate main Orders table
orders = pd.DataFrame({
    'OrderID': np.arange(1, num_rows + 1),
    'Client': np.random.choice(clients, num_rows),
    'Product': np.random.choice(products, num_rows),
    'SourceCountry': np.random.choice(countries, num_rows),
    'DestinationCountry': np.random.choice(countries, num_rows),
    'Warehouse': np.random.choice(warehouses, num_rows),
    'TransportMode': np.random.choice(transport_modes, num_rows),
    'Status': np.random.choice(statuses, num_rows),
    'OrderDate': pd.to_datetime('2022-01-01') + pd.to_timedelta(np.random.randint(0, 900, size=num_rows), unit='d'),
    'DeliveryDays': np.random.randint(1, 30, size=num_rows),
    'WeightKg': np.round(np.random.uniform(0.5, 1000, size=num_rows), 2),
    'CostUSD': np.round(np.random.uniform(100, 5000, size=num_rows), 2)
})

orders['DeliveryDate'] = orders['OrderDate'] + pd.to_timedelta(orders['DeliveryDays'], unit='d')

# Dimension tables
clients_df = pd.DataFrame({
    'Client': clients,
    'ClientRegion': np.random.choice(countries, len(clients))
})

products_df = pd.DataFrame({
    'Product': products,
    'ProductCategory': np.random.choice(['Electronics', 'Clothing', 'Furniture', 'Machinery', 'Perishables'], len(products))
})

warehouses_df = pd.DataFrame({
    'Warehouse': warehouses,
    'LocationCountry': np.random.choice(countries, len(warehouses))
})

# Save to Excel
file_path = "MNC_Logistics_Dataset.xlsx"
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    orders.to_excel(writer, sheet_name='Orders', index=False)
    clients_df.to_excel(writer, sheet_name='Clients', index=False)
    products_df.to_excel(writer, sheet_name='Products', index=False)
    warehouses_df.to_excel(writer, sheet_name='Warehouses', index=False)

file_path
