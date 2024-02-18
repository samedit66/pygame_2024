import pygame 


class Game:
    
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 600 
        self.WINDOW_HEIGHT = 600
        self.FPS = 60 

        self.main_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.running = True
        

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return 

    def update_game_state(self):   
        pass 

    def render(self):
        pass

    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(self.FPS)
        pygame.quit()    

        
game = Game()
game.game_loop()