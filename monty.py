import random

def simulate_monty_hall(num_doors, num_simulations):
    """
    Simulates the Monty Hall problem for a given number of doors.

    Args:
        num_doors (int): The total number of doors in the game.
        num_simulations (int): The number of times to run the simulation.

    Returns:
        tuple: A tuple containing the win percentage for switching
               and the win percentage for staying.
    """
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_simulations):
        # Set up the doors. Doors are represented by numbers from 0 to num_doors-1.
        # Randomly choose one door to have the prize.
        prize_door = random.randint(0, num_doors - 1)
        
        # Contestant makes their initial choice.
        player_choice = random.randint(0, num_doors - 1)

        # Monty needs to open a door that is not the player's choice and not the prize door.
        # Create a list of doors Monty can open.
        monty_options = []
        for i in range(num_doors):
            if i != player_choice and i != prize_door:
                monty_options.append(i)
        
        # Monty opens one of the available doors.
        # In the 3-door problem, there's sometimes only one choice for Monty.
        # In problems with more doors, he picks one at random from the options.
        monty_opens = random.choice(monty_options)

        # The player is given the option to switch.
        # Find the door(s) the player can switch to.
        # It's any door that isn't their original choice and isn't the one Monty opened.
        switch_options = []
        for i in range(num_doors):
            if i != player_choice and i != monty_opens:
                switch_options.append(i)
        
        # For the 3-door problem, there is only one door to switch to.
        # For problems with more doors, the player would pick one of the remaining doors.
        switched_choice = random.choice(switch_options)

        # --- Tally the results ---
        
        # Check if the player would win by switching.
        if switched_choice == prize_door:
            switch_wins += 1
            
        # Check if the player would win by staying with their original choice.
        if player_choice == prize_door:
            stay_wins += 1
            
    # Calculate percentages
    switch_win_percentage = (switch_wins / num_simulations) * 100
    stay_win_percentage = (stay_wins / num_simulations) * 100
    
    return switch_win_percentage, stay_win_percentage


if __name__ == "__main__":
    NUM_SIMULATIONS = 10000

    # --- Part (a): Classic 3-Door Problem ---
    print(f"(a) Simulating the classic Monty Hall problem with 3 doors for {NUM_SIMULATIONS} iterations...")
    
    three_door_switch, three_door_stay = simulate_monty_hall(num_doors=3, num_simulations=NUM_SIMULATIONS)
    
    print(f"\nResults for 3 Doors:")
    print(f"  Winning percentage by SWITCHING: {three_door_switch:.2f}%")
    print(f"  Winning percentage by NOT SWITCHING: {three_door_stay:.2f}%")
    print("\n" + "="*50 + "\n")

    # --- Part (b): 4-Door Variation ---
    print(f"(b) Simulating the Monty Hall problem with 4 doors for {NUM_SIMULATIONS} iterations...")
    print("    (Prize is behind one door, Monty opens one goat door)")

    four_door_switch, four_door_stay = simulate_monty_hall(num_doors=4, num_simulations=NUM_SIMULATIONS)

    print(f"\nResults for 4 Doors:")
    print(f"  Winning percentage by SWITCHING: {four_door_switch:.2f}%")
    print(f"  Winning percentage by NOT SWITCHING: {four_door_stay:.2f}%")
