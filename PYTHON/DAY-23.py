from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp

def convert_temperature(temp, unit):
    try:
        temp = float(temp)
    except ValueError:
        return "❌ Invalid input. Enter a number."

    if unit == "C":
        converted = (temp * 9/5) + 32
        return f"{temp}°C = {converted:.2f}°F"
    elif unit == "F":
        converted = (temp - 32) * 5/9
        return f"{temp}°F = {converted:.2f}°C"
    else:
        return "❌ Invalid unit. Please use 'C' or 'F'."


class TempConverterGUI(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(15), **kwargs)

        self.label_title = MDLabel(
            text="  [b]Temperature Converter[/b]",
            halign="center",
            theme_text_color="Primary",
            markup=True,
            font_style="H5"
        )

        self.temp_input = MDTextField(
            hint_text="Enter temperature (e.g., 100)",
            mode="rectangle",
            input_filter="float"
        )

        self.unit_value = "C"
        self.menu_items = [
            {
                "text": "C",
                "on_release": lambda x="C": self.set_unit(x)
            },
            {
                "text": "F",
                "on_release": lambda x="F": self.set_unit(x)
            }
        ]
        self.unit_menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=2
        )
        self.unit_button = MDRaisedButton(
            text="Select Unit (C/F)",
            pos_hint={"center_x": 0.5},
            on_release=self.open_menu
        )

        self.convert_button = MDRaisedButton(
            text="Convert",
            md_bg_color=(0.2, 0.6, 1, 1),
            on_release=self.convert
        )

        self.result_label = MDLabel(
            text=" Result will appear here",
            halign="center",
            theme_text_color="Secondary"
        )

        self.add_widget(self.label_title)
        self.add_widget(self.temp_input)
        self.add_widget(self.unit_button)
        self.add_widget(self.convert_button)
        self.add_widget(self.result_label)

    def open_menu(self, instance):
        self.unit_menu.caller = instance
        self.unit_menu.open()

    def set_unit(self, unit):
        self.unit_value = unit
        self.unit_button.text = f"Selected Unit: {unit}"
        self.unit_menu.dismiss()

    def convert(self, instance):
        temp = self.temp_input.text
        unit = self.unit_value
        result = convert_temperature(temp, unit)
        self.result_label.text = result


class TemperatureApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"  # or "Dark" if you're a night owl 🌚
        return TempConverterGUI()


if __name__ == "__main__":
    TemperatureApp().run()
