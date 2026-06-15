IT Asset Inventory & CMDB Management System.


This project is a Configuration Management Database (CMDB) built with Python, Tkinter, and MySQL. It provides a user-friendly interface for managing IT assets, including adding, viewing, updating, deleting, and generating reports.

The system also integrates contextual metadata from the user’s Edge browser tabs to understand what the user is currently viewing, which helps provide relevant assistance.

Features
Asset Management
-->Add new assets
-->View existing assets
-->Update asset details
-->Delete assets
-->Mark assets as inactive
-->Detect duplicate assets

Dashboard
-->Displays total, active, inactive, and duplicate assets

UI
-->Scrollable dashboard
-->Color-coded stat cards
-->Interactive buttons for each module

Project Structure
CMDB-Python/
│── main.py
│── database.py
└── modules/
    │── add_asset.py
    │── view_asset.py
    │── update_asset.py
    │── delete_asset.py
    │── inactive_asset.py
    │── duplicate_asset.py
    │── report.py
