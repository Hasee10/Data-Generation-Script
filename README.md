# 📦 MNC Logistics Dataset Generator

## 🧭 Overview

This project generates a large-scale, synthetic logistics dataset designed for data analytics, visualization, and business intelligence tools especially for platforms like Power BI. The output is an Excel workbook titled

```
MNC_Logistics_Dataset.xlsx
```

This workbook contains realistic but randomly generated logistics data for use in dashboards, analytics models, and data warehousing practice.

---

## 📁 Output Excel File Structure

The Excel file includes the following sheets:

1. **Orders** — Main transactional data with 1 million rows
2. **Clients** — Dimension table for clients
3. **Products** — Dimension table for products
4. **Warehouses** — Dimension table for warehouses

---

## ⚙️ How to Run the Script

### 🖥️ Requirements:

* Python 3.8+
* Required libraries:

  * `pandas`
  * `numpy`
  * `xlsxwriter` (automatically used by `pandas.ExcelWriter`)

Install them (if not already):

```bash
pip install pandas numpy
```

### ▶️ Execution:

From your terminal or PowerShell (in the project directory):

```bash
python pyy.py
```

The script will generate a file named `MNC_Logistics_Dataset.xlsx` in the same folder.

---

## 🔍 What the Script Does (Step-by-Step)

### 1. 🧪 Importing Libraries

It uses:

* `pandas`: for structured data creation and Excel export
* `numpy`: for efficient array-based random data generation
* `random`: for Python-based seed control
* `datetime`: to compute delivery and order timelines

---

### 2. 🔄 Reproducibility

The script sets fixed seeds (`np.random.seed(42)` and `random.seed(42)`) so that every run produces the same dataset, useful for testing and comparisons.

---

### 3. 📌 Constants and Domain Setup

It simulates real-world logistics fields with controlled randomness:

* 🔢 1,000,000 unique orders
* 🌍 Countries: USA, Germany, India, China, Brazil, etc.
* 🚛 Transport Modes: Air, Sea, Road, Rail
* 📦 Statuses: In Transit, Delivered, Pending, Delayed, Cancelled
* 👤 500 Clients (Client\_1 to Client\_500)
* 🛒 1000 Products
* 🏬 20 Warehouses

---

### 4. 📊 Main Table: Orders

Generated as a DataFrame with 1 million records containing:

| Column               | Description                            |
| -------------------- | -------------------------------------- |
| `OrderID`            | Unique order number                    |
| `Client`             | Random client from list                |
| `Product`            | Random product from list               |
| `SourceCountry`      | Random country of origin               |
| `DestinationCountry` | Random destination                     |
| `Warehouse`          | Random warehouse                       |
| `TransportMode`      | Air, Sea, Road, Rail                   |
| `Status`             | Order status                           |
| `OrderDate`          | Date between Jan 2022 and mid-2024     |
| `DeliveryDays`       | Integer from 1 to 30                   |
| `WeightKg`           | Float weight between 0.5kg and 1000kg  |
| `CostUSD`            | Float price between \$100 and \$5000   |
| `DeliveryDate`       | Calculated as OrderDate + DeliveryDays |

---

### 5. 🧱 Dimension Tables

Each dimension table gives context for linking and filtering:

#### 🧑‍💼 Clients:

* 500 entries: `Client_1` to `Client_500`
* Each assigned a random region

#### 🛍️ Products:

* 1000 entries: `Product_1` to `Product_1000`
* Randomly categorized into:

  * Electronics, Clothing, Furniture, Machinery, Perishables

#### 🏢 Warehouses:

* 20 entries: `WH_1` to `WH_20`
* Randomly placed in one of the countries

---

### 6. 💾 Excel File Export

Using `pandas.ExcelWriter` with `xlsxwriter`, it writes each DataFrame to a separate sheet in a single `.xlsx` file.

| Sheet Name | Contents                  |
| ---------- | ------------------------- |
| Orders     | 1M transactional records  |
| Clients    | Client dimension table    |
| Products   | Product dimension table   |
| Warehouses | Warehouse dimension table |

---

## 📊 Intended Use

This dataset is ideal for:

* Power BI and Tableau dashboards
* ETL pipeline testing
* Dimension modeling (star/snowflake schema)
* SQL practice and training
* Machine learning prototyping (e.g., delivery time prediction)

---

## 📦 File Output Example

Once complete, you will find:

```
📁 IntegCubes_DataSet/
├── pyy.py
├── MNC_Logistics_Dataset.xlsx
└── README.md
```

---

## ✅ Final Notes

* The script is modular and can be extended to include more fields, new dimensions, or realistic constraints.
* Due to its size (1 million rows), Excel may lag on weaker machines; use CSV or SQL exports if needed.

