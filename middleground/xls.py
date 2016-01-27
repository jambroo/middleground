import xlrd

import tempfile
import os

class Xlsx:
    def __init__(self, data):
        outTemp = tempfile.mkstemp(suffix=".xlsx")
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

    def __str__(self):
        return self.data
