import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import ttk

# === Paramètres par défaut ===
DEFAULT_NUM_CITIES = 20
DEFAULT_POP_SIZE = 100
DEFAULT_NUM_GENERATIONS = 200
DEFAULT_MUTATION_RATE = 0.01

class TSPGeneticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP - Algorithme Génétique Évolué")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        ttk.Label(root, text="Optimisation du Voyageur de Commerce", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        frm = ttk.Frame(root)
        frm.pack(pady=5)

        self.num_cities_var = tk.IntVar(value=DEFAULT_NUM_CITIES)
        self.pop_size_var = tk.IntVar(value=DEFAULT_POP_SIZE)
        self.num_gen_var = tk.IntVar(value=DEFAULT_NUM_GENERATIONS)
        self.mutation_rate_var = tk.DoubleVar(value=DEFAULT_MUTATION_RATE)

        self._create_labeled_entry(frm, "Nombre de villes :", self.num_cities_var)
        self._create_labeled_entry(frm, "Taille de population :", self.pop_size_var)
        self._create_labeled_entry(frm, "Nombre de générations :", self.num_gen_var)
        self._create_labeled_entry(frm, "Taux de mutation (0.0 - 1.0) :", self.mutation_rate_var)

        ttk.Button(root, text="Lancer la simulation", command=self.launch_simulation).pack(pady=20)

    def _create_labeled_entry(self, parent, label, variable):
        frame = ttk.Frame(parent)
        frame.pack(pady=3, fill='x')
        ttk.Label(frame, text=label, width=30).pack(side='left')
        ttk.Entry(frame, textvariable=variable, width=10).pack(side='right')

    def launch_simulation(self):
        num_cities = self.num_cities_var.get()
        pop_size = self.pop_size_var.get()
        num_gen = self.num_gen_var.get()
        mutation_rate = self.mutation_rate_var.get()

        cities = np.random.rand(num_cities, 2) * 100

        def calc_distance(path):
            return sum(np.linalg.norm(cities[path[i]] - cities[path[(i + 1) % num_cities]]) for i in range(num_cities))

        def init_population():
            return [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]

        def selection(pop, scores):
            idx = np.argsort(scores)
            return [pop[i] for i in idx[:pop_size // 2]]

        def crossover(p1, p2):
            a, b = sorted(random.sample(range(num_cities), 2))
            child = [-1]*num_cities
            child[a:b] = p1[a:b]
            pointer = b
            for i in range(num_cities):
                city = p2[(b + i) % num_cities]
                if city not in child:
                    child[pointer % num_cities] = city
                    pointer += 1
            return child

        def mutate(path):
            if random.random() < mutation_rate:
                a, b = random.sample(range(num_cities), 2)
                path[a], path[b] = path[b], path[a]
            return path

        def evolve(pop):
            scores = [calc_distance(p) for p in pop]
            selected = selection(pop, scores)
            children = []
            while len(children) < pop_size:
                p1, p2 = random.sample(selected, 2)
                children.append(mutate(crossover(p1, p2)))
            return children, min(scores), pop[np.argmin(scores)]

        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'o-', lw=2, color='tab:blue')
        title = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center", fontsize=13, color='tab:red')

        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)

        pop = init_population()
        best_path = pop[0]
        best_score = calc_distance(best_path)

        def init_plot():
            return line,

        def update_plot(frame):
            nonlocal pop, best_path, best_score
            pop, score, path = evolve(pop)
            if score < best_score:
                best_score = score
                best_path = path
            ordered = cities[best_path + [best_path[0]]]
            line.set_data(ordered[:, 0], ordered[:, 1])
            title.set_text(f"Génération: {frame+1} | Distance: {best_score:.2f}")
            return line, title

        ani = animation.FuncAnimation(fig, update_plot, frames=num_gen,
                                      init_func=init_plot, blit=True, repeat=False)
        plt.title("Optimisation TSP - Algorithme Génétique")
        plt.tight_layout()
        plt.show()

        # === Sauvegarde des résultats ===
        # 1. Image du trajet optimal
        fig_final, ax_final = plt.subplots()
        ax_final.set_title("Trajet optimal trouvé")
        ordered = cities[best_path + [best_path[0]]]
        ax_final.plot(ordered[:, 0], ordered[:, 1], 'o-', lw=2, color='green')
        for i, (x, y) in enumerate(cities):
            ax_final.text(x, y, str(i), fontsize=8, ha='right')
        ax_final.set_xlim(0, 100)
        ax_final.set_ylim(0, 100)
        fig_final.tight_layout()
        fig_final.savefig("trajet_optimal.png")

        # 2. Export CSV : coordonnées des villes et ordre du trajet
        import csv
        with open("trajet_optimal.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Ordre", "Ville", "X", "Y"])
            for i, city_index in enumerate(best_path):
                x, y = cities[city_index]
                writer.writerow([i+1, city_index, x, y])
            x, y = cities[best_path[0]]
            writer.writerow([len(best_path)+1, best_path[0], x, y])
        print("Résultats enregistrés : 'trajet_optimal.png' et 'trajet_optimal.csv'")

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPGeneticApp(root)
    root.mainloop()
