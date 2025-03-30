from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (500, 300)
class GreeterApp(App):
    greeting_text = StringProperty("")

    def build(self):
        self.title = "Greeter Program"
        return Builder.load_file("dynamic_labels.kv")

    def greet(self):
        name = self.root.ids.input_name.text
        self.greeting_text = f"Hello {name}"

    def clear(self):
        self.root.ids.input_name.text = ""
        self.greeting_text = ""


if __name__ == "__main__":
    GreeterApp().run()
