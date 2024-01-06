from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])

window = QWidget()
window.setWindowTitle('Ваша анкета')
window.resize(550, 600)

label1 = QLabel("Як вас звати?(просто ім'я)")
label2 = QLabel('Скільки вам років?(цифрами)')
label3 = QLabel('Ваша стать:')
label4 = QLabel('Що вам подобається?')
label5 = QLabel('Що вам не подобається?')

text1 = QLineEdit()
text2 = QLineEdit()
text4 = QLineEdit()
text5 = QLineEdit()

list1 = QComboBox()
list1.addItems(["1","2","3"])

ch1=QRadioButton("чоловіча")
ch2=QRadioButton("жіноча")
ch3=QRadioButton("---")

h1=QHBoxLayout()
h1.addWidget(ch1)
h1.addWidget(ch2)
h1.addWidget(ch3)

b=QPushButton("Завершити")

v=QVBoxLayout()
v.addWidget(label1)
v.addWidget(text1)
v.addWidget(label2)
v.addWidget(text2)
v.addWidget(label3)
v.addLayout(h1)
v.addWidget(label4)
v.addWidget(text4)
v.addWidget(label5)
v.addWidget(text5)
v.addWidget(b, alignment=Qt.AlignCenter)
window.setLayout(v)


window1 = QWidget()
window1.setWindowTitle('Перевірте')
window1.resize(200, 350)

f = QVBoxLayout()
b1 = QPushButton('Все добре')
b2 = QPushButton('Назад')

c = QHBoxLayout()
lb1 = QLabel("")
lb2 = QLabel("")
lb3= QLabel("")
lb4 = QLabel("")
lb5 = QLabel("")
f.addWidget(lb1)
f.addWidget(lb2)
f.addWidget(lb3)
f.addWidget(lb4)
f.addWidget(lb5)

c.addWidget(b1)
c.addWidget(b2)
f.addLayout(c)

window1.setLayout(f)
window1.hide()

def perev ():
    lb1.setText("Ім'я: "+text1.text())
    lb2.setText('Вік: '+text2.text())
    if ch1.isChecked():
        lb3.setText ('Стать: чоловік')
    if ch2.isChecked():
        lb3.setText('Стать: жінка')
    if ch3.isChecked():
        lb3.setText('Стать: ---')
    lb4.setText('Люблю: '+text4.text())
    lb5.setText('Не люблю: '+text5.text())

    

    window1.show()

def dobre ():
    with open ("ankets.txt", "a", encoding="utf-8") as file:
        file.write(lb1.text()+'\n')
        file.write(lb2.text()+'\n')
        file.write(lb3.text()+'\n')
        file.write(lb4.text()+'\n')
        file.write(lb5.text()+'\n'+'\n')
        window1.hide()

def clean():
    text1.clear()
    text2.clear()
    text4.clear()
    text5.clear()
    window1.hide()


b.clicked.connect(perev)
b1.clicked.connect(dobre)
b2.clicked.connect(clean)

window.show()
app.exec_()
