import pygame, sys, socket, threading, time, random
from pygame.locals import *

def main():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    sakiStage = 0
    stage = 1
    numberOfPlayer = 5
    numberOfChoose = 0
    Variables = {"posClick":(0,0), "posMotion":(0,0), "isClick":False}
    FPS = 30
    path = "resources"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    clock = pygame.time.Clock()

    pygame.display.set_caption("One Night Ultimate Werewolf")

    Color = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), 
            "magenta": (255, 0, 255), "orange": (255, 127, 0), "pink": (255, 192, 203), "backgroundColor": (255, 244, 78), 
            "brown": (150, 75, 0), "cyan": (0, 255, 255), "indigo": (75, 0, 130), "lightpurple": (206, 156, 206), 
            "purple": (128, 0, 128), "violet": (143, 0, 255), "gray": (128, 128, 128)}

    try:
        myCardFont = pygame.font.Font(path + "/fonts/NIXGONFONTS M 2.0.ttf", 20)
    except:
        path = "."
        myCardFont = pygame.font.Font(path + "/fonts/NIXGONFONTS M 2.0.ttf", 20)
    myCardFontBig = pygame.font.Font(path + "/fonts/NIXGONFONTS M 2.0.ttf", 40)

    Doppelganger = pygame.image.load(path + "/images/doppelganger.png")
    Drunk = pygame.image.load(path + "/images/drunk.png")
    Hunter = pygame.image.load(path + "/images/hunter.png")
    Insomniac = pygame.image.load(path + "/images/insomniac.png")
    Mason = pygame.image.load(path + "/images/mason.png")
    Minion = pygame.image.load(path + "/images/minion.png")
    Robber = pygame.image.load(path + "/images/robber.png")
    Seer = pygame.image.load(path + "/images/seer.png")
    Tanner = pygame.image.load(path + "/images/tanner.png")
    Troublemaker = pygame.image.load(path + "/images/troublemaker.png")
    Villager = pygame.image.load(path + "/images/villager.png")
    Werewolf = pygame.image.load(path + "/images/werewolf.png")

    chooseDoppelganger = pygame.image.load(path + "/images/choose/doppelganger80.png")
    chooseDrunk = pygame.image.load(path + "/images/choose/drunk80.png")
    chooseHunter = pygame.image.load(path + "/images/choose/hunter80.png")
    chooseInsomniac = pygame.image.load(path + "/images/choose/insomniac80.png")
    chooseMason = pygame.image.load(path + "/images/choose/mason80.png")
    chooseMinion = pygame.image.load(path + "/images/choose/minion80.png")
    chooseRobber = pygame.image.load(path + "/images/choose/robber80.png")
    chooseSeer = pygame.image.load(path + "/images/choose/seer80.png")
    chooseTanner = pygame.image.load(path + "/images/choose/tanner80.png")
    chooseTroublemaker = pygame.image.load(path + "/images/choose/troublemaker80.png")
    chooseVillager = pygame.image.load(path + "/images/choose/villager80.png")
    chooseWerewolf = pygame.image.load(path + "/images/choose/werewolf80.png")

    Character = [Villager, Werewolf, Seer, Robber, Troublemaker, Tanner, Drunk, Hunter, Mason, Insomniac, Minion, Doppelganger]
    chooseCharacter = [chooseVillager, chooseWerewolf, chooseSeer, chooseRobber, chooseTroublemaker, chooseTanner, chooseTanner,
            chooseDrunk, chooseHunter, chooseMason, chooseInsomniac, chooseMinion, chooseDoppelganger]
    PlayerList = list()

    try:
        while True:
            pygame.mouse.set_visible(True)
            screen.fill(Color["backgroundColor"])
            if stage == 1:
                if sakiStage != stage:
                    sakiStage = stage
                txt1 = myCardFontBig.render("select Host or User", True, Color["black"])
                txtObj1 = txt1.get_rect()
                txtObj1.center = (width//2, height//2)
                screen.blit(txt1, txtObj1)

            pygame.display.flip()
    
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    Variables["posClick"] = pygame.mouse.get_pos()
                    Variables["isClick"] = True
                elif event.type == MOUSEMOTION:
                    Variables["posMotion"] = pygame.mouse.get_pos()
                elif event.type == KEYDOWN:
                    pass
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            clock.tick(FPS)
    except KeyboardInterrupt:
        sock.close()
        pygame.quit()
        sys.exit()
        print("Bye")

main()
