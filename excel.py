from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter


workbook = load_workbook('waluty.xlsx')

def closeWorkbook():
    workbook.save('waluty.xlsx')

#Loop through rows to find the first empty one
def findNextEmptyRow():
    worksheet = workbook['Aktualny Stan']
    for cell in worksheet["A"]:
        if cell.value is None:
            return cell.row
