import pygame,os

# Base Menu class. Inherit from this class to create new menus. Recommended that each menu gets its own file
class Menu():
    def __init__(self, game):
        self.game = game
        self.font_name = os.path.join(self.game.dir,"menus","november.ttf")
        self.font = pygame.font.Font(self.font_name, 20 )
        self.run_display = False
        self.cursor_img = self.font.render('*', True, (255,255,255))
        self.cursor_rect = self.cursor_img.get_rect()
        self.offset  = -50
        self.index, self.newline = 0,0
        self.states = {}
    
    # Override this function in your new menu class
    def display_menu(self):
        pass

    # Draws text to the screen    
    def draw_text(self, text, size, color, x, y):
        text_surface = self.font.render(text, True, color, size)
        text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.game.display.blit(text_surface, text_rect)

    # Draws a cursor to the screen. Currently just an *, can be customized
    def draw_cursor(self):
        self.game.display.blit(self.cursor_img, (self.cursor_rect.x + self.offset, self.cursor_rect.y) )

    # Function that moves the cursor up and down by the specified 'index' value.
    # Will reset after all the states have been traversed
    def move_cursor(self):
        if self.game.actions['brake']: # Move the Cursor Down
            self.index = (self.index + 1) % len(self.states)
        if self.game.actions['accel']: # Move the Cursor Down
            self.index = abs((self.index - 1) % len(self.states))
        self.cursor_rect.center = (self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 + (self.index * self.newline) )


        
