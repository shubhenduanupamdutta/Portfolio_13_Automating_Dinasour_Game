import sys
import pyautogui
import time
from PIL import Image


# CONSTANT PARAMETERS
DISTANCE_FROM_DINOSAUR = 400


def detect_dinosaur():
    region = pyautogui.locateOnScreen('images/initial_dinosaur.png')
    if region is None:
        raise Exception('Dinosaur not found. Is game screen visible?')
    return region, True


def start_game():
    print("Starting game...")
    pyautogui.press('space')
    print("Game started!")


def detect_obstacle(left, top, width, height):
    im = pyautogui.screenshot(region=(left, top, width, height))
    obstacle_color = 0
    background_color = 0
    for pixel in im.getdata():
        if obstacle_color > 20:
            return True
        if pixel == (83, 83, 83) or pixel == (172, 172, 172):
            obstacle_color += 1
    return False

def jump():
    print("Jumping...")
    pyautogui.press('space')
    print("Jumped!")


def dinosaur_at_game_screen():
    region = pyautogui.locateOnScreen('images/dinosaur_head.png')
    if region is None:
        return False, False
    return region, True


def main():
    time.sleep(5)
    if detect_dinosaur()[1]:
        start_game()

    time.sleep(3)

    region, found = dinosaur_at_game_screen()
    if found:
        print("Dinosaur at game screen!")
    else:
        return sys.exit("Dinosaur not at game screen. Exiting...")

    left = region.left + region.width + 10
    top = region.top
    width = region.width * 3.3
    height = region.height * 2 - 20

    while True:
        if detect_obstacle(left, top, width, height):
            jump()

if __name__ == '__main__':
    print('Starting...')
    main()
