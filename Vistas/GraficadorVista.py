import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraficadorVista(ctk.CTkToplevel):
    def __init__(self, datos_grafica):
        super().__init__()

        self.title(f"Codificación {datos_grafica['titulo']}")
        self.geometry("800x600")

        # Crear figura de matplotlib
        self.figura = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figura.add_subplot(111)

        # Graficar
        self.ax.step(datos_grafica['tiempo'], datos_grafica['senal'],
                     where='post', linewidth=2, color='blue')

        # Configurar la gráfica
        self.ax.set_xlabel('Tiempo (bits)')
        self.ax.set_ylabel('Nivel de voltaje')
        self.ax.set_title(f"{datos_grafica['titulo']} - Serial: {datos_grafica['serial']}")
        self.ax.grid(True, alpha=0.3)
        self.ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

        # Integrar matplotlib en la ventana de CustomTkinter
        canvas = FigureCanvasTkAgg(self.figura, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Botón para cerrar
        btn_cerrar = ctk.CTkButton(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=10)