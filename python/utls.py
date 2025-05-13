from openpyxl.worksheet import worksheet

def getCellValue(worksheet:worksheet.Worksheet, row, col):
    value = worksheet.cell(row=row, column=col).value
    if value == None:
        return ''
    return str(value).strip()