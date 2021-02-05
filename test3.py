from openpyxl import load_workbook, worksheet

import MK
MK.MakeExFile()

filename = "file.xlsx"
wb = load_workbook(filename)
ws = wb.worksheets[0]
wb.save(filename)
