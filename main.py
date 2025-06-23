import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

API_URL = "https://example.com/api/aviator/latest"  # placeholder

class AviatorStats(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.result_label = Label(text="Cargando estadísticas...", font_size=24)
        self.add_widget(self.result_label)
        Clock.schedule_interval(self.fetch_stats, 10)

    def fetch_stats(self, *args):
        try:
            # Placeholder request, replace with real endpoint
            response = requests.get(API_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.result_label.text = f"Último multiplicador: {data.get('multiplier', 'N/A')}"
            else:
                self.result_label.text = "Error al obtener datos"
        except Exception as e:
            self.result_label.text = f"Sin conexión ({e.__class__.__name__})"

class AviatorApp(App):
    def build(self):
        return AviatorStats()

if __name__ == "__main__":
    AviatorApp().run()