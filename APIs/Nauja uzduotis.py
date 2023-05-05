import time
import tkinter as tk
import requests
import json
import random


class TurnyrasApp(tk.Frame):
    def __init__(self, kazkas=None):
        super().__init__(kazkas)
        self.kazkas = kazkas
        self.padetis()
        self.mygtukai()

    def create_widgets(self):
        self.pradzios_mygtukas = tk.Button(self, text="Pradeti Turnyra", command=self.turnyro_pradzia)
        self.pradzios_mygtukas.padetis(row=0, column=0, padx=100, pady=50)

    def chuck_norris(self):
        r = requests.get('https://api.chucknorris.io/jokes/random')
        bairis = json.loads(r.text)
        juokelis = bairis['value']
        return juokelis

    def turnyro_pradzia(self):
        dalyviai = [self.chuck_norris() for _ in range(8)]

        ketvirtfinalis = self.pradeti("KETVIRTFINALIS", dalyviai, 4)
        pusfinalis = self.pradeti("PUSFINALIS", ketvirtfinalis, 2)
        finalas = self.pradeti("FINALAS", pusfinalis, 1)

        winner = finalas[0]
        self.show_winner(winner)

    def pradeti(self, stage_name, dalyviai, num_matches):
        stage_list = []
        for i in range(num_matches):
            match_title = f"{stage_name} {i + 1}"
            self.master.title(match_title)
            pirmas, antras = dalyviai[0], dalyviai[1]

            chosen_winner = self.match(match_title, pirmas, antras)

            stage_list.append(chosen_winner)
            dalyviai = dalyviai[2:]

        return stage_list

    def match(self, match_title, pirmas, antras):
        match_window = tk.Toplevel(self.master)
        match_window.title(match_title)

        options = [f"1. {pirmas}", f"2. {antras}"]

        for index, option in enumerate(options):
            label = tk.Label(match_window, text=option)
            label.grid(row=index, column=0, padx=100, pady=50)

        result_var = tk.StringVar()
        result_entry = tk.Entry(match_window, textvariable=result_var)
        result_entry.grid(row=2, column=0, padx=100, pady=50)

        submit_button = tk.Button(match_window, text="Submit", command=match_window.destroy)
        submit_button.grid(row=3, column=0, padx=100, pady=50)

        self.wait_window(match_window)

        choice = result_var.get()
        if choice == "1":
            return pirmas
        elif choice == "2":
            return antras
        else:
            return random.choice([pirmas, antras])

    def show_winner(self, winner):
        winner_window = tk.Toplevel(self.master)
        winner_window.title("Laimetojas")

        winner_label = tk.Label(winner_window, text=f"Laimetojas yra: {winner}")
        winner_label.grid(row=0, column=0, padx=100, pady=50)

        ok_button = tk.Button(winner_window, text="Gerai", command=winner_window.destroy)
        ok_button.grid(row=1, column=0, padx=100, pady=50)

        self.wait_window(winner_window)
        time.sleep(4)
        exit()


root = tk.Tk()
turnyras_app = TurnyrasApp(root)
turnyras_app.mainloop()