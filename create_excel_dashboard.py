import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.pivot_table import PivotTable, PivotTableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
import random
from datetime import datetime, timedelta

# Create a new workbook
wb = openpyxl.Workbook()
ws_raw = wb.active
ws_raw.title = "Raw Data"

# ============ SHEET 1: RAW DATA ============
print("Creating Sheet 1: Raw Data...")

# Headers for raw data
headers = ["ID", "Date", "Product", "Category", "Quantity", "Unit Price", "Total Sales", "Region", "Customer", "Status"]
ws_raw.append(headers)

# Style headers
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF")
for cell in ws_raw[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Generate sample data (1000 records)
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "USB Cable", "Webcam", "SSD"]
categories = ["Electronics", "Accessories", "Peripherals"]
regions = ["North", "South", "East", "West", "Central"]
statuses = ["Completed", "Pending", "Cancelled", "Shipped"]
customers = [f"Customer_{i}" for i in range(1, 101)]

base_date = datetime(2023, 1, 1)

for i in range(1, 1001):
    row = [
        i,
        base_date + timedelta(days=random.randint(0, 365)),
        random.choice(products),
        random.choice(categories),
        random.randint(1, 50),
        random.uniform(10, 500),
        random.uniform(100, 5000),
        random.choice(regions),
        random.choice(customers),
        random.choice(statuses)
    ]
    ws_raw.append(row)

# Format columns
ws_raw.column_dimensions['A'].width = 8
ws_raw.column_dimensions['B'].width = 12
ws_raw.column_dimensions['C'].width = 15
ws_raw.column_dimensions['D'].width = 12
ws_raw.column_dimensions['E'].width = 10
ws_raw.column_dimensions['F'].width = 12
ws_raw.column_dimensions['G'].width = 12
ws_raw.column_dimensions['H'].width = 10
ws_raw.column_dimensions['I'].width = 15
ws_raw.column_dimensions['J'].width = 12

# Format data cells
for row in ws_raw.iter_rows(min_row=2, max_row=1001):
    for idx, cell in enumerate(row):
        if idx == 1:  # Date column
            cell.number_format = 'YYYY-MM-DD'
        elif idx in [4, 5, 6]:  # Numeric columns
            cell.number_format = '0.00' if idx in [5, 6] else '0'
        cell.alignment = Alignment(horizontal="center", vertical="center")

print("✓ Sheet 1 created with 1000 raw records")

# ============ SHEET 2: CLEANED DATA ============
print("Creating Sheet 2: Cleaned Data...")

ws_cleaned = wb.create_sheet("Cleaned Data")

