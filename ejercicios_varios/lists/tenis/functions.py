import random as rd

def create_points():
    return [rd.randint(0,100) for i in range(6)]

def create_players():
    return ["Anette", "Juan", "Pedro", "Omoplato", "Ruu", "Benjamin"]

def select_winner(array, points):
    pos = 0
    winner = rd.choice(array)
    for i in array:
        if i != winner:
            pos += 1
        else:
            pass
    points_selected = points[pos]
    print(f"El ganador es: {winner}, su puntuacion es {points_selected}")
    return winner

def main():

    points = create_points
    players = create_players
    select_winner(players, points)

if __name__ == "__main__":
    main()
 