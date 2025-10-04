import tkinter as tk
from tkinter import ttk, messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Ingreso de nueva tarea.
        label = tk.Label(root, text="Ingrese una nueva tarea:", font=("Arial", 12), bg="#f0f0f0")
        label.pack(pady=(10, 0))

        self.entry_tarea = tk.Entry(root, width=45, font=("Arial", 12))
        self.entry_tarea.pack(pady=5)
        self.entry_tarea.focus_set()

        # Botones
        frame_botones = tk.Frame(root, bg="#f0f0f0")
        frame_botones.pack(pady=5)

        btn_agregar = tk.Button(frame_botones, text="Añadir", width=12, command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_completar = tk.Button(frame_botones, text="Marcar Completada", width=15, command=self.marcar_completada)
        btn_completar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=12, command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.tree = ttk.Treeview(root, columns=("Tarea"), show="headings")
        self.tree.heading("Tarea", text="Tareas pendientes")
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Estilos para diferenciar tareas
        self.tree.tag_configure("pendiente", background="white")
        self.tree.tag_configure("completada", background="khaki")

        # Eventos
        self.entry_tarea.bind("<Return>", lambda e: self.agregar_tarea())     # ENTER para agregar una tarea
        self.root.bind("<c>", lambda e: self.marcar_completada())             # C para marcar completada la tarea
        self.root.bind("<d>", lambda e: self.eliminar_tarea())                # D para eliminar tarea
        self.root.bind("<Escape>", lambda e: self.root.destroy())             # Esc para salir

        # Doble clic para marcar o desmarcar
        self.tree.bind("<Double-1>", self.alternar_estado)

    # Funciones principales
    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tree.insert("", "end", values=(tarea,), tags=("pendiente",))
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingresar una tarea antes de añadirla.")

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.item(item, tags=("completada",))
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcarla como completada.")

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.delete(item)
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

    def alternar_estado(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            etiquetas = self.tree.item(item, "tags")
            if "completada" in etiquetas:
                self.tree.item(item, tags=("pendiente",))
            else:
                self.tree.item(item, tags=("completada",))

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
