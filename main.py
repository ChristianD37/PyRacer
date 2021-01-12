from data.gameFiles.game import Game

g = Game()

while g.running:
    # If the player is not playing the game, show the appropriate menu
    g.current_menu.display_menu()
    while g.playing:
        # Begin playing the game
        g.game_loop()