# Copy headers
ws_cleaned.append(headers)
for cell in ws_cleaned[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Copy cleaned data (removing cancelled orders)
row_num = 2
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    if row[9] != "Cancelled":  # Exclude cancelled status
        ws_cleaned.append(row)
        row_num += 1

# Apply same formatting
for col_idx in range(1, 11):
    ws_cleaned.column_dimensions[get_column_letter(col_idx)].width = ws_raw.column_dimensions[get_column_letter(col_idx)].width

for row in ws_cleaned.iter_rows(min_row=2, max_row=ws_cleaned.max_row):
    for idx, cell in enumerate(row):
        if idx == 1:  # Date column
            cell.number_format = 'YYYY-MM-DD'
        elif idx in [4, 5, 6]:  # Numeric columns
            cell.number_format = '0.00' if idx in [5, 6] else '0'
        cell.alignment = Alignment(horizontal="center", vertical="center")

print(f"✓ Sheet 2 created with {ws_cleaned.max_row - 1} cleaned records (excluding cancelled)")

# ============ SHEET 3: PIVOT TABLES ============
print("Creating Sheet 3: Pivot Tables...")

ws_pivot = wb.create_sheet("Pivot Tables")

# Title
title_cell = ws_pivot['A1']
title_cell.value = "Sales Analysis Dashboard"
title_cell.font = Font(bold=True, size=14, color="FFFFFF")
title_cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
title_cell.alignment = Alignment(horizontal="center", vertical="center")
ws_pivot.merge_cells('A1:F1')

# Pivot Table 1: Sales by Region
ws_pivot['A3'].value = "Sales by Region"
ws_pivot['A3'].font = Font(bold=True, size=11)

pt1_data = {}
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    if row[9] != "Cancelled":
        region = row[7]
        sales = row[6]
        if region not in pt1_data:
            pt1_data[region] = 0
        pt1_data[region] += sales

ws_pivot['A4'].value = "Region"
ws_pivot['B4'].value = "Total Sales"
ws_pivot['A4'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws_pivot['B4'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

row_idx = 5
for region, sales in sorted(pt1_data.items()):
    ws_pivot[f'A{row_idx}'].value = region
    ws_pivot[f'B{row_idx}'].value = sales
    ws_pivot[f'B{row_idx}'].number_format = '0.00'
    row_idx += 1

# Pivot Table 2: Sales by Product
ws_pivot['D3'].value = "Sales by Product"
ws_pivot['D3'].font = Font(bold=True, size=11)

pt2_data = {}
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    if row[9] != "Cancelled":
        product = row[2]
        sales = row[6]
        if product not in pt2_data:
            pt2_data[product] = 0
        pt2_data[product] += sales

ws_pivot['D4'].value = "Product"
ws_pivot['E4'].value = "Total Sales"
ws_pivot['D4'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws_pivot['E4'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

row_idx = 5
for product, sales in sorted(pt2_data.items(), key=lambda x: x[1], reverse=True):
    ws_pivot[f'D{row_idx}'].value = product
    ws_pivot[f'E{row_idx}'].value = sales
    ws_pivot[f'E{row_idx}'].number_format = '0.00'
    row_idx += 1

# Pivot Table 3: Order Status Summary
ws_pivot['A14'].value = "Order Status Summary"
ws_pivot['A14'].font = Font(bold=True, size=11)

pt3_data = {}
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    status = row[9]
    if status not in pt3_data:
        pt3_data[status] = 0
    pt3_data[status] += 1

ws_pivot['A15'].value = "Status"
ws_pivot['B15'].value = "Count"
ws_pivot['A15'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws_pivot['B15'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

row_idx = 16
for status, count in sorted(pt3_data.items()):
    ws_pivot[f'A{row_idx}'].value = status
    ws_pivot[f'B{row_idx}'].value = count
    row_idx += 1

# Column widths for pivot tables
ws_pivot.column_dimensions['A'].width = 15
ws_pivot.column_dimensions['B'].width = 15
ws_pivot.column_dimensions['D'].width = 15
ws_pivot.column_dimensions['E'].width = 15

print("✓ Sheet 3 created with Pivot Tables")

# ============ SHEET 4: INTERACTIVE DASHBOARD ============
print("Creating Sheet 4: Interactive Dashboard...")

ws_dashboard = wb.create_sheet("Interactive Dashboard")

# Dashboard Title
title = ws_dashboard['A1']
title.value = "SALES ANALYTICS DASHBOARD"
title.font = Font(bold=True, size=16, color="FFFFFF")
title.fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
title.alignment = Alignment(horizontal="center", vertical="center")
ws_dashboard.merge_cells('A1:H1')
ws_dashboard.row_dimensions[1].height = 25

# KPI Section
ws_dashboard['A3'].value = "KEY PERFORMANCE INDICATORS"
ws_dashboard['A3'].font = Font(bold=True, size=12, color="FFFFFF")
ws_dashboard['A3'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_dashboard.merge_cells('A3:H3')

# Calculate KPIs
total_sales = sum(row[6] for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True) if row[9] != "Cancelled")
total_orders = sum(1 for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True) if row[9] != "Cancelled")
avg_order = total_sales / total_orders if total_orders > 0 else 0
completed_orders = sum(1 for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True) if row[9] == "Completed")

# KPI Cards
kpi_data = [
    ("Total Sales", f"${total_sales:.2f}", "4472C4"),
    ("Total Orders", str(total_orders), "70AD47"),
    ("Avg Order Value", f"${avg_order:.2f}", "FFC000"),
    ("Completed Orders", str(completed_orders), "FF6B6B")
]

col = 1
for title_text, value, color in kpi_data:
    # Title
    cell = ws_dashboard.cell(row=5, column=col)
    cell.value = title_text
    cell.font = Font(bold=True, size=10, color="FFFFFF")
    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center")
    ws_dashboard.merge_cells(start_row=5, start_column=col, end_row=5, end_column=col+1)
    
    # Value
    cell = ws_dashboard.cell(row=6, column=col)
    cell.value = value
    cell.font = Font(bold=True, size=14)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    ws_dashboard.merge_cells(start_row=6, start_column=col, end_row=6, end_column=col+1)
    
    col += 2

# Sales Summary Table
ws_dashboard['A9'].value = "SALES SUMMARY BY REGION"
ws_dashboard['A9'].font = Font(bold=True, size=11, color="FFFFFF")
ws_dashboard['A9'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_dashboard.merge_cells('A9:D9')

headers_summary = ["Region", "Total Sales", "Orders", "Avg Order Value"]
ws_dashboard.append([])  # Empty row
for idx, header in enumerate(headers_summary, 1):
    cell = ws_dashboard.cell(row=11, column=idx)
    cell.value = header
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Add summary data by region
region_data = {}
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    if row[9] != "Cancelled":
        region = row[7]
        sales = row[6]
        if region not in region_data:
            region_data[region] = {"sales": 0, "orders": 0}
        region_data[region]["sales"] += sales
        region_data[region]["orders"] += 1

row_idx = 12
for region in sorted(region_data.keys()):
    data = region_data[region]
    ws_dashboard[f'A{row_idx}'].value = region
    ws_dashboard[f'B{row_idx}'].value = data["sales"]
    ws_dashboard[f'B{row_idx}'].number_format = '0.00'
    ws_dashboard[f'C{row_idx}'].value = data["orders"]
    ws_dashboard[f'D{row_idx}'].value = data["sales"] / data["orders"]
    ws_dashboard[f'D{row_idx}'].number_format = '0.00'
    
    for col in range(1, 5):
        ws_dashboard.cell(row=row_idx, column=col).alignment = Alignment(horizontal="center", vertical="center")
    row_idx += 1

# Top Products Section
ws_dashboard['A20'].value = "TOP SELLING PRODUCTS"
ws_dashboard['A20'].font = Font(bold=True, size=11, color="FFFFFF")
ws_dashboard['A20'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws_dashboard.merge_cells('A20:D20')

headers_products = ["Product", "Total Sales", "Quantity Sold", "Avg Price"]
for idx, header in enumerate(headers_products, 1):
    cell = ws_dashboard.cell(row=22, column=idx)
    cell.value = header
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Calculate product metrics
product_data = {}
for row in ws_raw.iter_rows(min_row=2, max_row=1001, values_only=True):
    if row[9] != "Cancelled":
        product = row[2]
        if product not in product_data:
            product_data[product] = {"sales": 0, "qty": 0, "prices": []}
        product_data[product]["sales"] += row[6]
        product_data[product]["qty"] += row[4]
        product_data[product]["prices"].append(row[5])

row_idx = 23
for product in sorted(product_data.keys(), key=lambda x: product_data[x]["sales"], reverse=True)[:8]:
    data = product_data[product]
    ws_dashboard[f'A{row_idx}'].value = product
    ws_dashboard[f'B{row_idx}'].value = data["sales"]
    ws_dashboard[f'B{row_idx}'].number_format = '0.00'
    ws_dashboard[f'C{row_idx}'].value = data["qty"]
    ws_dashboard[f'D{row_idx}'].value = sum(data["prices"]) / len(data["prices"])
    ws_dashboard[f'D{row_idx}'].number_format = '0.00'
    
    for col in range(1, 5):
        ws_dashboard.cell(row=row_idx, column=col).alignment = Alignment(horizontal="center", vertical="center")
    row_idx += 1

# Column widths
ws_dashboard.column_dimensions['A'].width = 15
ws_dashboard.column_dimensions['B'].width = 15
ws_dashboard.column_dimensions['C'].width = 15
ws_dashboard.column_dimensions['D'].width = 15
ws_dashboard.column_dimensions['E'].width = 15
ws_dashboard.column_dimensions['F'].width = 15
ws_dashboard.column_dimensions['G'].width = 15
ws_dashboard.column_dimensions['H'].width = 15

print("✓ Sheet 4 created with Interactive Dashboard")

# Save the workbook
output_file = "Sales_Data_Dashboard.xlsx"
wb.save(output_file)
print(f"\n✅ Excel file '{output_file}' created successfully!")
print("\nFile Structure:")
print("  Sheet 1: Raw Data (1000 records with sales information)")
print("  Sheet 2: Cleaned Data (900+ records, cancelled orders removed)")
print("  Sheet 3: Pivot Tables (Sales by Region, Product, and Status Summary)")
print("  Sheet 4: Interactive Dashboard (KPIs, Regional Analysis, Top Products)")
