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
            (0, HEIGHT - 40, WIDTH, 40),  # Zemin
            (300, HEIGHT - 200, 100, 20),  # Platform 1
            (500, HEIGHT - 300, 100, 20),  # Platform 2
        ],
        'obstacles': [
            (400, HEIGHT - 60, 40, 20),  # Engel 1
        ],
        'collectibles': [
            (350, HEIGHT - 230, "coin"),  # Para 1
            (550, HEIGHT - 330, "coin"),  # Para 2
        ],
        'finish_pos': (WIDTH - 50, HEIGHT - 60)
    },
    
    # Level 2 - Zorlaşmaya Başlıyor
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, WIDTH, 40),  # Zemin
            (200, HEIGHT - 150, 80, 20),  # Platform 1
            (350, HEIGHT - 250, 80, 20),  # Platform 2
            (500, HEIGHT - 350, 80, 20),  # Platform 3
            (350, HEIGHT - 450, 80, 20),  # Platform 4
            (200, HEIGHT - 550, 80, 20),  # Platform 5
        ],
        'obstacles': [
            (300, HEIGHT - 60, 40, 20),  # Engel 1
            (450, HEIGHT - 370, 40, 20),  # Engel 2
            (300, HEIGHT - 470, 40, 20),  # Engel 3
        ],
        'collectibles': [
            (230, HEIGHT - 180, "coin"),  # Para 1
            (380, HEIGHT - 280, "coin"),  # Para 2
            (530, HEIGHT - 380, "coin"),  # Para 3
            (380, HEIGHT - 480, "coin"),  # Para 4
            (230, HEIGHT - 580, "coin"),  # Para 5
        ],
        'finish_pos': (200, HEIGHT - 580)
    },
    
    # Level 3 - Level Devil Zorluk
    {
        'player_pos': (50, HEIGHT - 100),
        'platforms': [
            (0, HEIGHT - 40, WIDTH, 40),  # Zemin
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
            (175, HEIGHT - 250, 60, 20),  # Engel 1
            (325, HEIGHT - 250, 60, 20),  # Engel 2
            (475, HEIGHT - 250, 60, 20),  # Engel 3
            (625, HEIGHT - 250, 60, 20),  # Engel 4
            
            (225, HEIGHT - 300, 60, 20),  # Engel 5
            (375, HEIGHT - 300, 60, 20),  # Engel 6
            (525, HEIGHT - 300, 60, 20),  # Engel 7
            
            # Engelli yol parçaları
            (150, HEIGHT - 430, 50, 10),  # Engel 8
            (250, HEIGHT - 430, 50, 10),  # Engel 9
            (350, HEIGHT - 430, 50, 10),  # Engel 10
            (450, HEIGHT - 430, 50, 10),  # Engel 11
            (550, HEIGHT - 430, 50, 10),  # Engel 12
            (650, HEIGHT - 430, 50, 10),  # Engel 13
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
            (0, HEIGHT - 40, WIDTH, 40),  # Zemin
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
            (200, HEIGHT - 170, 50, 10),
            (200, HEIGHT - 310, 50, 10),
            (200, HEIGHT - 410, 50, 10),
            
            # Üst platform engelleri
            (550, 120, 10, 10),
            (600, 120, 10, 10),
            (650, 120, 10, 10),
            (700, 120, 10, 10),
            
            # Düşen tuzaklar
            (400, HEIGHT - 300, 20, 260),  # Dikine duvarlar
            (700, HEIGHT - 250, 20, 210),
            
            # Ölüm bölgesi
            (420, HEIGHT - 80, 280, 40),  # Tuzak zemin
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