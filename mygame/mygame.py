import pygame
import glob

x = 50
y = 50

pygame.init()
janela = pygame.display.set_mode((600,400))

janela_aberta = True
fundo = pygame.image.load('imgs/map.png')

pygame.font.init()

fontP = pygame.font.get_default_font()
fontColetado = pygame.font.SysFont(fontP, 45)

miku_0 = pygame.image.load('imgs/quieto (1).png')
miku_2 = pygame.image.load('imgs/direita (1).png')
miku_2_1 = pygame.image.load('imgs/direita (2).png')
miku_2_2 = pygame.image.load('imgs/direita (3).png')
miku_2_3 = pygame.image.load('imgs/direita (4).png')
miku_2_4 = pygame.image.load('imgs/direita (5).png')

miku_3 = pygame.image.load('imgs/esquerda (1).png')
miku_3_1 = pygame.image.load('imgs/esquerda (2).png')
miku_3_2 = pygame.image.load('imgs/esquerda (3).png')
miku_3_3 = pygame.image.load('imgs/esquerda (4).png')
miku_3_4 = pygame.image.load('imgs/esquerda (5).png')

miku_4_1 = pygame.image.load('imgs/tras (1).png')
miku_4_2 = pygame.image.load('imgs/tras (2).png')

miku = pygame.image.load('imgs/frente (1).png')
miku_1_1 = pygame.image.load('imgs/frente (2).png')
miku_1_2 = pygame.image.load('imgs/frente (3).png')


foguinho1 = pygame.image.load('imgs/Fluid-rej_1.png')
foguinho2 = pygame.image.load('imgs/Fluid-rej2.png')
foguinho3 = pygame.image.load('imgs/Fluid-rej3.png')
foguinho4 = pygame.image.load('imgs/Fluid-rej4.png')
foguinho5 = pygame.image.load('imgs/Fluid-rej5.png')
foguinho6 = pygame.image.load('imgs/Fluid-rej6.png')
foguinho7 = pygame.image.load('imgs/Fluid-rej7.png')
foguinho8 = pygame.image.load('imgs/Fluid-rej8.png')

foguinho1 = pygame.transform.scale(foguinho1, [20,20])
foguinho2 = pygame.transform.scale(foguinho2, [20,20])
foguinho3 = pygame.transform.scale(foguinho3, [20,20])
foguinho4 = pygame.transform.scale(foguinho4, [20,20])
foguinho5 = pygame.transform.scale(foguinho5, [20,20])
foguinho6 = pygame.transform.scale(foguinho6, [20,20])
foguinho7 = pygame.transform.scale(foguinho7, [20,20])
foguinho8 = pygame.transform.scale(foguinho8, [20,20])

mana = pygame.image.load('imgs/mana.png')
mana1 = pygame.image.load('imgs/mana1.png')
mana2 = pygame.image.load('imgs/mana2.png')
mana3 = pygame.image.load('imgs/mana3.png')
mana4 = pygame.image.load('imgs/mana4.png')

mana = pygame.transform.scale(mana, [20,90])
mana1 = pygame.transform.scale(mana1, [20,90])
mana2 = pygame.transform.scale(mana2, [20,90])
mana3 = pygame.transform.scale(mana3, [20,90])
mana4 = pygame.transform.scale(mana4, [20,90])

manaPotion = pygame.image.load('imgs/pt2.png')
manaPotion = pygame.transform.scale(manaPotion, [30,30])

nivelMana = [mana, mana1, mana2, mana3, mana4]
qntMana = 0
manazero = 0
potMana = 0


livrinho = pygame.image.load('imgs/book.png')
livrinho = pygame.transform.scale(livrinho, [30,30])
menssagem = 0

travaBook = 0
travaPotion = 0
pickbook = 0
direcionMagic = 4
tiroTrue = 0
tiro = 8
xf = 0
yf = 0

andar = 2
direcion = 0
i = 1
j = 1
k = 1
l = 1
meiox = x + 32
meioy = y + 32

