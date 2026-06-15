from tkinter import *
from tkinter import ttk
from database import cursor

def inactive_asset_window():

    window = Toplevel()
    window.title("Inactive Assets")
    window.geometry("1000x400")

    columns = (
        "ID",
        "Tag",
        "Name",
        "Type",
        "Owner",
        "Department",
        "Status"
    )

    tree = ttk.Treeview(window, columns=columns, show="headings")

    tree.heading("ID", text="Asset ID")
    tree.heading("Tag", text="Asset Tag")
    tree.heading("Name", text="Asset Name")
    tree.heading("Type", text="Asset Type")
    tree.heading("Owner", text="Owner")
    tree.heading("Department", text="Department")
    tree.heading("Status", text="Status")

    tree.pack(fill=BOTH, expand=True)

    cursor.execute("""
    SELECT
        AssetID,
        AssetTag,
        AssetName,
        AssetType,
        OwnerName,
        Department,
        Status
    FROM Assets
    WHERE Status='Inactive'
    """)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=tuple(row))