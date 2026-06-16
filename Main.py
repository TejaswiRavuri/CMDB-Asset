from tkinter import *
from tkinter import ttk

import database

from Modules.add_asset import add_asset_window
from Modules.view_asset import view_asset_window
from Modules.update_asset import update_asset_window
from Modules.delete_asset import delete_asset_window
from Modules.inactive_asset import inactive_asset_window
from Modules.duplicate_asset import duplicate_asset_window
from Modules.report import generate_report



root = Tk()

root.title("IT Asset Inventory & CMDB Management System")
root.geometry("900x650")



canvas = Canvas(root)

scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

scroll_frame = Frame(canvas)


scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window(
    (0, 0),
    window=scroll_frame,
    anchor="nw"
)


canvas.configure(
    yscrollcommand=scrollbar.set
)



def on_mousewheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all(
    "<MouseWheel>",
    on_mousewheel
)


canvas.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar.pack(
    side="right",
    fill="y"
)




def get_count(query):

    database.cursor.execute(query)

    result = database.cursor.fetchone()

    return result[0]





Label(
    scroll_frame,
    text="IT Asset Inventory & CMDB Management System",
    font=("Arial", 22, "bold")
).pack(pady=20)



Label(
    scroll_frame,
    text="Configuration Management Database",
    font=("Arial", 13)
).pack(pady=5)





stats_frame = Frame(scroll_frame)

stats_frame.pack(pady=15)



total_assets = get_count(
    "SELECT COUNT(*) FROM Assets"
)


active_assets = get_count(
    "SELECT COUNT(*) FROM Assets WHERE Status='Active'"
)


inactive_assets = get_count(
    "SELECT COUNT(*) FROM Assets WHERE Status='Inactive'"
)


duplicate_assets = get_count("""
SELECT COUNT(*)
FROM
(
SELECT SerialNumber
FROM Assets
GROUP BY SerialNumber
HAVING COUNT(*)>1
) A
""")


stats_text = f"""

Total Assets : {total_assets}

Active Assets : {active_assets}

Inactive Assets : {inactive_assets}

Duplicate Serials : {duplicate_assets}

"""


Label(
    stats_frame,
    text=stats_text,
    font=("Arial", 12, "bold")
).pack()




style = ttk.Style()


style.configure(
    "TButton",
    font=("Arial", 12),
    padding=10
)



button_frame = Frame(scroll_frame)

button_frame.pack(pady=20)



buttons = [

    ("Add Asset", add_asset_window),

    ("View Assets", view_asset_window),

    ("Update Asset", update_asset_window),

    ("Delete Asset", delete_asset_window),

    ("Inactive Assets", inactive_asset_window),

    ("Duplicate Assets", duplicate_asset_window),

    ("Generate Report", generate_report),

    ("Exit", root.destroy)

]



for text, command in buttons:

    ttk.Button(
        button_frame,
        text=text,
        command=command,
        width=30

    ).pack(pady=8)




Label(
    scroll_frame,
    text="Python | MS SQL Server | Tkinter | CMDB",
    font=("Arial", 10)
).pack(pady=20)



root.mainloop()
