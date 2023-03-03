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

class QuestionPage(Screen):
    def __init__(self, page_index: int) -> None:
        super().__init__()
        self.page_index = page_index

    def compose(self) -> ComposeResult:
        options = [None, None, None, None, 
                ["What should you use to free the lobster?", "A. Your hands ", "B. Your wired headphones", "C. Grill tongs from a nearby display", "D. A pen from your pocket"],
                None,
                ["Which aisle should you use to exit the grocery store?", "A. Frozen food aisle. It seems quiet.",
                    "B. Vegetable aisle. There are only one or two shoppers, minding their own business.",
                    "C. Snack aisle. It seems busy, but maybe that will cover your tracks.",
                    "D. Beverage aisle. Do lobsers like soda?"]
                ]
        self.styles.background = "#4682B4"
        self.styles.text_align = "center"
        self.styles.align_horizontal = "center"
        yield Grid(
            Static(""),
            Static(options[self.page_index][0]),
            Static(options[self.page_index][1]),
            Static(options[self.page_index][2]),
            Static(options[self.page_index][3]),
            Static(options[self.page_index][4]))

class TextPage(Screen):

    def __init__(self, page_index: int) -> None:
        super().__init__()
        self.page_index = page_index

    def compose(self) -> ComposeResult:
        text = ["After a long day in a cubicle, you find yourself browsing the aisles of your favorite nostalgic grocery store.", 
                "As you pass the meat counter, you can't help but notice a dirty tank with a single occupant: one lonely lobster.",
                "🦞",
                "The sight stops you in your tracks. You realize you have no choice. You have to free the lobster.",
                None,
                "The lobster hears the music playing through your headphones. It seems like it likes this song. It climbs up your headphones and into your inventory.",
                None,
                "You made it out of the grocery store!  You hear a happy noise from inside your inventory.",
                "You can see the glistening waves of the ocean in the distance.",
                "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
                ]
        self.styles.background = "#4682B4"
        self.styles.align_vertical = "middle"
        realization  = text[self.page_index]
        self.box = Static(realization)
        self.box.styles.text_align = "center"
        yield Footer()
        yield self.box

class ErrorPage(Screen):
    def compose(self) -> ComposeResult:
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
        self.styles.animate("opacity", value=0.0, duration=8.0)
class AnotherChancePage(Screen):

    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        self.styles.background = "#4682B4"
        self.styles.align_vertical = "middle"
        self.box = Static(self.message)
        self.box.styles.text_align = "center"
        yield Button("Click Here to Return", variant="primary", id="return")
        yield Footer()
        yield self.box
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "return":
            self.app.pop_screen()
class InventoryPage(Screen):

    def __init__(self, items: list) -> None:
        super().__init__()
        self.items = items

    def compose(self) -> ComposeResult:        
        self.styles.background = "#4682B4"
        self.styles.align_vertical = "middle"
        self.box = Static("Items:\n" + '\n'.join(self.items))
        self.box.styles.text_align = "center"
        yield Button("Click Here to Return", variant = "primary", id="return")
        yield Footer()
        yield self.box
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "return":
            self.app.pop_screen()
class GameOverPage(Screen):

    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        self.styles.align_vertical = "middle"
        self.box = Static("GAME OVER!\n" + self.message + "\nPlease use 'q' to quit the program")
        self.box.styles.text_align = "center"
        yield self.box
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "return":
            self.app.pop_screen()

#Main application:
class LobsterLiberatorApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="enter", action="enter", description="Enter to continue"), 
        Binding(key="i", action="i", description="View inventory")]
    
    def compose(self) -> ComposeResult:
        yield Footer()
    def on_mount(self) -> None:
        self.counter = 0
        self.app.push_screen(Title())
        

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color
        
    async def on_key(self, event: events.Key) -> None:
        screens = [TextPage(self.counter), TextPage(self.counter), TextPage(self.counter), TextPage(self.counter), QuestionPage(self.counter),
                None, QuestionPage(self.counter), TextPage(self.counter), TextPage(self.counter)]
        correct_answer = [None, None, None, None, "b", None, "c"]
        if event.key == "enter":
            self.app.push_screen(screens[self.counter])
            self.counter += 1
        if event.key == "a":
            response_a = [ErrorPage(),ErrorPage(),ErrorPage(), ErrorPage(),ErrorPage(),ErrorPage()]
            if "a" == correct_answer[self.counter-1]:
                self.app.push_screen(response_a[self.counter])
                self.counter+=1
            elif self.counter-1 == 4:
                self.app.push_screen(AnotherChancePage("The lobster tries to pinch your fingers."))
            else:
                self.app.push_screen(GameOverPage("Someone spotted a lobster claw hanging out of your bag."))
        if event.key == "b":
            response_b = [ErrorPage(),ErrorPage(),ErrorPage(), ErrorPage(),ErrorPage(),TextPage(self.counter),ErrorPage()]
            if "b" == correct_answer[self.counter-1]:
                self.app.push_screen(response_b[self.counter])
                self.counter+=1
            else:
                self.app.push_screen(GameOverPage("Someone spotted a lobster claw hanging out of your bag."))
        if event.key == "c":
            response_c = [ErrorPage(),ErrorPage(),ErrorPage(), ErrorPage(),ErrorPage(),ErrorPage(), ErrorPage(), TextPage(self.counter),ErrorPage()]
            if "c" == correct_answer[self.counter-1]:
                self.app.push_screen(response_c[self.counter])
                self.counter+=1
            elif self.counter-1 == 4:
                self.app.push_screen(AnotherChancePage("The lobster easily avoids the tongs."))
            else:
                self.app.push_screen(GameOverPage("Someone spotted a lobster claw hanging out of your bag."))
        if event.key == "d":
            response_d = [ErrorPage(),ErrorPage(),ErrorPage(), ErrorPage(),ErrorPage(),ErrorPage()]
            if "d" == correct_answer[self.counter-1]:
                self.app.push_screen(response_d[self.counter])
                self.counter+=1
            elif self.counter-1 == 4:
                self.app.push_screen(AnotherChancePage("The lobster doesn't seem interested in the pen."))
            else:
                self.app.push_screen(GameOverPage("Someone spotted a lobster claw hanging out of your bag."))
        if event.key == "i":
            inventory = ["pen", "wired headphones"]
            if self.counter > 4:
                inventory.append("lobster")
            self.app.push_screen(InventoryPage(inventory))
if __name__ == "__main__":
    app = LobsterLiberatorApp()
    app.run()

