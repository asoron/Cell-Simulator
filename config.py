#config.py
class Config:
    # Pencere ayarları
    WIDTH = 1920
    HEIGHT = 1080
    BG_COLOR = '#202020FF'  # Daha koyu arka plan
    
    # Hücre ayarları
    CELL_COUNT = 400  # Daha fazla parçacık
    CELL_SIZE = 10    # Daha küçük parçacıklar
    CELL_COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'cyan','orange']  
    
    # Fizik ayarları
    FRICTION = 0.75        # Daha az sürtünme = daha akıcı hareket
    BORDER_FORCE = 10     # Daha yumuşak sınır etkileşimi
    BORDER_DISTANCE = 100  # Daha geniş sınır etkileşim alanı
    EFFECTIVE_DISTANCE = 250  # Parçacıklar arası etkileşim mesafesi
    FORCE_MULTIPLIER = 0.75   # Daha güçlü etkileşimler
    
    # Fare etkileşimi
    MOUSE_ATTRACTION_STRENGTH = 0.5
    MOUSE_ATTRACTION_RADIUS = 100
    
    # Etkileşim matrisi
    INTERACTION_MATRIX = {
    'red': {
        'blue': -0.7,    # Kırmızı ve mavi birbirini çok fazla iter
        'green': 0.5,    # Kırmızı ve yeşil hafif çekim
        'red': 1.2,      # Kırmızılar kendi aralarında orta derecede çekim
        'yellow': -0.3,  # Kırmızı ve sarı hafif itme
        'purple': 0.5,   # Kırmızı ve mor orta derecede çekim
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'blue': {
        'red': 0.6,      # Mavi ve kırmızı hafif çekim
        'green': -0.5,   # Mavi ve yeşil hafif itme
        'blue': 1.3,     # Maviler kendi aralarında güçlü çekim
        'yellow': 0.2,   # Mavi ve sarı zayıf çekim
        'purple': 0.7,   # Mavi ve mor orta derecede çekim
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'green': {
        'red': -0.4,     # Yeşil ve kırmızı hafif itme
        'blue': 0.3,     # Yeşil ve mavi hafif çekim
        'green': 1.1,    # Yeşiller kendi aralarında orta derecede çekim
        'yellow': 0.6,   # Yeşil ve sarı orta derecede çekim
        'purple': -0.2,  # Yeşil ve mor hafif itme
        'cyan': -0.5, 
        'orange': -0.5,
    },
    'yellow': {
        'red': 0.2,      # Sarı ve kırmızı zayıf çekim
        'blue': -0.1,    # Sarı ve mavi zayıf itme
        'green': 0.5,    # Sarı ve yeşil orta derecede çekim
        'yellow': 1.0,   # Sarılar kendi aralarında orta derecede çekim
        'purple': 0.3,   # Sarı ve mor zayıf çekim
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'purple': {
        'red': 0.5,      # Mor ve kırmızı orta derecede çekim
        'blue': 0.5,     # Mor ve mavi orta derecede çekim
        'green': -0.1,   # Mor ve yeşil zayıf itme
        'yellow': 0.4,   # Mor ve sarı zayıf çekim
        'purple': 1.4,   # Morlar kendi aralarında güçlü çekim
        'cyan': -0.5, 
        'orange': -0.5,
    },
    'cyan': {
        'red': -.5,      # Mor ve kırmızı orta derecede çekim
        'blue': -.5,     # Mor ve mavi orta derecede çekim
        'green': -.5,   # Mor ve yeşil zayıf itme
        'yellow': -.5,   # Mor ve sarı zayıf çekim
        'purple': -.5,   # Morlar kendi aralarında güçlü çekim
        'cyan': -1, 
        'orange': -1,
    },
    'orange': {
        'red': -.5,      # Mor ve kırmızı orta derecede çekim
        'blue': -.5,     # Mor ve mavi orta derecede çekim
        'green': -.5,   # Mor ve yeşil zayıf itme
        'yellow': -.5,   # Mor ve sarı zayıf çekim
        'purple': -.5,   # Morlar kendi aralarında güçlü çekim
        'cyan': -1, 
        'orange': -1,
    }
    

  
}
