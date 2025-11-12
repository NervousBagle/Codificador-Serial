import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("Codificador de Seriales")
        self.grid_rowconfigure(12, weight=1)  # configure grid system
        self.grid_columnconfigure(2, weight=1)

        vcmd = (self.register(self.validar_binario), '%P')
        # add widgets to app
        ## Añadir entrada de texto
        self.entry = ctk.CTkEntry(self, placeholder_text="Ingrese el serial",
            width=300, height=30,
            textvariable=tk.StringVar(), validate="key", validatecommand=vcmd)
        self.entry.grid(row=0, column=0, padx=20, pady=10)

        ## Añadir boton de confirmacion
        self.button = ctk.CTkButton(self, text="Codificar", command=self.codificar)
        self.button.grid(row=0, column=1, padx=20, pady=10)

        ## Añadir botones de elegir metodo
        def radiobutton_event():
            print("radiobutton toggled, current value:", self.radio_var.get())
        self.radio_var = ctk.StringVar(value="No seleccionado")

        ## Unipolar
        self.unpolarRadioBtn = ctk.CTkRadioButton(self, text="Unipolar",
            command=radiobutton_event, variable=self.radio_var, value="Unipolar")
        self.unpolarRadioBtn.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        ##Polares
        self.polaresLbl = ctk.CTkLabel(self, text="Polares", fg_color="transparent")
        self.polaresLbl.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        ### Manchester
        self.manchesterRadioBtn = ctk.CTkRadioButton(self, text="Manchester",
            command=radiobutton_event, variable=self.radio_var, value="Manchester")
        self.manchesterRadioBtn.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        ### Manchester Diferencial
        self.manchesterDiferencialRadioBtn = ctk.CTkRadioButton(self, text="Manchester Diferencial",
            command=radiobutton_event, variable=self.radio_var, value="Manchester Diferencial")
        self.manchesterDiferencialRadioBtn.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        ### NRZ-I
        self.NRZIRadioBtn = ctk.CTkRadioButton(self, text="NRZ-I",
            command=radiobutton_event, variable=self.radio_var, value="NRZ-I")
        self.NRZIRadioBtn.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
        ### NRZ-L
        self.NRZLRadioBtn = ctk.CTkRadioButton(self, text="NRZ-L",
            command=radiobutton_event, variable=self.radio_var, value="NRZ-L")
        self.NRZLRadioBtn.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        ### RZ
        self.RZRadioBtn = ctk.CTkRadioButton(self, text="RZ",
            command=radiobutton_event, variable=self.radio_var, value="RZ")
        self.RZRadioBtn.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

        ## Bipolares
        self.bipolaresLbl = ctk.CTkLabel(self, text="Bipolares", fg_color="transparent")
        self.bipolaresLbl.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
        ### AMI
        self.aMIRadioBtn = ctk.CTkRadioButton(self, text="AMI",
            command=radiobutton_event, variable=self.radio_var, value="AMI")
        self.aMIRadioBtn.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)
        ### B8ZS
        self.bOchoZSRadioBtn = ctk.CTkRadioButton(self, text="B8ZS",
            command=radiobutton_event, variable=self.radio_var, value="B8ZS")
        self.bOchoZSRadioBtn.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)
        ### HDB3
        self.hDB3RadioBtn = ctk.CTkRadioButton(self, text="HDB3",
            command=radiobutton_event, variable=self.radio_var, value="HDB3")
        self.hDB3RadioBtn.grid(row=11, column=0, padx=10, pady=10, sticky=tk.W)

    # add methods to app
    def validar_binario(self, texto):
        """Permite solo 0 y 1 en la entrada."""
        return all(c in "01" for c in texto)

    def codificar(self):
        print("Codificando...")
        serial_ingresado = self.entry.get()
        metodoCodificador = self.radio_var.get()
        if not serial_ingresado:
            messagebox.showwarning("Advertencia", "Debe ingresar un serial antes de continuar.")
            return

        if metodoCodificador == "No seleccionado":
            messagebox.showwarning("Advertencia", "Debe seleccionar un método de codificación.")
            return

        print(f"Codificando con método: {metodoCodificador}")
        print(f"Serial ingresado: {serial_ingresado}")


App().mainloop()