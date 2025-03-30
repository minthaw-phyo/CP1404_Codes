from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the KV file once at the top
Builder.load_file('dynamic_labels.kv')

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

        for name in self.names:
            label = Label(text=name)
            self.ids.main.add_widget(label)

class DynamicLabelsApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    DynamicLabelsApp().run()
