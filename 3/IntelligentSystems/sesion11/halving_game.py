"""
Halving Game
=================   

A simple game where two players take turns to either subtract 1 or halve a number.
The player who makes the number reach 0 wins.
"""

class HalvingGame():
    """
    A simple game where two players take turns to either subtract 1 or halve a number.
    The player who makes the number reach 0 wins.
    """
    def __init__(self, initial_number: int):
        self.n = initial_number
        self.current_player = 0

    def __str__(self):
        return f"HalvingGame(n={self.n})"

    def start_state(self):
        """
        Returns the initial state of the game.
        """
        return (+1, self.n)

    def actions(self, state):
        """
        Returns the possible actions for the current state.
        """
        _, _ = state
        return ['-', '/']

    def succ(self, state, action):
        """
        Returns the successor state after applying the action.
        """
        player, number = state
        if action == '-':
            return (-player, number - 1)
        if action == '/':
            return (-player, number // 2)
        raise ValueError("Invalid action")

    def is_end(self, state):
        """
        Returns True if the game is over, i.e., if the number is 0.
        """
        _, number = state
        return number == 0

    def utility(self, state):
        """
        Returns the utility of the game state.
        Returns +inf for player 0 and -inf for player 1.
        """
        player, _ = state
        assert self.is_end(state), "Game is not over"
        return player * float('inf')  # player 0 wins if number is 0, player 1 wins if number is 1

    def player(self, state):
        """
        Returns the player whose turn it is.
        """
        player, _ = state
        return player

def human_policy(game, state):
    """
    Returns the action chosen by the human player.
    """
    while True:
        print(f'Human Policy: enter move for state {state}', end=' ')
        action = input().strip()
        if action in game.actions(state):
            return action
        print("Invalid action, please try again.")

policies = {
    1:human_policy,
    -1:human_policy
}

def halving_game(initial_number: int, policy: callable = None):
    """
    Play the halving game with a given number initial_number and a policy for the players.
    """
    game = HalvingGame(initial_number)
    state = game.start_state()
    print(f'Starting game with initial state: {state}')

    while not game.is_end(state):
        player = game.player(state)
        action = policies[player](game, state) if policy is None else policy(game, state)
        state = game.succ(state, action)
        print(f"After action '{action}', new state: {state}")

    print(f"Game over! Final state: {state}, Utility: {game.utility(state)}")
    print("Player 0 wins!" if game.utility(state) > 0 else "Player 1 wins!")
    return game.utility(state)


if __name__ == "__main__":
    n = int(input("Enter the initial number for the game: "))
    halving_game(initial_number=n)
