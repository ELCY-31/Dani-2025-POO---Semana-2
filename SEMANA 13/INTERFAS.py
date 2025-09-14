import tkinter as tk

# Crear una ventana
app = tk.Tk()
app.geometry('600x300')  # ancho x alto
app.title('Mi primera pagina')
app.configure(background='pink')

# Componente GUI - Nombre
label_nombre = tk.Label(app, text='INGRESE SU NOMBRE:', font=('Arial', 12))
label_nombre.pack(pady=10)
entrada_nombre = tk.Entry(app, font=('Arial', 12))
entrada_nombre.pack(pady=10)

# Componente GUI - Edad
label_edad = tk.Label(app, text='INGRESE SU EDAD:', font=('Arial', 12))
label_edad.pack(pady=10)
entrada_edad = tk.Entry(app, font=('Arial', 12))
entrada_edad.pack(pady=10)

# Función para el botón
def agregar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    print("Nombre ingresado:", nombre)
    print("Edad ingresada:", edad)
    entrada_nombre.delete(0, tk.END)  # limpiar nombre
    entrada_edad.delete(0, tk.END)    # limpiar edad

# Botón
btn_agregar = tk.Button(app, text='Agregar', font=('Arial', 12), bg='red', command=agregar)
btn_agregar.pack(pady=10)

app.mainloop()


