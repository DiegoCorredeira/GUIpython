import PySimpleGUI as sg

theme = sg.theme('BlueMono')


def primeiraTela():
    flayout = [
        [sg.Text('Bem vindo!')],
        [sg.Text('Faça o cadastro dos filmes que já foram assistido.')],
        [sg.Button('ENTRAR'), sg.Cancel('SAIR')]
    ]

    janela = sg.Window("Filmes", flayout, size=(500, 100), element_justification="center")

    button, values = janela.Read()
    if button == 'ENTRAR':
        janela.close()
    if button == 'SAIR':
        exit()


primeiraTela()
