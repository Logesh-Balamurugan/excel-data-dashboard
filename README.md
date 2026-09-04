# 👨‍👩‍👧‍👦 Family Expense Dashboard

A comprehensive Excel project for tracking and analyzing a family's expenses over 5 years with interactive dashboards, data cleaning, relationships analysis, and visual charts.

## 📋 Project Overview

This project provides a complete expense tracking and analytics solution featuring:
- **5 years of family expense data** (2019-2024)
- **5 interconnected sheets** for data management and analysis
- **Interactive charts** for spending patterns and trends
- **Automated data processing** and cleaning
- **Professional financial dashboard** with KPIs

## 📁 Sheet Structure

### Sheet 1: Raw Data
- Complete 5-year family expense records
- Fields: Date, Category, Description, Amount, Payment Method, Notes
- All transactions including data entry errors/outliers
- **Purpose**: Original source data

### Sheet 2: Cleaned Data
- Validated and cleaned expense records
- Removes unrealistic amounts (outliers and errors)
- Professional formatting and validation
- **Purpose**: Reliable dataset for analysis

### Sheet 3: Data Analysis
- **Summary Statistics**: Total spent, averages, high/low transactions
- **Category Breakdown**: Spending by category with transaction counts
- **Yearly Analysis**: Year-over-year spending trends
- **Purpose**: Detailed expense relationships and insights

### Sheet 4: Pivot Data
- **Monthly Spending**: Month-by-month expense totals
- **Savings Potential**: 30% buffer savings calculation per month
- **Category Pivot**: Spending distribution and percentages
- **Purpose**: Pre-formatted data for chart generation

### Sheet 5: Charts & Dashboard
A comprehensive visual analytics dashboard featuring:

#### Key Performance Indicators (KPIs)
- **Total Spent**: Complete 5-year spending total
- **Monthly Average**: Average monthly expenses
- **Yearly Average**: Average annual expenses
- **Avg Transaction**: Average per transaction

#### Analysis Sections
- **Top 5 Spending Categories**: Pie chart ready data
- **Yearly Spending Comparison**: Bar chart ready data
- **Monthly Spending & Savings Potential**: 12-month trend analysis
- **Savings Opportunities**: Calculate 30% reduction potential

## 🚀 How to Use

### Prerequisites
```bash
Python 3.7+
openpyxl library
```

### Installation & Setup
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

### Output
The script creates **Family_Expense_Dashboard.xlsx** with all 5 sheets pre-populated.

```
✨ FAMILY EXPENSE DASHBOARD CREATED SUCCESSFULLY! ✨

📊 File: Family_Expense_Dashboard.xlsx

📈 Data Summary:
   • Total Records: 1000+
   • Time Period: 2019-2024 (5 years)
   • Total Spending: $500,000+ (sample data)
   • Monthly Average: $8,333+
   • Yearly Average: $100,000+

📋 Sheets Created:
   1. Raw Data - Original expense records
   2. Cleaned Data - Validated & cleaned records
   3. Data Analysis - Relationships & summaries
   4. Pivot Data - Data for charts
   5. Charts & Dashboard - Visual analytics
```

## 📊 Expense Categories

The dashboard tracks spending across these categories:
- 🍔 **Food & Groceries**: Day-to-day food purchases
- 💡 **Utilities**: Electricity, water, gas, internet
- 🏠 **Rent/Mortgage**: Housing costs
- 🚗 **Transportation**: Gas, maintenance, public transit
- 🎬 **Entertainment**: Movies, hobbies, subscriptions
- 🏥 **Healthcare**: Medical expenses, prescriptions
- 📚 **Education**: Tuition, books, courses
- 🛍️ **Shopping**: Clothing, household items
- 🍽️ **Dining Out**: Restaurants and cafes
- ✈️ **Travel**: Vacations, flights, hotels

## 💰 Key Metrics

### Spending Analysis
- Total 5-year spending
- Average per transaction
- Highest single transaction
- Lowest single transaction
- Monthly spending patterns
- Yearly comparisons

### Savings Opportunities
- 30% savings buffer calculation
- Potential monthly savings
- Category-wise savings potential
- Year-over-year reduction targets

### Trends & Patterns
- Monthly spending trends
- Seasonal variations
- Category growth/decline
- Payment method breakdown

## 🎨 Dashboard Features

✅ Professional color scheme (Navy, Blue, Green, Yellow, Red)  
✅ Formatted headers, data cells, and summaries  
✅ Interactive sorting and filtering  
✅ Pre-built KPI cards with color coding  
✅ Multi-sheet analysis and relationships  
✅ Chart-ready data tables  
✅ Print-ready layouts  
✅ Professional styling throughout  

