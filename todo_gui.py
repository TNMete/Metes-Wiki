import tkinter as tk
from tkinter import messagebox


# To-Do-Liste mit GUI
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-Liste")
        self.root.geometry("400x500")

        # Liste der Aufgaben
        self.tasks = []

        # Eingabefeld für neue Aufgaben
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Button zum Hinzufügen von Aufgaben
        self.add_button = tk.Button(
            root,
            text="Aufgabe hinzufügen",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
        )
        self.add_button.pack(pady=5)

        # Liste der Aufgaben anzeigen
        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 14))
        self.task_listbox.pack(pady=10)

        # Button zum Löschen von Aufgaben
        self.delete_button = tk.Button(
            root,
            text="Aufgabe löschen",
            command=self.delete_task,
            bg="#F44336",
            fg="white",
            font=("Arial", 12),
        )
        self.delete_button.pack(pady=5)

        # Button zum Markieren als erledigt
        self.mark_button = tk.Button(
            root,
            text="Als erledigt markieren",
            command=self.mark_completed,
            bg="#FFC107",
            fg="black",
            font=("Arial", 12),
        )
        self.mark_button.pack(pady=5)

    def add_task(self):
        """Fügt eine Aufgabe zur Liste hinzu."""
        task = self.task_entry.get()
        if task.strip():  # Leere Eingaben ignorieren
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)  # Eingabefeld leeren
        else:
            messagebox.showwarning("Warnung", "Die Aufgabe darf nicht leer sein!")

    def delete_task(self):
        """Löscht die ausgewählte Aufgabe."""
        try:
            selected_index = self.task_listbox.curselection()[
                0
            ]  # Ausgewählten Index abrufen
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warnung", "Bitte wähle eine Aufgabe aus!")

    def mark_completed(self):
        """Markiert die ausgewählte Aufgabe als erledigt."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warnung", "Bitte wähle eine Aufgabe aus!")

    def update_task_list(self):
        """Aktualisiert die Anzeige der Aufgaben."""
        self.task_listbox.delete(0, tk.END)  # Liste leeren
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")


# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
