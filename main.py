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


layout = [
    [sg.Text('Nome do filme:', size=(15, 1)), sg.Input(key='-NAME-'), ],
    [sg.Text('Nota para o filme:', size=(15, 1)), sg.Input(key='Nota para o filme')],
    [sg.Text('Data em que foi assistido:', size=(15, 1)), sg.InputText(key='Date'),
     sg.CalendarButton("Calendário", close_when_date_chosen=True, target="Date", format='%d/%m/%Y',
                       size=(10, 1))],
    [sg.Text('Filmes Cadastrados')],
    [sg.Listbox('NAME', size=(50, 10), key='-BOX-')],

    [sg.Button('Enviar'), sg.Button('Sair'), sg.Button('Deletar')]

]

primeiraTela()
janela = sg.Window('Cadastro', layout)
while True:
    button, values = janela.read()

    if button == 'Enviar':
        ID = randint(1, 999)
        NAME = values['-NAME-'].capitalize()
    if button == 'Sair':
        exit()

    if NAME != '':
        backend.write(ID, NAME)

        janela.find_element('-NAME-').Update('')

    if button == 'Deletar':
        if NAME:
            x = values['-BOX-'][0]
            backend.delete(x)