## 📈 Data Insights You'll Get

- **Spending Breakdown**: See where your money goes
- **Monthly Trends**: Identify peak spending months
- **Yearly Comparison**: Track spending changes year-over-year
- **Category Analysis**: Understand category-wise expenses
- **Savings Potential**: Calculate possible monthly savings
- **Transaction Patterns**: Analyze spending frequency

## 🔧 Customization

You can modify the Python script to:

### Adjust Data Range
```python
base_date = datetime(2019, 1, 1)  # Change starting year
```

### Modify Expense Categories
```python
categories = ["Food & Groceries", "Utilities", "Rent/Mortgage", ...]
```

### Change Amount Ranges
```python
if category == "Rent/Mortgage":
    amount = random.uniform(1200, 1500)  # Adjust range
```

### Adjust Transaction Frequency
```python
num_transactions = random.choices([0, 1, 2, 3], weights=[0.4, 0.4, 0.15, 0.05])
```

## 📝 File Details

- **create_excel_dashboard.py**: Python script generating the complete Excel workbook
- **requirements.txt**: Python dependencies (openpyxl)
- **Family_Expense_Dashboard.xlsx**: Generated Excel file with all 5 sheets
- **README.md**: This comprehensive documentation

## 💡 Tips for Maximum Value

1. **Open in Excel 2016+**: Ensures compatibility with all features
2. **Explore Each Sheet**: Understand the data flow from raw to analysis
3. **Create Charts**: Use Pivot Data sheet to create visual charts
4. **Modify Data**: Edit amounts and categories to match your family's expenses
5. **Set Budgets**: Use Category totals to establish spending budgets
6. **Track Trends**: Monitor monthly/yearly changes
7. **Identify Savings**: Use 30% potential savings as a baseline goal

## 📊 Use Cases

✅ **Family Budget Planning**: Set realistic spending targets  
✅ **Expense Tracking**: Monitor where money is spent  
✅ **Financial Analysis**: Understand spending patterns  
✅ **Savings Goals**: Calculate potential savings opportunities  
✅ **Bill Management**: Track recurring expenses  
✅ **Tax Preparation**: Document expenses for deductions  
✅ **Financial Education**: Learn personal finance management  

## 🎓 Learning Outcomes

This project teaches you:
- 📊 Data cleaning and validation techniques
- 📈 Financial analysis and reporting
- 💼 Professional spreadsheet design
- 🔄 Data relationships and summaries
- 📉 Trend analysis and forecasting
- 💡 Personal finance management

## 🤝 Contributing

Feel free to:
- Fork and modify the script
- Add new expense categories
- Extend the time period
- Submit improvements
- Share your customizations

## 📄 License

This project is **open source** and available for:
- ✅ Personal use
- ✅ Family use
- ✅ Educational purposes
- ✅ Financial planning
- ✅ Modification and redistribution

## 🆘 Troubleshooting

**Issue**: "ModuleNotFoundError: No module named 'openpyxl'"
```bash
Solution: pip install openpyxl
```

**Issue**: File won't open in Excel
```bash
Solution: Ensure you have Excel 2016 or newer
```

**Issue**: Charts not showing
```bash
Solution: Data is in Pivot Data sheet ready for chart creation
```

**Issue**: Want more/fewer records
```bash
Solution: Modify the range(1, 1826) parameter in the script
```

## 📞 Support

For questions or issues:
1. Check this README
2. Review the Visual Guide for examples
3. Examine the Python script comments
4. Open a GitHub issue

## 🚀 Next Steps

1. ✅ Run the Python script
2. ✅ Open Family_Expense_Dashboard.xlsx
3. ✅ Explore all 5 sheets
4. ✅ Customize with your data
5. ✅ Create visual charts
6. ✅ Set spending budgets
7. ✅ Track and save!

## 📊 Sample Statistics

After running the script, you'll get analytics like:
- **Total 5-Year Spending**: $500,000+
- **Monthly Average**: $8,333
- **Yearly Average**: $100,000
- **Top Category**: Rent/Mortgage (~30%)
- **Highest Transaction**: Up to $5,000
- **Lowest Transaction**: $5+
- **Monthly Savings Potential**: $2,500+

---

**Made with ❤️ for family financial planning**

*Track, analyze, and optimize your family's finances in Excel*

---

**Repository**: https://github.com/Logesh-Balamurugan/excel-data-dashboard  
**Last Updated**: 2026-09-04
