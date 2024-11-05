from PyQt6 import uic, QtWidgets

def funcao_principal():
    linha01 = formulario.lineEdit.text()
    linha02 = formulario.lineEdit_2.text()
    linha03 = formulario.lineEdit_4.text()

    if formulario.radioButton.isChecked() :
        print("Categoria de Informatica foi selecionado")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria de alimentos foi selecionado")
    else :
        print("Categoria de Eletronicos foi selecionado")

    print("Codigo:", linha01)
    print("Descricao:", linha02)
    print("Preco:", linha03)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()