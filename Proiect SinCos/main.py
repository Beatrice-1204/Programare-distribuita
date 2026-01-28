import math
import tkinter as tk
from tkinter import ttk, messagebox


class SinCosApp(tk.Tk):    #mostenire, clasa principala a unei ferestre GUI
    def __init__(self):   #constructor
        super().__init__()   #apeleaza contructorul clasei parinte (creeaza fereastra)
        self.title("Calculator trigonometric")
        self.geometry("820x420")
        self.minsize(820, 420)
        #self.resizable(False, False)

        # Unit: degrees or radians
        self.angle_unit = tk.StringVar(value="deg")

        # Precision for display
        self.precision = tk.IntVar(value=10)

        # Result text
        self.result_var = tk.StringVar(value="—")

        self._build_ui()  #apeleaza metoda care construieste interfata grafica

    # ---------------- UI ----------------

    def _build_ui(self):   #metoda care creaza componentele grafice
        main = ttk.Frame(self, padding=16) #creaza containerul Frame
        main.pack(fill="both", expand=True) #ocupa tot spatiul disponibil

        title = ttk.Label(main, text="Calculator sin / cos", font=("Segoe UI", 14, "bold"))
        title.pack(anchor="w") #aliniere la stanga

        ttk.Label(main, text="Introdu un unghi:").pack(anchor="w", pady=(12, 4))

        entry_row = ttk.Frame(main) #Frame pt alinierea pe orizontala
        entry_row.pack(fill="x") #ocupa latimea

        self.angle_entry = ttk.Entry(entry_row) #campul de introducere a textului
        self.angle_entry.pack(side="left", fill="x", expand=True) #apare in partea stanga si se intinde pe latime
        self.angle_entry.focus() #cursorul apare automat in campul de imput

        self.unit_label = ttk.Label(entry_row, text="(grade)")  #afiseaza unitatea corecta
        self.unit_label.pack(side="left", padx=(10, 0)) #spatiu intre input si text

        #frame separat pentru butoane radio
        unit_row = ttk.Frame(main)
        unit_row.pack(anchor="w", pady=(10, 0))

        ttk.Radiobutton(
            unit_row, text="Grade", value="deg",
            variable=self.angle_unit, command=self._on_unit_change #fct apelata la schimbare
        ).pack(side="left")

        #al doilea radio button
        ttk.Radiobutton(
            unit_row, text="Radiani", value="rad",
            variable=self.angle_unit, command=self._on_unit_change
        ).pack(side="left", padx=(12, 0))

        buttons = ttk.Frame(main)
        buttons.pack(fill="x", pady=(14, 0))

        ttk.Button(buttons, text="sin", command=self.compute_sin).pack(side="left", expand=True, fill="x")
        ttk.Button(buttons, text="cos", command=self.compute_cos).pack(side="left", expand=True, fill="x", padx=10)
        ttk.Button(buttons, text="Clear", command=self.clear).pack(side="left", expand=True, fill="x")
        ttk.Button(buttons, text="π", command=self.insert_pi).pack(side="left", expand=True, fill="x", padx=(10, 0))

        ttk.Separator(main).pack(fill="x", pady=14)

        ttk.Label(main, text="Rezultat:").pack(anchor="w")

        self.result_var = tk.StringVar(value="—")
        self.result_label = ttk.Label(main, textvariable=self.result_var, font=("Consolas", 12))
        self.result_label.pack(anchor="w", pady=(6, 0))

        hint = ttk.Label(
            main,
            text="Tip: poți introduce valori ca 30, -45, 3.14, 1e-3",
            foreground="#555"
        )
        hint.pack(anchor="w", pady=(10, 0))

    def _on_unit_change(self):
        if self.angle_unit.get() == "deg":
            self.unit_label.config(text="(grade)")
        else:
            self.unit_label.config(text="(radiani)")

    def insert_pi(self):
        self.angle_entry.insert(tk.INSERT, "pi")
        self.angle_entry.focus()

    #def _read_angle(self) -> float:
     #   raw = self.angle_entry.get().strip().replace(",", ".")
      #  if not raw:
       #     raise ValueError("Câmpul este gol. Introdu un număr.")
        #try:
         #   return float(raw)
       # except ValueError:
        #    raise ValueError("Valoare invalidă. Introdu un număr (ex: 30, 3.14, -0.5).")

    def _read_angle(self) -> float:
        raw = self.angle_entry.get().strip().lower().replace(",", ".")
        if not raw:
            raise ValueError("Câmpul este gol. Introdu un număr sau o expresie (ex: pi/2).")

        # Permitem doar caractere matematice simple
        allowed = set("0123456789.+-*/()pie ")
        if any(ch not in allowed for ch in raw):
            raise ValueError("Expresie invalidă. Folosește doar cifre și: + - * / ( ) pi")

        # Înlocuim 'pi' cu valoarea lui math.pi
        expr = raw.replace("pi", str(math.pi))

        try:
            return eval(expr, {"__builtins__": {}}, {})
        except Exception:
            raise ValueError("Nu am putut evalua expresia. Exemple: pi, pi/2, 2*pi, 3*pi/4, 1.57")

    def _to_radians(self, angle: float) -> float:
        return math.radians(angle) if self.angle_unit.get() == "deg" else angle

    def compute_sin(self):
        try:
            angle = self._read_angle()
            rad = self._to_radians(angle)
            value = math.sin(rad)
            self.result_var.set(f"sin({angle}) = {value:.10f}")
        except Exception as e:
            messagebox.showerror("Eroare", str(e))

    def compute_cos(self):
        try:
            angle = self._read_angle()
            rad = self._to_radians(angle)
            value = math.cos(rad)
            self.result_var.set(f"cos({angle}) = {value:.10f}")
        except Exception as e:
            messagebox.showerror("Eroare", str(e))

    def clear(self):
        self.angle_entry.delete(0, tk.END)
        self.result_var.set("—")
        self.angle_entry.focus()


if __name__ == "__main__":
    app = SinCosApp()
    app.mainloop()
