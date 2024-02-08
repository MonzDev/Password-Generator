from functions import gui, main_function, new_window

# Interface gráfica e lógica

interface = [
    [gui.Text('Selecione as opções desejadas',
              font=16, key='start', justification='c')],

    [gui.Text('Tipo de senha', font=16, size=15, key='pass_text'),
        gui.Combo(['De A à Z', 'Numérico', 'Alfanumérico'], readonly=True, 
                  font=16, size=13, key='tipo', default_value='-- Selecionar')],

    [gui.Text('Tamanho da senha', font=16, size=15),
        gui.Combo(list(range(8, 31)), font=16, key='size',
                  default_value=12, readonly=True)],

    [gui.Button('Gerar Senha', font=16, size=(25, 2)),
     gui.Button('Sair', font=16, size=(8, 2))],

    [gui.Text(size=35, font=20, key='vazio', justification='c')],

    [gui.Input(size=45, key='campo', justification='c')],
    [gui.Button('\t\t Salvar Senha\t\t       ')]
]

janela = gui.Window('Password Generator', interface,
                    enable_close_attempted_event=True)

success = False

while True:

    # Primeira etapa de verificação de eventos

    evento, valores = janela.read()
    if evento in (gui.WINDOW_CLOSE_ATTEMPTED_EVENT, 'Sair') and gui.popup_yes_no('Realmente deseja sair?') == 'Yes':
        break
    elif evento == 'Gerar Senha':

        # Segunda etapa de verificação de eventos para evitar possíveis erros

        valores['size'] = int(valores['size'])

        if valores['tipo'] == 'De A à Z':
            generator = main_function(1, valores['size'])
            janela['vazio'].update('Senha gerada com sucesso!')
            janela['campo'].update(f'{generator}')
            success = True

        elif valores['tipo'] == 'Numérico':
            generator = main_function(2, valores['size'])
            janela['vazio'].update('Senha gerada com sucesso!')
            janela['campo'].update(f'{generator}')
            success = True

        elif valores['tipo'] == 'Alfanumérico':
            generator = main_function(3, valores['size'])
            janela['vazio'].update('Senha gerada com sucesso!')
            janela['campo'].update(f'{generator}')
            success = True

        elif valores['tipo'] in '-- Selecionar':
            gui.popup('Você deve escolher o tipo de caracter\n\tantes de gerar a senha')

    # Após a senha ser gerada, o usuário pode salvar em um arquivo de texto

    elif evento == '\t\t Salvar Senha\t\t       ':
        if not success:
            janela['vazio'].update('Você ainda não gerou nenhuma senha')
        else:
            success = True
            password = generator
            new_window(password)

janela.close()
