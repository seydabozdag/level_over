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
            
            (100, HEIGHT - 150, 60, 30),  # Platform 1            
            (250, HEIGHT - 150, 60, 20),  # Platform 2            
            (400, HEIGHT - 150, 60, 30),  # Platform 3            
            (550, HEIGHT - 150, 60, 20),  # Platform 4            
            (700, HEIGHT - 150, 60, 30),  # Platform 5
            
            (25, HEIGHT - 150, 60, 30),  # Spike Platform X
            (175, HEIGHT - 150, 60, 30),  # Spike Platform 1 
            (325, HEIGHT - 150, 60, 30),  # Spike Platform 2
            (475, HEIGHT - 150, 60, 30),  # Spike Platform 3
            (625, HEIGHT - 150, 60, 30),  # Spike Platform 4
            
            
            (100, HEIGHT - 260, 60, 30),  # Spike Platform 6            
            (250, HEIGHT - 260, 60, 20),  # Spike Platform 7            
            (400, HEIGHT - 260, 60, 30),  # Spike Platform 8            
            (550, HEIGHT - 260, 60, 20),  # Spike Platform 9            
            (700, HEIGHT - 260, 60, 30),  # Spike Platform 10
            
            (25, HEIGHT -  260, 60, 20),   # Platform 6
            (175, HEIGHT - 260, 60, 30),  # Platform 7 
            (325, HEIGHT - 260, 60, 20),  # Platform 8
            (475, HEIGHT - 260, 60, 30),  # Platform 9
            (625, HEIGHT - 260, 60, 20),  # Platform 10
            

            
            (100, HEIGHT - 370, 60, 30),  # Spike Platform 6            
            (250, HEIGHT - 370, 60, 20),  # Spike Platform 7            
            (400, HEIGHT - 370, 60, 20),  # Spike Platform 8            
            (550, HEIGHT - 370, 60, 30),  # Spike Platform 9            
            (700, HEIGHT - 370, 60, 20),  # Spike Platform 10
            
            (25, HEIGHT -  370, 60, 20),   # Platform 6
            (175, HEIGHT - 370, 60, 30),  # Platform 7 
            (325, HEIGHT - 370, 60, 30),  # Platform 8
            (475, HEIGHT - 370, 60, 20),  # Platform 9
            (625, HEIGHT - 370, 60, 30),  # Platform 10
            
            (50, HEIGHT - 480, 100,  40),  # Platform 10
            (150, HEIGHT - 480, 100, 40),  # Platform 11
            (250, HEIGHT - 480, 100, 40),  # Platform 12
            (350, HEIGHT - 480, 100, 40),  # Platform 13
            (450, HEIGHT - 480, 100, 40),  # Platform 14
            (550, HEIGHT - 480, 100, 40),  # Platform 15
            (650, HEIGHT - 480, 100, 40),  # Platform 16
            (750, HEIGHT - 480, 100, 40),  # Platform 17
            
            
            
        ],
        'obstacles': [
            (40, HEIGHT - 160, 30, 10, 'spikes'),  # Engel X
            (190, HEIGHT - 160, 30, 10, 'spikes'),  # Engel 1
            (340, HEIGHT - 160, 30, 10, 'spikes'),  # Engel 2
            (490, HEIGHT - 160, 30, 10, 'spikes'),  # Engel 3
            (640, HEIGHT - 160, 30, 10, 'spikes'),  # Engel 4
            
            (115, HEIGHT - 270, 30, 10, 'spikes'),  # Spike Platform 6            
            (265, HEIGHT - 270, 30, 10, 'spikes'),  # Spike Platform 7            
            (415, HEIGHT - 270, 30, 10, 'spikes'),  # Spike Platform 8            
            (565, HEIGHT - 270, 30, 10, 'spikes'),  # Spike Platform 9            
            (715, HEIGHT - 270, 30, 10, 'spikes'),  # Spike Platform 10
            
            (40, HEIGHT -  380, 30, 10, 'spikes'),  # Engel X
            (190, HEIGHT - 380, 30, 10, 'spikes'),  # Engel 1
            (340, HEIGHT - 380, 30, 10, 'spikes'),  # Engel 2
            (490, HEIGHT - 380, 30, 10, 'spikes'),  # Engel 3
            (640, HEIGHT - 380, 30, 10, 'spikes'),  # Engel 4
            
            
            
            
        ],
        'collectibles': [
            (123, HEIGHT - 170, "coin"),  # Para 1
            (273, HEIGHT - 170, "coin"),  # Para 2
            (423, HEIGHT - 170, "coin"),  # Para 3
            (573, HEIGHT - 170, "coin"),  # Para 4
            (723, HEIGHT - 170, "coin"),  # Para 5
            
            (48,  HEIGHT - 280, "coin"),  # Para 6
            (198, HEIGHT - 280, "coin"),  # Para 7
            (348, HEIGHT - 280, "coin"),  # Para 8
            (498, HEIGHT - 280, "coin"),  # Para 9
            (648, HEIGHT - 280, "coin"),  # Para 10
            
            (123, HEIGHT - 390, "coin"),  # Para 11
            (273, HEIGHT - 390, "coin"),  # Para 12
            (423, HEIGHT - 390, "coin"),  # Para 13
            (573, HEIGHT - 390, "coin"),  # Para 14
            (723, HEIGHT - 390, "coin"),  # Para 15
        
        ],
        'finish_pos': (WIDTH - 50, HEIGHT - 500)
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
            (150, HEIGHT - 150, 50, 20),
            (250, HEIGHT - 260, 50, 20),
            (150, HEIGHT - 370, 50, 20),
            (250, HEIGHT - 480, 50, 20),
            
            (210, HEIGHT - 205, 30, 10),
            (210, HEIGHT - 315, 30, 10),
            (210, HEIGHT - 425, 30, 10),
            
            
            (390, HEIGHT - 280, 30, 10),
            (390, HEIGHT - 250, 30, 10),
            (390, HEIGHT - 220, 30, 10),
            (390, HEIGHT - 190, 30, 10),
            (390, HEIGHT - 160, 30, 10),
            (390, HEIGHT - 130, 30, 10),
            (390, HEIGHT - 100, 30, 10),
            (390, HEIGHT - 70, 30, 10),
            
            
            (720, HEIGHT - 220, 30, 10),
            (720, HEIGHT - 190, 30, 10),
            (720, HEIGHT - 160, 30, 10),
            (720, HEIGHT - 130, 30, 10),
            (720, HEIGHT - 100, 30, 10),
            (720, HEIGHT - 70, 30, 10),
            
            
            
            # Hareketli platform izlenimi veren yapı
            (460, HEIGHT - 190, 50, 30),
            (520, HEIGHT - 230, 50, 10),
            (580, HEIGHT - 270, 50, 10),
            (640, HEIGHT - 310, 50, 30),
            (580, HEIGHT - 350, 50, 10),
            (520, HEIGHT - 390, 50, 10),
            (460, HEIGHT - 430, 50, 30),
            
            # Üst platform
            (500, HEIGHT- 500, 100, 20),
            (600, HEIGHT - 500, 100, 20),
            (700, HEIGHT - 500, 100, 20),
            
        ],
        'obstacles': [
            # Dikey engelleyiciler
            (210, HEIGHT - 215, 30, 10, 'spikes'),
            (210, HEIGHT - 325, 30, 10, 'spikes'),
            (210, HEIGHT - 435, 30, 10, 'spikes'),
            

            
            # Düşen tuzaklar
            (390, HEIGHT - 300, 30, 20, 'spikes'),
            (390, HEIGHT - 270, 30, 20, 'spikes'),
            (390, HEIGHT - 240, 30, 20, 'spikes'),
            (390, HEIGHT - 210, 30, 20, 'spikes'),
            (390, HEIGHT - 180, 30, 20, 'spikes'),
            (390, HEIGHT - 150, 30, 20, 'spikes'),
            (390, HEIGHT - 120, 30, 20, 'spikes'),
            (390, HEIGHT - 90, 30, 20, 'spikes'),
            (390, HEIGHT - 60, 30, 20, 'spikes'),
            
            
            (720, HEIGHT - 240, 30, 20, 'spikes'),
            (720, HEIGHT - 210, 30, 20, 'spikes'),
            (720, HEIGHT - 180, 30, 20, 'spikes'),
            (720, HEIGHT - 150, 30, 20, 'spikes'),
            (720, HEIGHT - 120, 30, 20, 'spikes'),
            (720, HEIGHT - 90, 30, 20, 'spikes'),
            (720, HEIGHT - 60, 30, 20, 'spikes'),
            
            # Ölüm bölgesi
            (420, HEIGHT - 60, 60, 20, 'spikes'),
            (480, HEIGHT - 60, 60, 20, 'spikes'),
            (540, HEIGHT - 60, 60, 20, 'spikes'),
            (600, HEIGHT - 60, 60, 20, 'spikes'),
            (660, HEIGHT - 60, 60, 20, 'spikes'),
        ],
        'collectibles': [
            # Dikey yoldaki paralar
            (168, HEIGHT - 170, "coin"),
            (268, HEIGHT - 280, "coin"),
            (168, HEIGHT - 390, "coin"),
            (268, HEIGHT - 500, "coin"),
            
            # Hareketli platformdaki paralar
            (480, HEIGHT - 220, "coin"),
            (540, HEIGHT - 260, "coin"),
            (600, HEIGHT - 300, "coin"),
            (660, HEIGHT - 340, "coin"),
            (600, HEIGHT - 380, "coin"),
            (540, HEIGHT - 420, "coin"),
            (480, HEIGHT - 460, "coin"),
        ],
        'finish_pos': (WIDTH - 50, HEIGHT - 520)
    }
]