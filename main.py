__version__ = "1.0.0"

import json
import os
from datetime import datetime

import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfnrxirexXQPaTAI7Bww1iJTt2lYx6I2pdJUTY0u5hYMXQXrg/formResponse"

ENTRY_IDS = {
    "date_year": "entry.459531169_year",
    "date_month": "entry.459531169_month",
    "date_day": "entry.459531169_day",
    "product": "entry.895127322",
    "batch_size": "entry.976902505",
    "batch_no": "entry.205077809",
    "no_of_packers": "entry.1693116674",
    "output": "entry.1905891278",
}

QUEUE_FILE = "offline_queue.json"

PRODUCTS = [
    "AFRABVITE 15ML DROPS",
    "AFRABVITE 100ML SYRUP",
    "ALLERGIN 60ML SYRUP",
    "AMIBAGYL 60ML SUSPENSION",
    "HOSPIMOX (AMOXYCILLIN) 125MG 100ML SUSPENSION",
    "CHEMOTRIM 100ML SUSPENSION",
    "CITRAMIN 15ML DROPS",
    "DETONIC 200ML SYRUP",
    "PANDA 15ML DROPS",
    "PANDA 60ML SYRUP",
    "STOPACID 200ML SUSPENSION",
    "AFRAB CHLOROQUINE DROPS 11ML",
    "AFRAB IBUPROFEN SUSPENSION",
    "AFRAB LORATADINE SYRUP (60ML)",
    "AFRAB METFORMIN TABLETS (3 X 10)",
    "AFRAB BRON SYRUP (200ML)",
    "AMIBAGYL TABLETS 200MG",
    "PANDA NIGHT CAPLETS (500MG) 10X10",
    "VITA JOY MOOD CARE TABLETS",
    "VITA JOY NEURO CARE TABLETS",
    "VITA JOY SLEEP CARE TABLETS",
]


def get_queue_path():
    app = App.get_running_app()
    if app is not None:
        return os.path.join(app.user_data_dir, QUEUE_FILE)
    return os.path.join(os.path.expanduser("~"), QUEUE_FILE)


def split_date(iso_date):
    if not iso_date:
        return "0", "0", "0"
    try:
        y, m, d = iso_date.split("-")
        return str(int(y)), str(int(m)), str(int(d))
    except ValueError:
        return "0", "0", "0"


def build_payload(data):
    y, m, d = split_date(data.get("date", ""))
    return {
        ENTRY_IDS["date_year"]: y,
        ENTRY_IDS["date_month"]: m,
        ENTRY_IDS["date_day"]: d,
        ENTRY_IDS["product"]: data.get("product", ""),
        ENTRY_IDS["batch_size"]: data.get("batch_size", ""),
        ENTRY_IDS["batch_no"]: data.get("batch_no", ""),
        ENTRY_IDS["no_of_packers"]: data.get("no_of_packers", ""),
        ENTRY_IDS["output"]: data.get("output", ""),
    }


def try_submit(data):
    try:
        response = requests.post(FORM_URL, data=build_payload(data), timeout=15)
        return response.status_code in (200, 201, 202)
    except requests.RequestException:
        return False


def load_queue(queue_path):
    if not os.path.exists(queue_path):
        return []
    try:
        with open(queue_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_queue(queue_path, queue):
    try:
        with open(queue_path, "w", encoding="utf-8") as f:
            json.dump(queue, f)
    except OSError:
        pass


def save_to_queue(data):
    queue_path = get_queue_path()
    queue = load_queue(queue_path)
    queue.append(data)
    save_queue(queue_path, queue)


def flush_queue():
    queue_path = get_queue_path()
    queue = load_queue(queue_path)
    if not queue:
        return 0

    remaining = []
    sent = 0

    for item in queue:
        if try_submit(item):
            sent += 1
        else:
            remaining.append(item)

    save_queue(queue_path, remaining)
    return sent


class ProductPicker(Popup):
    def __init__(self, on_pick, **kwargs):
        super().__init__(title="Select Product", size_hint=(0.95, 0.9), **kwargs)
        self.on_pick = on_pick

        root = BoxLayout(orientation="vertical", padding=8, spacing=8)

        self.search = TextInput(
            hint_text="Type to search product...",
            multiline=False,
            size_hint_y=None,
            height=48,
        )
        self.search.bind(text=self.refresh)
        root.add_widget(self.search)

        self.scroll = ScrollView()
        self.list_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=2)
        self.list_layout.bind(minimum_height=self.list_layout.setter("height"))
        self.scroll.add_widget(self.list_layout)
        root.add_widget(self.scroll)

        self.add_widget(root)
        self.refresh(None, "")

    def refresh(self, instance, value):
        self.list_layout.clear_widgets()
        query = (value or "").strip().lower()
        items = [p for p in PRODUCTS if query in p.lower()] if query else PRODUCTS

        for item in items:
            btn = Button(
                text=item,
                size_hint_y=None,
                height=44,
                halign="left",
                valign="middle",
            )
            btn.bind(on_release=lambda b, text=item: self.pick(text))
            self.list_layout.add_widget(btn)

    def pick(self, text):
        self.on_pick(text)
        self.dismiss()


class PackerForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=10, **kwargs)
        Window.softinput_mode = "below_target"

        self.fields = {}

        def add_row(label_text, key, hint="", input_type="text"):
            row = BoxLayout(size_hint_y=None, height=52, spacing=6)
            row.add_widget(Label(text=label_text, size_hint_x=0.35, halign="left"))

            ti = TextInput(
                hint_text=hint,
                multiline=False,
                input_type=input_type,
                size_hint_x=0.65,
            )
            row.add_widget(ti)
            self.add_widget(row)

            self.fields[key] = ti
            return ti

        # Date
        add_row("Date:", "date", "YYYY-MM-DD")
        self.fields["date"].text = datetime.now().strftime("%Y-%m-%d")

        # Product
        product_row = BoxLayout(size_hint_y=None, height=52, spacing=6)
        product_row.add_widget(Label(text="Product:", size_hint_x=0.35))
        self.product_btn = Button(text="Tap to choose product", size_hint_x=0.65)
        self.product_btn.bind(on_release=self.open_product_picker)
        product_row.add_widget(self.product_btn)
        self.add_widget(product_row)
        self.selected_product = ""

        # Batch No
        add_row("Batch No:", "batch_no")

        # Output
        add_row("Output:", "output", input_type="number")

        # No of Packers
        add_row("No of Packers:", "no_of_packers", input_type="number")

        # Batch size
        add_row("Batch size:", "batch_size", input_type="number")

        # Buttons
        button_row = BoxLayout(size_hint_y=None, height=56, spacing=8)

        submit_btn = Button(text="Submit")
        submit_btn.bind(on_release=self.submit)
        button_row.add_widget(submit_btn)

        sync_btn = Button(text="Sync")
        sync_btn.bind(on_release=self.sync_queue)
        button_row.add_widget(sync_btn)

        clear_btn = Button(text="Clear")
        clear_btn.bind(on_release=self.clear_form)
        button_row.add_widget(clear_btn)

        self.add_widget(button_row)

        self.status = Label(text="Ready", size_hint_y=None, height=32)
        self.add_widget(self.status)

    def open_product_picker(self, instance):
        ProductPicker(on_pick=self.set_product).open()

    def set_product(self, name):
        self.selected_product = name
        self.product_btn.text = name

    def collect_data(self):
        return {
            "date": self.fields["date"].text.strip(),
            "product": self.selected_product,
            "batch_no": self.fields["batch_no"].text.strip(),
            "output": self.fields["output"].text.strip(),
            "no_of_packers": self.fields["no_of_packers"].text.strip(),
            "batch_size": self.fields["batch_size"].text.strip(),
        }

    def submit(self, instance):
        data = self.collect_data()

        if not data["product"] or data["product"] not in PRODUCTS:
            self.status.text = "Please choose a valid product."
            return

        if not all(data.values()):
            self.status.text = "Please fill in every field."
            return

        if try_submit(data):
            self.status.text = "Submitted successfully."
            self.clear_form()
        else:
            save_to_queue(data)
            self.status.text = "Saved offline. Tap Sync to retry."

    def sync_queue(self, instance):
        sent = flush_queue()
        if sent > 0:
            self.status.text = f"Synced {sent} item(s)."
        else:
            self.status.text = "Nothing to sync."

    def clear_form(self, instance=None):
        self.selected_product = ""
        self.product_btn.text = "Tap to choose product"

        for field in self.fields.values():
            field.text = ""

        self.fields["date"].text = datetime.now().strftime("%Y-%m-%d")


class PackerApp(App):
    def build(self):
        self.title = "Packers Daily Entry"
        return PackerForm()


if __name__ == "__main__":
    PackerApp().run()