import math
import tkinter as tk
from tkinter import ttk, messagebox

class EduMathToolkit:
    """
    EduMath-Toolkit: Módulo principal para simulaciones matemáticas
    y geometría computacional para el nivel secundario y bachillerato.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("EduMath-Toolkit v1.0.0")
        self.root.geometry("600x450")
        
        self.setup_ui()

    def setup_ui(self):
        title = ttk.Label(self.root, text="EduMath Toolkit - Módulo Geométrico", font=("Helvetica", 16, "bold"))
        title.pack(pady=15)

        description = ttk.Label(
            self.root, 
            text="Herramienta de cálculo de áreas y perímetros mediante coordenadas (Fórmula Shoelace).",
            wraplength=500
        )
        description.pack(pady=10)

        # Botón de prueba
        self.btn_calc = ttk.Button(self.root, text="Ejecutar Cálculo Demo", command=self.ejecutar_demo)
        self.btn_calc.pack(pady=20)

    def calcular_shoelace(self, vertices):
        """Calcula el área de un polígono dadas sus coordenadas (x, y)."""
        n = len(vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) / 2.0

    def ejecutar_demo(self):
        # Coordenadas de ejemplo (Triángulo)
        puntos = [(0, 0), (4, 0), (4, 3)]
        area = self.calcular_shoelace(puntos)
        messagebox.showinfo("Resultado", f"Área calculada para el polígono de prueba: {area} u²")

if __name__ == "__main__":
    root = tk.Tk()
    app = EduMathToolkit(root)
    root.mainloop()
