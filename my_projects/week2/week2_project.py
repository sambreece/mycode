#textual 
#pip install textual
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Button
from textual import events
from time import sleep
#figlet
#pip install pyfiglet
from pyfiglet import Figlet
#rich-pixels
#pip install rich-pixels
from rich_pixels import Pixels
from rich.align import Align

class HowToFreeLobster(Screen):
    def compose(self) -> ComposeResult:
        self.styles.background = "#4682B4"
        self.styles.text_align = "center"
        yield Grid(
            Static(""),
            Static("What should you use to free the lobster?"),
            Static("A. Your hands "),
            Static("B. Your wired headphones"),
            Static("C. Grill tongs from a nearby display"),
            Static("D. A pen from your pocket"))

class TextPage(Screen):

    def __init__(self, page_index: int) -> None:
        super().__init__()
        self.page_index = page_index

    def compose(self) -> ComposeResult:
        text = ["After a long day in a cubicle, you find yourself browsing the aisles of your favorite nostalgic grocery store.", "As you pass the meat counter, you can't help but notice a dirty tank with a single occupant: one lonely lobster.","🦞","The sight stops you in your tracks. You realize you have no choice. You have to free the lobster."]
        self.styles.background = "#4682B4"
        self.styles.align_vertical = "middle"
        realization  = text[self.page_index]
        self.box = Static(realization)
        self.box.styles.text_align = "center"
        yield Footer()
        yield self.box

class ErrorPage(Screen):
    def compose(self) -> ComposeResult:
        self.styles.background = "#black"
        self.styles.align_vertical = "middle"
        intro = "OOPS. There was an error. Please use 'q' to quit the program."
        self.box =  Static(intro)
        self.box.styles.text_align = "center"
        yield self.box

class Title(Screen):
    def action_generate_title(self):
        font = Figlet(font='big')
        return Pixels.from_ascii(font.renderText('lobster liberator'))
    
    def compose(self) -> ComposeResult:
        self.box = Static(self.action_generate_title())
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        self.box.styles.color = "black"
        self.box.styles.padding = (10, 2)
        yield Footer()
        yield self.box
    def on_mount(self):
        self.box.styles.animate("opacity", value=0.0, duration=8.0)
        
#Main application:
class LobsterLiberatorApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="enter", action="enter", description="Enter to continue")]
    def compose(self) -> ComposeResult:
        yield Footer()
    def on_mount(self) -> None:
        self.counter = 0
        self.app.push_screen(Title())
        

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color
        
    async def on_key(self, event: events.Key) -> None:
        screens = [TextPage(self.counter), TextPage(self.counter), TextPage(self.counter), TextPage(self.counter)]
        if event.key == "enter":
            self.app.push_screen(screens[self.counter])
            self.counter += 1
        if event.key == "a":
            response_a = [ErrorPage(), ErrorPage(),ErrorPage()]
            self.app.exit()
        if event.key == "b":
            self.app.exit()
        if event.key == "c":
            self.app.exit()
        if event.key == "d":
            self.app.exit()
if __name__ == "__main__":
    app = LobsterLiberatorApp()
    app.run()

