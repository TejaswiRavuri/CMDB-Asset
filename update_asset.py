from tkinter import *
from tkinter import messagebox
from database import conn, cursor

def update_asset_window():

    window = Toplevel()
    window.title("Update Asset")
    window.geometry("400x300")

    Label(window, text="Asset Tag").pack(pady=5)
    asset_tag = Entry(window, width=30)
    asset_tag.pack()

    Label(window, text="New Owner Name").pack(pady=5)
    owner_name = Entry(window, width=30)
    owner_name.pack()

    Label(window, text="New Status").pack(pady=5)
    status = Entry(window, width=30)
    status.pack()

    def update_asset():

        cursor.execute("""
        UPDATE Assets
        SET OwnerName=?,
            Status=?,
            LastUpdated=GETDATE()
        WHERE AssetTag=?
        """,
        owner_name.get(),
        status.get(),
        asset_tag.get()
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Asset Updated Successfully"
        )

    Button(
        window,
        text="Update Asset",
        command=update_asset,
        width=20
    ).pack(pady=20)