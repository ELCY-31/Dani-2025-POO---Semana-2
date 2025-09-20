import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaEventos:
    def __init__(self, ventana):
        self.root = ventana
        self.root.title("Agenda de Eventos")
        self.root.geometry("700x400")
        self.root.configure(bg="lightblue")

        # FRAME PRINCIPAL (Lista de eventos)
        frame_lista = tk.Frame(root, bg="white", bd=2, relief="groove")
        frame_lista.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # TreeView para mostrar eventos
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)
        self.tree.pack(side="left", fill="both", expand=True)
        # Encabezados
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Ajuste de tamaño de columnas
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=300, anchor="w")

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # FRAME DE ENTRADA DE DATOS
        frame_form = tk.Frame(root, bg="lightgrey", bd=2, relief="groove")
        frame_form.pack(side="top", fill="x", padx=10, pady=5)

        # Campo de Fecha con DatePicker
        tk.Label(frame_form, text="Fecha:", bg="lightgrey", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_form, date_pattern="dd/mm/yyyy")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Campo de Hora
        tk.Label(frame_form, text="Hora:", bg="lightgrey", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_form)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        # Campo de Descripción
        tk.Label(frame_form, text="Descripción:", bg="lightgrey", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(frame_form, width=40)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # MARCO DE BOTONES
        frame_botones = tk.Frame(root, bg="lightblue")
        frame_botones.pack(side="bottom", fill="x", pady=10)
        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", bg="green", fg="white", command=self.agregar_evento)
        btn_agregar.pack(side="left", padx=10)
        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", bg="red", fg="white", command=self.eliminar_evento)
        btn_eliminar.pack(side="left", padx=10)
        btn_salir = tk.Button(frame_botones, text="Salir", bg="gray", fg="white", command=root.quit)
        btn_salir.pack(side="right", padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpiar entradas
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            for item in seleccion:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaEventos(root)
    root.mainloop()
