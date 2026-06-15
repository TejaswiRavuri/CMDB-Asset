from tkinter import *
from tkinter import messagebox
from database import conn, cursor

def delete_asset_window():

    window = Toplevel()
    window.title("Delete Asset")
    window.geometry("400x250")

    Label(window, text="Enter Asset Tag").pack(pady=10)
    asset_tag = Entry(window, width=35)
    asset_tag.pack()

    def delete_asset():

        cursor.execute(
            "DELETE FROM Assets WHERE AssetTag=?",
            asset_tag.get()
        )

        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Asset Tag not found")
        else:
            messagebox.showinfo("Success", "Asset Deleted Successfully")

    Button(
        window,
        text="Delete Asset",
        command=delete_asset,
        width=20
    ).pack(pady=20)