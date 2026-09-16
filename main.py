from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import requests
import json
import os
from datetime import datetime

# ============================================================
# CONFIG — your real entry IDs
# ============================================================
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfnrxirexXQPaTAI7Bww1iJTt2lYx6I2pdJUTY0u5hYMXQXrg/formResponse"

ENTRY_IDS = {
    "date_year":     "entry.459531169_year",
    "date_month":    "entry.459531169_month",
    "date_day":      "entry.459531169_day",
    "product":       "entry.895127322",
    "batch_size":    "entry.976902505",
    "batch_no":      "entry.205077809",
    "no_of_packers": "entry.1693116674",
    "output":        "entry.1905891278",
}

PRODUCTS = [
    "AFRABVITE 15ML DROPS",
    "AFRABVITE 100ML SYRUP",
    "ALLERGIN 60ML SYRUP",
    "AMIBAGYL 60ML SUSPENSION",
    "HOSPIMOX (AMOXYCILLIN) 125MG 100ML SUSPENSION",
    "CILLINOX SUSP. (AMPI/CLOX) 100MLS",
    "AMIBAGYL TABLETS 200MG",
    "BANEDIF OINTMENT",
    "BANEDIF POWDER",
    "CHEMOTRIM 100ML SUSPENSION",
    "CILLINOX 12ML DROPS",
    "CITRAMIN 15ML DROPS",
    "CHLORAF 100ML SUSPENSION",
    "CHEMOTRIM TAB 480MG (10X10)",
    "CHEMOTRIM 60ML SUSPENSION",
    "DETONIC 200ML SYRUP",
    "DIASTOP 100ML SUSPENSION",
    "DETONIC SYRUP (1 LTR)",
    "ENAPHRIN NASAL DROPS (10ML)",
    "FUNGUSOL 20GM CREAM",
    "FUNGUSOL 20GM POWDER",
    "FUNGUSOL 50ML LOTION",
    "GLIBENOL CAPLETS 5MG (10X10)",
    "AFRAB CHLOROQUINE DROPS 11ML",
    "AFRAB IBUPROFEN SUSPENSION",
    "LA-TESEN TABLETS",
    "NOSPAMIN 15ML DROPS",
    "NOCOF DROPS",
    "OTO MED 8ML DROPS",
    "PANDA 15ML DROPS",
    "PANDA 60ML SYRUP",
    "PANDA TABLET 96'S",
    "PANDA TABLET 1000'S",
    "PANDA COLD DROPS",
    "REUMEX LOTION",
    "STOPACID 200ML SUSPENSION",
    "TUSSYLIN 100ML SYRUP [Adult]",
    "TUSSYLIN 100ML SYRUP [Infant]",
    "CITRAMIN SYRUP 100ML",
    "CYSTAZOLE SUSPENSION",
    "HALOPERIDOL TABLETS (10MG)",
    "HALOPERIDOL TABLETS (5MG)",
    "PANDA COLD SYRUP",
    "PANDA NIGHT CAPLETS (500MG) 10X10",
    "CYSTAZOLE CAPLETS (200MG)",
    "NOCOF SYRUP",
    "FUNGUSOL PLUS CREAM",
    "FUNGUSOL PLUS LOTION",
    "AFRAB LORATADINE SYRUP (60ML)",
    "AFRAB LORATADINE TABS (10X10)",
    "AFRAB LORATADINE TABS 10MG (10 X 2)",
    "DETONIC PLUS SYRUP",
    "AFRAB METFORMIN TABLETS (3 X 10)",
    "PANDA NIGHT CAPLETS (12 X 8)",
    "AMIBAGYL TABLETS 200MG (1000'S)",
    "AFRABVITE PLUS DROPS",
    "AFRAMIN SYRUP (200ML)",
    "PANDA NIGHT SYRUP (60ML)",
    "AFRAB IVY SYRUP (100ML)",
    "THIVY SYRUP (100ML)",
    "AFRAB GRIPE WATER (100ML)",
    "STOPACID 200ML SUSPENSION (strawberry)",
    "STOPACID 200ML SUSPENSION (banana)",
    "PANDA SUSPENSION (60ML)",
    "AFRAB CIPROFLOXACIN CAPLET 500MG (10'S)",
    "PANDA NIGHT CAPLETS (2x10)",
    "PANDA CAPLETS 500mg (10X10)",
    "PANDA CAPLETS 500mg (10 X 2)",
    "PANDA NIGHT DROPS (15ML)",
    "AFRAGRA TABLETS (100MG (1 X 4)",
    "HOSPIMOX CAPSULES",
    "NOSPAMIN SYRUP",
    "AFRAB LEVOFLOXACIN CAPLET 500MG (10'S)",
    "CITRAMIN PLUS TAB (Effervescent)",
    "AFRAB ALENDOMAX 70mg",
    "B-Cor 2.5MG (10X3)",
    "B-Cor 5MG (15 X 2)",
    "B-Cor TABLETS 10MG (10 X 3)",
    "AFRAB RESPAL 1mg (2 X 10)",
    "AFRAB RISPERIDON 2mg (2 X 10)",
    "AFRAB RISPERIDON 4mg (2 X 10)",
    "PANDA EXTRA CAPLETS 500MG (10X10)",
    "AFRAB SALBUTAMOL SYRUP 100ML",
    "LATESEN DS CAPLETS (1 X 6)",
    "AFRAB SALBUTAMOL TABLET 4MG (10X10)",
    "ALFALEX CAPSULES 200MG (1 X 10)",
    "ALFALEX CAPSULES 400MG",
    "HISTOLAT SYRUP (60ML)",
    "HISTOLAT TABLETS (5MG)",
    "ALFADOX TABLETS (3x1)",
    "AFRAB IBUPROFEN DS DROPS 30ML",
    "ALFADOX SUSPENSION (15ML)",
    "AFRABRON SYRUP(200ML)",
    "ULTRA LINC TABLETS 5MG(2x15)",
    "ULTRA LINC TABLETS 20MG(1x4)",
    "AFRADIN DROPS(30ML)",
    "DEKOLIK SYRUP(60ML)",
    "AFRAB IBUPROFEN EFFERVESCENT",
    "AFRAB IBUPROFEN DS SUSPENSION 100ML",
    "PANDA EFFERVESCENT",
    "AFRAB TERAD DROPS(25ML)",
    "AFRAB SIMETHICONE DROPS",
    "TERAD CAPLETS (1X30)",
    "CITRAMIN DROPS 30ML",
    "AFRABVITE DROPS 30ML",
    "AFRABVITE PLUS DROPS 30ML",
    "PANDA DROPS 30ML",
    "NOCOF DROPS 30ML",
    "SOLOMAX SYRUP 100ML",
    "AFRABLEX SYRUP (100ML)",
    "AFRAB ZINC 11MG TABLETS(10 X 3)",
    "AFRAB LORATADINE SYRUP 100ML",
    "AFRAB ORS POWDER(3x1)",
    "AFRAB ZINC SULPHATE 20MG TABLETS(1 X 10)",
    "AFRAB HAND SANITIZER (100ML)",
    "METFORMIN TABLETS(10 X 10)",
    "AFRAB CHLOROQUINE TABLETS(1 x 10)",
    "LA-TESEN TABLETS 20/120MG (2 X 24)",
    "CETRAZEE TABLETS 60's",
    "AFRAB HYOSCINE BUTYLBROMIDE SYRUP",
    "LATESEN DISPERSIBLE TABS (6'S)",
    "DETONIC SYRUP (100ML)",
    "RESPERIDONE SYRUP",
    "IBUPROFEN TABLETS",
    "AFRABRON TABLETS(3 X 10)",
    "AFRAB LISINOPRIL TABLET 5MG(2 X 14)",
    "AFRAB LISINOPRIL TABLET 10MG(2 X 14)",
    "AFRAB AMLODIPINE TABLETS 5MG(2 X 14)",
    "AFRAB AMLODIPINE TABLETS 10MG(2 X 14)",
    "VITA JOY MOOD CARE TABLETS",
    "VITA JOY NEURO CARE TABLETS",
    "VITA JOY POSTNATAL CARE TABLETS",
    "VITA JOY PRENATAL CARE TABLETS",
    "VITA JOY SLEEP CARE TABLETS",
    "VITA JOY STRESS RELAX CARE TABLETS",
    "VITA JOY FEMALE TEEN CARE TABLETS",
    "VITA JOY MALE TEEN CARE TABLETS",
]

