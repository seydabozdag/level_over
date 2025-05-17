import pygame
import sys
import os
from sprites import Player, Platform, Obstacle, Collectible ,Chest
from settings import *
try:
    from level import levels
except ImportError:
    print("Error: 'level' module or 'levels' object not found.")
    levels = []  # Provide a fallback or handle the error appropriately

class Game:
    def show_pause_screen(self):
        """Pause menüsü"""
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        resume = self.font.render("Resume", True, WHITE)
        restart = self.font.render("Restart Level", True, WHITE)
        main_menu = self.font.render("Main Menu", True, WHITE)

        resume_rect = resume.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
        restart_rect = restart.get_rect(center=(WIDTH//2, HEIGHT//2))
        main_menu_rect = main_menu.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))

        selected = "resume"

        paused = True
        while paused and self.paused:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    self.running = False
                    self.paused = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if selected == "resume": selected = "restart"
                        elif selected == "restart": selected = "main_menu"
                    elif event.key == pygame.K_UP:
                        if selected == "main_menu": selected = "restart"
                        elif selected == "restart": selected = "resume"
                    elif event.key == pygame.K_RETURN:
                        if selected == "resume":
                            self.paused = False
                            paused = False
                        elif selected == "restart":
                            self.deaths += 1
                            self.load_level(self.current_level)
                            self.paused = False
                            paused = False
                        elif selected == "main_menu":
                            self.paused = False
                            paused = False
                            self.playing = False
                            self.show_main_menu()

            # Seçimi renklendir
            resume = self.font.render("Resume", True, YELLOW if selected == "resume" else WHITE)
            restart = self.font.render("Restart Level", True, YELLOW if selected == "restart" else WHITE)
            main_menu = self.font.render("Main Menu", True, YELLOW if selected == "main_menu" else WHITE)

            self.screen.blit(overlay, (0, 0))
            self.screen.blit(resume, resume_rect)
            self.screen.blit(restart, restart_rect)
            self.screen.blit(main_menu, main_menu_rect)
            pygame.display.flip()

    def run(self):
        """Oyun döngüsü"""
        self.playing = True
        while self.playing:
            if self.paused:
                self.show_pause_screen()
            else:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

    def __init__(self):
        ...
        self.paused = False
      

    def show_main_menu(self):
        """Ana menü ekranı"""
        self.screen.blit(self.background, (0, 0))
        
        title = self.font.render("LEVEL DEVIL", True, RED)
        title = pygame.transform.scale(title, (title.get_width() * 2, title.get_height() * 2))
        start = self.font.render("Start Game", True, WHITE)
        exit_game = self.font.render("Exit", True, WHITE)
        
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//4))
        start_rect = start.get_rect(center=(WIDTH//2, HEIGHT//2))
        exit_rect = exit_game.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))

        selected = "start"

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected = "exit"
                    elif event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_RETURN:
                        if selected == "start":
                            waiting = False
                            self.new_game()  # <-- keep this
                        elif selected == "exit":
                            pygame.quit()
                            sys.exit()

            # Renk değişimleri ile seçim görseli
            if selected == "start":
                start = self.font.render("Start Game", True, YELLOW)
                exit_game = self.font.render("Exit", True, WHITE)
            else:
                start = self.font.render("Start Game", True, WHITE)
                exit_game = self.font.render("Exit", True, YELLOW)

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(start, start_rect)
            self.screen.blit(exit_game, exit_rect)
            pygame.display.flip()

    def __init__(self):
        pygame.init()
        pygame.mixer.init()  
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Level Over")
        self.clock = pygame.time.Clock()
        
        # Oyun değişkenleri
        self.running = True
        self.playing = False
        self.game_over = False
        self.current_level = 0
        self.score = 0
        self.deaths = 0
        
        # Font ayarları
        self.font = pygame.font.Font(None, 36)
        
        # Sprite grupları
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        
        # Arkaplan resmi
        self.background = pygame.image.load(os.path.join('assets', 'background.png')).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        
        # Ses efektleri
        self.jump_sound = pygame.mixer.Sound(os.path.join('assets', 'jump.wav'))
        self.death_sound = pygame.mixer.Sound(os.path.join('assets', 'death.wav'))
        self.collect_sound = pygame.mixer.Sound(os.path.join('assets', 'collect.wav'))
        
        self.collected_collectibles = {}  # {level_index: set of (x, y, type)}
        
    def new_game(self):
        """Yeni oyun başlatır"""
        self.score = 0
        self.deaths = 0
        self.current_level = 0 
        self.load_level(self.current_level)
        self.run()
    def load_level(self, level_index):
        """Seçilen seviyeyi yükler"""
        # Tüm grupları temizle
        self.all_sprites.empty()
        self.platforms.empty()
        self.obstacles.empty()
        self.collectibles.empty()
        
        # Seviye verilerini al
        level_data = levels[level_index]
        
        # Oyuncuyu oluştur
        self.player = Player(self, level_data['player_pos'])
        self.all_sprites.add(self.player)
        
        # Platformları oluştur
        for plat in level_data['platforms']:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            
        # Engelleri oluştur
        for obs in level_data['obstacles']:
            o = Obstacle(self, *obs)
            self.all_sprites.add(o)
            self.obstacles.add(o)
            
        # Toplanabilir öğeleri oluştur
        # for col in level_data['collectibles']:
        #     c = Collectible(*col)
        #     self.all_sprites.add(c)
        #     self.collectibles.add(c)
        already_collected = self.collected_collectibles.get(level_index, set())
        for x, y, ctype in level_data['collectibles']:
            if (x, y, ctype) not in already_collected:
                collectible = Collectible(x, y, ctype)
                self.all_sprites.add(collectible)
                self.collectibles.add(collectible)
            
        # # Bitiş noktasını ayarla
        self.finish_pos = level_data['finish_pos']

        # Bitiş sandığını oluştur
        self.chest = Chest(*level_data['finish_pos'])
        self.all_sprites.add(self.chest)
        
    def run(self):
        """Oyun döngüsü"""
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    def events(self):
        """Olayları işle"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                    self.player.jump()
                    self.jump_sound.play()
                if event.key == pygame.K_r:
                    # Seviyeyi yeniden başlat
                    self.deaths += 1
                    self.load_level(self.current_level)
                if event.key == pygame.K_ESCAPE:
                    # Oyunu durdur ve ana menüye dön
                    self.paused = not self.paused  # Sadece ESCAPE durumunda pause
                    self.playing = False
                    
    def update(self):
        """Oyun dünyasını güncelle"""
        self.all_sprites.update()
        
        # Oyuncu ile platform çarpışmalarını kontrol et
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                
                if self.player.pos.y < lowest.rect.centery:
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0
                    self.player.jumping = False
        
        # Oyuncu ile engel çarpışmalarını kontrol et
        hits = pygame.sprite.spritecollide(self.player, self.obstacles, False)
        if hits:
            self.death_sound.play()
            self.deaths += 1
            self.load_level(self.current_level)
            
        # Oyuncu ile toplanabilir öğe çarpışmalarını kontrol et
        hits = pygame.sprite.spritecollide(self.player, self.collectibles, True)
        for hit in hits:
            self.score += 10
            self.collect_sound.play()
    # Record collected collectible
            if self.current_level not in self.collected_collectibles:
                self.collected_collectibles[self.current_level] = set()
            self.collected_collectibles[self.current_level].add((hit.rect.x, hit.rect.y, "coin"))

            
        # # Bitiş noktasına ulaşmayı kontrol et
        # if abs(self.player.pos.x - self.finish_pos[0]) < 20 and abs(self.player.pos.y - self.finish_pos[1]) < 20:
        #     self.current_level += 1
        #     if self.current_level < len(levels):
        #         self.load_level(self.current_level)
        #     else:
        #         # Oyunu bitir
        #         self.game_over = True
        #         self.playing = False
                
         # Bitiş sandığına ulaşmayı kontrol et
        if abs(self.player.pos.x - self.finish_pos[0]) < 20 and abs(self.player.pos.y - self.finish_pos[1]) < 20:

            if self.chest.opened:  # Eğer sandık açıldıysa
                self.current_level += 1
            if self.current_level < len(levels):
                self.load_level(self.current_level)
            else:
                self.game_over = True
                self.playing = False

        # Oyuncu ile sandık çarpışmalarını kontrol et
        hits = pygame.sprite.spritecollide(self.player, [self.chest], False)
        if hits and not self.chest.opened:
            self.chest.opened = True
            self.current_level += 1
            if self.current_level < len(levels):
                self.load_level(self.current_level)
            else:
                # Oyunu bitir
                self.game_over = True
                self.playing = False



        # Ekrandan düşmeyi kontrol et
        if self.player.pos.y > HEIGHT:
            self.death_sound.play()
            self.deaths += 1
            self.load_level(self.current_level)
            
    def draw(self):
        """Ekranı çiz"""
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        
        # # Bitiş noktasını çiz
        # pygame.draw.rect(self.screen, GREEN, 
        #                  (self.finish_pos[0] - 15, self.finish_pos[1] - 15, 30, 30)) # burda 
        
                         
        # Skor ve ölüm sayısını göster
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        deaths_text = self.font.render(f"Deaths: {self.deaths}", True, WHITE)
        level_text = self.font.render(f"Level: {self.current_level + 1}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(deaths_text, (10, 50))
        self.screen.blit(level_text, (WIDTH - 120, 10))
        
        pygame.display.flip()
        
    def show_start_screen(self):
        """Başlangıç ekranını göster"""
        self.screen.blit(self.background, (0, 0))
        
        title = self.font.render("LEVEL DEVIL", True, RED)
        start_text = self.font.render("Press any key to start", True, WHITE)
        controls = self.font.render("Controls: Arrow keys to move, SPACE to jump, R to reset", True, WHITE)
        
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
        self.screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        self.screen.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT * 3 // 4))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    
    def show_game_over_screen(self):
        """Oyun sonu ekranını göster"""
        self.screen.blit(self.background, (0, 0))
        
        title = self.font.render("GAME OVER", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
        deaths_text = self.font.render(f"Total Deaths: {self.deaths}", True, BLACK)
        restart_text = self.font.render("Press any key to restart", True, WHITE)
        
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 30))
        self.screen.blit(deaths_text, (WIDTH // 2 - deaths_text.get_width() // 2, HEIGHT // 2 + 10))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT * 3 // 4))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    self.game_over = False

# Oyunu başlat
if __name__ == "__main__":
    game = Game()
    show_menu = True

    while game.running:
        if show_menu:
            game.show_main_menu()
            show_menu = False
        if game.game_over:
            game.show_game_over_screen()
            
            game.game_over = False
            show_menu = True  # Show menu after game over

    pygame.quit()
    sys.exit()