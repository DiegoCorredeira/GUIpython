import PySimpleGUI as sg

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


filmes = []
layout = [
    [sg.Text('Nome do filme:', size=(15, 1)), sg.Input(key='-NAME-'), ],
    [sg.Text('Nota para o filme:', size=(15, 1)), sg.Input(key='Nota para o filme')],
    [sg.Text('Data em que foi assistido:', size=(15, 1)), sg.InputText(key='Date'),
     sg.CalendarButton("Calendário", close_when_date_chosen=True, target="Date", format='%d/%m/%Y',
                       size=(10, 1))],
    [sg.Text('Filmes Cadastrados')],
    [sg.Listbox(filmes, size=(50, 10), key='-BOX-')],

    [sg.Submit('Enviar'), sg.Cancel('Sair'), sg.Button('Deletar')]

]

primeiraTela()
janela = sg.Window('Cadastro', layout)
button, values = janela.read()
