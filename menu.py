import sys
import curses
from curses import panel
from snake import snake

screen = curses.initscr() #Inicia a biblioteca e retorna um obj da janela que representa a tela inteira;
curses.noecho() #Desativa o eco automático de pressionamento de tecla;
curses.curs_set(0) #Usamos para desabilitar um cursor piscando;
curses.start_color() #Usamos para definir cor para o terminal, nesse caso as cores paddrões;
screen.keypad(1)
_panel = panel.new_panel(screen) #Cria janelas empilhadas;
panel.update_panels() #Cria janelas empilhadas;
MENU = ['Start', 'Exit']

def clearScreen():
    screen.clear()
    _panel.hide()
    panel.update_panels()

def display():
    position = 0
    _panel.top()
    _panel.show()
    screen.clear()
    
    while True:
        #Adicionando um título para o menu
        screen.addstr(1, 1, "========== Snake =========", curses.A_BOLD)
        screen.refresh()
        curses.doupdate()

        for i, item in enumerate(MENU):
            mode = curses.A_NORMAL
            if i == position:
                mode = curses.A_REVERSE

            screen.addstr(3 + i, 10, f'{i}. {item}', mode)

        #A função getch é usada para aguardar a capturar o pressionamento da tecla
        key = screen.getch()

        if key == curses.KEY_UP:
            position = 0
        elif key == curses.KEY_DOWN:
            position = len(MENU) - 1
        elif key in [curses.KEY_ENTER, ord ('\n')]:
            if position == len(MENU) -1:
                sys.exit(0)
            else:
                clearScreen()
                snake()
                break
    screen.clear()
    _panel.hide()
    panel.update_panels()
    curses.doupdate()

def run(object):
    display()

if __name__ == '__main__':
    curses.wrapper(run)