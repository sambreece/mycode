#!usr/bin/env python3
import TermTk as ttk

    # Create a root object (it is a widget that represent the terminal)
root = ttk.TTk()

    # Create a window and attach it to the root (parent=root)
helloWin = ttk.TTkWindow(parent=root,pos = (1,1), size=(30,10), title="Hello Window", border=True)

    # Define the Label and attach it to the window (parent=helloWin)
ttk.TTkLabel(parent=helloWin, pos=(5,5), text="Hello World")

    # Start the Main loop
root.mainloop()
