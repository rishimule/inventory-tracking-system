import csv
from fpdf import FPDF
from tkinter import messagebox
from tkinter import filedialog


def makecsv():
    """"Export to database.csv"""
    try:
        conn = sqlite3.connect('inventory.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM dmce_inventory", conn)

        # file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("csv file", "*.csv"),("All Files", "*.*") ))

        db_df.to_csv('database.csv', index=False)
    except:
        pass


class PDF(FPDF):
    """Customizing the fpdf Options"""

    def footer(self):
        """Custom Footer"""
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Print centered page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

def CsvtoPDF():
    """Function To export CSV to PDF"""
    makecsv()
    try:
        # To count the no of Columns (ncol)

        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=(("pdf file", "*.pdf"),("All Files", "*.*") ))

        with open('database.csv',"r") as file:
            reader = csv.reader(file,delimiter = ",")
            ncol = len(next(reader))

        with open('database.csv', newline='') as f:
            reader = csv.reader(f)
            pdf = PDF(orientation = 'L', unit = 'mm', format='Legal')
            pdf.add_page(orientation = 'L')
            page_width = pdf.w - 2 * pdf.l_margin

            pdf.set_font('Times','B', 14.0)
            pdf.cell(page_width, 0.0, 'Inventory Data', align='C')
            pdf.ln(10)

            pdf.set_font('Courier', '', 12)

            col_width = page_width/(ncol - 1)

            pdf.ln(1)

            th = pdf.font_size + 2

            isHead = True
            for row in reader:

                if isHead:
                    #To Make the Tabe Head as BOLD
                    pdf.set_font('Courier', 'B', 12)
                    isHead = False

                else:
                    pdf.set_font('Courier', '', 12)

                for x in range(int(ncol - 1)):
                    pdf.cell(col_width, th, str(row[x]), border=1)

                pdf.ln(th)

            pdf.ln(10)

            pdf.set_font('Times','',10.0)
            pdf.cell(page_width, 0.0, '- end of report -', align='C')

            pdf.output(filename, 'F')

        messagebox.showinfo("Success",f"Data Successfully Exported to '{filename}' !!!")

    except:
        messagebox.showerror("Error","Close other programs and try again.")


if __name__ == '__main__':
    """Start the Conversion"""
    CsvtoPDF()
