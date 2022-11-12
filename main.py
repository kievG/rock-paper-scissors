import rpsmodules


def main() -> None:
    human_player_name: str = input("> Enter your name: ")
    print()
    """Main function."""
    print("""Choose game mode: 
            1 human vs computer
            2 computer vs computer
            3 Quit game.""")
    print()
    while True:
        try:
            command: str = input("> Enter game mode: ")
            rpsmodules.run_rock_paper_scissors(command, human_player_name)

        except ValueError as e:
            pass

if __name__ == "__main__":
    main()