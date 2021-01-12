from data.menus.menu import Menu

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.states = {0 : "Volume", 1 : "Controls"}
        self.index, self.newline = 0, 40 
        self.cursor_rect.center = (self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 )

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            self.handle_input()
            self.game.display.fill((0,0,0))
            self.draw_text("Options", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H /4)
            self.draw_text("Volume", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 )
            self.draw_text("Controls", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + self.newline)
            self.draw_cursor()
            self.game.draw_screen()
            self.game.reset_keys()
    
    def handle_input(self):
        self.move_cursor()
        if self.game.actions['start']:
                if self.states[self.index] == "Volume":
                    print("Volume Menu")
                if self.states[self.index] == "Controls":
                    print("Controls Menu")
                    self.game.current_menu = self.game.controls_menu
                self.run_display = False
        if self.game.actions['run']:
                self.game.current_menu = self.game.main_menu
                self.run_display = False