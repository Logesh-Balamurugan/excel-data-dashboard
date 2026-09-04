# 📊 Excel Data Dashboard Project

A comprehensive Excel project that handles thousands of data records with interactive dashboards, data cleaning, and advanced analytics using pivot tables.

## 📋 Project Overview

This project demonstrates enterprise-level data handling in Microsoft Excel with:
- **1000+ records** of sample sales data
- **4 interconnected sheets** for data management and analysis
- **Interactive dashboard** with KPIs and visual analytics
- **Automated data processing** using Python

## 📁 Sheet Structure

### Sheet 1: Raw Data
- Contains 1,000 raw records of sales transactions
- Fields: ID, Date, Product, Category, Quantity, Unit Price, Total Sales, Region, Customer, Status
- Data includes various products, regions, and order statuses
- **Purpose**: Source data for analysis and cleaning

### Sheet 2: Cleaned Data
- Cleaned version of raw data (cancelled orders removed)
- ~900+ valid records for analysis
- Formatted with consistent styling
- **Purpose**: Reliable dataset for accurate reporting

### Sheet 3: Pivot Tables
Multiple pivot table analyses:
1. **Sales by Region** - Total sales aggregated by geographic region
2. **Sales by Product** - Performance metrics for each product
3. **Order Status Summary** - Count of orders by status (Completed, Pending, Shipped, Cancelled)
- **Purpose**: Quick insights into sales patterns

### Sheet 4: Interactive Dashboard
A comprehensive analytics dashboard featuring:

#### Key Performance Indicators (KPIs)
- **Total Sales**: Aggregate revenue from all orders
- **Total Orders**: Count of completed transactions
- **Average Order Value**: Mean transaction value
- **Completed Orders**: Number of successfully completed orders

#### Sales Summary by Region
- Regional breakdown of sales performance
- Order counts per region
- Average order value by region

#### Top Selling Products
- Top 8 products by revenue
- Quantity sold per product
- Average pricing analysis

## 🚀 How to Use

### Prerequisites
```bash
python 3.7+
openpyxl library
```

### Installation
```bash
# Clone the repository
git clone https://github.com/Logesh-Balamurugan/excel-data-dashboard.git
cd excel-data-dashboard

# Install dependencies
pip install -r requirements.txt
```

### Generate the Excel File
```bash
python create_excel_dashboard.py
```

This will create **Sales_Data_Dashboard.xlsx** in the current directory.

### Output
```
✅ Excel file 'Sales_Data_Dashboard.xlsx' created successfully!

File Structure:
  Sheet 1: Raw Data (1000 records with sales information)
  Sheet 2: Cleaned Data (900+ records, cancelled orders removed)
  Sheet 3: Pivot Tables (Sales by Region, Product, and Status Summary)
  Sheet 4: Interactive Dashboard (KPIs, Regional Analysis, Top Products)
```

## 📊 Data Specifications

### Sample Data Range
- **Date Range**: January 2023 - December 2023
- **Products**: Laptop, Mouse, Keyboard, Monitor, Headphones, USB Cable, Webcam, SSD
- **Categories**: Electronics, Accessories, Peripherals
- **Regions**: North, South, East, West, Central
- **Customers**: 100+ unique customer records
- **Order Statuses**: Completed, Pending, Shipped, Cancelled

### Data Volume
- **Total Records**: 1,000
- **Valid Records (Cleaned)**: 900+
- **Data Points**: 10 fields per record = 10,000+ data points

## 🎯 Features

✅ Handles thousands of records efficiently  
✅ Automated data cleaning pipeline  
✅ Professional styling and formatting  
✅ Interactive pivot tables for quick analysis  
✅ Comprehensive KPI dashboard  
✅ Regional and product-level analytics  
✅ Ready-to-use Excel file  
✅ Scalable Python script  

## 🔧 Customization

You can modify the script to:
- Change the number of records: Update the `range(1, 1001)` parameter
- Add different products/regions: Modify the lists in the script
- Adjust date ranges: Change the `base_date` variable
- Add more metrics: Extend the pivot table and dashboard sections

## 📈 Analysis Use Cases

1. **Sales Performance**: Track revenue by region and product
2. **Customer Insights**: Analyze order patterns and customer distribution
3. **Product Analysis**: Identify top-selling products
4. **Quality Metrics**: Monitor order completion rates
5. **Pricing Strategy**: Analyze average order values across regions

## 📝 File Details

- **create_excel_dashboard.py**: Main Python script that generates the Excel file
- **requirements.txt**: Python dependencies
- **Sales_Data_Dashboard.xlsx**: Generated Excel file (created after running the script)

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

## 📄 License

This project is open source and available for personal and commercial use.

## 💡 Tips

- Open the Excel file in Microsoft Excel for best compatibility
- All charts and pivot tables are fully interactive in Excel
- You can filter, sort, and drill down into any data
- The dashboard updates automatically if you modify the source data
- Use "Refresh All" in Excel to update pivot tables after data changes

## 📧 Support

For questions or issues, please open a GitHub issue in the repository.

---

**Happy analyzing! 📊**
