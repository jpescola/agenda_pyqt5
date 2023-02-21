from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QInputDialog, QListWidgetItem


def carregar():
    get_dia()  # busca o dia atual
    t.lista.clear()  # limpa a lista

    try:
        f = open(str(dia) + '.dat', 'r')  # abre o arquivo da data atual
        compromissos = f.readlines()  # carrega os compromissos do dia
    except FileNotFoundError as e:
        compromissos = []  # não há compromissos neste dia

    # cria a agenda do dia com horários de meia-noite às onze da noite
    for h in range(24):
        compromisso = str(h) + 'h '  # compromisso vazio na hora atual

        # verifica se há compromisso para a hora atual neste dia
        for c in compromissos:
            if c.startswith(compromisso):
                compromisso = c.replace('\n', '')

        # item sem formatação
        # t.lista.addItem(compromisso)

        # item formatado
        item = QListWidgetItem(compromisso)
        if h % 2 == 0:
            item.setBackground(QColor('#eee'))
        t.lista.addItem(item)


def get_dia():
    global dia
    dia = t.calendario.selectedDate().toPyDate()


def sair():
    exit()


def salvar(compromisso, hora):
    f = open(str(dia) + '.dat', 'a')  # append
    f.write(hora + 'h ' + compromisso + '\n')
    f.close()


def editar():
    global window
    hora = t.lista.currentItem().text().split('h ')[0]
    compromisso, ok = QInputDialog.getText(window, 'Editar compromisso', 'Detalhes:')
    if ok:
        salvar(compromisso, hora)
        carregar()


def excluir():
    hora = t.lista.currentItem().text().split('h ')[0]

    f = open(str(dia) + '.dat', 'r+')  # abre o arquivo do dia atual
    compromissos = f.readlines()  # busca a lista de compromissos do dia

    # remove o compromisso da lista
    for i, c in enumerate(compromissos):
        prefixo = str(hora) + 'h '
        if c.startswith(prefixo):
            compromissos.pop(i)
            break

    f.seek(0)  # move para o início do arquivo
    f.truncate()  # exclui o conteúdo do arquivo
    f.writelines(compromissos)  # substitui o conteúdo do arquivo
    f.close()  # fecha o arquivo
    carregar()  # recarrega a lista na tela


# inicializando a janela
Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
# app.aboutToQuit.connect(salvar)
window = Window()
t = Form()
t.setupUi(window)  # carrega os componentes

# define os eventos dos botões
t.actionSair.triggered.connect(sair)  # QAction usa triggered ao invés de clicked
t.calendario.clicked.connect(carregar)
dia = t.calendario.selectedDate().toPyDate()
t.lista.itemDoubleClicked.connect(editar)
t.excluir.clicked.connect(excluir)

carregar()

# apresenta a janela
window.show()
app.exec()
