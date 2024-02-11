import tkinter as tk
from tkinter import messagebox

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Risttahuka Kalkulaator")
        self.geometry("400x400")

        self.label_pikkus = tk.Label(self, text="Pikkus:")
        self.label_pikkus.pack()
        self.entry_pikkus = tk.Entry(self)
        self.entry_pikkus.pack()

        self.label_laius = tk.Label(self, text="Laius:")
        self.label_laius.pack()
        self.entry_laius = tk.Entry(self)
        self.entry_laius.pack()

        self.label_korgus = tk.Label(self, text="Kõrgus:")
        self.label_korgus.pack()
        self.entry_korgus = tk.Entry(self)
        self.entry_korgus.pack()

        self.button_arvuta = tk.Button(self, text="Arvuta", command=self.arvuta_kujund)
        self.button_arvuta.pack()

        self.label_mootmed = tk.Label(self, text="")
        self.label_mootmed.pack()

        self.label_taispindala = tk.Label(self, text="")
        self.label_taispindala.pack()

        self.label_ruumala = tk.Label(self, text="")
        self.label_ruumala.pack()

        self.label_diagonaal = tk.Label(self, text="")
        self.label_diagonaal.pack()

        # Võimaldab arvutada ka Enter klahvi vajutamisega
        self.bind("<Return>", self.arvuta_kujund)

    def arvuta_kujund(self, event=None):
        try:
            pikkus_str = self.entry_pikkus.get()
            laius_str = self.entry_laius.get()
            korgus_str = self.entry_korgus.get()

            if not (pikkus_str and laius_str and korgus_str):
                raise ValueError("Kõik väljad peavad olema täidetud.")

            if not (pikkus_str.replace('.', '', 1).isdigit() and laius_str.replace('.', '', 1).isdigit() and korgus_str.replace('.', '', 1).isdigit()):
                raise ValueError("Kõik mõõtmed peavad olema arvud.")

            pikkus = float(pikkus_str)
            laius = float(laius_str)
            korgus = float(korgus_str)

            if pikkus <= 0 or laius <= 0 or korgus <= 0:
                raise ValueError("Kõik mõõtmed peavad olema positiivsed.")

            kujund = self.controller.loodud_kujund(pikkus, laius, korgus)
            taispindala = kujund.arvuta_taispindala()
            ruumala = kujund.arvuta_ruumala()
            diagonaal = kujund.arvuta_diagonaal()

            self.label_mootmed.config(text=f"Pikkus: {pikkus:.2f}, Laius: {laius:.2f}, Kõrgus: {korgus:.2f}")
            self.label_taispindala.config(text=f"Täispindala: {taispindala:.2f}")
            self.label_ruumala.config(text=f"Ruumala: {ruumala:.2f}")
            self.label_diagonaal.config(text=f"Diagonaal: {diagonaal:.2f}")
        except ValueError as ve:
            messagebox.showerror("Viga", str(ve))