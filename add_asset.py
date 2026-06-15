from tkinter import *
from tkinter import messagebox
from database import conn, cursor

def add_asset_window():

    window = Toplevel()
    window.title("Add Asset")
    window.geometry("500x600")

    Label(window, text="Asset Tag").pack()
    asset_tag = Entry(window, width=40)
    asset_tag.pack()

    Label(window, text="Asset Name").pack()
    asset_name = Entry(window, width=40)
    asset_name.pack()

    Label(window, text="Asset Type").pack()
    asset_type = Entry(window, width=40)
    asset_type.pack()

    Label(window, text="Serial Number").pack()
    serial_number = Entry(window, width=40)
    serial_number.pack()

    Label(window, text="Owner Name").pack()
    owner_name = Entry(window, width=40)
    owner_name.pack()

    Label(window, text="Department").pack()
    department = Entry(window, width=40)
    department.pack()

    Label(window, text="Purchase Date (YYYY-MM-DD)").pack()
    purchase_date = Entry(window, width=40)
    purchase_date.pack()

    Label(window, text="Status").pack()
    status = Entry(window, width=40)
    status.pack()

    Label(window, text="Location").pack()
    location = Entry(window, width=40)
    location.pack()

    def save_asset():

        cursor.execute("""
        INSERT INTO Assets
        (
        AssetTag,
        AssetName,
        AssetType,
        SerialNumber,
        OwnerName,
        Department,
        PurchaseDate,
        Status,
        LocationName
        )
        VALUES (?,?,?,?,?,?,?,?,?)
        """,
        asset_tag.get(),
        asset_name.get(),
        asset_type.get(),
        serial_number.get(),
        owner_name.get(),
        department.get(),
        purchase_date.get(),
        status.get(),
        location.get()
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Asset Added Successfully"
        )

    Button(
        window,
        text="Save Asset",
        command=save_asset,
        width=20
    ).pack(pady=20)