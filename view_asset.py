from tkinter import *
from tkinter import ttk
from database import cursor

def view_asset_window():

    window = Toplevel()
    window.title("View Assets")
    window.geometry("1200x500")

    columns = (
        "ID",
        "Tag",
        "Name",
        "Type",
        "Serial",
        "Owner",
        "Department",
        "Status",
        "Location"
    )

    tree = ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )

    tree.heading("ID", text="Asset ID")
    tree.heading("Tag", text="Asset Tag")
    tree.heading("Name", text="Asset Name")
    tree.heading("Type", text="Asset Type")
    tree.heading("Serial", text="Serial Number")
    tree.heading("Owner", text="Owner")
    tree.heading("Department", text="Department")
    tree.heading("Status", text="Status")
    tree.heading("Location", text="Location")

    tree.pack(fill=BOTH, expand=True)

    cursor.execute("""
    SELECT
        AssetID,
        AssetTag,
        AssetName,
        AssetType,
        SerialNumber,
        OwnerName,
        Department,
        Status,
        LocationName
    FROM Assets
    """)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=tuple(row))