""" 
Functions Rock-Paper-Scissors Game.
Player may choose to be a game participant or a spectator in a bot match.
"""
import random, time

def user_input() -> str:
    """Get user input."""
    player: str = input('Rock, Paper, Scissors GO!: ')
    # match input with hand signs and return an str value
    match player:
        case 'r' | 'R' | 'ROCK' | 'rock' :
            player = 'ROCK'
            return player
        case 'p' | 'P' | 'PAPER' | 'paper':
            player = 'PAPER'
            return player
        case 's' | 'S' | 'SCISSORS' | 'scissors':
            player = 'SCISSORS'
            return player
        case _:
            print('Invalid hand signal!')

def computer_input() -> str:
    """Generate random hand signs for computer player."""
    computer: int = random.randint(0,2)
    # match computer input with str signs and return case
    match computer:
        case 0:
            computer = 'ROCK'
            return computer
        case 1:
            computer = 'PAPER'
            return computer
        case 2:
            computer = 'SCISSORS'
            return computer


def referee(user_input: str = None, computer_input: str = None) -> int:
    """Create a referee to determine winner for each match.
    Retrun the score as a tuple."""

    match (user_input, computer_input):
        case ('ROCK', 'SCISSORS'):
            decision = 1, 0
            return decision
        case ('ROCK', 'PAPER'):
            decision = 0, 1
            return decision
        case ('PAPER', 'ROCK'):
            decision = 1, 0
            return decision
        case ('PAPER', 'SCISSORS'):
            decision = 0, 1
            return decision
        case ('SCISSORS', 'PAPER'):
            decision = 1, 0
            return decision
        case ('SCISSORS', 'ROCK'):
            decision = 0, 1
            return decision
        case ('ROCK', 'ROCK') | ('PAPER', 'PAPER') | ('SCISSORS', 'SCISSORS'):
            decision = 1, 1
            return decision
        case ( _ , 'ROCK') | ( _ , 'PAPER') | ( _ , 'SCISSORS'):
            decision = 0, 1
            return decision

def set_matches() -> int:
    """Create a function that determines the number of matches played.
    Return the number of matches as an int."""
    matches: int = input('Set number of matches: ')
    return int(matches)


def pundit(input1: int, input2: int) -> str:
    """Create a pundit who announces the signs that each player chooses in the match."""
    print(f"It's {input1} vs {input2}! ")


def scorer(player_score1: int, player_score2: int, mode: str, player_name: str) -> int:
    """Create an announcer that updates the score after each match."""
    if mode == '1':
        print(f"""Current scores: {player_name} > {player_score1} | {player_score2} < Ultron""")
    else:
        print(f"""Current scores: Ryu > {player_score1} | {player_score2} < Ken""")


def announce_winner(player_score1: int, player_score2: int, command: str, player_name: str) -> str:
    """Create an announcer that proclaims the winner when the number of matches concluded."""
    if player_score1 == player_score2:
        print(f"It's a DRAW!")
    elif command == '2':
        if (player_score1 < player_score2):
            print(f'Ken WINS!')
        else:
            print(f'Ryu WINS!')
    elif command == '1':
        if (player_score1 > player_score2):
            print(f'{player_name} WINS!')
        else:
            print(f'Ultron WINS!')


def round_girl(matches: int) -> str:
    """Create an announcer for each match."""
    print(f"Round {matches + 1}, FIGHT!")


def rock_paper_scissors_bot(command: str, player_name: str) -> None:
    """Create a match where the participants are bots."""
    # set number of matches
    matches = set_matches()
    print('Enjoy the game in spectator mode.')
    # set player scores to zero
    player1_score: int = 0
    player2_score: int = 0
    # loop over the number of matches
    for match in range(matches):
        # program announces match number
        round_girl(match)
        # players choose signs
        player1, player2  = computer_input(), computer_input()
        # pundit announces hands chosen
        pundit(player1, player2)
        # referee chooses winner
        decision =  referee(player1, player2)
        # scores are tallied
        player1_score += decision[0]
        player2_score += decision[1]
        # scorer are updated
        scorer(player1_score, player2_score, command, player_name)
        time.sleep(1)
        print()
    # winner is announced
    announce_winner(player1_score, player2_score, command, player_name)


def rock_paper_scissors_hum(command: str, player_name: str) -> None:
    """Create a match where the human battles a computer."""
    # set number of matches
    matches = set_matches()
    print('Get ready to play!')
    # set player scores to zero
    player1_score: int = 0
    player2_score: int = 0
    # loop over the number of matches
    for match in range(matches):
        # players choose hand
        round_girl(match)
        player1, player2  = user_input(), computer_input()
        # pundit announces hands chosen
        pundit(player1, player2)
        # referee chooses winner
        decision =  referee(player1, player2)
        # scores are tallied
        player1_score += decision[0]
        player2_score += decision[1]
        # scores are updated
        scorer(player1_score, player2_score, command, player_name)
        time.sleep(2)
        print()
    announce_winner(player1_score, player2_score, command, player_name)
    

def run_rock_paper_scissors(command: str, player_name: str) -> None:
    """Display user interface."""
    # match user options with cases
    match command:
        case '1':
            rock_paper_scissors_hum(command, player_name)
            print()
        case '2': 
            rock_paper_scissors_bot(command, player_name)
            print()
        case '3':
            print('Goodbye!')
            quit()
        case 'quit' | 'exit' | 'q':
            print('Goodbye!')
            quit()
        case _:
            print('Invalid game mode.')
    