import pygame
from pygame.locals import * #esse '*' esta dizendo que dentro do meu submodulo 'locals', vai ta importando todas as funções que ele contem.
#obs o submodulo locals esta dentro da biblioteca py game.
from sys import exit #quando eu clicar pra fechar a janela que vamos criar essa função vai ser chamada, e vai fechar a janela
from random import randint #sorteia valores dentro de um determinado intervalo



pygame.init()

pygame.mixer.music.set_volume(0.3) #para aumentar o barulho da musica de fundo
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3') #musica de fudo que vai tocar enquanto o jogo acontece
pygame.mixer.music.play(-1) #vai repetir a musica de fundo


barulho_colisao = pygame.mixer.Sound('smw_coin.wav') #musica da colisão #variavel #fora a musica de fundo, todos os outros sons tem q ter a extensao 'wav' pq se nao da erro
#barulho_colisao.set_volume() - caso eu queira aumentar o barulho da colisão


largura = 640
altura = 480 
x = int(largura / 2) # essa variavel vai controlar o movimento do retangulo 
y = int(altura / 2) #faz com que o retangulo apreça no meio da tela  # essa variavel vai controlar o movimento do retangulo 
x_azul = randint(40,600) #a variavel vai receber uma funçao randint #toda vez que eu rodar o codigo a variavl xazul e yazul vai receber diferentes valores vai escolher um numero aleatorio entre 40 e 600
y_azul = randint(50,430) #vai escolher um numero aleatorio entre 50 e 430


pontos = 0 #variavel vai começar com 0
fonte = pygame.font.SysFont('arial', 40, True, True) #1°parametro(tipo da fonte), 2°param.(tamanho do texto), 3°param(se vc quer que o texto esteja em negrito escreva: True , se não: False), 4°param.(se vc quer que o texto esteja em italico escreva: True , se não: False)



tela = pygame.display.set_mode((largura,altura)) #largura e altura da tela 
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock() 


while True: #loop principal do jogo
    relogio.tick(30) #30 freimes por segundo, a velocidade que o retangulo se movimenta
    tela.fill((0,0,0)) #prencheu a tela de preto  a cada interação do retangulo
    mensagem = f'Pontos: {pontos}'#oque vc quer q esteja escrito no texto
    texto_formatado = fonte.render(mensagem, True, (255,255,255)) #varaivel #vai juntar a mensagem  #cor do texto 
    for event in pygame.event.get(): #vai checar se algum evento ocorreu
        if event.type == QUIT: #quero que meu jogo feche 
            pygame.quit()
            exit() #chamou a função pra fechar o jogo

        if pygame.key.get_pressed()[K_a]: #se eu pressionar e segurar a tecla 'a', eu quero que o meu objeto se mova para a esquerda
            x = x - 20
        if pygame.key.get_pressed()[K_d]: #move para direita, tecla 'd'
            x = x + 20
        if pygame.key.get_pressed()[K_w]: #move para cima , tecla 'w'
            y = y - 20
        if pygame.key.get_pressed()[K_s]: #move para baixo 
            y = y + 20 

        

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50) ) #desenhar retangulo # 1° param.= tela, 2° param.= tupla (variaveis=rgb/que são as cores), 3° param.= (x,y, largura, altura)
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) #desenhar retangulo azul #cores #x,y,largura,altura

    if ret_vermelho.colliderect(ret_azul): #condiçao de colisao #se o retangulo vermelho encostar no retangulo azul, eu quero que aconteça algo
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1 #toda vez que houver uma colisao a variavel 'pontos' vai receber ela mesma + 1
        barulho_colisao.play() #onde a colisão funciona



    tela.blit(texto_formatado, (450, 40))#para o texto aparecer na tela #(posiçao x, y) #posiçao que o texto vai aparecer na tela
       
   

    pygame.display.update() # a cada interação ela atualiza a tela do jogo


