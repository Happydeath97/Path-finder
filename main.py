import time
import pygame
from herni_plan import *
import queue

WIDTH = 750
ROWS = 50
TILESIZE = WIDTH // ROWS
BLACK = (0, 0, 0)
CLOCK = pygame.time.Clock()
MAPA = WORLD_MAP
pygame.display.set_caption("PATH FINDER")

WIN = pygame.display.set_mode((WIDTH, WIDTH))

def find_path(mapa):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        start = "O"
        end = "X"
        start_pos = find_start(mapa, start)
        q = queue.Queue()
        q.put((start_pos, [start_pos]))
        visited = set()

        while not q.empty():
            current_pos, path = q.get()
            row, col = current_pos
            i = path[-1]
            r, c = i
            pygame.draw.rect(WIN, (61, 90, 254), (c*TILESIZE, r*TILESIZE, TILESIZE, TILESIZE))
            pygame.display.update()
            time.sleep(0.005)
            if mapa[row][col] == end:
                for i in path:
                    r, c = i
                    pygame.draw.rect(WIN, (144, 202, 249), (c*TILESIZE, r*TILESIZE, TILESIZE, TILESIZE))
                    pygame.display.update()
                while True:
                    pygame.init()
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        pygame.quit()
                        exit()

            neighbors = find_neighbors(mapa, row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                r, c = neighbor
                if mapa[r][c] == "x":
                    continue

                new_path = path + [neighbor]
                q.put((neighbor, new_path))
                visited.add(neighbor)

def find_neighbors(mapa, row, col):
    neighbors = []

    if row > 0:     # up
        neighbors.append((row - 1, col))
    if row + 1 < len(mapa):     # down
        neighbors.append((row + 1, col))
    if col > 0:     # left
        neighbors.append((row, col - 1))
    if col + 1 < len(mapa[0]):      # right
        neighbors.append((row, col + 1))

    return neighbors

def find_start(mapa, start):
    for r, row in enumerate(mapa):
        for c, value in enumerate(row):
            if value == start:
                return r, c

    return None

def turn1():
    if pygame.mouse.get_pressed()[0]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        row = y // TILESIZE
        column = x // TILESIZE
        if MAPA[row][column] == "x":
            MAPA[row][column] = "#"

    if pygame.key.get_pressed()[pygame.K_v]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        row = y // TILESIZE
        column = x // TILESIZE
        if MAPA[row][column] == "x":
            MAPA[row][column] = "O"

    if pygame.key.get_pressed()[pygame.K_c]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        row = y // TILESIZE
        column = x // TILESIZE
        if MAPA[row][column] == "x":
            MAPA[row][column] = "X"

    if pygame.mouse.get_pressed()[2]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        row = y // TILESIZE
        column = x // TILESIZE
        MAPA[row][column] = "x"

def draw_win():
    WIN.fill(BLACK)
    size_btwn = WIDTH // ROWS
    x = 0
    y = 0
    for i in range(ROWS):
        x += size_btwn
        y += size_btwn

        pygame.draw.line(WIN, (255, 255, 255), (x, 0), (x, WIDTH))
        pygame.draw.line(WIN, (255, 255, 255), (0, y), (WIDTH, y))

    for row_index, row in enumerate(MAPA):
        for col_index, col in enumerate(row):
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if col == "#":      # Path
                pygame.draw.rect(WIN, (160, 100, 80), (x, y, TILESIZE, TILESIZE))
            if col == "x":      # Wall
                pygame.draw.rect(WIN, (110, 110, 110), (x+1, y+1, TILESIZE-2, TILESIZE-2))
            if col == "O":      # Start
                pygame.draw.rect(WIN, (0, 160, 0), (x, y, TILESIZE, TILESIZE))
            if col == "X":      # Cil
                pygame.draw.rect(WIN, (160, 0, 0), (x, y, TILESIZE, TILESIZE))

    pygame.display.update()

def main():
    flag = True
    while flag:
        pygame.time.delay(0)
        CLOCK.tick(60)
        draw_win()
        turn1()
        find_path(MAPA)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()


if __name__ == "__main__":
    main()
