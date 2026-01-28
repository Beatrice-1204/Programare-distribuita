import math #pt fctii matematice
import tkinter as tk  #pt interfete
from tkinter import ttk, messagebox


#clasa principala / mosteneste tk.Tk pt a fi aplicatia o fereastra
class SinCosApp(tk.Tk):
    def __init__(self):
        super().__init__()  #apel constructor
        self.title("Calculator Trigonometric (sin/cos/tan/cot)")
        self.geometry("820x420")
        self.minsize(820, 420)

        # Unit: degrees or radians
        self.angle_unit = tk.StringVar(value="deg")

        # precizia pt nr zecimale
        self.precision = tk.IntVar(value=10)

        # Result text
        self.result_var = tk.StringVar(value="—")

        self._build_ui()

    # UI
    def _build_ui(self):
        #container principal
        root = ttk.Frame(self, padding=14)
        root.pack(fill="both", expand=True)

        # Layout: left (calculator) + right (history)
        left = ttk.Frame(root)
        left.pack(side="left", fill="both", expand=True)

        right = ttk.Frame(root)
        right.pack(side="right", fill="y", padx=(14, 0))

        title = ttk.Label(left, text="Calculator de expresii trigonometrice", font=("Segoe UI", 14, "bold"))
        title.pack(anchor="w")

        # Expression row
        expr_row = ttk.Frame(left)
        expr_row.pack(fill="x", pady=(12, 6))

        ttk.Label(expr_row, text="Expresie:").pack(side="left")

        #entry unde utilizatorul scrie expresia
        self.expr_entry = ttk.Entry(expr_row)
        self.expr_entry.pack(side="left", fill="x", expand=True, padx=(8, 8))
        self.expr_entry.focus()

        ttk.Button(expr_row, text="C", width=4, command=self.clear_expression).pack(side="left")

        # unitate + precizie
        options = ttk.Frame(left)
        options.pack(fill="x", pady=(6, 10))

        unit_box = ttk.LabelFrame(options, text="Unitate")
        unit_box.pack(side="left", padx=(0, 12))

        ttk.Radiobutton(
            unit_box, text="Grade", value="deg",
            variable=self.angle_unit
        ).pack(side="left", padx=8, pady=6)

        ttk.Radiobutton(
            unit_box, text="Radiani", value="rad",
            variable=self.angle_unit
        ).pack(side="left", padx=8, pady=6)

        #grup pt precizie
        prec_box = ttk.LabelFrame(options, text="Precizie (zecimale)")
        prec_box.pack(side="left")

        prec_combo = ttk.Combobox(
            prec_box,
            values=[2, 4, 6, 10, 15],
            state="readonly",
            width=6
        )
        prec_combo.set(str(self.precision.get()))
        prec_combo.pack(side="left", padx=10, pady=6)

        #actualizare precizie la schimbare
        def on_prec_change(_evt=None):
            try:
                self.precision.set(int(prec_combo.get()))
            except ValueError:
                self.precision.set(10)

        prec_combo.bind("<<ComboboxSelected>>", on_prec_change)

        # Buttons grid
        grid = ttk.Frame(left)
        grid.pack(fill="x", pady=(6, 0))

        # fct aux pt crearea butoanelor
        def btn(text, r, c, cmd, colspan=1):
            b = ttk.Button(grid, text=text, command=cmd)
            b.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=4, pady=4)
            return b

        # Make columns expand
        for i in range(6):
            grid.columnconfigure(i, weight=1)

        # Row 0: trig
        btn("sin", 0, 0, lambda: self.insert_text("sin("))
        btn("cos", 0, 1, lambda: self.insert_text("cos("))
        btn("tan", 0, 2, lambda: self.insert_text("tan("))
        btn("cot", 0, 3, lambda: self.insert_text("cot("))
        btn("π",   0, 4, lambda: self.insert_text("pi"))
        btn(")",   0, 5, lambda: self.insert_text(")"))

        # Row 1: parentheses & operators
        btn("(", 1, 0, lambda: self.insert_text("("))
        btn("+", 1, 1, lambda: self.insert_text("+"))
        btn("-", 1, 2, lambda: self.insert_text("-"))
        btn("*", 1, 3, lambda: self.insert_text("*"))
        btn("/", 1, 4, lambda: self.insert_text("/"))
        btn("^", 1, 5, lambda: self.insert_text("**"))  # exponent

        # Row 2: numbers
        btn("7", 2, 0, lambda: self.insert_text("7"))
        btn("8", 2, 1, lambda: self.insert_text("8"))
        btn("9", 2, 2, lambda: self.insert_text("9"))
        btn("sqrt", 2, 3, lambda: self.insert_text("sqrt("))
        btn("abs", 2, 4, lambda: self.insert_text("abs("))
        btn("e", 2, 5, lambda: self.insert_text("e"))

        # Row 3: numbers
        btn("4", 3, 0, lambda: self.insert_text("4"))
        btn("5", 3, 1, lambda: self.insert_text("5"))
        btn("6", 3, 2, lambda: self.insert_text("6"))
        btn("pi/2", 3, 3, lambda: self.insert_text("pi/2"))
        btn("2*pi", 3, 4, lambda: self.insert_text("2*pi"))
        btn("DEL", 3, 5, self.backspace)

        # Row 4: numbers + dot + evaluate
        btn("1", 4, 0, lambda: self.insert_text("1"))
        btn("2", 4, 1, lambda: self.insert_text("2"))
        btn("3", 4, 2, lambda: self.insert_text("3"))
        btn("0", 4, 3, lambda: self.insert_text("0"))
        btn(".", 4, 4, lambda: self.insert_text("."))
        btn("=", 4, 5, self.evaluate_expression)

        # Result area
        ttk.Separator(left).pack(fill="x", pady=12)
        ttk.Label(left, text="Rezultat:").pack(anchor="w")

        self.result_label = ttk.Label(left, textvariable=self.result_var, font=("Consolas", 13))
        self.result_label.pack(anchor="w", pady=(6, 0))

        hint = ttk.Label(
            left,
            text="Exemple: sin(30)+cos(60)*2 (Grade) | sin(pi/6)+cos(pi/3)*2 (Radiani)",
            foreground="#555"
        )
        hint.pack(anchor="w", pady=(10, 0))

        # Enter key evaluates
        self.bind("<Return>", lambda _e: self.evaluate_expression())

        # ---------------- History ----------------
        ttk.Label(right, text="History", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.history = tk.Listbox(right, height=16, width=34)
        self.history.pack(fill="y", expand=True, pady=(8, 8))

        hist_btns = ttk.Frame(right)
        hist_btns.pack(fill="x")

        ttk.Button(hist_btns, text="Clear", command=self.clear_history).pack(side="left", fill="x", expand=True)
        ttk.Button(hist_btns, text="Use", command=self.use_selected_history).pack(side="left", fill="x", expand=True, padx=(8, 0))

        # Double-click uses item
        self.history.bind("<Double-Button-1>", lambda _e: self.use_selected_history())

    # Fctii aux
    def insert_text(self, s: str):
        self.expr_entry.insert(tk.INSERT, s)
        self.expr_entry.focus()

    def backspace(self):
        pos = self.expr_entry.index(tk.INSERT)
        if pos > 0:
            self.expr_entry.delete(pos - 1, pos)
        self.expr_entry.focus()

    def clear_expression(self):
        self.expr_entry.delete(0, tk.END)
        self.result_var.set("—")
        self.expr_entry.focus()

    def clear_history(self):
        self.history.delete(0, tk.END)

    def use_selected_history(self):
        sel = self.history.curselection()
        if not sel:
            return
        line = self.history.get(sel[0])
        # We stored as: "<expr> = <result>"
        expr = line.split(" = ", 1)[0].strip()
        self.expr_entry.delete(0, tk.END)
        self.expr_entry.insert(0, expr)
        self.expr_entry.focus()

    # evaluarea expresiei
    def evaluate_expression(self):
        expr = self.expr_entry.get().strip()
        if not expr:
            messagebox.showerror("Eroare", "Introdu o expresie.")
            return

        # Normalize
        expr = expr.lower().replace(",", ".").replace("π", "pi")

        # filtru
        allowed_chars = set("0123456789.+-*/()_ piabscotnrgqel")
        # se aporba litere pt functii, etc
        if any(ch not in allowed_chars for ch in expr):
            messagebox.showerror(
                "Eroare",
                "Expresia conține caractere nepermise.\n"
                "Folosește doar cifre și: + - * / ( ) . sin cos tan cot sqrt abs pi e"
            )
            return

        # conversia in rad daca e cazul
        def to_rad(x: float) -> float:
            return math.radians(x) if self.angle_unit.get() == "deg" else x

        # fct Trig
        def sin(x):  # noqa: A001
            return math.sin(to_rad(float(x)))

        def cos(x):  # noqa: A001
            return math.cos(to_rad(float(x)))

        def tan(x):  # noqa: A001
            # tan = sin/cos with domain check
            c = cos(x)
            if abs(c) < 1e-12:
                raise ValueError("tan este nedefinit (cos ≈ 0).")
            return sin(x) / c

        def cot(x):  # noqa: A001
            s = sin(x)
            if abs(s) < 1e-12:
                raise ValueError("cot este nedefinit (sin ≈ 0).")
            return cos(x) / s

        #mediu pt evaluare
        safe_env = {
            "sin": sin,
            "cos": cos,
            "tan": tan,
            "cot": cot,
            "pi": math.pi,
            "e": math.e,
            "sqrt": lambda x: math.sqrt(float(x)),
            "abs": lambda x: abs(float(x)),
        }

        try:
            result = eval(expr, {"__builtins__": {}}, safe_env)

            # Format with selected precision
            p = self.precision.get()
            if isinstance(result, (int, float)):
                formatted = f"{result:.{p}f}"
            else:
                formatted = str(result)

            unit_txt = "°" if self.angle_unit.get() == "deg" else "rad"
            self.result_var.set(f"{formatted}   ({unit_txt})")

            # Add to history
            self.history.insert(tk.END, f"{expr} = {formatted}")

        except Exception as ex:
            messagebox.showerror("Eroare", str(ex))


if __name__ == "__main__":
    app = SinCosApp()
    app.mainloop()
