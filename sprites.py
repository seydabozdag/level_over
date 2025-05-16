import pygame
import os
from settings import *
vec = pygame.math.Vector2

# class Chest(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.spritesheet = SpriteSheet(os.path.join('assets', 'chest.png'))  # Sandık sprite sheet

#         # Animasyon kareleri (örneğe göre ayarla)
#         self.frames = [
#             self.spritesheet.get_image(0, 0, 32, 32),   # kapalı
#             self.spritesheet.get_image(32, 0, 32, 32),  # açılıyor 1
#             self.spritesheet.get_image(64, 0, 32, 32),  # açılıyor 2
#             self.spritesheet.get_image(96, 0, 32, 32),  # tam açık
#         ]
        
#         self.image = self.frames[0]
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)

#         self.frame_index = 0
#         self.last_update = pygame.time.get_ticks()
#         self.opened = False

    # def update(self):
    #     """Sandık animasyonu"""
    #     if not self.opened:
    #         now = pygame.time.get_ticks()
    #         if now - self.last_update > 100:  # Her 100ms'de bir kare değiştir
    #             self.last_update = now
    #             self.frame_index += 1
    #             if self.frame_index >= len(self.frames):
    #                 self.frame_index = len(self.frames) - 1
    #                 self.opened = True
    #             self.image = self.frames[self.frame_index]

