#!usr/bin/env python3
import TermTk as ttk
    # Set the VBoxLayout as default in the terminal widget
root = ttk.TTk(layout=ttk.TTkVBoxLayout())

    # Create main boxes:
top_box = ttk.TTkWindow(parent=root, border=True)
bottom_box = ttk.TTkWindow(parent=root, border=True)

    #Put buttons in bottom box
ttk.TTkButton(parent=bottom_box, border=True, text="Button1")
ttk.TTkButton(parent=bottom_box, border=True, text="Button2")

root.mainloop()
