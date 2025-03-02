import pygame, sys, random

clock = pygame.time.Clock()

# Inicialização do Pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Torre da escalada')

# Carregamento das imagens
cavaleiroImg = pygame.image.load('cavaleiro.png')
cavaleiroW = 55
cavaleiroH = 55
cavaleiroImg = pygame.transform.scale(cavaleiroImg, (cavaleiroW, cavaleiroH))

vidaImg = pygame.image.load('cc.jpeg')
vidaImg = pygame.transform.scale(vidaImg, (55, 55))

vidas = 5

# Função para criar plataformas aleatoriamente sem sobreposição
def cria_plataformas():
    plataformas = []
    for i in range(10):
        while True:
            x = random.randint(0, 900)  # Deixe um espaço de 100 para a largura da plataforma
            y = random.randint(100, 750)
            nova_plataforma = pygame.Rect(x, y, 100, 20)
            
            # Verifica se a plataforma colide com outras
            colisao = False
            for plataforma in plataformas:
                if nova_plataforma.colliderect(plataforma):
                    colisao = True
                    break
            
            if not colisao:
                plataformas.append(nova_plataforma)
                break
    return plataformas

# Função para desenhar vidas na tela
def desenha_vidas(vidas):
    for i in range(vidas):
        gameDisplay.blit(vidaImg, (10 + i*60, 10))

# Função para desenhar as plataformas
def desenha_plataformas(plataformas):
    for plataforma in plataformas:
        pygame.draw.rect(gameDisplay, (0, 0, 0), plataforma)

# Função de colisão com as plataformas
def colidir_plataformas(cavaleiro_rect, plataformas):
    for plataforma in plataformas:
        if cavaleiro_rect.colliderect(plataforma):
            return plataforma
    return None

# Inicialização das variáveis
CavaleiroX = 500
cavaleiroY = 700
velocidade_x = 0
velocidade_y = 0
gravidade = 0.5
salto = -10
fase = 1
plataformas = cria_plataformas()
pulos_disponiveis = 2

FIM = False

# Loop principal do jogo
while not FIM and vidas > 0 and fase <= 5:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            FIM = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and pulos_disponiveis > 0:
                velocidade_y = salto
                pulos_disponiveis -= 1
            elif evento.key == pygame.K_LEFT:
                velocidade_x = -3
            elif evento.key == pygame.K_RIGHT:
                velocidade_x = 3
            elif evento.key == pygame.K_SPACE:
                pygame.quit()
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                velocidade_x = 0

    # Aplicar gravidade
    cavaleiroY += velocidade_y
    velocidade_y += gravidade

    # Atualizar posição do cavaleiro
    CavaleiroX += velocidade_x

    # Impedir que o cavaleiro saia da tela
    if CavaleiroX < 0:
        CavaleiroX = 0
    elif CavaleiroX > 900:  # 1000 - cavaleiroW
        CavaleiroX = 900

    # Impedir que o cavaleiro ultrapasse o topo da tela
    if cavaleiroY < 0:
        cavaleiroY = 0
        velocidade_y = 0

    # Verificar colisões
    cavaleiro_rect = pygame.Rect(CavaleiroX, cavaleiroY, cavaleiroW, cavaleiroH)
    plataforma_colidida = colidir_plataformas(cavaleiro_rect, plataformas)
    if plataforma_colidida and velocidade_y > 0:
        cavaleiroY = plataforma_colidida.top - cavaleiroH
        velocidade_y = 0
        pulos_disponiveis = 2  # Restaurar a quantidade de pulos disponíveis ao colidir com uma plataforma

    # Impedir que o cavaleiro atravesse o chão
    if cavaleiroY + cavaleiroH > 800:
        cavaleiroY = 800 - cavaleiroH
        velocidade_y = 0
        pulos_disponiveis = 2  # Restaurar a quantidade de pulos disponíveis ao tocar o chão

    # Atualização do display
    gameDisplay.fill((169,169,169))

    # Desenha as vidas
    desenha_vidas(vidas)
    
    # Desenha as plataformas
    desenha_plataformas(plataformas)

    # Desenha o cavaleiro
    gameDisplay.blit(cavaleiroImg, (CavaleiroX, cavaleiroY))

    # Verifica se o cavaleiro alcançou o topo
    if cavaleiroY < 50:
        fase += 1
        CavaleiroX = 500
        cavaleiroY = 700
        plataformas = cria_plataformas()

    pygame.display.update()

    clock.tick(60)
pygame.quit()
