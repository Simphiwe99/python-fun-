import sys

class ATM(QMainwindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0,0, 1920, 1080)
        self.setWindowTitle("ATM")
        self.initUI()




    def initUI(self):
        self.setStyleSheet("jujutsu-kaisen-sukuna-yuji-itadori-uhdpaper.com-hd-7.3234.jpg")
        self.welcome_message = QLabel(self)
        self.welcome_message.setStyleSheet('border-image: none')

        welcome_font = QtGui.Qfont()
        welcome_font.setFamily('AGENCYR')
        welcome_font.setPointSize(50)

        self.welcome_message.setText('Insert card to Begin')
        self.welcome_message.setFont(welcome_font)
        self.welcome_message.setGeometry(700, 100, 700, 100)

        self.card_inserted_button = QPushButton(self)
        self.card_inserted_button.setGeometry(200, 0, 1000, 1000)
        self.card_inserted_button.setStyleSheet('border-image: none; background-color: rgba(0,0,0,0)')
        self.card_inserted_button.clicked.connect(self.NextScreen)


    def NextScreen(self):
        self.main_page_attributes = []

        font = QtGui.QFont()
        font.setFamily("AGENCYR")
        font.setPointSize(18)

        font1 = QtGui.QFont()
        font1.setFamily('AGENCYR')
        font1.setPointSize(24)

        font2 = QtGui.QFont()
        font2.setFamily('AGENCYR')
        font2.setPointSize(24)

        self.card_insert_button.hide()
        self.welcome_message.setText("")


        self.banner = QLabel(self)
        self.banner.setGeometry(0,0,500,1000)
        self.banner.setStyleSheet('background-color: rgbg(35,64,153,.8): border-image: none')
        self.main_page_attributes.append(self.banner)
        self.banner.show()

        self.atm_label = QLabel(self)
        self.atm_label.setGeometry(20,20,100,100)
        self.atm_label.setStyleSheet('border-image: none')
        self.atm_label.setText('ATM')
        self.atm_label.setFont(font1)
        self.main_page_attributes.append(self.atm_label)
        self.atm_label.show()

        self.name_label = QLabel(self)
        self.name_label.setGeometry(80,200,200,100)
        self.name_label.setStyleSheet('border-image: none; color: white; background-color:none')
        self.name_label.setText('NAME')
        self.name_label.setFont(font2)
        self.main_page_attributes.append(self.name_label)
        self.name_label.show()

        self.actual_name = QLabel(self)
        self.actual_name.setGetmetry(80,265,200,100)
        self.actual_name.setStyleSheet('border-image: none; color: black; background-color: none')
        self.actual_name.setText('Black Ghost')
        self.actual_name.setFont(font1)
        self.main_page_attributes.append(self.actual_name)
        self.actual_name.show()

        self.account1 = QLabel(self)
        self.account1.setGeometry(80,265,200,100)
        self.account1.setStyleSheet('border-image: none; color: white; background-color: none')
        self.account1.setText('Account #1')
        self.account1.setFont(font2)
        self.main_page_attributes.append(self.account1)
        self.account1.show()

        
        self.account1_balance = QLabel(self)
        self.account1_balance.setGeometry(80,265,200,100)
        self.account1_balance.setStyleSheet('border-image: none; color: black; background-color: none')
        self.account1_balance.setText('R25 ,956.73')
        self.account1_balance.setFont(font1)
        self.main_page_attributes.append(self.account1_balance)
        self.account1_balance.show()

        
        self.account2 = QLabel(self)
        self.account2.setGeometry(80,265,200,100)
        self.account2.setStyleSheet('border-image: none; color: white; background-color: none')
        self.account2.setText('Account #2')
        self.account2.setFont(font2)
        self.main_page_attributes.append(self.account2)
        self.account2.show()

        
        self.account2_balance = QLabel(self)
        self.account2_balance.setGeometry(80,265,200,100)
        self.account2_balance.setStyleSheet('border-image: none; color: black; background-color: none')
        self.account2_balance.setText('R 55 ,000.00')
        self.account2_balance.setFont(font1)
        self.main_page_attributes.append(self.account2_balance)
        self.account2_balance.show()


