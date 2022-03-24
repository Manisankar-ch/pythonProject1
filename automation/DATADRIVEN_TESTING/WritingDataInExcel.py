import openpyxl
path="E:\ExcelFiles\book1.xlsx"

wb=openpyxl.load_workbook(path)
sheet=wb.active

for r in range(1,5):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="welcome"

wb.save(path)
