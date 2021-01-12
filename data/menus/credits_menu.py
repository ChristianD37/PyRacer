import pygame
from data.menus.menu import Menu

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.credx, self.credy = self.game.DISPLAY_W/2, self.game.DISPLAY_H/4

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0, 0, 0))
            self.draw_text("Credits", 20, pygame.Color((255,255,255)), self.credx, self.credy)
            self.draw_text("Template by Christian Duenas", 14, pygame.Color((255,255,255)), self.credx, self.game.DISPLAY_H * .45)
            self.draw_text("\"November\" Font by Tepid Monkey Fonts", 14, pygame.Color((255,255,255)), self.credx, self.game.DISPLAY_H * .5 + 30)
            self.game.get_events()
            if self.game.actions['start'] or self.game.actions['run']:
                self.run_display = False
                self.game.current_menu = self.game.main_menu
            self.game.draw_screen()
            self.game.reset_keys()
        