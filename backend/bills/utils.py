
import openpyxl

from config.settings import DATA_DIR


def get_bills_list(xlsx=f'{DATA_DIR}/bills.xlsx'):
    wb = openpyxl.load_workbook(xlsx)
    sheet = wb.active
    col_names = []
    for column in sheet.iter_cols(1, sheet.max_column):
        col_names.append(column[0].value)
    bills = []
    for row in range(2, sheet.max_row+1):
        bill = {}
        for column in range(1, sheet.max_column):
            bill[col_names[column-1]] = sheet.cell(row=row,
                                                   column=column).value
        bills.append(bill)
    return bills
