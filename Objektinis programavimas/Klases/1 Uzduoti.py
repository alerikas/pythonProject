import requests
import json
import random
import time
import tkinter as tk

class BairiuDialog(tk.Toplevel):
    def __init__(self, parent, pirmas, antras, stage):
        tk.Toplevel.__init__(self, parent)
        self.result = None
        self.title(stage)

        self.label = tk.Label(self, text=f"1. {pirmas}\n\n2. {antras}\n\nKuris bairis eina į {stage}?\n")
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Enter", command=self.submit)
        self.button.pack(padx=10, pady=10)

    def submit(self):
        self.result = self.entry.get()
        self.destroy()

class TurnyrasApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Bairių Turnyras")
        self.master.geometry("500x300")
        self.pack()

        self.info_label = tk.Label(self, text="Bairiai paruošti!")
        self.info_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Pradėti turnyrą", command=self.start_turnyras)
        self.start_button.pack(pady=10)

    def chuck_norris(self):
        r = requests.get('https://api.chucknorris.io/jokes/random')
        bairis = json.loads(r.text)
        juokelis = bairis['value']
        return juokelis

    def start_turnyras(self):
        self.start_button.config(state="disabled")

        dalyviai = [self.chuck_norris() for _ in range(8)]

        self.info_label.config(text="KETVIRTFINALIS")
        self.master.update()
        time.sleep(1)

        pusfinalis = self.stage(dalyviai, "pusfinalį", "PUSFINALIS")
        finalas = self.stage(pusfinalis, "finalą", "FINALAS")
        cempionas = self.stage(finalas, "čempionu", "ČEMPIONATAS")

        self.info_label.config(text=f"ČEMPIONAS: {cempionas[0]}")
        self.master.update()

    def stage(self, dalyviai, stage_name, stage_title):
        stage_list = []
        while dalyviai:
            pirmas, antras = dalyviai[:2]
            dalyviai = dalyviai[2:]

            choice_dialog = BairiuDialog(self.master, pirmas, antras, stage_title)
            verdiktas = choice_dialog.result

            if verdiktas == "1":
                stage_list.append(pirmas)
            elif verdiktas == "2":
                stage_list.append(antras)
            else:
                atsitiktinis = random.choice([pirmas, antras])
                stage_list.append(atsitiktinis)

        return stage_list


root = tk.Tk()
turnyras_app = TurnyrasApp(root)
turnyras_app.mainloop()