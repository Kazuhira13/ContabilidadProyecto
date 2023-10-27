import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def punto_Equilibrio():
    try:
        unidades = int(entrada_unidades.get())
        costos = int(entrada_costos.get())
        fijos = int(entrada_fijos.get())
        margen = unidades - costos
        cubrir = fijos / margen
        porcentaje = margen / unidades
        vender = fijos / porcentaje
        vender2 = fijos/0.55
        etique_resultados.config(text=f"El margen es: {margen}, unidades minimas: {cubrir}, las unidades a vender son: Q.{vender}")

        conceptos = ["inicio", "Unidades para Cubrir", "Unidades a Vender"]
        valores = [margen, cubrir, vender2*2.6]
        valores2 = [fijos, vender, vender2*2.1]
        valores3 = [margen,fijos ,vender2]
        # Asegúrate de que "Unidades para Cubrir" esté entre el punto de equilibrio y los costos fijos
        if cubrir > vender:
            valores[1] = cubrir
        else:
            valores[1] = vender
        # Limpiar la gráfica existente
        plot.clear()

        # Dibuja las líneas
        plot.plot(conceptos, valores, marker='o', linestyle='-',label='ingresos totales' )
        plot.plot(conceptos, valores2, marker='o', linestyle='-',label='costos totales')
        plot.plot(conceptos, valores3, marker='o', linestyle='-',label='Costos variables')
        plot.set_title("Resultados en un Plano Cartesiano")
        plot.set_xlabel("valor x")
        plot.set_ylabel("Valor y")

        # Mostrar el valor de "margen" en el eje Y
        plot.text("Unidades para Cubrir",margen,f"{cubrir}")
        plot.text("Unidades a Vender",margen,f"{cubrir+1000}")

        plot.axvline(x="Unidades para Cubrir", color='yellow', linestyle='--')
        plot.axhline(y=fijos, color='blue', linestyle='--', label='Costos Fijos')
        plot.axhline(y=vender, color='yellow', linestyle='--', label='punto de equilibrio')

        plot.legend()
        plot.grid(color='0.7')

        # Actualizar el lienzo de Matplotlib
        canvas.draw()

    except ValueError:
        etique_resultados.config(text="Ingrese un valor numérico válido")

ventana = tk.Tk()
ventana.title("Calculadora de punto de equilibrio")
ventana.geometry("1000x800")

titulo_label = tk.Label(ventana, text="Calculadora de punto de equilibrio", font=("Helvetica", 11), bg="#F3F4F6")
titulo_label.pack(pady=10)
titulo_label = tk.Label(ventana, text="Timothy Gerald Palma Perez 0907-20-6162", font=("Helvetica", 11), bg="#F3F4F6")
titulo_label.pack(pady=10)
etiqueta_unidades = tk.Label(ventana, text="Unidades Vendidas:",font=('Helvetica', 12))
etiqueta_unidades.pack(pady=5)
entrada_unidades = tk.Entry(ventana)
entrada_unidades.pack(pady=5)

etiqueta_costos = tk.Label(ventana, text="Costos Variables por Unidad:",font=('Helvetica', 12))
etiqueta_costos.pack(pady=5)
entrada_costos = tk.Entry(ventana)
entrada_costos.pack(pady=5)

etiqueta_fijos = tk.Label(ventana, text="Costos Fijos:",font=('Helvetica', 12))
etiqueta_fijos.pack(pady=5)
entrada_fijos = tk.Entry(ventana)
entrada_fijos.pack(pady=5)

boton = tk.Button(ventana, text="Calcular Punto de Equilibrio", command=punto_Equilibrio , font=('Helvetica', 13))
boton.pack(pady=10)

etique_resultados = tk.Label(ventana, text="", font=('Helvetica', 14))
etique_resultados.pack(pady=10)

# Crear un objeto Figure de Matplotlib
fig = Figure(figsize=(8, 8))
plot = fig.add_subplot(111)

# Crear un lienzo de Matplotlib para tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack()

ventana.mainloop()