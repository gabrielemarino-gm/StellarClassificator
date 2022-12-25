
import tkinter as tk
import pickle
import pandas as pd

# Crea la finestra principale
root = tk.Tk()
root.geometry("350x500+50+50")

label_g = tk.Label(root, text = "g:")
label_r = tk.Label(root, text = "r:")
label_i = tk.Label(root, text = "i:")
label_z = tk.Label(root, text = "z:")
label_specobjid = tk.Label(root, text = "specobjid:")
label_redshift = tk.Label(root, text = "redshift:")
label_plate = tk.Label(root, text = "plate:")
label_mjd = tk.Label(root, text = "mjd:")

entry_g = tk.Entry(root)
entry_r = tk.Entry(root)
entry_i = tk.Entry(root)
entry_z = tk.Entry(root)
entry_specobjid = tk.Entry(root)
entry_redshift = tk.Entry(root)
entry_plate = tk.Entry(root)
entry_mjd = tk.Entry(root)

# Posiziona la etichetta e il pulsante nella finestra
label_g.grid(row=0, column=0, pady=10, padx=10, sticky="e")
entry_g.grid(row=0, column=1)

label_r.grid(row=1, column=0, pady=10, padx=10, sticky="e")
entry_r.grid(row=1, column=1)

label_i.grid(row=2, column=0, pady=10, padx=10, sticky="e")
entry_i.grid(row=2, column=1)

label_z.grid(row=3, column=0, pady=10, padx=10, sticky="e")
entry_z.grid(row=3, column=1)

label_specobjid.grid(row=4, column=0, pady=10, padx=10)
entry_specobjid.grid(row=4, column=1)

label_redshift.grid(row=5, column=0, pady=10, padx=10)
entry_redshift.grid(row=5, column=1)

label_plate.grid(row=6, column=0, pady=10, padx=10)
entry_plate.grid(row=6, column=1)

label_mjd.grid(row=7, column=0, pady=10, padx=10)
entry_mjd.grid(row=7, column=1)

label_res = tk.Label(root)
label_res.grid(row=9, column=1, pady=10, padx=10)

def start():
    # Apri il file in modalità di lettura binaria
    with open('model.pkl', 'rb') as f:
        # Carica il modello dal file
        classifier = pickle.load(f)

    g = float(entry_g.get())
    r = float(entry_r.get())
    i = float(entry_i.get())
    z = float(entry_z.get())
    specobjid = float(entry_specobjid.get())
    redshift = float(entry_redshift.get())
    plate = float(entry_plate.get())
    mjd = float(entry_mjd.get())

    df = pd.DataFrame(
    {
        "g": [g],
        "r": [r],
        "i": [i],
        "z": [z],
        "specobjid": [specobjid],
        "redshift": [redshift],
        "plate": [plate],
        "mjd": [mjd]
    })

    y_pred = classifier.predict(df)

    if y_pred == 0:
        label_res.config(text="GALAXY")
    elif y_pred == 1:
        label_res.config(text="STAR")
    else:
        label_res.config(text="QUASAR")


def reset():
    entry_g.delete(0, tk.END)
    entry_r.delete(0, tk.END)
    entry_i.delete(0, tk.END)
    entry_z.delete(0, tk.END)
    entry_specobjid.delete(0, tk.END)
    entry_redshift.delete(0, tk.END)
    entry_plate.delete(0, tk.END)
    entry_mjd.delete(0, tk.END)
    label_res.config(text="")

# Crea un pulsante
buttonReset = tk.Button(root, text = "Reset", command=reset)
buttonStart = tk.Button(root, text = "Start", command=start)

buttonReset.grid(row=8, column=1, pady=10, padx=10, sticky="sw")
buttonStart.grid(row=8, column=1, pady=10, padx=10, sticky="se")


# Avvia il ciclo di eventi di Tkinter
root.mainloop()
