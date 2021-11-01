import openpyxl


class XlsxSheet:
    def __init__(self, xlsx_file_location, phone_number_column, name_column=""):
        self.number_list = []
        self.xlsx_file_location = xlsx_file_location
        self.phone_number_column = phone_number_column
        self.name_column = name_column

    def get_numbers_from_xlsx(self):
        wb = openpyxl.load_workbook(self.xlsx_file_location)
        # print(wb.sheetnames)
        sheet = wb['Sheet1']
        if not self.name_column:
            names = sheet['a']
        else:
            names = sheet[self.name_column]
        numbers = sheet[self.phone_number_column]
        for number in numbers:
            # print(name.value)
            # print(number.value)
            self.number_list.append(number.value)
        return self.number_list
