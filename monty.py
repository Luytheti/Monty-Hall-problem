import random 

def simulate_monty_hall(num_doors, num_simulations):
    switch_wins = 0   # Count wins when we switch
    stay_wins = 0     # Count wins when we stay

    for _ in range(num_simulations):
        # Randomly place the prize behind one door
        prize_door = random.randint(0, num_doors - 1)
        
        # Player randomly chooses one door
        player_choice = random.randint(0, num_doors - 1)

        # Monty chooses a door to open (not the player’s, not the prize)
        monty_options = [i for i in range(num_doors) if i != player_choice and i != prize_door]
        monty_opens = random.choice(monty_options)

        # Switching means: choose another door that is not your original choice 
        # and not the one Monty opened
        switch_options = [i for i in range(num_doors) if i != player_choice and i != monty_opens]
        switched_choice = random.choice(switch_options)

        # Check results
        if switched_choice == prize_door:
            switch_wins += 1
        if player_choice == prize_door:
            stay_wins += 1

    # Convert counts to percentages
    switch_win_percentage = (switch_wins / num_simulations) * 100
    stay_win_percentage = (stay_wins / num_simulations) * 100
    
    return switch_win_percentage, stay_win_percentage


# ---------------- MAIN ----------------
if __name__ == "__main__":
    NUM_SIMULATIONS = 10000

    # (a) Classic Monty Hall Problem with 3 doors
    print(f"Simulating Monty Hall with 3 doors ({NUM_SIMULATIONS} simulations)...")
    switch_3, stay_3 = simulate_monty_hall(3, NUM_SIMULATIONS)
    print(f"Winning percentage by SWITCHING: {switch_3:.2f}%")
    print(f"Winning percentage by STAYING:   {stay_3:.2f}%\n")

    # (b) Variation with 4 doors
    print(f"Simulating Monty Hall with 4 doors ({NUM_SIMULATIONS} simulations)...")
    switch_4, stay_4 = simulate_monty_hall(4, NUM_SIMULATIONS)
    print(f"Winning percentage by SWITCHING: {switch_4:.2f}%")
    print(f"Winning percentage by STAYING:   {stay_4:.2f}%")
