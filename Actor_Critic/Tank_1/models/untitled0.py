from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np

class PolynomialCalculatorApp(App):
    def build(self):
        self.title = 'Polynomial Derivative Calculator'
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title_label = Label(text='Polynomial Derivative Calculator', font_size=18)
        self.root.add_widget(title_label)

        coefficients_label = Label(text='Enter coefficients (separated by commas):', font_size=12)
        self.root.add_widget(coefficients_label)

        self.entry_coefficients = TextInput(font_size=12, multiline=False)
        self.root.add_widget(self.entry_coefficients)

        entry_degree_label = Label(text='Degree of Derivation:', font_size=12)
        self.root.add_widget(entry_degree_label)

        self.entry_degree = TextInput(font_size=12, multiline=False)
        self.root.add_widget(self.entry_degree)

        entry_b_label = Label(text='Enter value of b:', font_size=12)
        self.root.add_widget(entry_b_label)

        self.entry_b = TextInput(font_size=12, multiline=False)
        self.root.add_widget(self.entry_b)

        calculate_button = Button(text='Calculate Derivatives', font_size=12)
        calculate_button.bind(on_press=self.calculate_derivative)
        self.root.add_widget(calculate_button)

        self.results_label = Label(font_size=12)
        self.root.add_widget(self.results_label)

        return self.root

    def calculate_derivative(self, instance):
        coefficients_str = self.entry_coefficients.text
        degree = int(self.entry_degree.text)
        b = float(self.entry_b.text)

        coefficients = [float(coeff.strip()) for coeff in coefficients_str.split(',')]
        polynome = np.poly1d(coefficients)

        self.results_label.text = ''  # Clear previous results

        for i in range(degree + 1):
            polynome_der = polynome.deriv(i)
            result = polynome_der(b)
            self.results_label.text += f'Derivative {i}: {polynome_der}\n'
            self.results_label.text += f'Result for b: {result}\n\n'

if __name__ == '__main__':
    PolynomialCalculatorApp().run()




