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
root.configure(bg="#ecf0f1")


canvas = Canvas(root, bg="#ecf0f1")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_frame = Frame(canvas, bg="#ecf0f1")

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


header_frame = Frame(scroll_frame, bg="#3498db")
header_frame.pack(fill="x")

Label(
    header_frame,
    text="IT Asset Inventory & CMDB Management System",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#3498db"
).pack(pady=15)

Label(
    header_frame,
    text="Configuration Management Database",
    font=("Arial", 13),
    fg="white",
    bg="#3498db"
).pack(pady=5)


def get_count(query):
    database.cursor.execute(query)
    result = database.cursor.fetchone()
    return result[0]

total_assets = get_count("SELECT COUNT(*) FROM Assets")
active_assets = get_count("SELECT COUNT(*) FROM Assets WHERE Status='Active'")
inactive_assets = get_count("SELECT COUNT(*) FROM Assets WHERE Status='Inactive'")
duplicate_assets = get_count("""
SELECT COUNT(*)
FROM (
    SELECT SerialNumber
    FROM Assets
    GROUP BY SerialNumber
    HAVING COUNT(*)>1
) A
""")


stats_frame = Frame(scroll_frame, bg="#ecf0f1")
stats_frame.pack(pady=20)

def create_stat_card(parent, title, value, color):
    frame = Frame(parent, bd=2, relief="groove", padx=20, pady=10, bg=color)
    Label(frame, text=title, font=("Arial", 12, "bold"), bg=color, fg="white").pack()
    Label(frame, text=value, font=("Arial", 16, "bold"), fg="white", bg=color).pack()
    frame.pack(side="left", padx=15, pady=10)

create_stat_card(stats_frame, "Total Assets", total_assets, "#1abc9c")
create_stat_card(stats_frame, "Active Assets", active_assets, "#2ecc71")
create_stat_card(stats_frame, "Inactive Assets", inactive_assets, "#e74c3c")
create_stat_card(stats_frame, "Duplicate Serials", duplicate_assets, "#f39c12")


button_frame = Frame(scroll_frame, bg="#ecf0f1")
button_frame.pack(pady=30)

button_colors = [
    "#2980b9", "#27ae60", "#8e44ad", "#c0392b",
    "#d35400", "#16a085", "#f1c40f", "#7f8c8d"
]

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

for i, (text, command) in enumerate(buttons):
    btn = Button(
        button_frame,
        text=text,
        width=30,
        bg=button_colors[i],
        fg="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=3,
        command=command
    )
    btn.pack(pady=8)


footer_frame = Frame(scroll_frame, bg="#34495e")
footer_frame.pack(fill="x", side="bottom")

Label(
    footer_frame,
    text="Python | MySQL | Tkinter | CMDB",
    font=("Arial", 10),
    fg="white",
    bg="#34495e"
).pack(pady=10)

root.mainloop()
