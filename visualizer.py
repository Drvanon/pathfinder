#!/usr/bin/env python3
import sys
import random
import pygame
from random_field import main
import pathfinder

# Global constants, I'm so sorry :(
BACKGROUND = (255, 255, 255)
LINE_COLOR = (200, 200, 200)
NODE_COLOR = (0, 0, 0)
SELECT_COLOR = (255, 0, 0)

START_COLOR = (0, 255, 0)
END_COLOR = (0, 0, 255)
PATH_COLOR = (13, 152, 186)

MARGIN = 10


def _node_pos(node):
    """Returns a tuple of (node.x, node.y) corrected for MARGIN."""
    return (MARGIN+node.x, MARGIN+node.y)


def draw_node(screen, node, color=NODE_COLOR):
    """Draws a circle with radius 2 at node's position on screen, in color."""
    pygame.draw.circle(screen, color, _node_pos(node), 2, 0)

def draw_connection(screen, node, node2, color=LINE_COLOR,
                    node_color=NODE_COLOR):
    """Draws a single connection between two nodes."""
    pygame.draw.line(screen, color, _node_pos(node), _node_pos(node2))

    pygame.draw.circle(screen, node_color, _node_pos(node), 2, 0)
    pygame.draw.circle(screen, node_color, _node_pos(node2), 2, 0)

def draw_connections(screen, node, color=LINE_COLOR, node_color=NODE_COLOR,
                     drawn=None):
    """Draws all connections between a node and it's neighbours."""
    if drawn is None:
        drawn = []

    for nb in node.neighbours:
        if (node, nb) in drawn or (nb, node) in drawn:
            continue
        draw_connection(screen, node, nb, color, node_color)
        drawn.append((node, nb))
    return drawn


def run(width, height, nodes_total, max_nbs, max_dist, step=False):
    print('Initializing Pygame... ', end='')
    sys.stdout.flush()
    pygame.init()
    print('done.')

    print('Creating screen... ', end='')
    sys.stdout.flush()
    size = width, height
    screen = pygame.display.set_mode(size)
    screen.fill(BACKGROUND)
    pygame.display.flip()
    print('done.')

    print('Generating and drawing nodes... ', end='')
    sys.stdout.flush()
    # Let's have a 10px padding.
    node_map = main(nodes_total, width-MARGIN*2, height-MARGIN*2, max_dist, max_nbs)
    node_rects = []
    for node in node_map:
        draw_node(screen, node)
        x, y = _node_pos(node)
        node_rects.append((pygame.Rect(x-3, y-3, 7, 7), node))
    print('done.')
    pygame.display.flip()

    print('Drawing connections... ', end='')
    sys.stdout.flush()
    drawn_connections = []
    for node in node_map:
        drawn_connections = draw_connections(
            screen, node, drawn=drawn_connections
        )

    print('done.')
    pygame.display.flip()

    print('Running main loop. Press R to start pathfinder.')
    sys.stdout.flush()
    selected = None

    start = random.choice(node_map)
    dest = random.choice(node_map)
    while start is dest:
        dest = random.choice(node_map)

    pf = pathfinder.Pathfinder(node_map, start, dest)

    clock = pygame.time.Clock()
    clock.tick()

    skip_all = False
    path = None
    pygame.time.set_timer(31, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == 31:
                if pf.step():
                    skip_all = True

        draw_node(screen, start, START_COLOR)
        draw_node(screen, dest, END_COLOR)
        pygame.display.flip()

        if not skip_all:
            path = []
            if pf.complete:
                path = pf.complete
            else:
                path = pf.queue[0]

        for i, node in enumerate(path):
            draw_node(screen, node, SELECT_COLOR)
            if not i == len(path) - 1:
                draw_connection(screen, node, path[i+1], PATH_COLOR,
                                PATH_COLOR)
        draw_node(screen, start, START_COLOR)
        draw_node(screen, dest, END_COLOR)
        pygame.display.flip()

if __name__ == '__main__':
    width = int(input('Screen width [100]: ') or 500)
    height = int(input('Screen height [100]: ') or 500)
    nodes_total = int(input('Amount of nodes [100]: ') or 100)
    max_nbs = int(input('Maximum neighbours [10]: ') or 10)
    max_dist = int(input('Maximum distance [20]: ') or 100)
    step = False

    run(width, height, nodes_total, max_nbs, max_dist, step)
