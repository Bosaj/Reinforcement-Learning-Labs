import random
import time
import os

# Définir la grille avec le trésor à (3, 2)
grid = [
    ['S', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'T', '.', '.'],
    ['.', '.', '.', '.', '.']
]

# Actions possibles
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Récompenses
rewards = {'T': 10, '#': -10, '.': -1, 'S': -1}

# Paramètres du Q-learning
alpha = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
episodes = 100

# Table Q initialisée
Q = {(i, j): {action: 0 for action in actions} for i in range(len(grid)) for j in range(len(grid[0]))}

# Fonction pour choisir une action
def choose_action(state):
    return random.choice(actions) if random.uniform(0, 1) < epsilon else max(Q[state], key=Q[state].get)

# Fonction pour déplacer l'agent
def move(state, action):
    x, y = state
    if action == 'UP' and x > 0: return (x - 1, y)
    if action == 'DOWN' and x < len(grid) - 1: return (x + 1, y)
    if action == 'LEFT' and y > 0: return (x, y - 1)
    if action == 'RIGHT' and y < len(grid[0]) - 1: return (x, y + 1)
    return state  # Si déplacement invalide, rester sur place

# Fonction pour afficher la grille dans le terminal avec chemin en vert
def print_grid(agent_pos, path, episode):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    print(f"🌟 Épisode: {episode}\n")  # Afficher le numéro de l'épisode
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == agent_pos:
                print("\033[91m🤖\033[0m", end=" ")  # Afficher l'agent en rouge
            elif (i, j) in path:
                print("\033[92m⬜\033[0m", end=" ")  # Afficher le chemin en vert
            elif grid[i][j] == 'S':
                print("🏁", end=" ")  # Départ
            elif grid[i][j] == 'T':
                print("💰", end=" ")  # Trésor
            elif grid[i][j] == '#':
                print("💀", end=" ")  # Piège
            else:
                print("⬜", end=" ")  # Case vide
        print()
    time.sleep(0.1)  # Pause pour l'animation

# Apprentissage Q-learning avec affichage terminal
for episode in range(1, episodes + 1):
    state = (0, 0)
    total_reward = 0
    done = False
    path = []  # Stocker le chemin parcouru

    while not done:
        path.append(state)  # Ajouter la position actuelle au chemin
        action = choose_action(state)
        next_state = move(state, action)
        reward = rewards[grid[next_state[0]][next_state[1]]]
        total_reward += reward

        # Mise à jour Q-table
        Q[state][action] += alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][action])
        
        state = next_state
        print_grid(state, path, episode)  # Afficher la grille animée

        if grid[state[0]][state[1]] in ['T', '#']:  # Si trésor ou piège atteint
            done = True

    epsilon = max(epsilon_min, epsilon * epsilon_decay)  # Réduction de l'exploration

print("\n✅ Apprentissage terminé ! 🚀")
