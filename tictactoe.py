import pygame
import ctypes


def show_off(text, color, x, y):
    """This Function Works For Title Font Of Game Start Button"""
    off_show = font1.render(text, True, color)
    play_window.blit(off_show, [x, y])
    pygame.display.update()


def show_off1(text, color, x, y):
    """This Function Works For Title Font Of Game Start Button"""
    off_show = font2.render(text, True, color)
    play_window.blit(off_show, [x, y])
    pygame.display.update()


def text_screen(text, color, x, y):
    """This Function is Working For Chatpatta Handwritings"""
    screen_text = title1.render(text, True, color)
    play_window.blit(screen_text, [x, y])
    pygame.display.update()


def circle_won():
    play_window.fill(black)
    pygame.draw.circle(play_window, lred, [(screensize[0] * 300) // 600, (screensize[1] * 250) // 550],
                       (screensize[1] * 115)//550, 5)
    show_off("Wins", lgreen, (screensize[0] * 190) // 600, (screensize[1] * 350) // 550)


def chowkdi_won():
    play_window.fill(black)
    pygame.draw.line(play_window, lgreen, [(screensize[0] * 190) // 600, (screensize[1] * 200) // 550], [(screensize[0]
        * 400) // 600, (screensize[1] * 320) // 550], 5)
    pygame.draw.line(play_window, lgreen, [(screensize[0] * 190) // 600, (screensize[1] * 320) // 550], [(screensize[0]
        * 400) // 600, (screensize[1] * 200) // 550], 5)
    show_off("Wins", lred, (screensize[0] * 190) // 600, (screensize[1] * 350) // 550)


def start_page():
    """This is the page of start graphics"""
    play_window.fill(black)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    show_off("GAME", lgreen, (screensize[0] * 150) // 600, (screensize[1] * 175) // 550)
    show_off("STARTS", lgreen, (screensize[0] * 150) // 600, (screensize[1] * 250) // 550)
    pygame.display.update()
    pygame.time.wait(2000)


def game_play():
    """This provides the screen of game match"""
    start_page()
    play_window.fill(black)
    pygame.mixer.music.play(10, 0.0)
    pygame.draw.line(play_window, lblue, [(screensize[0] * 110) // 600, (screensize[1] * 200) // 550], [(screensize[0] * 490) // 600, (screensize[1] * 200) // 550], 3)
    pygame.draw.line(play_window, lblue, [(screensize[0] * 110) // 600, (screensize[1] * 300) // 550], [(screensize[0] * 490) // 600, (screensize[1] * 300) // 550], 3)
    pygame.draw.line(play_window, lblue, [(screensize[0] * 233) // 600, (screensize[1] * 100) // 550], [(screensize[0] * 233) // 600, (screensize[1] * 400) // 550], 3)
    pygame.draw.line(play_window, lblue, [(screensize[0] * 367) // 600, (screensize[1] * 100) // 550], [(screensize[0] * 367) // 600, (screensize[1] * 400) // 550], 3)
    text_screen("Created By :-", lblue, (screensize[0] * 390) // 600, (screensize[1] * 465) // 550)
    text_screen("Sarthak Patel", lgreen, (screensize[0] * 410) // 600, (screensize[1] * 500) // 550)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)


# colors
black = (20, 20, 20)
red = (255, 0, 0)
green = (51, 119, 255)
lgreen = (25, 255, 25)
violet = (85, 0, 102)
lred = (255, 25, 64)
lblue = (173, 216, 230)
brown = (77, 51, 0)
white = (255, 255, 255)

# Game Variables
exit_game = False
Play_var = 0
game_object = 'circle'
num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Initialize the module
pygame.init()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0)//2, (user32.GetSystemMetrics(1)*8)//10

# Windows size
play_window = pygame.display.set_mode(screensize)

# Font Declaration
font1 = pygame.font.Font('Fonts//design.graffiti.SNAP____.ttf', (screensize[0]*6)//50)
title1 = pygame.font.Font('Fonts//Creation.ttf', (screensize[0]*28)//600)
font2 = pygame.font.Font('Fonts//Algerian Regular.ttf', (screensize[0]*46)//600)

# Image Loading
sp = pygame.image.load('Images//Tic-Tac-Toe-Game-red.png')

# Setting Icon
pygame.display.set_icon(sp)
pygame.display.update()

# Updating Title Game
pygame.display.set_caption("Tic Tac Toe", 'SD')
pygame.display.update()

#Music setting
pygame.mixer.music.load('Music//bgm.mp3')

# Font Declaration
play_window.fill(black)
show_off("TIC", lred, (screensize[0]*220)//600, (screensize[1]*70)//550)
show_off("TAC", lred, (screensize[0]*215)//600, (screensize[1]*150)//550)
show_off("TOE", lred, (screensize[0]*215)//600, (screensize[1]*230)//550)
show_off1("PLAY", violet, (screensize[0]*240)//600, (screensize[1]*380)//550)
pygame.draw.rect(play_window, red, [(screensize[0]*235)//600, (screensize[1]*379)//550, (screensize[0]*125)//600, (screensize[1]*50)//550], -1)
text_screen("Created By :-", lblue, (screensize[0]*390)//600, (screensize[1]*465)//550)
text_screen("Sarthak Patel", lgreen, (screensize[0]*410)//600, (screensize[1]*500)//550)

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (screensize[0]*235)//600 <= pos[0] <= (screensize[0]*360)//600 and (screensize[1]*379)//550 <= pos[1] <= (screensize[1]*429)//550 and Play_var == 0:
                Play_var = 1
                game_play()
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
        if event.type == pygame.MOUSEBUTTONDOWN and Play_var == 1:
            pos1 = pygame.mouse.get_pos()
            rows = 4
            if (screensize[0] * 110) // 600 <= pos1[0] <= (screensize[0] * 233) // 600:
                col = 0
            elif (screensize[0] * 233) // 600 <= pos1[0] <= (screensize[0] * 367) // 600:
                col = 1
            elif (screensize[0] * 367) // 600 <= pos1[0] <= (screensize[0] * 490) // 600:
                col = 2
            if (screensize[1] * 100) // 550 <= pos1[1] <= (screensize[1] * 200) // 550:
                rows = 0
            elif (screensize[1] * 200) // 550 <= pos1[1] <= (screensize[1] * 300) // 550:
                rows = 1
            elif (screensize[1] * 300) // 550 <= pos1[1] <= (screensize[1] * 400) // 550:
                rows = 2
            if col == 0 and rows == 0 and num[0][0] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 171) // 600, (screensize[1] * 150) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[0][0] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 190) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 111) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 111) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 190) // 550], 2)
                    game_object = 'circle'
                    num[0][0] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 1 and rows == 0 and num[1][0] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 300) // 600, (screensize[1] * 150) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[1][0] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 190) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 111) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 111) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 190) // 550], 2)
                    game_object = 'circle'
                    num[1][0] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 2 and rows == 0 and num[2][0] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 428) // 600, (screensize[1] * 150) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[2][0] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 190) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 111) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 111) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 190) // 550], 2)
                    game_object = 'circle'
                    num[2][0] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 0 and rows == 1 and num[0][1] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 171) // 600, (screensize[1] * 250) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[0][1] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 290) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 211) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 211) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 290) // 550], 2)
                    game_object = 'circle'
                    num[0][1] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 1 and rows == 1 and num[1][1] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 300) // 600, (screensize[1] * 250) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[1][1] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 290) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 211) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 211) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 290) // 550], 2)
                    game_object = 'circle'
                    num[1][1] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 2 and rows == 1 and num[2][1] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 428) // 600, (screensize[1] * 250) // 550],
                                      (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[2][1] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 290) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 211) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 211) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 290) // 550], 2)
                    game_object = 'circle'
                    num[2][1] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            elif col == 0 and rows == 2 and num[0][2] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 171) // 600, (screensize[1] * 350) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[0][2] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 390) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 311) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 121) // 600, (screensize[1] * 311) // 550],
                                     [(screensize[0] * 221) // 600, (screensize[1] * 390) // 550], 2)
                    game_object = 'circle'
                    num[0][2] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONUP)
            elif col == 1 and rows == 2 and num[1][2] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 300) // 600, (screensize[1] * 350) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[1][2] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 390) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 311) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 244) // 600, (screensize[1] * 311) // 550],
                                     [(screensize[0] * 355) // 600, (screensize[1] * 390) // 550], 2)
                    game_object = 'circle'
                    num[1][2] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONUP)
            elif col == 2 and rows == 2 and num[2][2] == 0:
                if game_object == 'circle':
                    pygame.draw.circle(play_window, lred, [(screensize[0] * 428) // 600, (screensize[1] * 350) // 550],
                                       (screensize[1] * 45)//550, 2)
                    game_object = 'rect'
                    num[2][2] = 1
                else:
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 390) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 311) // 550], 2)
                    pygame.draw.line(play_window, lgreen, [(screensize[0] * 378) // 600, (screensize[1] * 311) // 550],
                                     [(screensize[0] * 478) // 600, (screensize[1] * 390) // 550], 2)
                    game_object = 'circle'
                    num[2][2] = 2
                pygame.display.update()
                pygame.event.clear(pygame.MOUSEBUTTONUP)
        if (num[0][0] == 1 and num[0][1] == 1 and num[0][2] == 1) or (num[1][0] == 1 and num[1][1] == 1 and num[1][2]
                == 1) or (num[2][0] == 1 and num[2][1] == 1 and num[2][2] == 1) or (num[1][0] == 1 and num[2][0] == 1
                and num[0][0] == 1) or (num[0][1] == 1 and num[1][1] == 1 and num[2][1] == 1) or (num[0][2] == 1 and
                num[1][2] == 1 and num[2][2] == 1) or (num[0][0] == 1 and num[1][1] == 1 and num[2][2] == 1) or \
                (num[0][2] == 1 and num[1][1] == 1 and num[2][0] == 1):
            pygame.time.wait(1000)
            play_window.fill(black)
            circle_won()
            pygame.display.update()
            pygame.time.wait(1000)
            exit_game = True
            exit()
        elif (num[0][0] == 2 and num[0][1] == 2 and num[0][2] == 2) or (num[1][0] == 2 and num[1][1] == 2 and num[1][2]
                == 2) or (num[2][0] == 2 and num[2][1] == 2 and num[2][2] == 2) or (num[1][0] == 2 and num[2][0] == 2
                and num[0][0] == 2) or (num[0][1] == 2 and num[1][1] == 2 and num[2][1] == 2) or (num[0][0]
                == 2 and num[1][1] == 2 and num[2][2] == 2) or (num[0][2] == 2 and num[1][1] == 2 and num[2][0] == 2) or \
                (num[0][2] == 2 and num[1][2] == 2 and num[2][2] == 2):
            pygame.time.wait(1000)
            play_window.fill(black)
            chowkdi_won()
            pygame.display.update()
            pygame.time.wait(1000)
            exit_game = True
            exit()
        elif num[0][0] != 0 and num[1][0]!=0 and num[2][0]!=0 and num[0][1]!=0 and num[1][1]!=0 and num[2][1]!=0 and \
                num[0][2] !=0 and num[1][2]!=0 and num[2][2]!=0:
            play_window.fill(black)
            show_off("TIE", lgreen, (screensize[0] * 150) // 600, (screensize[1] * 175) // 550)
            show_off("MATCH", lgreen, (screensize[0] * 150) // 600, (screensize[1] * 250) // 550)
            pygame.display.update()
            exit_game = True
            exit()
	

pygame.display.quit()
quit()