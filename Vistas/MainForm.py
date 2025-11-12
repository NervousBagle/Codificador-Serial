import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from Controladores import MainControl

from Controladores.MainControl import MainControl


def validar_binario(texto):
    """Permite solo 0 y 1 en la entrada."""
    return all(c in "01" for c in texto)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("Codificador de Seriales")
        self.grid_rowconfigure(12, weight=1)  # configure grid system
        self.grid_columnconfigure(2, weight=1)

        vcmd = (self.register(validar_binario), '%P')
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
        self.polares_lbl = ctk.CTkLabel(self, text="Polares", fg_color="transparent")
        self.polares_lbl.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        ### Manchester
        self.manchester_radio_btn = ctk.CTkRadioButton(self, text="Manchester",
            command=radiobutton_event, variable=self.radio_var, value="Manchester")
        self.manchester_radio_btn.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        ### Manchester Diferencial
        self.manchester_diferencial_radio_btn = ctk.CTkRadioButton(self, text="Manchester Diferencial",
            command=radiobutton_event, variable=self.radio_var, value="Manchester Diferencial")
        self.manchester_diferencial_radio_btn.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        ### NRZ-I
        self.nrz_i_radio_btn = ctk.CTkRadioButton(self, text="NRZ-I",
            command=radiobutton_event, variable=self.radio_var, value="NRZ-I")
        self.nrz_i_radio_btn.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
        ### NRZ-L
        self.nrz_l_radio_btn = ctk.CTkRadioButton(self, text="NRZ-L",
            command=radiobutton_event, variable=self.radio_var, value="NRZ-L")
        self.nrz_l_radio_btn.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        ### RZ
        self.rz_radio_btn = ctk.CTkRadioButton(self, text="RZ",
            command=radiobutton_event, variable=self.radio_var, value="RZ")
        self.rz_radio_btn.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

        ## Bipolares
        self.bipolares_lbl = ctk.CTkLabel(self, text="Bipolares", fg_color="transparent")
        self.bipolares_lbl.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
        ### AMI
        self.ami_radio_btn = ctk.CTkRadioButton(self, text="AMI",
            command=radiobutton_event, variable=self.radio_var, value="AMI")
        self.ami_radio_btn.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)
        ### B8ZS
        self.bochozs_radio_btn = ctk.CTkRadioButton(self, text="B8ZS",
            command=radiobutton_event, variable=self.radio_var, value="B8ZS")
        self.bochozs_radio_btn.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)
        ### HDB3
        self.hdbtres_radio_btn = ctk.CTkRadioButton(self, text="HDB3",
            command=radiobutton_event, variable=self.radio_var, value="HDB3")
        self.hdbtres_radio_btn.grid(row=11, column=0, padx=10, pady=10, sticky=tk.W)

    # add methods to app

    def codificar(self):
        print("Codificando...")
        serial_ingresado = self.entry.get()
        metodo_codificador = self.radio_var.get()

        if not serial_ingresado:
            messagebox.showwarning("Advertencia", "Debe ingresar un serial antes de continuar.")
            return

        if metodo_codificador == "No seleccionado":
            messagebox.showwarning("Advertencia", "Debe seleccionar un método de codificación.")
            return

        controlador = MainControl()
        controlador.recibir_datos(metodo_codificador, serial_ingresado)

App().mainloop()