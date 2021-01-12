import pygame
from data.menus.menu import Menu
from data.util.controls import write_controls

class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.index, self.newline = 0, 30 
        self.cursor_rect.center =  (self.game.DISPLAY_W/2, self.game.DISPLAY_H/8 )
        self.states = {0 : "Left", 1 : "Right", 2 : "Up" , 3 : "Down", 4 : "Start", 5 : "Jump", 6 : "Run" }
        self.offset = -80

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            self.handle_input()
            self.game.display.fill((0,0,0))
            self.display_current_controls()
            self.draw_cursor()
            self.game.draw_screen()
            self.game.reset_keys()

    # Helper function to display current controls 
    def display_current_controls(self):
        i = 0
        for control in self.game.controls:
            self.draw_text(control + ':' + pygame.key.name(self.game.controls[control]),20, 
            (255,255,255), self.game.DISPLAY_W/2, self.game.DISPLAY_H/8 + i)
            i += self.newline

    # Helper Function to allow the player to select a new control
    def handle_input(self):
        self.move_cursor()
        self.cursor_rect.center = (self.game.DISPLAY_W/2, self.game.DISPLAY_H/8 + (self.index * self.newline) )
        if self.game.actions['run']:
                self.game.current_menu = self.game.options_menu
                self.run_display = False
        if self.game.actions['start']:
            self.set_new_control()

    # Helper function to set new control. Writes new control to json file
    def set_new_control(self):
        done = False
        while not done:
            self.game.display.fill((0,0,0))
            self.draw_text('Enter a New Key', 20, (255, 255, 255), self.game.DISPLAY_W / 2,self.game.DISPLAY_H / 4)
            for event in pygame.event.get():               
                if event.type == pygame.KEYDOWN:
                    self.game.controls[self.states[self.index]] = event.key
                    done = True
                    write_controls(self.game.controls)
            self.game.draw_screen()