import PySimpleGUI as sg
from random import randint
import backend

theme = sg.theme('BlueMono')


def primeiraTela():
    flayout = [
        [sg.Text('Bem vindo!')],
        [sg.Text('Faça o cadastro dos filmes que já foram assistido.')],
        [sg.Button('ENTRAR'), sg.Button('SAIR')]
    ]

    janela = sg.Window("Filmes", flayout, size=(500, 100), element_justification="center")

    button, values = janela.read()
    if button == 'ENTRAR':
        janela.close()
    if button == 'SAIR':
        exit()


ID = ''
NAME = backend.read_task()

layout = [
    [sg.Text('Nome do filme:', size=(15, 1)), sg.Input(key='-NAME-'), ],
    [sg.Text('Filmes Cadastrados')],
    [sg.Listbox(NAME, size=(50, 10), key='-BOX-')],

    [sg.Button('Enviar'), sg.Button('Sair'), sg.Button('Deletar')]

]

primeiraTela()
janela = sg.Window('Cadastro', layout)
while True:
    button, values = janela.read()

    if NAME != '':
        backend.write(ID, NAME)
    NAME = backend.read_task()


    if button == 'Enviar':
        ID = randint(1, 999)
        NAME = values['-NAME-'].capitalize()



    janela.find_element('-NAME-').Update('')
    janela.find_element('-BOX-').Update(NAME)

    if button == 'Deletar':
        if NAME:
            x = values['-BOX-'][0]
            backend.delete(x)
            NAME = backend.read_task()
            janela.find_element('-BOX-').Update(NAME)

    if button == 'Sair':
        exit()
