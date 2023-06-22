import pygame, sys, random, time

pygame.init()

# variable
witdh = 1000
hight = 500
input_text = ""
m_s_r_c = [-1]
typing_flag = False
started_time = 0
ended_time = 0
real_time = 0
incorrects = []
next_level = False
start_button = True

# display
win = pygame.display.set_mode((witdh,hight))
pygame.display.set_caption("Type Speed Test")

# function
def show_text(display,message,x,y,size,font,color):
    font = pygame.font.Font(font,size)
    text = font.render(message,True,color)
    display.blit(text,(x,y))

def make_sentence():
    global m_s_r_c
    with open("sentence.txt", "r", encoding="utf-8") as file:
        text = file.read()
        sentence = text.split("\n")
        num = random.randint(0, len(sentence)-1)
        while 1:
            if num != m_s_r_c[0]:
                m_s_r_c[0] = num
                return sentence[num]
            else:
                num = random.randint(0, len(sentence)-1)
                continue
        # return random.choice(sentence)
    
def calculat():
    global incorrects
    incorrects = []
    correct = 0
    for index, character in enumerate(sentence):
        try:
            if character == input_text[index]:
                correct += 1
            else:
                incorrects.append(index+1)
        except:
            pass
    percent = int(correct*100/len(sentence))
    show_text(win, f"{correct}/{len(sentence)} - %{percent}", 780, 40, 40, "caveat.regular.ttf", (50,90,20))
    show_text(win, f"Wrongs -> {incorrects}", 20, 310, 40, "caveat.regular.ttf", (50,90,20))




# start-up
win.fill((30,160,140))
show_text(win, "TypinG SpeeD TesT", 10, 10, 90, "TiltPrism-Regular.ttf", (140,30,160))
sentence = make_sentence()
show_text(win, sentence, 30, 130, 30, "permanent-marker.regular.ttf", (140,30,160))
pygame.draw.rect(win, (200,100,30), (30,200,940,60), 5)
show_text(win, "Click on Rectangle to start timer", 20, 400, 30, "permanent-marker.regular.ttf", (100,102,108))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if (30 < x_mouse < 970) and (200 < y_mouse < 260) and start_button:
                typing_flag = True
                win.fill((30, 160, 140), (20, 400, 510, 50))
                started_time = time.time()
            if (850 < x_mouse < 1000) and (400 < y_mouse < 600) and next_level:
                input_text = ''
                win.fill((30,160,140))
                show_text(win, "TypinG SpeeD TesT", 10, 10, 90, "TiltPrism-Regular.ttf", (140,30,160))
                sentence = make_sentence()
                show_text(win, sentence, 30, 130, 30, "permanent-marker.regular.ttf", (140,30,160))
                pygame.draw.rect(win, (200,100,30), (30,200,940,60), 5)
                show_text(win, "Click on Rectangle to start timer", 20, 400, 30, "permanent-marker.regular.ttf", (100,102,108))
                start_button = True
        if (event.type == pygame.KEYDOWN) and typing_flag:
            if event.key == pygame.K_RETURN:
                win.fill((30, 160, 140), (780, 40, 200, 60))
                calculat()
                typing_flag = False
                start_button = False
                # ended_time = time.time()
                # real_time = ended_time - started_time
                # win.fill((30, 160, 140), (20, 360, 970, 40))
                # show_text(win, f"{str(real_time)} seconds", 20, 350, 40, "permanent-marker.regular.ttf", (100,102,108))
                win.fill((30,200,180), (850, 400, 150, 200))
                show_text(win, "NeXt", 875, 425, 50, "TiltPrism-Regular.ttf", (140,30,160))
                next_level = True
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
                win.fill((30, 160, 140), (35,205,930,50))
                show_text(win, input_text, 35, 205, 25, "IndieFlower.ttf", (200,50,30))
            else:
                input_text += event.unicode
                win.fill((30, 160, 140), (35,205,930,50))
                show_text(win, input_text, 35, 205, 25, "IndieFlower.ttf", (200,50,30))
    if typing_flag:
        ended_time = time.time()
        real_time = ended_time - started_time
        win.fill((30, 160, 140), (20, 360, 970, 40))
        show_text(win, f"{str(real_time)} seconds", 20, 350, 40, "permanent-marker.regular.ttf", (100,102,108))
    pygame.display.update()