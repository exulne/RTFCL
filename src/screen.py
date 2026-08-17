from textual.app import App, ComposeResult
from textual.widgets import Checkbox, Button, Header, Footer
import json

with open('/home/cubxfy/Projects/exulne/RTFCL/database/states.json', "r") as file:
    data = json.load(file)

class CheckboxDemo(App):
    BINDINGS = [
        ("d", "toggle_dark", "Dark Mode"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        yield Checkbox("twitter", id="twitter", value=data.get("twitter", False))
        yield Checkbox("reddit", id="reddit", value=data.get("reddit", False))
        yield Checkbox("youtube -> RTFCL", id="youtube", value=data.get("youtube", False))
        yield Checkbox("whateversLeft", id="remaining", value=data.get("remaining", False))
        yield Checkbox("all", id="all", value=data.get("all", False))

        yield Footer()

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        name = event.checkbox.label
        state = event.value

        self.notify(str(event.value))
        
        data[event.checkbox.id] = event.value
        with open('/home/cubxfy/Projects/exulne/RTFCL/database/states.json', "w") as file:
            json.dump(data, file, indent=4)
    

if __name__ == "__main__":
    CheckboxDemo().run()
    
