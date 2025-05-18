# Oyun seviyeleri
from settings import *

"""
Her seviye için:
- player_pos: Oyuncunun başlangıç pozisyonu (x, y)
- platforms: Platform listesi (x, y, genişlik, yükseklik)
- obstacles: Engel listesi (x, y, genişlik, yükseklik)
- collectibles: Toplanabilir öğe listesi (x, y, tip)
- finish_pos: Bitiş noktası (x, y)
"""

levels = [
    # Level 1 - Basit Başlangıç
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, 100, 40),  # Zemin1
            (100, HEIGHT - 40, 100, 40),  # Zemin2
            (200, HEIGHT - 40, 100, 40),  # Zemin3
            (300, HEIGHT - 40, 100, 40),  # Zemin4
            (400, HEIGHT - 40, 100, 40),  # Zemin5
            (500, HEIGHT - 40, 100, 40),  # Zemin6
            (600, HEIGHT - 40, 100, 40),  # Zemin7
            (700, HEIGHT - 40, 100, 40),  # Zemin8
            (250, HEIGHT - 150, 100, 30),  # Platform 1
            (450, HEIGHT - 150, 100, 30),  # Platform 2
            (250, HEIGHT - 260, 100, 30),  # Platform 3
            (450, HEIGHT - 260, 100, 30),  # Platform 4
            (150, HEIGHT - 370, 100, 30),  # Platform 5
            (350, HEIGHT - 370, 100, 30),  # Platform 6
            (550, HEIGHT - 370, 100, 30),  # Platform 7
            (150, HEIGHT - 480, 100, 30),  # Platform 8
            (350, HEIGHT - 480, 100, 20),  # Platform 9
            (550, HEIGHT - 480, 100, 30),  # Platform 10
        ],
        'obstacles': [
            (380, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 1
            
            (380, HEIGHT - 390, 40, 20, 'spikes'),  # Engel 2
            
            
        ],
        'collectibles': [
            (295, HEIGHT - 180, "coin"),  # Para 1
            (495, HEIGHT - 180, "coin"),  # Para 2
            (295, HEIGHT - 290, "coin"),  # Para 3
            (495, HEIGHT - 290, "coin"),  # Para 4
            
            (195, HEIGHT - 400, "coin"),  # Para 5
            #(495, HEIGHT - 400, "coin"),  # Para 6
            (595, HEIGHT - 400, "coin"),  # Para 7
            
            (195, HEIGHT - 510, "coin"),  # Para 8
            (395, HEIGHT - 510, "coin"),  # Para 9
            (595, HEIGHT - 510, "coin"),  # Para 10
        ],
        'finish_pos': (WIDTH - 50, HEIGHT - 60)
    },
    
    # Level 2 - Zorlaşmaya Başlıyor
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, 100, 40),  # Zemin1
            (100, HEIGHT - 40, 100, 40),  # Zemin2
            (200, HEIGHT - 40, 100, 40),  # Zemin3
            (300, HEIGHT - 40, 100, 40),  # Zemin4
            (400, HEIGHT - 40, 100, 40),  # Zemin5
            (500, HEIGHT - 40, 100, 40),  # Zemin6
            (600, HEIGHT - 40, 100, 40),  # Zemin7
            (700, HEIGHT - 40, 100, 40),  # Zemin8
            
            
            (200, HEIGHT - 150, 80, 30),  # Platform 1
            (350, HEIGHT - 250, 80, 30),  # Platform 2
            (500, HEIGHT - 350, 80, 30),  # Platform 3
            (350, HEIGHT - 450, 80, 30),  # Platform 4
            (200, HEIGHT - 550, 80, 30),  # Platform 5
            (500, HEIGHT - 550, 80, 30),  # Platform 6
            
            
            (150, HEIGHT - 200, 40, 20),  # Platform 10
            (50, HEIGHT - 300, 40, 20),  # Platform 11
            (150, HEIGHT - 400, 40, 20),  # Platform 12
            (50, HEIGHT - 500, 40, 20),  # Platform 13
            (450, HEIGHT - 300, 40, 20),  # Platform 14
            (150, HEIGHT - 400, 40, 20),  # Platform 15
            (450, HEIGHT - 500, 40, 20),  # Platform 16
            (300, HEIGHT - 500, 40, 20),  # Platform 17
        ],
        'obstacles': [
            (300, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 1
            (450, HEIGHT - 320, 40, 20, 'spikes'),  # Engel 2
            (300, HEIGHT - 520, 40, 20, 'spikes'),  # Engel 3
            (450, HEIGHT - 520, 40, 20, 'spikes'),  # Engel 4
            (340, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 5
            (380, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 6
            (420, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 7
            (460, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 8
            (500, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 9
            (540, HEIGHT - 60, 40, 20, 'spikes'),  # Engel 10 
        ],
        'collectibles': [
            (235, HEIGHT - 180, "coin"),  # Para 1
            (385, HEIGHT - 280, "coin"),  # Para 2
            (535, HEIGHT - 380, "coin"),  # Para 3
            (385, HEIGHT - 480, "coin"),  # Para 4
            #(230, HEIGHT - 580, "coin"),  # Para 5
            (535, HEIGHT - 580, "coin"),  # Para 6
            
            (160, HEIGHT - 220, "coin"), # Para 7
            (60, HEIGHT - 320, "coin"), # Para 8
            (160, HEIGHT - 420, "coin"), # Para 9
            (60, HEIGHT - 520, "coin"), # Para 10
            (160, HEIGHT - 420, "coin"), # Para 12
            
            
        ],
        'finish_pos': (230, HEIGHT - 570)
    },
    
    # Level 3 - Level Devil Zorluk
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, 100, 40),  # Zemin1
            (100, HEIGHT - 40, 100, 40),  # Zemin2
            (200, HEIGHT - 40, 100, 40),  # Zemin3
            (300, HEIGHT - 40, 100, 40),  # Zemin4
            (400, HEIGHT - 40, 100, 40),  # Zemin5
            (500, HEIGHT - 40, 100, 40),  # Zemin6
            (600, HEIGHT - 40, 100, 40),  # Zemin7
            (700, HEIGHT - 40, 100, 40),  # Zemin8
            (100, HEIGHT - 250, 60, 20),  # Platform 1
            (250, HEIGHT - 250, 60, 20),  # Platform 2
            (400, HEIGHT - 250, 60, 20),  # Platform 3
            (550, HEIGHT - 250, 60, 20),  # Platform 4
            (700, HEIGHT - 250, 60, 20),  # Platform 5
            
            (150, HEIGHT - 300, 60, 20),  # Platform 6
            (300, HEIGHT - 300, 60, 20),  # Platform 7
            (450, HEIGHT - 300, 60, 20),  # Platform 8
            (600, HEIGHT - 300, 60, 20),  # Platform 9
            
            (50, HEIGHT - 450, 700, 20),  # Platform 10
        ],
        'obstacles': [
            (175, HEIGHT - 250, 60, 20, 'spikes'),  # Engel 1
            (325, HEIGHT - 250, 60, 20, 'spikes'),  # Engel 2
            (475, HEIGHT - 250, 60, 20, 'spikes'),  # Engel 3
            (625, HEIGHT - 250, 60, 20, 'spikes'),  # Engel 4
            
            (225, HEIGHT - 300, 60, 20, 'spikes'),  # Engel 5
            (375, HEIGHT - 300, 60, 20, 'spikes'),  # Engel 6
            (525, HEIGHT - 300, 60, 20, 'spikes'),  # Engel 7
            
            # Engelli yol parçaları
            (150, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 8
            (250, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 9
            (350, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 10
            (450, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 11
            (550, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 12
            (650, HEIGHT - 430, 50, 10, 'spikes'),  # Engel 13
        ],
        'collectibles': [
            (130, HEIGHT - 180, "coin"),  # Para 1
            (280, HEIGHT - 180, "coin"),  # Para 2
            (430, HEIGHT - 180, "coin"),  # Para 3
            (580, HEIGHT - 180, "coin"),  # Para 4
            (730, HEIGHT - 180, "coin"),  # Para 5
            
            (180, HEIGHT - 330, "coin"),  # Para 6
            (330, HEIGHT - 330, "coin"),  # Para 7
            (480, HEIGHT - 330, "coin"),  # Para 8
            (630, HEIGHT - 330, "coin"),  # Para 9
            
            # Hareket gerektiren paralar
            (200, HEIGHT - 480, "coin"),  # Para 10
            (300, HEIGHT - 480, "coin"),  # Para 11
            (400, HEIGHT - 480, "coin"),  # Para 12
            (500, HEIGHT - 480, "coin"),  # Para 13
            (600, HEIGHT - 480, "coin"),  # Para 14
        ],
        'finish_pos': (WIDTH - 50, HEIGHT - 480)
    },
    
    # Level 4 - Ekstrem Zorluk
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, 100, 40),  # Zemin1
            (100, HEIGHT - 40, 100, 40),  # Zemin2
            (200, HEIGHT - 40, 100, 40),  # Zemin3
            (300, HEIGHT - 40, 100, 40),  # Zemin4
            (400, HEIGHT - 40, 100, 40),  # Zemin5
            (500, HEIGHT - 40, 100, 40),  # Zemin6
            (600, HEIGHT - 40, 100, 40),  # Zemin7
            (700, HEIGHT - 40, 100, 40),  # Zemin8
            # Dikey platform yolu
            (150, HEIGHT - 120, 50, 20),
            (250, HEIGHT - 200, 50, 20),
            (150, HEIGHT - 280, 50, 20),
            (250, HEIGHT - 360, 50, 20),
            (150, HEIGHT - 440, 50, 20),
            
            # Hareketli platform izlenimi veren yapı
            (400, HEIGHT - 150, 40, 10),
            (460, HEIGHT - 190, 40, 10),
            (520, HEIGHT - 230, 40, 10),
            (580, HEIGHT - 270, 40, 10),
            (640, HEIGHT - 310, 40, 10),
            (700, HEIGHT - 350, 40, 10),
            
            # Üst platform
            (500, 100, 300, 20),
        ],
        'obstacles': [
            # Dikey engelleyiciler
            (200, HEIGHT - 170, 50, 10, 'spikes'),
            (200, HEIGHT - 310, 50, 10, 'spikes'),
            (200, HEIGHT - 410, 50, 10, 'spikes'),
            
            # Üst platform engelleri
            (550, 120, 10, 10, 'spikes'),
            (600, 120, 10, 10, 'spikes'),
            (650, 120, 10, 10, 'spikes'),
            (700, 120, 10, 10, 'spikes'),
            
            # Düşen tuzaklar
            (400, HEIGHT - 300, 20, 260, 'spikes'),  # Dikine duvarlar
            (700, HEIGHT - 250, 20, 210, 'spikes'),
            
            # Ölüm bölgesi
            (420, HEIGHT - 80, 280, 40, 'spikes'),  # Tuzak zemin
        ],
        'collectibles': [
            # Dikey yoldaki paralar
            (175, HEIGHT - 150, "coin"),
            (275, HEIGHT - 230, "coin"),
            (175, HEIGHT - 310, "coin"),
            (275, HEIGHT - 390, "coin"),
            (175, HEIGHT - 470, "coin"),
            
            # Hareketli platformdaki paralar
            (420, HEIGHT - 180, "coin"),
            (480, HEIGHT - 220, "coin"),
            (540, HEIGHT - 260, "coin"),
            (600, HEIGHT - 300, "coin"),
                        (660, HEIGHT - 340, "coin"),
                        (720, HEIGHT - 380, "coin")
                    ],
                    'finish_pos': (WIDTH - 50, HEIGHT - 480)
                }
            ]