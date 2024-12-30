import tkinter as tk
import os

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        if expression == "100+612":
            trigger_easter_egg()
        else:
            try:
                result = eval(expression)
                log.append(f"{expression} = {result}")
                update_log()
                screen_var.set(result)
                expression = str(result)
            except Exception as e:
                screen_var.set("Erreur")
                expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

def update_log():
    """Met à jour la zone de log."""
    log_text.config(state="normal")  # Activer la zone de texte pour la mise à jour
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, "\n".join(log))
    log_text.config(state="disabled")  # Désactiver la zone de texte après la mise à jour

def clear_log():
    """Efface l'historique des calculs."""
    log.clear()
    update_log()

def trigger_easter_egg():
    """Déclenche l'easter egg : exécute une commande dans le terminal."""
    if os.name == "nt":  # Système Windows
        os.system("start cmd /k curl ASCII.live/can-you-hear-me")
    elif os.name == "posix":  # Systèmes Unix/Linux/Mac
        os.system("xterm -e curl ASCII.live/can-you-hear-me")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")
root.geometry("400x550")
root.resizable(False, False)

expression = ""
log = []  # Liste pour stocker l'historique des calculs
screen_var = tk.StringVar()

# Écran de la calculatrice
screen = tk.Entry(root, textvar=screen_var, font="Arial 30 bold", justify="right")
screen.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10)

# Boutons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15 bold", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Log des calculs
log_label = tk.Label(root, text="Historique des calculs :", font="Arial 12 bold")
log_label.pack(anchor="w", padx=10)

log_text = tk.Text(root, height=8, font="Arial 12", state="disabled", bg="#f0f0f0")
log_text.pack(fill=tk.BOTH, padx=10, pady=10)

# Bouton pour effacer les logs
clear_log_button = tk.Button(root, text="Effacer les logs", font="Arial 12 bold", command=clear_log, bg="red", fg="white")
clear_log_button.pack(pady=10)

root.mainloop()
