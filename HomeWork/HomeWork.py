import random

# Définir la grille avec le trésor à (3, 2)
grid = [
    ['S', '°', '°', '°', '°'],  # Ligne 0
    ['°', '#', '°', '#', '°'],  # Ligne 1
    ['°', '°', '°', '°', '°'],  # Ligne 2
    ['°', '°', 'T', '°', '°'],  # Ligne 3 (trésor à (3, 2))
    ['°', '°', '°', '°', '°']   # Ligne 4
]

# Définir les actions possibles
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Définir les récompenses
rewards = {
    'T': 10,  # Trésor
    '#': -10,  # Piège
    '°': -1,   # Déplacement normal
    'S': -1    # Départ
}

# Paramètres de la simulation
episodes = 1000  # Nombre d'épisodes

# Fonction pour effectuer un déplacement
def move(state, action):
    x, y = state
    if action == 'UP' and x > 0:
        return (x - 1, y)
    elif action == 'DOWN' and x < len(grid) - 1:
        return (x + 1, y)
    elif action == 'LEFT' and y > 0:
        return (x, y - 1)
    elif action == 'RIGHT' and y < len(grid[0]) - 1:
        return (x, y + 1)
    return (x, y)  # Si le déplacement est invalide, rester sur place

# Statistiques pour suivre les résultats
stats = {
    'treasure_found': 0,
    'trap_fallen': 0,
    'total_reward': 0
}

# Boucle de simulation
for episode in range(episodes):
    state = (0, 0)  # État initial (départ)
    total_reward = 0
    done = False

    while not done:
        action = random.choice(actions)  # Choisir une action aléatoire
        next_state = move(state, action)  # Effectuer le déplacement
        reward = rewards[grid[next_state[0]][next_state[1]]]  # Obtenir la récompense
        total_reward += reward

        state = next_state  # Passer à l'état suivant

        # Vérifier si l'épisode est terminé (trésor ou piège atteint)
        if grid[state[0]][state[1]] == 'T':
            stats['treasure_found'] += 1
            done = True
        elif grid[state[0]][state[1]] == '#':
            stats['trap_fallen'] += 1
            done = True

    # Mettre à jour les statistiques
    stats['total_reward'] += total_reward

    # Afficher les résultats périodiquement
    if (episode + 1) % 100 == 0:
        print(f"Épisode {episode + 1}, Récompense totale : {total_reward}")

# Afficher la grille
print("\nGrille :")
for row in grid:
    print(" ".join(row))

# Afficher les statistiques finales
print("\nStatistiques finales :")
print(f"Trésors trouvés : {stats['treasure_found']}")
print(f"Pièges tombés : {stats['trap_fallen']}")
print(f"Récompense totale moyenne par épisode : {stats['total_reward'] / episodes:.2f}")