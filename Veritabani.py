import pyodbc
import tkinter as tk

conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=.;"
    r"DATABASE=otopark;"
    r"Trusted_conneciton=yes;"
)



conn = pyodbc.connect(conn_str)
cursor = conn.cursor()




def populate_treeview(tree, data):
    for row in data:
        tree.insert("", "end", values=row)


def UyeListesi():
    cursor.execute("Select * from Uyeler")
    return cursor.fetchall()
