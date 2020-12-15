import sqlite3
import pandas as pd
from tkinter import messagebox

def toCSV():
    """"Export to database.csv"""
    try:
        conn = sqlite3.connect('inventory.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pd.read_sql_query("SELECT * FROM dmce_inventory", conn)
        db_df.to_csv('Database.csv', index=False)
        messagebox.showinfo("Success","Data Successfully Exported to 'Database.csv' !!!")
    except:
        messagebox.showerror("Error","Close other programs and try again.")

if __name__ == '__main__':
    toCSV()
