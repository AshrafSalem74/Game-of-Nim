import random

def game_Creation():
    """
    Generates a random numbers of piles for the nim game
    
    Returns: 
    Returns a list of integers that represents the number of piles total stones
    """
    piels_number = random.randint(2, 5)
    total_stones = random.randint(piels_number * 2 + 1, piels_number * 5)
    piles = [random.randint(1, total_stones - (piels_number - i))
             for i in range(piels_number)]
    return piles

def display_piles(piles):
    """
     Display the current state of the piles.

    Parameters:
    - piles (list): A list containing the number of stones in each pile.

    Prints the current state of each pile, showing the number of stones in each pile.
    """

    print("Current piles:")
    for i in range(len(piles)):
        print(f"Pile {i+1}: {piles[i]} stones")

def VS_Player(piles):
    """
    Asks the human player for a move.
    Parameters:
    - piles (list): A list representing the current state of the piles, where each element represents the number of stones in a pile.

    This function modifies the `piles` list in-place based on the player's move.
    """
    valid_input = False
    while not valid_input:
        pile_index = int(input("Enter the pile number (1 to {}): ".format(len(piles)))) - 1
        if 0 <= pile_index < len(piles):
            removed_stones = int(input("Enter the number of stones to remove: "))
            if 1 <= removed_stones <= piles[pile_index]:
                piles[pile_index] -= removed_stones
                print("You removed {} stones from the chosen pile {}.".format(removed_stones, pile_index + 1))
                valid_input = True
            else:
                print("Invalid number of stones. Please enter a number between 1 and {} Or it Cant be less than Zero".format(piles[pile_index]))
        else:
            print("Invalid pile number. Please enter a number between 1 and {} Or it Cant be less than Zero".format(len(piles)))


def calculateNimSum(piles):
    """
    Calculates the Nim sum of the current game state.
    Parameters:
    - piles (list): A list representing the current state of the piles, where each element represents the number of stones in a pile.

    Returns:
    - int: The Nim sum of the game state.

    The Nim sum is calculated by XORing the number of stones in each pile.
    """
    nim_sum = 0
    for stones in piles:
        nim_sum ^= stones
    return nim_sum

def findBestMove(piles):
    """
    Finds the best move using dynamic programming.
    """
    nim_sum = calculateNimSum(piles)

    #If nim_sum is 0, make a random move
    if nim_sum == 0:
        pile_index = random.randint(0, len(piles) - 1)
        while piles[pile_index] == 0:
            pile_index = random.randint(0, len(piles) - 1)
        removed_stones = random.randint(1, piles[pile_index])
        return pile_index, removed_stones

    #finds a pile and number of stones to remove such that nim_sum becomes 0
    for i in range(len(piles)):
        new_nim_sum = nim_sum ^ piles[i]
        if new_nim_sum < piles[i]:
            return i, piles[i] - new_nim_sum

    # If no such move is found, makes  a random move
    pile_index = random.randint(0, len(piles) - 1)
    while piles[pile_index] == 0:
        pile_index = random.randint(0, len(piles) - 1)
    removed_stones = random.randint(1, piles[pile_index])
    return pile_index, removed_stones

def VS_AI(piles):
    """
    Generates the AI's move.
    Parameters:
    - piles (list): A list representing the current state of the piles, where each element
                   represents the number of stones in a pile.

    Returns:
    - None

    This function modifies the `piles` list in-place based on the AI's move.
    """
    pile_index, removed_stones = findBestMove(piles)
    piles[pile_index] -= removed_stones
    print("AI removed {} stones from pile {}.".format(removed_stones, pile_index + 1))

def winner_check(piles):
    return all(stones == 0 for stones in piles)


def nim_game():
    print("Welcome to the Game of Nim!")
    player_mode = input("Choose player mode (player/computer): ")
    while player_mode not in ["player", "computer"]:
        print("Invalid mode. Please choose either 'player' or 'computer'.")
        player_mode = input("Choose player mode (player/computer): ")

    piles = game_Creation()
    current_player = 0

    while not winner_check(piles):
        display_piles(piles)
        if player_mode == "player" or current_player == 0:
            print(f"Player {current_player}'s turn")
            VS_Player(piles)
        else:
            print("Computer's turn")
            VS_AI(piles)
        current_player = (current_player + 1) % 2

    if player_mode == "player":
        if current_player == 0:
            print(f"Player 1 wins!")
        elif current_player == 1:
            print(f"Player 0 wins!")
            
    elif player_mode == "computer" and  current_player == 1:
        print("Congrates You Won")
    else:
        print("AI wins!")

if __name__ == "__main__":
    nim_game()