class SpriteSheet:
    """Sprite sheet sınıfı animasyonlar için"""
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        
    def get_image(self, x, y, width, height):
        """Sprite sheet'ten bir kare al"""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        
        # Sprite sheet yükleme
        self.spritesheet = SpriteSheet(os.path.join('assets', 'player_sheet.png'))
        
        # Animasyon kareleri
        self.standing_frames = [
            self.spritesheet.get_image(0, 0, 32, 32),
            self.spritesheet.get_image(32, 0, 32, 32),
            self.spritesheet.get_image(64, 0, 32, 32),
            self.spritesheet.get_image(96, 0, 32, 32)
        ]
        
        self.walk_frames_r = [
            self.spritesheet.get_image(0, 64, 32, 32),
            self.spritesheet.get_image(32, 64, 32, 32),
            self.spritesheet.get_image(64, 64, 32, 32),
            self.spritesheet.get_image(96, 64, 32, 32),
            self.spritesheet.get_image(128, 64, 32, 32),
            self.spritesheet.get_image(160, 64, 32, 32),
            self.spritesheet.get_image(192, 64, 32, 32),
            self.spritesheet.get_image(224, 64, 32, 32),
            self.spritesheet.get_image(0, 96, 32, 32),
            self.spritesheet.get_image(32, 96, 32, 32),
            self.spritesheet.get_image(64, 96, 32, 32),
            self.spritesheet.get_image(96, 96, 32, 32),
            self.spritesheet.get_image(128, 96, 32, 32),
            self.spritesheet.get_image(160, 96, 32, 32),
            self.spritesheet.get_image(192, 96, 32, 32),
            self.spritesheet.get_image(224, 96, 32, 32)
        ]
        
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))
            
        self.jump_frame = self.spritesheet.get_image(0, 64, 32, 32)
        
        self.jump_frames_r = [
            self.spritesheet.get_image(0, 160, 32, 32),
            self.spritesheet.get_image(32, 160, 32, 32),
            self.spritesheet.get_image(64, 160, 32, 32),
            self.spritesheet.get_image(96, 160, 32, 32),
            self.spritesheet.get_image(128, 160, 32, 32),
            self.spritesheet.get_image(160, 160, 32, 32),
            self.spritesheet.get_image(192, 160, 32, 32),
            self.spritesheet.get_image(224, 160, 32, 32),
        ]
        self.jump_frames_l = []
        for frame in self.jump_frames_r:
            self.jump_frames_l.append(pygame.transform.flip(frame, True, False))
        
        # Başlangıç karesi
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        
        # Hareket için vektör
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
        # Animasyon değişkenleri
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.facing_right = True
        
    def update(self):
        """Oyuncuyu güncelle"""
        self.animate()
        
        # Yerçekimi
        self.acc = vec(0, GRAVITY)
        
        # Tuş girişlerini kontrol et
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.facing_right = True
            
        # Sürtünme uygula
        self.acc.x += self.vel.x * PLAYER_FRICTION
        
        # Hareket denklemleri
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
            
        self.pos += self.vel + 0.5 * self.acc
        
        # Ekran sınırlarını kontrol et
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
            
        # Kordinatları güncelle
        self.rect.midbottom = self.pos
        
    def jump(self):
        """Karakter zıplama"""
        # Sadece bir platformun üzerinde iken zıplayabilir
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP
        
    def animate(self):
        """Karakter animasyonları"""
        now = pygame.time.get_ticks()
        
        # Yürüme animasyonu
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
            
        
        
        
        if self.jumping and self.walking:
            if now - self.last_update > 100:  # Her 100ms'de bir kare değiştir
                self.last_update = now
                self.current_frame = (self.current_frame +1 ) 
                
                if self.vel.x > 0 and self.current_frame<len(self.jump_frames_r):  # Sağa doğru
                    self.image = self.jump_frames_r[self.current_frame]
                elif self.current_frame<len(self.jump_frames_r):  # Sola doğru
                    self.image = self.jump_frames_l[self.current_frame]
                
                
                self.image = self.jump_frame
                if self.facing_right:
                    self.image = self.jump_frame
                else:
                    self.image = pygame.transform.flip(self.jump_frame, True, False)
                
            
        
        
        
        # Yürüme animasyonu
        if self.walking:
            if now - self.last_update > 100:  # Her 100ms'de bir kare değiştir
                self.last_update = now
                self.current_frame = (self.current_frame +1 ) % len(self.walk_frames_r)
                
                if self.vel.x > 0:  # Sağa doğru
                    self.image = self.walk_frames_r[self.current_frame]
                else:  # Sola doğru
                    self.image = self.walk_frames_l[self.current_frame]
                    
        # Dururken animasyon
        if not self.jumping and not self.walking:
            if now - self.last_update > 350:  # Her 350ms'de bir kare değiştir
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                
        # Zıplama animasyonu
        if self.jumping:
            if now - self.last_update > 75:  # Her 100ms'de bir kare değiştir
                self.last_update = now
                entered_frame = self.current_frame
                self.current_frame = (self.current_frame +1 ) % len(self.jump_frames_r)
                
                if self.vel.x > 0 and self.current_frame-entered_frame < len(self.jump_frames_r):  # Sağa doğru
                    self.image = self.jump_frames_r[self.current_frame]
                elif self.current_frame-entered_frame<len(self.jump_frames_r):  # Sola doğru
                    self.image = self.jump_frames_l[self.current_frame]
                else:
                    self.image = self.jump_frame
                    if self.facing_right:
                        self.image = self.jump_frame
                    else:
                        self.image = pygame.transform.flip(self.jump_frame, True, False)
            
        

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=PLATFORM_COLOR):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=RED):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Collectible(pygame.sprite.Sprite):

    def __init__(self, x, y, type="coin"):
        pygame.sprite.Sprite.__init__(self)
        
        # Sprite sheet yükleme
        self.spritesheet = SpriteSheet(os.path.join('assets', 'collectibles.png'))
        
        # Animasyon kareleri (para için)
        self.frames = [
            self.spritesheet.get_image(0, 0, 16, 16),
            self.spritesheet.get_image(16, 0, 16, 16),
            self.spritesheet.get_image(32, 0, 16, 16),
            self.spritesheet.get_image(48, 0, 16, 16)
        ]
        
        # Başlangıç karesi
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animasyon değişkenleri
        self.current_frame = 0
        self.last_update = 0
        
    def update(self):
        """Animasyonu güncelle"""
        now = pygame.time.get_ticks()
        
        # Animasyon
        if now - self.last_update > 200:  # Her 200ms'de bir kare değiştir
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]