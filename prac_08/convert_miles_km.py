from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 300)
class ConvertMilesApp(App):

    def build(self):

        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self):
        try:
            miles = float(self.root.ids.input_number.text)
            km = miles * 1.60934
            self.root.ids.output_number.text = f"{km:.2f} km"
        except ValueError:
            self.root.ids.output_number.text = "Invalid input"


    def increase_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(value + 1)
        except ValueError:
            self.root.ids.input_number.text = "0"

    def decrease_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(value - 1)
        except ValueError:
            self.root.ids.input_number.text = "0"


ConvertMilesApp().run()
