import sqlite3
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog

def toCSV():
    """"Export to database.csv"""
    try:
        conn = sqlite3.connect('inventory.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM dmce_inventory", conn)

        file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("csv file", "*.csv"),("All Files", "*.*") ))

        db_df.to_csv(file_name, index=False)
        messagebox.showinfo("Success",f"Data Successfully Exported to\n '{file_name}' !!!")
    except:
        messagebox.showerror("Error","Close other programs and try again.")

if __name__ == '__main__':
    toCSV()
