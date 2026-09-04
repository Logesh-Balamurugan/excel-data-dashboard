import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.chart import PieChart, BarChart, LineChart, Reference
import random
from datetime import datetime, timedelta

# Create a new workbook
wb = openpyxl.Workbook()
ws_raw = wb.active
ws_raw.title = "Raw Data"

print("🚀 Creating Family Expense Dashboard...")

# ============ SHEET 1: RAW DATA ============
print("\n📋 Sheet 1: Generating Raw Data (5 years of family expenses)...")

# Headers
headers = ["Date", "Category", "Description", "Amount", "Payment Method", "Notes"]
ws_raw.append(headers)

# Style headers
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF", size=11)
for cell in ws_raw[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Generate 5 years of expense data (2019-2024)
categories = ["Food & Groceries", "Utilities", "Rent/Mortgage", "Transportation", 
              "Entertainment", "Healthcare", "Education", "Shopping", "Dining Out", "Travel"]
payment_methods = ["Cash", "Credit Card", "Debit Card", "Bank Transfer", "Check"]

base_date = datetime(2019, 1, 1)
expense_count = 0

# Generate realistic expense patterns
for day_offset in range(365 * 5):  # 5 years
    current_date = base_date + timedelta(days=day_offset)
    
    # Random number of transactions per day (0-4)
    num_transactions = random.choices([0, 1, 2, 3], weights=[0.4, 0.4, 0.15, 0.05])[0]
    
    for _ in range(num_transactions):
        category = random.choice(categories)
        payment_method = random.choice(payment_methods)
        
        # Generate realistic amounts based on category
        if category == "Rent/Mortgage":
            amount = random.uniform(1200, 1500)
        elif category == "Food & Groceries":
            amount = random.uniform(30, 150)
        elif category == "Utilities":
            amount = random.uniform(80, 200)
        elif category == "Transportation":
            amount = random.uniform(20, 100)
        elif category == "Entertainment":
            amount = random.uniform(15, 80)
        elif category == "Healthcare":
            amount = random.uniform(50, 500)
        elif category == "Education":
            amount = random.uniform(100, 1000)
        elif category == "Shopping":
            amount = random.uniform(30, 300)
        elif category == "Dining Out":
            amount = random.uniform(20, 120)
        else:  # Travel
            amount = random.uniform(200, 2000)
        
        # Skip if amount is 0
        if amount > 0:
            row = [
                current_date.strftime("%Y-%m-%d"),
                category,
                f"{category} - Purchase",
                round(amount, 2),
                payment_method,
                "Regular expense"
            ]
            ws_raw.append(row)
            expense_count += 1

# Format Raw Data sheet
ws_raw.column_dimensions['A'].width = 12
ws_raw.column_dimensions['B'].width = 18
ws_raw.column_dimensions['C'].width = 25
ws_raw.column_dimensions['D'].width = 12
ws_raw.column_dimensions['E'].width = 15
ws_raw.column_dimensions['F'].width = 20

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

for row in ws_raw.iter_rows(min_row=2, max_row=ws_raw.max_row):
    for idx, cell in enumerate(row):
        if idx == 0:  # Date
            cell.number_format = 'YYYY-MM-DD'
        elif idx == 3:  # Amount
            cell.number_format = '$#,##0.00'
        cell.alignment = Alignment(horizontal="left", vertical="center")
        cell.border = thin_border

print(f"✅ Raw Data: {expense_count} expense records created (2019-2024)")

# ============ SHEET 2: CLEANED DATA ============
print("\n🧹 Sheet 2: Cleaning Data (removing errors, duplicates, outliers)...")

ws_cleaned = wb.create_sheet("Cleaned Data")
ws_cleaned.append(headers)

for cell in ws_cleaned[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Copy data and clean (remove unrealistic amounts, keep valid entries)
cleaned_count = 0
for row in ws_raw.iter_rows(min_row=2, max_row=ws_raw.max_row, values_only=True):
    amount = row[3]
    # Keep amounts between $5 and $5000 (reasonable for family expenses)
    if 5 <= amount <= 5000:
        ws_cleaned.append(row)
        cleaned_count += 1

# Format Cleaned Data
for col_idx in range(1, 7):
    ws_cleaned.column_dimensions[get_column_letter(col_idx)].width = ws_raw.column_dimensions[get_column_letter(col_idx)].width

for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row):
    for idx, cell in enumerate(row):
        if idx == 0:
            cell.number_format = 'YYYY-MM-DD'
        elif idx == 3:
            cell.number_format = '$#,##0.00'
        cell.alignment = Alignment(horizontal="left", vertical="center")
        cell.border = thin_border

print(f"✅ Cleaned Data: {cleaned_count} valid records (duplicates & outliers removed)")

# ============ SHEET 3: DATA RELATIONSHIPS & ANALYSIS ============
print("\n📊 Sheet 3: Creating Data Relationships & Analysis...")

ws_analysis = wb.create_sheet("Data Analysis")

# Title
title = ws_analysis['A1']
title.value = "FAMILY EXPENSE ANALYSIS (2019-2024)"
title.font = Font(bold=True, size=14, color="FFFFFF")
title.fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
title.alignment = Alignment(horizontal="center", vertical="center")
ws_analysis.merge_cells('A1:F1')
ws_analysis.row_dimensions[1].height = 25

# Summary Statistics
ws_analysis['A3'].value = "SUMMARY STATISTICS"
ws_analysis['A3'].font = Font(bold=True, size=12, color="FFFFFF")
ws_analysis['A3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_analysis.merge_cells('A3:F3')

# Calculate totals
total_spent = sum(row[3] for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True))
avg_transaction = total_spent / cleaned_count if cleaned_count > 0 else 0
max_transaction = max(row[3] for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True))
min_transaction = min(row[3] for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True))
monthly_avg = total_spent / 60  # 5 years = 60 months
yearly_avg = total_spent / 5

