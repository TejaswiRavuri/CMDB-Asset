from tkinter import messagebox
import pandas as pd
from database import conn

def generate_report():

    query = """
    SELECT
        AssetID,
        AssetTag,
        AssetName,
        AssetType,
        SerialNumber,
        OwnerName,
        Department,
        PurchaseDate,
        Status,
        LocationName,
        LastUpdated
    FROM Assets
    """

    df = pd.read_sql(query, conn)

    file_path = "reports/Asset_Report.xlsx"

    df.to_excel(file_path, index=False)

    messagebox.showinfo(
        "Success",
        "Asset Report Generated Successfully in reports folder"
    )