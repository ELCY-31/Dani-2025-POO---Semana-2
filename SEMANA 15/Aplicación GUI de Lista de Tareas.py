import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Lista de Tareas")
        self.master.geometry("500x400")

        # Lista interna de tareas.
        self.tasks = []
        # Entrada de texto para poder escribir una nueva tarea
        self.task_entry = tk.Entry(master, font=("Arial", 12))
        self.task_entry.pack(pady=10, fill=tk.X, padx=10)
        self.task_entry.focus()
        # Vincular la tecla Enter para añadir tarea
        self.task_entry.bind("<Return>", self.add_task_event)

        # Botones
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Espacio para mostrar tareas
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=12)
        self.task_listbox.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

    # Funciones
    def add_task_event(self, event):
        """Añadir tarea al presionar Enter"""
        self.add_task()

    def add_task(self):
        """Añadir nueva tarea"""
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Aviso", "Por favor escribe una tarea antes de añadir.")
            return
        self.tasks.append({"text": task_text, "completed": False})
        self.refresh_listbox()
        self.task_entry.delete(0, tk.END)

    def complete_task_event(self, event):
        """Alternar completada al hacer doble clic"""
        self.complete_task()

    def complete_task(self):
        """Marcar tarea seleccionada como completada"""
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.refresh_listbox()
        except IndexError:
            messagebox.showinfo("Info", "Selecciona una tarea primero.")

    def delete_task(self):
        """Eliminar tarea seleccionada"""
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.refresh_listbox()
        except IndexError:
            messagebox.showinfo("Info", "Selecciona una tarea primero.")

    def refresh_listbox(self):
        """Actualizar el Listbox según la lista de tareas"""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_listbox.insert(tk.END, "✔" + task["text"])
            else:
                self.task_listbox.insert(tk.END, task["text"])

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
