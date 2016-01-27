import xlrd

import tempfile
import os

class Xls:
    # This class handles both xls and can be extended to handle xlsx
    def __init__(self, data):
        outTemp = tempfile.mkstemp(suffix=self.get_extension())
        outfile = outTemp[1]
        outfp = open(outfile, 'wb')
        outfp.write(data)
        outfp.close()

        workbook = xlrd.open_workbook(outfile)
        sheets = workbook.sheet_names()

        output = ""

        for sheet in sheets:
            worksheet = workbook.sheet_by_name(sheet)
            num_rows = worksheet.nrows
            num_cells = worksheet.ncols

            for curr_row in range(num_rows):
                row = worksheet.row(curr_row)
                for index_col in range(num_cells):
                    value = worksheet.cell_value(curr_row, index_col)

                    try:
                        output += str(value) + "\t"
                    except:
                        output += "\t"

                output += "\n"

            output += "\n"

        self.data = output.strip()

        os.unlink(outfile)

    def get_extension(self):
        return "xls"

    def __str__(self):
        return self.data


class Xlsx(Xls):
    def get_extension(self):
        return "xlsx"
