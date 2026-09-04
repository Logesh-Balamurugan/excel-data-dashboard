# Excel Dashboard Project - Quick Start Guide

## What's Included?

This project creates a professional Excel dashboard that analyzes **1,000+ sales records** with:

### 📊 4 Interactive Sheets:
1. **Raw Data** - 1,000 original sales records
2. **Cleaned Data** - Filtered, quality-assured dataset (~900 records)
3. **Pivot Tables** - Quick analytics summaries
4. **Interactive Dashboard** - Visual KPIs and insights

## 🚀 Quick Start

### Step 1: Install Python (if not already installed)
- Download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Script
```bash
python create_excel_dashboard.py
```

### Step 4: Open the Excel File
- Find `Sales_Data_Dashboard.xlsx` in your project folder
- Open it in Microsoft Excel
- Explore the 4 sheets!

## 📈 Dashboard Highlights

### KPI Metrics
- **Total Sales**: Sum of all completed transactions
- **Total Orders**: Count of valid orders
- **Average Order Value**: Mean price per order
- **Completed Orders**: Successfully processed transactions

### Analysis Sections
- Sales breakdown by region (North, South, East, West, Central)
- Top products ranked by revenue
- Order status tracking
- Regional performance comparison

## 🎯 Use Cases

✅ Sales reporting and analytics  
✅ Regional performance tracking  
✅ Product performance analysis  
✅ Customer insights  
✅ Business intelligence  

## 💻 Technical Details

- **Language**: Python 3.7+
- **Excel Library**: openpyxl
- **Data Records**: 1,000 sales transactions
- **File Format**: .xlsx (Microsoft Excel)

## 📝 Data Included

| Field | Sample Values |
|-------|---|
| Products | Laptop, Mouse, Keyboard, Monitor, Headphones, USB Cable, Webcam, SSD |
| Regions | North, South, East, West, Central |
| Categories | Electronics, Accessories, Peripherals |
| Statuses | Completed, Pending, Shipped, Cancelled |
| Date Range | Jan 2023 - Dec 2023 |

## 🔄 Next Steps

After running the script:
1. Open `Sales_Data_Dashboard.xlsx`
2. Click on Sheet tabs to explore different views
3. Use Excel's built-in features to:
   - Filter data
   - Sort records
   - Create additional charts
   - Export reports

## 📚 Learn More

For detailed information about each sheet, check the [README.md](README.md) file.

## ❓ Troubleshooting

**Error: "ModuleNotFoundError: No module named 'openpyxl'"**
```bash
pip install openpyxl
```

**Excel file not created?**
- Ensure Python script ran without errors
- Check that you have write permissions in the folder
- Try running in a different directory

**Need more records?**
- Edit `create_excel_dashboard.py`
- Change `range(1, 1001)` to `range(1, 5001)` for 5,000 records

---

**Created with ❤️ for data analytics enthusiasts**
