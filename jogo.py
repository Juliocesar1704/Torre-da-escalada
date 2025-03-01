import pygame, sys

# Definindo cores

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)      
BLUE = (0, 0, 255)       
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)   
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0) 
PURPLE = (128, 0, 128) 
BROWN = (165, 42, 42)  
PINK = (255, 105, 180) 
GRAY = (128, 128, 128) 
LIME = (0, 255, 0)     
TEAL = (0, 128, 128)   
OLIVE = (128, 128, 0)  
SLATEBLUE = (106, 90, 205)
GOLD = (255, 215, 0)
LAVENDER = (230, 230, 250)
PEACH = (255, 218, 185)
MINT = (189, 252, 201)
LIGHTPINK = (255, 182, 193)
SKYBLUE = (135, 206, 235)
LIGHTYELLOW = (255, 255, 224)
LIGHTGREEN = (144, 238, 144)
DARKGRAY = (169, 169, 169)
LIGHTGRAY = (211, 211, 211)
SILVER = (192, 192, 192)
DIMGRAY = (105, 105, 105)


# Inicializa o relógio e o Pygame
clock = pygame.time.Clock()
pygame.init()

# Definição do tamanho da tela
altura = 1600
largura = 1200
gameDisplay = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Torre da Escalada')

# Carregamento das imagens
cavaleiroImg = pygame.image.load('cv.jpg')
cavaleiroA = 50
cavaleiroL = 50
cavaleiroImg = pygame.transform.scale(cavaleiroImg, (cavaleiroA, cavaleiroL))

vidaImg = pygame.image.load('cc.jpeg')
vidaImg = pygame.transform.scale(vidaImg, (55, 55))

vidas = 5


# Mapa
mapa = [
    "......VVP...........................................................................................................................................................................",
    "...............PTTPTT.................................................................................................................................................................",
    ".....PPTTPP..........................................................................................................................................................................",
    "....................................................................................................................................................................................",
    "............PPTTTPP..................................................................................................................................................................",
    "..............TTT...................................................................................................................................................................",
    "...PPP................................................................................................................................................................................",
    ".................PPPPP................................................................................................................................................................",
    "....................................................................................................................................................................................",
    ".....PPPP.......................................................................................................................................................................",
    "....................................................................................................................................................................................",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
]

# Definindo o tamanho dos blocos
largura_plataforma = largura // 32
altura_plataforma = altura // 16

largura_base = largura
altura_base = altura// 10


# Loop principal do jogo
while True:
    # Verificando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()

    # Desenhando o mapa
    gameDisplay.fill(BLACK)  # Preenche a tela com a cor preta
    
    # Desenha os blocos do mapa
    for linha, i in enumerate(mapa):
        for coluna in range(0, 16):
            x = coluna * largura_plataforma
            y = linha * altura_plataforma
            bloco = mapa[linha][coluna]
            cor = BLACK
            if bloco == 'P':
                cor_da_plataforma = YELLOW
                pygame.draw.rect(gameDisplay, cor_da_plataforma, (x, y, largura_plataforma, altura_plataforma))
            elif bloco == 'B':
                cor_da_base = GRAY
                pygame.draw.rect(gameDisplay, cor_da_base, (x, y, largura_base, altura_base))
            elif bloco == 'T':
                cor_da_armadilha = RED
                
    #COMPRIMENTO DO PERSONAGEM E ARMADILHAS
    
    cavaleiro = pygame.dray.rect(mapa,(cavaleiroImg),x,y,40,50)
    armadilha = pygame.dray.rect(mapa,(RED),x,y,30,35)
    
    if armadilha.colliderect(cavaleiro):
        vidas -= 1
        cavaleirox = largura//2 - cavaleiroL //2
        cavaleiroy = largura//2 - cavaleiroA//2
    if vidas == 0:
        print('Você MORREU!')
        pygame.quit
        print
        

    pygame.display.update()  # Atualiza a tela

    # Controla a taxa de quadros por segundo
    clock.tick(60)
