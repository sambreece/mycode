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
            Static("What should you use to free the lobster?"),
            Static("A. Your hands "),
            Static("B. Your wired headphones"),
            Static("C. Grill tongs from a nearby display"),
            Static("D. A pen from your pocket"))

class TheRealization(Screen):
    def compose(self) -> ComposeResult:
        realization  = "The sight stops you in your tracks. You realize you have no choice. You have to free the lobster."
        self.box = Static(realization)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        self.box.styles.padding = (10, 2)
        yield Footer()
        yield self.box

class LobsterPhoto(Screen):
    def compose(self) -> ComposeResult:
        self.box = Static("🦞")
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        #self.box.styles.align_horizontal = "center"
        self.box.styles.color = "red"
        self.box.styles.padding = (10, 2)
        yield Footer()
        yield self.box


class LobsterIntro(Screen):
    def compose(self) -> ComposeResult:
        tank = "As you pass the meat counter, you can't help but notice a dirty tank with a single occupant: one lonely lobster."
        self.box = Static(tank)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        self.box.styles.padding = (10, 2)
        yield Footer()
        yield self.box

class Backstory(Screen):
    def compose(self) -> ComposeResult:
        intro = "After a long day in a cubicle, you find yourself browsing the aisles of your favorite nostalgic grocery store. "
        self.box = Static(intro)
        self.box.styles.background = "#4682B4"
        self.box.styles.text_align = "center"
        self.box.styles.padding = (10, 2)
        yield Footer()
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
        screens = [Backstory(),LobsterIntro(), LobsterPhoto(), TheRealization(), HowToFreeLobster()]
        if event.key == "enter":
            self.app.push_screen(screens[self.counter])
        #if event.key == "q":
        #    self.app.exit()
        self.counter += 1
if __name__ == "__main__":
    app = LobsterLiberatorApp()
    app.run()