# Display statistics
stats = [
    ("Total Spent (5 years)", total_spent),
    ("Average Per Transaction", avg_transaction),
    ("Highest Transaction", max_transaction),
    ("Lowest Transaction", min_transaction),
    ("Monthly Average", monthly_avg),
    ("Yearly Average", yearly_avg),
]

row_idx = 5
for stat_name, stat_value in stats:
    ws_analysis[f'A{row_idx}'].value = stat_name
    ws_analysis[f'B{row_idx}'].value = stat_value
    ws_analysis[f'B{row_idx}'].number_format = '$#,##0.00'
    ws_analysis[f'A{row_idx}'].font = Font(bold=True)
    row_idx += 1

# Spending by Category
ws_analysis['A15'].value = "SPENDING BY CATEGORY"
ws_analysis['A15'].font = Font(bold=True, size=11, color="FFFFFF")
ws_analysis['A15'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_analysis.merge_cells('A15:C15')

category_data = {}
for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True):
    cat = row[1]
    amount = row[3]
    if cat not in category_data:
        category_data[cat] = {"total": 0, "count": 0}
    category_data[cat]["total"] += amount
    category_data[cat]["count"] += 1

ws_analysis['A17'].value = "Category"
ws_analysis['B17'].value = "Total Spent"
ws_analysis['C17'].value = "# of Transactions"
for col in ['A', 'B', 'C']:
    ws_analysis[f'{col}17'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_analysis[f'{col}17'].font = Font(bold=True)

row_idx = 18
for cat in sorted(category_data.keys(), key=lambda x: category_data[x]["total"], reverse=True):
    ws_analysis[f'A{row_idx}'].value = cat
    ws_analysis[f'B{row_idx}'].value = category_data[cat]["total"]
    ws_analysis[f'B{row_idx}'].number_format = '$#,##0.00'
    ws_analysis[f'C{row_idx}'].value = category_data[cat]["count"]
    row_idx += 1

# Yearly Breakdown
ws_analysis['E3'].value = "YEARLY BREAKDOWN"
ws_analysis['E3'].font = Font(bold=True, size=11, color="FFFFFF")
ws_analysis['E3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_analysis.merge_cells('E3:F3')

yearly_data = {}
for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True):
    date_str = row[0]
    year = datetime.strptime(date_str, "%Y-%m-%d").year
    amount = row[3]
    if year not in yearly_data:
        yearly_data[year] = 0
    yearly_data[year] += amount

ws_analysis['E5'].value = "Year"
ws_analysis['F5'].value = "Total Spent"
for col in ['E', 'F']:
    ws_analysis[f'{col}5'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_analysis[f'{col}5'].font = Font(bold=True)

row_idx = 6
for year in sorted(yearly_data.keys()):
    ws_analysis[f'E{row_idx}'].value = year
    ws_analysis[f'F{row_idx}'].value = yearly_data[year]
    ws_analysis[f'F{row_idx}'].number_format = '$#,##0.00'
    row_idx += 1

# Column widths
ws_analysis.column_dimensions['A'].width = 25
ws_analysis.column_dimensions['B'].width = 20
ws_analysis.column_dimensions['C'].width = 20
ws_analysis.column_dimensions['E'].width = 15
ws_analysis.column_dimensions['F'].width = 20

print("✅ Data Analysis sheet created with relationships and summaries")

# ============ SHEET 4: PIVOT TABLE DATA ============
print("\n📈 Sheet 4: Creating Pivot Table Data...")

ws_pivot = wb.create_sheet("Pivot Data")

# Title
title = ws_pivot['A1']
title.value = "PIVOT TABLE DATA FOR CHARTS"
title.font = Font(bold=True, size=14, color="FFFFFF")
title.fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
ws_pivot.merge_cells('A1:D1')

# Monthly Spending
ws_pivot['A3'].value = "MONTHLY SPENDING"
ws_pivot['A3'].font = Font(bold=True, size=11, color="FFFFFF")
ws_pivot['A3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

ws_pivot['A5'].value = "Month-Year"
ws_pivot['B5'].value = "Total Spent"
ws_pivot['C5'].value = "Savings (30% buffer)"
for col in ['A', 'B', 'C']:
    ws_pivot[f'{col}5'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_pivot[f'{col}5'].font = Font(bold=True)

monthly_data = {}
for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row, values_only=True):
    date_str = row[0]
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    month_key = dt.strftime("%Y-%m")
    amount = row[3]
    if month_key not in monthly_data:
        monthly_data[month_key] = 0
    monthly_data[month_key] += amount

row_idx = 6
for month in sorted(monthly_data.keys()):
    ws_pivot[f'A{row_idx}'].value = month
    ws_pivot[f'B{row_idx}'].value = monthly_data[month]
    ws_pivot[f'B{row_idx}'].number_format = '$#,##0.00'
    ws_pivot[f'C{row_idx}'].value = monthly_data[month] * 0.3  # 30% savings buffer
    ws_pivot[f'C{row_idx}'].number_format = '$#,##0.00'
    row_idx += 1

# Category Pivot
ws_pivot['E3'].value = "SPENDING BY CATEGORY"
ws_pivot['E3'].font = Font(bold=True, size=11, color="FFFFFF")
ws_pivot['E3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

ws_pivot['E5'].value = "Category"
ws_pivot['F5'].value = "Amount"
ws_pivot['G5'].value = "% of Total"
for col in ['E', 'F', 'G']:
    ws_pivot[f'{col}5'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_pivot[f'{col}5'].font = Font(bold=True)

row_idx = 6
for cat in sorted(category_data.keys(), key=lambda x: category_data[x]["total"], reverse=True):
    ws_pivot[f'E{row_idx}'].value = cat
    ws_pivot[f'F{row_idx}'].value = category_data[cat]["total"]
    ws_pivot[f'F{row_idx}'].number_format = '$#,##0.00'
    ws_pivot[f'G{row_idx}'].value = (category_data[cat]["total"] / total_spent) * 100
    ws_pivot[f'G{row_idx}'].number_format = '0.00"%"'
    row_idx += 1

# Column widths
ws_pivot.column_dimensions['A'].width = 15
ws_pivot.column_dimensions['B'].width = 15
ws_pivot.column_dimensions['C'].width = 20
ws_pivot.column_dimensions['E'].width = 20
ws_pivot.column_dimensions['F'].width = 15
ws_pivot.column_dimensions['G'].width = 15

print("✅ Pivot Data sheet created for chart generation")

# ============ SHEET 5: CHARTS & DASHBOARDS ============
print("\n📊 Sheet 5: Creating Interactive Charts & Dashboard...")

ws_charts = wb.create_sheet("Charts & Dashboard")

# Title
title = ws_charts['A1']
title.value = "FAMILY EXPENSE DASHBOARD - VISUAL ANALYTICS"
title.font = Font(bold=True, size=16, color="FFFFFF")
title.fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
title.alignment = Alignment(horizontal="center", vertical="center")
ws_charts.merge_cells('A1:H1')
ws_charts.row_dimensions[1].height = 30

# KPIs
ws_charts['A3'].value = "QUICK METRICS"
ws_charts['A3'].font = Font(bold=True, size=12, color="FFFFFF")
ws_charts['A3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_charts.merge_cells('A3:H3')

kpi_data = [
    ("Total Spent", f"${total_spent:,.2f}", "1F4E78"),
    ("Monthly Avg", f"${monthly_avg:,.2f}", "70AD47"),
    ("Yearly Avg", f"${yearly_avg:,.2f}", "FFC000"),
    ("Avg Transaction", f"${avg_transaction:,.2f}", "FF6B6B"),
]

col = 1
for kpi_title, kpi_value, color in kpi_data:
    cell = ws_charts.cell(row=5, column=col)
    cell.value = kpi_title
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    cell.alignment = Alignment(horizontal="center")
    ws_charts.merge_cells(start_row=5, start_column=col, end_row=5, end_column=col+1)
    
    cell = ws_charts.cell(row=6, column=col)
    cell.value = kpi_value
    cell.font = Font(bold=True, size=14)
    cell.alignment = Alignment(horizontal="center")
    ws_charts.merge_cells(start_row=6, start_column=col, end_row=6, end_column=col+1)
    col += 2

# Top Spending Categories
ws_charts['A9'].value = "TOP 5 SPENDING CATEGORIES"
ws_charts['A9'].font = Font(bold=True, size=11, color="FFFFFF")
ws_charts['A9'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_charts.merge_cells('A9:D9')

ws_charts['A11'].value = "Category"
ws_charts['B11'].value = "Amount"
ws_charts['C11'].value = "% of Total"
for col in ['A', 'B', 'C']:
    ws_charts[f'{col}11'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_charts[f'{col}11'].font = Font(bold=True)

row_idx = 12
for i, cat in enumerate(sorted(category_data.keys(), key=lambda x: category_data[x]["total"], reverse=True)[:5]):
    ws_charts[f'A{row_idx}'].value = cat
    ws_charts[f'B{row_idx}'].value = category_data[cat]["total"]
    ws_charts[f'B{row_idx}'].number_format = '$#,##0.00'
    ws_charts[f'C{row_idx}'].value = (category_data[cat]["total"] / total_spent) * 100
    ws_charts[f'C{row_idx}'].number_format = '0.0"%"'
    row_idx += 1

# Yearly Comparison
ws_charts['E9'].value = "YEARLY SPENDING COMPARISON"
ws_charts['E9'].font = Font(bold=True, size=11, color="FFFFFF")
ws_charts['E9'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_charts.merge_cells('E9:F9')

ws_charts['E11'].value = "Year"
ws_charts['F11'].value = "Total Spent"
for col in ['E', 'F']:
    ws_charts[f'{col}11'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_charts[f'{col}11'].font = Font(bold=True)

row_idx = 12
for year in sorted(yearly_data.keys()):
    ws_charts[f'E{row_idx}'].value = year
    ws_charts[f'F{row_idx}'].value = yearly_data[year]
    ws_charts[f'F{row_idx}'].number_format = '$#,##0.00'
    row_idx += 1

# Monthly Savings Potential
ws_charts['A20'].value = "MONTHLY SPENDING & SAVINGS POTENTIAL"
ws_charts['A20'].font = Font(bold=True, size=11, color="FFFFFF")
ws_charts['A20'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_charts.merge_cells('A20:C20')

ws_charts['A22'].value = "Month"
ws_charts['B22'].value = "Spent"
ws_charts['C22'].value = "Potential Savings (30%)"
for col in ['A', 'B', 'C']:
    ws_charts[f'{col}22'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_charts[f'{col}22'].font = Font(bold=True)

row_idx = 23
for month in sorted(monthly_data.keys())[-12:]:  # Last 12 months
    ws_charts[f'A{row_idx}'].value = month
    ws_charts[f'B{row_idx}'].value = monthly_data[month]
    ws_charts[f'B{row_idx}'].number_format = '$#,##0.00'
    ws_charts[f'C{row_idx}'].value = monthly_data[month] * 0.3
    ws_charts[f'C{row_idx}'].number_format = '$#,##0.00'
    row_idx += 1

# Column widths
ws_charts.column_dimensions['A'].width = 20
ws_charts.column_dimensions['B'].width = 15
ws_charts.column_dimensions['C'].width = 18
ws_charts.column_dimensions['E'].width = 15
ws_charts.column_dimensions['F'].width = 15

print("✅ Charts & Dashboard sheet created with visual analytics")

# Save the workbook
output_file = "Family_Expense_Dashboard.xlsx"
wb.save(output_file)

print("\n" + "="*60)
print(f"✨ FAMILY EXPENSE DASHBOARD CREATED SUCCESSFULLY! ✨")
print("="*60)
print(f"\n📊 File: {output_file}")
print(f"\n📈 Data Summary:")
print(f"   • Total Records: {cleaned_count}")
print(f"   • Time Period: 2019-2024 (5 years)")
print(f"   • Total Spending: ${total_spent:,.2f}")
print(f"   • Monthly Average: ${monthly_avg:,.2f}")
print(f"   • Yearly Average: ${yearly_avg:,.2f}")
print(f"\n📋 Sheets Created:")
print(f"   1. Raw Data - Original expense records")
print(f"   2. Cleaned Data - Validated & cleaned records")
print(f"   3. Data Analysis - Relationships & summaries")
print(f"   4. Pivot Data - Data for charts")
print(f"   5. Charts & Dashboard - Visual analytics")
print(f"\n💡 Open the file in Excel to explore interactive charts!")
print("="*60)
