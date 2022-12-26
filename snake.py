import curses
from random import randint

curses.initscr()
curses.noecho()
curses.curs_set(0)
screen = curses.newwin(20, 50, 0, 0)
screen.keypad(1)
screen.border(0)
screen.nodelay(1)

ESC = 27 # ASCII 27 = ESCAPE

def snake():
    snake = [(1,3), (1,2), (1,1)]
    food = (10,20)
    screen.addch(food[0], food[1], 'ѽ')
    
    score = 0

    key = curses.KEY_RIGHT

    while key != ESC:
        screen.addstr(0, 2, f'Pontuação {score} ')

        screen.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)
        old_key = key
        event = screen.getch()
        key = event if event != -1 else old_key

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT,  curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = old_key
        
        y = snake[0][0]
        x = snake[0][1]

        if key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        elif key == curses.KEY_LEFT:
            x -= 1

        snake.insert(0, (y, x))

        if y == 0 or y == 19:
            break
        if x == 0 or x == 49:
            break

        if snake [0] in snake[1:]:
            break
        if snake[0] == food:
            score += 1
            food = ()
            while food == ():
                food = (randint(1, 18), randint(1, 48))
                if food == snake:
                    food = ()
            screen.addch(food[0], food[1], 'ѽ')
        else:
            last = snake.pop()
            screen.addch(last[0], last[1], ' ')
        screen.addch(snake[0][0], snake[0][1], '●')