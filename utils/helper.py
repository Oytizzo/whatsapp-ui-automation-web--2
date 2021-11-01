import openpyxl


class XlsxSheet:
    def __init__(self, xlsx_file_location, phone_number_cell):
        self.number_list = []
        self.xlsx_file_location = xlsx_file_location
        self.phone_number_cell = phone_number_cell

    def get_numbers_from_xlsx(self):
        wb = openpyxl.load_workbook(self.xlsx_file_location)
        sheet = wb['Sheet1']
        number = sheet[self.phone_number_cell]
        return number.value
