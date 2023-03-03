#textual 
#pip install textual
from textual.app import App, ComposeResult
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

from lobster_side import lobster

class LobsterPhoto(Screen):
    def compose(self) -> ComposeResult:
        self.box = Static(lobster)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        self.box.styles.color = "red"
        self.box.styles.padding = (10, 2)
        yield self.box


class LobsterIntro(Screen):
    def compose(self) -> ComposeResult:
        tank = "As you pass the meat counter, you can't help but notice a dirty tank with a single occupant: one lonely lobster."
        self.box = Static(tank)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        #self.box.styles.color = "white"
        self.box.styles.padding = (10, 2)
        yield self.box

class Backstory(Screen):
    def compose(self) -> ComposeResult:
        intro = "After a long day in a cubicle, you find yourself browsing the aisles of your favorite nostalgic grocery store. "
        self.box = Static(intro)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        #self.box.styles.color = "white"
        self.box.styles.padding = (10, 2)
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
        yield self.box

    def on_mount(self):
        self.box.styles.animate("opacity", value=0.0, duration=8.0)
        
        
#Main application:
class LobsterLiberatorApp(App):

    def on_mount(self) -> None:
        self.counter = 0
        self.app.push_screen(Title())
        

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color
        
    async def on_key(self, event: events.Key) -> None:
        screens = [Backstory(),LobsterIntro(), LobsterPhoto()]
        if event.key == "enter":
            self.app.push_screen(screens[self.counter])
        if event.key == "q":
            self.app.exit()
        self.counter += 1
if __name__ == "__main__":
    app = LobsterLiberatorApp()
    app.run()

