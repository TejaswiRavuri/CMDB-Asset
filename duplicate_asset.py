from tkinter import *
from tkinter import ttk
from database import cursor

def duplicate_asset_window():

    window = Toplevel()
    window.title("Duplicate Assets")
    window.geometry("1000x400")

    columns = (
        "SerialNumber",
        "DuplicateCount"
    )

    tree = ttk.Treeview(window, columns=columns, show="headings")

    tree.heading("SerialNumber", text="Serial Number")
    tree.heading("DuplicateCount", text="Duplicate Count")

    tree.pack(fill=BOTH, expand=True)

    cursor.execute("""
    SELECT
        SerialNumber,
        COUNT(*) AS DuplicateCount
    FROM Assets
    GROUP BY SerialNumber
    HAVING COUNT(*) > 1
    """)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=tuple(row))