import random
from typing import Tuple

def simulate_generalized_monty_hall(num_doors: int, num_simulations: int) -> Tuple[float, float]:
    """
    Simulates the generalized Monty Hall problem where Monty opens all losing doors
    except for the one with the prize and the one the player chose.

    Args:
        num_doors: The total number of doors in the simulation.
        num_simulations: The number of times to run the simulation.

    Returns:
        A tuple containing the winning percentages for switching and staying.
    """
    switch_wins = 0  # Count wins when we switch
    stay_wins = 0  # Count wins when we stay

    for _ in range(num_simulations):
        # Randomly place the prize behind one door
        prize_door = random.randint(0, num_doors - 1)
        
        # Player randomly chooses one door
        player_choice = random.randint(0, num_doors - 1)

        # Monty opens all non-prize doors that the player did not choose.
        # This leaves only two doors: the player's choice and one other.
        # This logic is much simpler and directly reflects the generalized problem.
        
        # Switching means choosing the one remaining unopened door
        # that is not your original choice.
        # This is guaranteed to be the prize door if your original choice was wrong.
        switched_choice = 0
        for door in range(num_doors):
            if door != player_choice and door != prize_door:
                # This door will be opened by Monty, so we can't switch to it.
                # In the generalized case, all of these doors are opened.
                pass
            elif door != player_choice:
                # This is the single door Monty leaves closed.
                switched_choice = door

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
    NUM_SIMULATIONS = 100000

    # (a) Classic Monty Hall Problem with 3 doors
    print(f"Simulating Generalized Monty Hall with 3 doors ({NUM_SIMULATIONS} simulations)...")
    switch_3, stay_3 = simulate_generalized_monty_hall(3, NUM_SIMULATIONS)
    print(f"Winning percentage by SWITCHING: {switch_3:.2f}% (Expected: 66.67%)")
    print(f"Winning percentage by STAYING:    {stay_3:.2f}% (Expected: 33.33%)\n")

    # (b) Variation with 4 doors
    print(f"Simulating Generalized Monty Hall with 4 doors ({NUM_SIMULATIONS} simulations)...")
    switch_4, stay_4 = simulate_generalized_monty_hall(4, NUM_SIMULATIONS)
    # The probability of winning by staying is 1/4.
    # The probability of winning by switching is 3/4.
    print(f"Winning percentage by SWITCHING: {switch_4:.2f}% (Expected: 75.00%)")
    print(f"Winning percentage by STAYING:    {stay_4:.2f}% (Expected: 25.00%)")