QUEUE_FILE = "offline_queue.json"


# ============================================================
# HELPERS
# ============================================================
def split_date(iso_date):
    y, m, d = iso_date.split("-")
    return str(int(y)), str(int(m)), str(int(d))


def build_payload(data):
    y, m, d = split_date(data["date"])
    return {
        ENTRY_IDS["date_year"]:     y,
        ENTRY_IDS["date_month"]:    m,
        ENTRY_IDS["date_day"]:      d,
        ENTRY_IDS["product"]:       data["product"],
        ENTRY_IDS["batch_size"]:    data["batch_size"],
        ENTRY_IDS["batch_no"]:      data["batch_no"],
        ENTRY_IDS["no_of_packers"]: data["no_of_packers"],
        ENTRY_IDS["output"]:        data["output"],
    }


def try_submit(data):
    try:
        r = requests.post(FORM_URL, data=build_payload(data), timeout=15)
        return r.status_code == 200
    except requests.RequestException:
        return False


def save_to_queue(data):
    queue = []
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE) as f:
            queue = json.load(f)
    queue.append(data)
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f)


def flush_queue():
    if not os.path.exists(QUEUE_FILE):
        return 0
    with open(QUEUE_FILE) as f:
        queue = json.load(f)
    remaining, sent = [], 0
    for item in queue:
        if try_submit(item):
            sent += 1
        else:
            remaining.append(item)
    with open(QUEUE_FILE, "w") as f:
        json.dump(remaining, f)
    return sent