timermanazero = 0
clock = pygame.time.Clock()
while janela_aberta:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] or comandos[pygame.K_RIGHT] and comandos[pygame.K_UP] or comandos[pygame.K_RIGHT] and comandos[pygame.K_DOWN]:
        x+= andar #direita
        direcion = 1
        i += 1
        if tiroTrue == 0:
            direcionMagic = 1
    elif comandos[pygame.K_LEFT] or comandos[pygame.K_LEFT] and comandos[pygame.K_UP] or comandos[pygame.K_LEFT] and comandos[pygame.K_DOWN]:
        x-= andar#esquerda
        direcion = 2
        j += 1
        if tiroTrue == 0:
            direcionMagic = 2
    elif comandos[pygame.K_UP]:
        y-= andar#cima
        direcion = 3
        k += 1
        if tiroTrue == 0:
            direcionMagic = 3
    elif comandos[pygame.K_DOWN]:
        y+= andar#baixo
        direcion = 4
        l += 1
        if tiroTrue == 0:
            direcionMagic = 4
    else:
        direcion = 0
    

    #comando status
    if comandos[pygame.K_t]:
        print('___________________________')
        print('i: ',i)
        print('j: ',j)
        print('k: ',k)
        print('l: ',l)
        print('direcion: ',direcion)
        print('timermanazero: ',timermanazero)
        print('qntMana: ',qntMana)
        print('xf: ',xf)
        print('yf: ',yf)
        print('direcionMagic: ',direcionMagic)
        print('x: ',x,' y: ',y)
    #comando para atirar bolinha de gelo
    if comandos[pygame.K_SPACE] and xf == 0 and pickbook == 1 and qntMana <= 2:#bolinha de gelo
        if qntMana >= 0:
            qntMana = qntMana + 1
                    
        tiroTrue = 1
        menssagem = 2
        if direcionMagic == 1:
            xf = x + 50
            yf = y + 32
            
        elif direcionMagic == 2:
            xf = x - 20
            yf = y + 32
            
        elif direcionMagic == 3:
            xf = x + 20
            yf = y - 32

        elif direcionMagic == 4:
            xf = x + 20
            yf = y + 70
            
    elif comandos[pygame.K_SPACE] and qntMana >= 3:
        manazero = 1
        qntMana = qntMana + 1
        timermanazero = 0
        
    meiox = x + 32
    meioy = y + 32
        
    #comando para coletar itens
    if comandos[pygame.K_f]:
        if meiox > 300 and meiox < 330 and meioy > 70 and meioy < 100 and travaBook == 0:
            pickbook = 1
            menssagem = 1
            travaBook = 1
        if meiox > 500 and meiox < 530 and meioy > 340 and meioy < 370 and travaPotion == 0:
            qntMana = 0
            potMana = 1
            travaPotion = 1
            
    #carregar fundo
    janela.fill([110, 22, 224])

    #carregar perssonagem
    if direcion == 0:
        if direcionMagic == 1:#direita
            janela.blit(miku_2, (x,y))

        if direcionMagic == 2:#esquerda
            janela.blit(miku_3, (x,y))

        if direcionMagic == 3:#cima
            janela.blit(miku_4_1, (x,y))

        if direcionMagic == 4:#baixo
            janela.blit(miku_0, (x,y))
        
    if direcion == 1: #direita

        if i > 0 and i <= 10:
            janela.blit(miku_2, (x,y))
            
        if i > 10 and i <= 20:
            janela.blit(miku_2_1, (x,y))
            
        if i > 20 and i <= 30:
            janela.blit(miku_2_2, (x,y))
            
        if i > 30 and i <= 40:
            janela.blit(miku_2_3, (x,y))
            
        if i > 40 and i <= 50:
            janela.blit(miku_2_4, (x,y))
        
        if i >= 50:
            i = 1
            
    if direcion == 3:#cima
        
        if k > 0 and k <= 10:
            janela.blit(miku_4_1, (x,y))
            
        if k > 10 and k <= 20:
            janela.blit(miku_4_2, (x,y))

        if k >= 20:
            k = 1
        
    if direcion == 2:#esquerda

        if j > 0 and j <= 10:
            janela.blit(miku_3, (x,y))
            
        if j > 10 and j <= 20:
            janela.blit(miku_3_1, (x,y))
            
        if j > 20 and j <= 30:
            janela.blit(miku_3_2, (x,y))

        if j > 30 and j <= 40:
            janela.blit(miku_3_3, (x,y))

        if j > 40 and j <= 50:
            janela.blit(miku_3_4, (x,y))

        if j >= 50:
            j = 1

    if direcion == 4:#baixo

        if l > 0 and l <= 10:
            janela.blit(miku_1_1, (x,y))
            
        if l > 10 and l <= 20:
            janela.blit(miku_1_2, (x,y))

        if l >= 20:
            l = 1

    #Barra de mana
    if qntMana <= 3:
        janela.blit(nivelMana[qntMana], (0,0))
    elif qntMana > 3:
        if manazero == 1 and timermanazero >= 0 and timermanazero < 6:
            janela.blit(nivelMana[4], (0,0))
            timermanazero = timermanazero + 1

        else:
            janela.blit(nivelMana[3], (0,0))
        

    #Pote de mana
    if potMana == 0:
        janela.blit(manaPotion, (500,340))

    #Pegando o livro
    if menssagem == 1:
        pygame.draw.rect(janela,(255,255,255),(0,230,600,170))
        text = fontColetado.render('Pressione Space', 1, (0,0,0))
        janela.blit(text, (190, 300))

    #carregar livrinho
    if pickbook == 0:
        janela.blit(livrinho, (300, 70))
                
    #carregar bolinha de gelo
    if tiroTrue == 1:
        if direcionMagic == 1:#direita
            xf = xf + tiro
            
            if xf <= 100:
                janela.blit(foguinho1, (xf, yf))

            elif xf > 100 and xf <= 200:
                janela.blit(foguinho2, (xf, yf))

            elif xf > 200 and xf <= 300:
                janela.blit(foguinho3, (xf, yf))

            elif xf > 300 and xf <= 400:
                janela.blit(foguinho4, (xf, yf))

            elif xf > 400 and xf <= 500:
                janela.blit(foguinho5, (xf, yf))

            elif xf > 500 and xf <= 600:
                janela.blit(foguinho6, (xf, yf))

            elif xf > 600 and xf <= 700:
                janela.blit(foguinho7, (xf, yf))

            elif xf > 700 and xf <= 800:
                janela.blit(foguinho8, (xf, yf))

            elif xf > 800:
                tiroTrue = 0
                xf = 0
                
        if direcionMagic == 2:#esquerda
            xf = xf - tiro
            
            if xf >= 800:
                janela.blit(foguinho1, (xf, yf))

            elif xf < 800 and xf >= 700:
                janela.blit(foguinho2, (xf, yf))

            elif xf < 700 and xf >= 600:
                janela.blit(foguinho3, (xf, yf))

            elif xf < 600 and xf >= 500:
                janela.blit(foguinho4, (xf, yf))

            elif xf < 500 and xf >= 400:
                janela.blit(foguinho5, (xf, yf))

            elif xf < 400 and xf >= 300:
                janela.blit(foguinho6, (xf, yf))

            elif xf < 300 and xf >= 200:
                janela.blit(foguinho7, (xf, yf))

            elif xf < 200 and xf >= 100:
                janela.blit(foguinho8, (xf, yf))
                
            elif xf < 100 and xf > 0:
                janela.blit(foguinho1, (xf, yf))

            elif xf <= 0:
                tiroTrue = 0
                xf = 0

        if direcionMagic == 3:#cima
            yf = yf - tiro
            
            if yf >= 600:
                janela.blit(foguinho1, (xf, yf))

            elif yf < 600 and yf >= 500:
                janela.blit(foguinho2, (xf, yf))

            elif yf < 500 and yf >= 400:
                janela.blit(foguinho3, (xf, yf))

            elif yf < 400 and yf >= 300:
                janela.blit(foguinho4, (xf, yf))

            elif yf < 300 and yf >= 200:
                janela.blit(foguinho5, (xf, yf))

            elif yf < 200 and yf >= 100:
                janela.blit(foguinho6, (xf, yf))

            elif yf < 100 and yf > 0:
                janela.blit(foguinho7, (xf, yf))

            elif yf <= 0:
                tiroTrue = 0
                yf = 0
                xf = 0

        if direcionMagic == 4:#baixo
            yf = yf + tiro
            
            if yf <= 100:
                janela.blit(foguinho1, (xf, yf))

            elif yf > 100 and yf <= 200:
                janela.blit(foguinho2, (xf, yf))

            elif yf > 200 and yf <= 300:
                janela.blit(foguinho3, (xf, yf))

            elif yf > 300 and yf <= 400:
                janela.blit(foguinho4, (xf, yf))

            elif yf > 400 and yf <= 500:
                janela.blit(foguinho5, (xf, yf))

            elif yf > 500 and yf < 600:
                janela.blit(foguinho6, (xf, yf))

            elif yf >= 600:
                tiroTrue = 0
                yf = 0
                xf = 0


            

pygame.quit()

