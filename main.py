import PySimpleGUI as sg


class Tela():
    def __init__(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text(' Nome do filme', size=(15, 1)), sg.Input(key='Nome do Filme'), ],
            [sg.Text('Nota para o filme', size=(15, 1)), sg.Input(key='Nota para o filme')],
            [sg.Text('Data', size=(15, 1)), sg.InputText(key='Date'),
             sg.CalendarButton("Calendário", close_when_date_chosen=True, target="Date", format='%d/%m/%Y',
                               size=(10, 1))],

            [sg.Submit('Enviar'), sg.Cancel('Sair')]

        ]

        janela = sg.Window("Dados do filme").layout(layout)

        self.button, self.values = janela.Read()
        if self.values in (sg.WIN_CLOSED, 'Cancel'):
            exit()

    def Iniciar(self):
        print(self.values)


tela = Tela()
tela.Iniciar()