# ============================================================
# SEARCHABLE PRODUCT PICKER
# ============================================================
class ProductPicker(Popup):
    def __init__(self, on_pick, **kwargs):
        super().__init__(title="Select Product", size_hint=(0.95, 0.9), **kwargs)
        self.on_pick = on_pick

        root = BoxLayout(orientation="vertical", padding=8, spacing=8)

        self.search = TextInput(
            hint_text="Type to search...",
            multiline=False,
            size_hint_y=None,
            height=48,
        )
        self.search.bind(text=self.refresh)
        root.add_widget(self.search)

        self.scroll = ScrollView()
        self.list_layout = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing=2
        )
        self.list_layout.bind(minimum_height=self.list_layout.setter("height"))
        self.scroll.add_widget(self.list_layout)
        root.add_widget(self.scroll)

        self.add_widget(root)
        self.refresh(None, "")

    def refresh(self, instance, value):
        self.list_layout.clear_widgets()
        q = value.strip().lower()
        matches = [p for p in PRODUCTS if q in p.lower()] if q else PRODUCTS
        for item in matches:
            btn = Button(
                text=item,
                size_hint_y=None,
                height=44,
                halign="left",
                valign="middle",
            )
            btn.bind(on_release=lambda b, t=item: self.pick(t))
            self.list_layout.add_widget(btn)

    def pick(self, text):
        self.on_pick(text)
        self.dismiss()


# ============================================================
# MAIN UI
# ============================================================
class PackerForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=10, **kwargs)
        Window.softinput_mode = "below_target"

        self.fields = {}

        def add_row(label, key, hint="", input_type="text"):
            row = BoxLayout(size_hint_y=None, height=52, spacing=6)
            row.add_widget(Label(text=label, size_hint_x=0.35, halign="left"))
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

        # 1. Date
        add_row("Date:", "date", "YYYY-MM-DD")
        self.fields["date"].text = datetime.now().strftime("%Y-%m-%d")

        # 2. Product
        prod_row = BoxLayout(size_hint_y=None, height=52, spacing=6)
        prod_row.add_widget(Label(text="Product:", size_hint_x=0.35, halign="left"))
        self.product_btn = Button(text="Tap to choose product", size_hint_x=0.65)
        self.product_btn.bind(on_release=self.open_product_picker)
        prod_row.add_widget(self.product_btn)
        self.add_widget(prod_row)
        self.selected_product = ""

        # 3. Batch No
        add_row("Batch No:", "batch_no")

        # 4. Output
        add_row("Output:", "output", input_type="number")

        # 5. No of Packers
        add_row("No of Packers:", "no_of_packers", input_type="number")

        # 6. Batch size
        add_row("Batch size:", "batch_size", input_type="number")

        # Buttons
        btns = BoxLayout(size_hint_y=None, height=56, spacing=8)
        submit = Button(text="Submit")
        submit.bind(on_release=self.submit)
        btns.add_widget(submit)

        sync = Button(text="Sync")
        sync.bind(on_release=self.sync_queue)
        btns.add_widget(sync)

        clear = Button(text="Clear")
        clear.bind(on_release=self.clear)
        btns.add_widget(clear)

        self.add_widget(btns)

        self.status = Label(text="Ready", size_hint_y=None, height=32)
        self.add_widget(self.status)

    def open_product_picker(self, *args):
        ProductPicker(on_pick=self.set_product).open()

    def set_product(self, name):
        self.selected_product = name
        self.product_btn.text = name

    def collect(self):
        return {
            "date":          self.fields["date"].text.strip(),
            "product":       self.selected_product,
            "batch_no":      self.fields["batch_no"].text.strip(),
            "output":        self.fields["output"].text.strip(),
            "no_of_packers": self.fields["no_of_packers"].text.strip(),
            "batch_size":    self.fields["batch_size"].text.strip(),
        }

    def submit(self, *args):
        data = self.collect()

        if data["product"] not in PRODUCTS:
            self.status.text = "Pick a product from the list."
            return
        if not all(data.values()):
            self.status.text = "Fill in every field."
            return

        if try_submit(data):
            self.status.text = "Submitted."
            self.clear()
        else:
            save_to_queue(data)
            self.status.text = "Saved offline - tap Sync."

    def sync_queue(self, *args):
        n = flush_queue()
        self.status.text = ("Synced %d entry(ies)." % n) if n else "Nothing to sync."

    def clear(self, *args):
        self.selected_product = ""
        self.product_btn.text = "Tap to choose product"
        for k, ti in self.fields.items():
            ti.text = ""
        self.fields["date"].text = datetime.now().strftime("%Y-%m-%d")


class PackerApp(App):
    def build(self):
        self.title = "Packers Daily Entry"
        return PackerForm()


if __name__ == "__main__":
    PackerApp().run()
