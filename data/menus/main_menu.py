from data.menus.menu import Menu

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.cursor_rect.center = (self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 )
        self.index = 0 
        self.states = {0 : "Start", 1 : "Options", 2 : "Credits"}
        self.newline = 40

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_dt()
            self.game.get_events()
            self.handle_input()
            self.game.display.fill((0,0,0))
            self.draw_text("Racing Game!", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/4)
            self.draw_text("Start", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/2)
            self.draw_text("Options", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + self.newline)
            self.draw_text("Credits", 40, (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + 2*self.newline)
            self.draw_cursor()
            self.game.draw_screen()
            self.game.reset_keys()
    
    def handle_input(self):
        self.move_cursor()
        if self.game.actions['start']:
                if self.states[self.index] == "Start":
                    self.run_display = False
                    self.game.playing = True
                elif self.states[self.index] == "Options":
                    self.game.current_menu = self.game.options_menu
                elif self.states[self.index] == "Credits":
                    self.game.current_menu = self.game.credits_menu
                self.run_display = False
                