

import sys, os, argparse, math, random

sys.path.append(os.path.join(sys.path[0],'../..'))

import TermTk as ttk

class graphTimerEvent():
    def __init__(self, w, type, delay):
        self.timer = ttk.TTkTimer()
        self.val = 10
        self.delay = delay
        self.switch = False
        self.w = w
        self.type = type
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1)
    @ttk.pyTTkSlot()
    def timerEvent(self):
        self.switch = not self.switch

        if self.type == 2: # Double sin alternated
            offset = 15
            if self.switch: val = [math.sin( self.val        *math.pi/40)*4*10]
            else:           val = [math.sin((self.val+offset)*math.pi/40)*4*7 ]

        self.val+=1
        self.w.addValue(val)
        self.timer.start(self.delay)

def demoGraph(root= None):
    frame = ttk.TTkFrame(parent=root, border=False, layout=ttk.TTkVBoxLayout())
    graphWidget1 = ttk.TTkGraph(parent=frame, direction=ttk.TTkK.LEFT, color=ttk.TTkColor.fg('#00dddd', modifier=ttk.TTkColorGradient(increment= 20)))
    graphTimerEvent(graphWidget1, 2, 0.1)
    return frame

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Full Screen', action='store_true')
    args = parser.parse_args()

    ttk.TTkLog.use_default_file_logging()

    #root = ttk.TTk()
        # Set the GridBoxLayout as default in the terminal widget
    root = ttk.TTk()
    grid_layout = ttk.TTkGridLayout()
    root.setLayout(grid_layout)

    # Create main boxes:
    top_box = ttk.TTkFrame(parent=root,pos=(1,1), size=(50,40), title="The Ocean", border=True, layout=ttk.TTkGridLayout())
    grid_layout.addWidget(top_box,0,0,1,3)

    #Make button box:
    button_box = ttk.TTkVBoxLayout()
    grid_layout.addItem(button_box, 1,0,1,3)

    button_box.addWidget(ttk.TTkButton(border=True,checkable=True, text="Button1"))
    button_box.addWidget(ttk.TTkButton(border=True,checkable=True, text="Button2"))
    button_box.addWidget(ttk.TTkButton(border=True,checkable=True,  text="Button3"))
    button_box.addWidget(ttk.TTkButton(border=True,checkable=True, text="Button4"))

    demoGraph(top_box)
    root.mainloop()
if __name__ == "__main__":
    main()
