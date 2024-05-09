from PyQt6.QtWidgets import *
from gui_vote import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_Name.hide()
        self.label_Title.show()
        self.label_Title.show()
        self.label_Thanks.hide()
        self.label_Winners.hide()
        self.label_Winners_Per.hide()
        self.label_No_Votes.hide()
        self.label_Current_Voter.hide()
        self.label_Pizza_Options.hide()
        self.label_Shop_Options.hide()
        self.label_Drink_Options.hide()
        self.label_Error.hide()
        self.lineEdit_Name.hide()
        self.pushButton_Pizza_1.hide()
        self.pushButton_Pizza_2.hide()
        self.pushButton_Pizza_3.hide()
        self.pushButton_Pizza_4.hide()
        self.pushButton_Shop_1.hide()
        self.pushButton_Shop_2.hide()
        self.pushButton_Shop_3.hide()
        self.pushButton_Shop_4.hide()
        self.pushButton_Drink_1.hide()
        self.pushButton_Drink_2.hide()
        self.pushButton_Drink_3.hide()
        self.pushButton_Drink_4.hide()
        self.pushButton_Enter.hide()
        self.pushButton_Vote.hide()
        self.pushButton_Start.clicked.connect(lambda: self.cast_votes(""))
        self.pushButton_Vote.clicked.connect(lambda: self.cast_votes(""))
        self.pushButton_Enter.clicked.connect(lambda: self.cast_votes("m"))
        self.pushButton_Shop_1.clicked.connect(lambda: self.cast_votes("a"))
        self.pushButton_Shop_2.clicked.connect(lambda: self.cast_votes("b"))
        self.pushButton_Shop_3.clicked.connect(lambda: self.cast_votes("c"))
        self.pushButton_Shop_4.clicked.connect(lambda: self.cast_votes("d"))
        self.pushButton_Pizza_1.clicked.connect(lambda: self.cast_votes("e"))
        self.pushButton_Pizza_2.clicked.connect(lambda: self.cast_votes("f"))
        self.pushButton_Pizza_3.clicked.connect(lambda: self.cast_votes("g"))
        self.pushButton_Pizza_4.clicked.connect(lambda: self.cast_votes("h"))
        self.pushButton_Drink_1.clicked.connect(lambda: self.cast_votes("i"))
        self.pushButton_Drink_2.clicked.connect(lambda: self.cast_votes("j"))
        self.pushButton_Drink_3.clicked.connect(lambda: self.cast_votes("k"))
        self.pushButton_Drink_4.clicked.connect(lambda: self.cast_votes("l"))
        self.label_Val_Winner.hide()
        self.label_Dom_Winner.hide()
        self.label_Hut_Winner.hide()
        self.label_Papa_Winner.hide()
        self.label_Sausage_Winner.hide()
        self.label_Hawaiian_Winner.hide()
        self.label_Pepperoni_Winner.hide()
        self.label_Supreme_Winner.hide()
        self.label_Coke_Winner.hide()
        self.label_Pepper_Winner.hide()
        self.label_Dew_Winner.hide()
        self.label_Barg_Winner.hide()
        self.label_Shop_Winner_Dom.hide()
        self.label_Shop_Winner_Hut.hide()
        self.label_Shop_Winner_Papa.hide()
        self.label_Shop_Winner_Val.hide()
        self.label_Pizza_Winner_Sausage.hide()
        self.label_Pizza_Winner_Pepperoni.hide()
        self.label_Pizza_Winner_Supreme.hide()
        self.label_Pizza_Winner_Hawaiian.hide()
        self.label_Drink_Winner_Pepper.hide()
        self.label_Drink_Winner_Dew.hide()
        self.label_Drink_Winner_Coke.hide()
        self.label_Drink_Winner_Barg.hide()
        self.shop_vote = None
        self.shop_winner = None
        self.pizza_vote = None
        self.pizza_winner = None
        self.drink_vote = None
        self.shop1 = 0
        self.shop2 = 0
        self.shop3 = 0
        self.shop4 = 0
        self.pizza1 = 0
        self.pizza2 = 0
        self.pizza3 = 0
        self.pizza4 = 0
        self.drink1 = 0
        self.drink2 = 0
        self.drink3 = 0
        self.drink4 = 0
        self.total_votes = 0

    def cast_votes(self, pressed):
        self.label_Current_Voter.hide()
        vote = pressed
        ans = self.lineEdit_Choice.text().strip().lower()
        print(ans)

        while ans != 'v' and ans != 'e':
            self.lineEdit_Choice.clear()
            self.label_Vote.hide()
            self.label_Exit.hide()
            self.label_Error.show()
            break

        if ans == 'v':
            self.label_Error.clear()
            self.label_Val_Winner.hide()
            self.label_Dom_Winner.hide()
            self.label_Hut_Winner.hide()
            self.label_Papa_Winner.hide()
            self.label_Sausage_Winner.hide()
            self.label_Hawaiian_Winner.hide()
            self.label_Pepperoni_Winner.hide()
            self.label_Supreme_Winner.hide()
            self.label_Coke_Winner.hide()
            self.label_Pepper_Winner.hide()
            self.label_Dew_Winner.hide()
            self.label_Barg_Winner.hide()
            self.label_Title.hide()
            self.label_Name.show()
            self.lineEdit_Name.show()
            self.pushButton_Start.hide()
            self.pushButton_Enter.hide()
            self.label_Vote.hide()
            self.label_Exit.hide()
            self.lineEdit_Choice.hide()
            self.pushButton_Vote.show()
            self.lineEdit_Choice.setText("n")

        elif ans == 'n':
            self.label_Name.hide()
            self.lineEdit_Name.hide()
            self.pushButton_Vote.hide()
            self.label_Shop_Options.show()
            self.pushButton_Shop_1.show()
            self.pushButton_Shop_2.show()
            self.pushButton_Shop_3.show()
            self.pushButton_Shop_4.show()
            self.lineEdit_Choice.setText("n")

            if vote == "a":
                name = self.lineEdit_Name.text()
                self.shop1 += 1
                self.total_votes += 1
                self.label_Current_Voter.setText(f'{name} you voted for')
                self.label_Shop_Options.hide()
                self.pushButton_Shop_1.hide()
                self.pushButton_Shop_2.hide()
                self.pushButton_Shop_3.hide()
                self.pushButton_Shop_4.hide()
                self.shop_vote = self.label_Val_Winner
                self.label_Pizza_Options.show()
                self.pushButton_Pizza_1.show()
                self.pushButton_Pizza_2.show()
                self.pushButton_Pizza_3.show()
                self.pushButton_Pizza_4.show()
                self.lineEdit_Choice.setText("o")

            elif vote == "b":
                self.shop2 += 1
                self.total_votes += 1
                self.label_Shop_Options.hide()
                self.pushButton_Shop_1.hide()
                self.pushButton_Shop_2.hide()
                self.pushButton_Shop_3.hide()
                self.pushButton_Shop_4.hide()
                self.shop_vote = self.label_Dom_Winner
                self.label_Pizza_Options.show()
                self.pushButton_Pizza_1.show()
                self.pushButton_Pizza_2.show()
                self.pushButton_Pizza_3.show()
                self.pushButton_Pizza_4.show()
                self.lineEdit_Choice.setText("o")

            elif vote == "c":
                self.shop3 += 1
                self.total_votes += 1
                self.label_Shop_Options.hide()
                self.pushButton_Shop_1.hide()
                self.pushButton_Shop_2.hide()
                self.pushButton_Shop_3.hide()
                self.pushButton_Shop_4.hide()
                self.shop_vote = self.label_Hut_Winner
                self.label_Pizza_Options.show()
                self.pushButton_Pizza_1.show()
                self.pushButton_Pizza_2.show()
                self.pushButton_Pizza_3.show()
                self.pushButton_Pizza_4.show()
                self.lineEdit_Choice.setText("o")

            elif vote == "d":
                self.shop4 += 1
                self.total_votes += 1
                self.label_Shop_Options.hide()
                self.pushButton_Shop_1.hide()
                self.pushButton_Shop_2.hide()
                self.pushButton_Shop_3.hide()
                self.pushButton_Shop_4.hide()
                self.shop_vote = self.label_Papa_Winner
                self.label_Pizza_Options.show()
                self.pushButton_Pizza_1.show()
                self.pushButton_Pizza_2.show()
                self.pushButton_Pizza_3.show()
                self.pushButton_Pizza_4.show()
                self.lineEdit_Choice.setText("o")

        elif ans == 'o':
            if vote == "e":
                self.pizza1 += 1
                self.label_Pizza_Options.hide()
                self.pushButton_Pizza_1.hide()
                self.pushButton_Pizza_2.hide()
                self.pushButton_Pizza_3.hide()
                self.pushButton_Pizza_4.hide()
                self.pizza_vote = self.label_Supreme_Winner
                self.label_Drink_Options.show()
                self.pushButton_Drink_1.show()
                self.pushButton_Drink_2.show()
                self.pushButton_Drink_3.show()
                self.pushButton_Drink_4.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "f":
                self.pizza2 += 1
                self.label_Pizza_Options.hide()
                self.pushButton_Pizza_1.hide()
                self.pushButton_Pizza_2.hide()
                self.pushButton_Pizza_3.hide()
                self.pushButton_Pizza_4.hide()
                self.pizza_vote = self.label_Hawaiian_Winner
                self.label_Drink_Options.show()
                self.pushButton_Drink_1.show()
                self.pushButton_Drink_2.show()
                self.pushButton_Drink_3.show()
                self.pushButton_Drink_4.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "g":
                self.pizza3 += 1
                self.label_Pizza_Options.hide()
                self.pushButton_Pizza_1.hide()
                self.pushButton_Pizza_2.hide()
                self.pushButton_Pizza_3.hide()
                self.pushButton_Pizza_4.hide()
                self.pizza_vote = self.label_Pepperoni_Winner
                self.label_Drink_Options.show()
                self.pushButton_Drink_1.show()
                self.pushButton_Drink_2.show()
                self.pushButton_Drink_3.show()
                self.pushButton_Drink_4.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "h":
                self.pizza4 += 1
                self.label_Pizza_Options.hide()
                self.pushButton_Pizza_1.hide()
                self.pushButton_Pizza_2.hide()
                self.pushButton_Pizza_3.hide()
                self.pushButton_Pizza_4.hide()
                self.pizza_vote = self.label_Sausage_Winner
                self.label_Drink_Options.show()
                self.pushButton_Drink_1.show()
                self.pushButton_Drink_2.show()
                self.pushButton_Drink_3.show()
                self.pushButton_Drink_4.show()
                self.lineEdit_Choice.setText("p")

        elif ans == "p":
            if vote == "i":
                name = self.lineEdit_Name.text()
                self.drink1 += 1
                self.label_Drink_Options.hide()
                self.pushButton_Drink_1.hide()
                self.pushButton_Drink_2.hide()
                self.pushButton_Drink_3.hide()
                self.pushButton_Drink_4.hide()
                self.drink_vote = self.label_Barg_Winner
                self.label_Current_Voter.setText(f'{name} you voted for')
                self.label_Current_Voter.show()
                self.shop_vote.show()
                self.pizza_vote.show()
                self.drink_vote.show()
                self.label_Thanks.show()
                self.pushButton_Enter.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "j":
                name = self.lineEdit_Name.text()
                self.drink2 += 1
                self.label_Drink_Options.hide()
                self.pushButton_Drink_1.hide()
                self.pushButton_Drink_2.hide()
                self.pushButton_Drink_3.hide()
                self.pushButton_Drink_4.hide()
                self.drink_vote = self.label_Coke_Winner
                self.label_Current_Voter.setText(f'{name} you voted for')
                self.label_Current_Voter.show()
                self.shop_vote.show()
                self.pizza_vote.show()
                self.drink_vote.show()
                self.label_Thanks.show()
                self.pushButton_Enter.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "k":
                name = self.lineEdit_Name.text()
                self.drink3 += 1
                self.label_Drink_Options.hide()
                self.pushButton_Drink_1.hide()
                self.pushButton_Drink_2.hide()
                self.pushButton_Drink_3.hide()
                self.pushButton_Drink_4.hide()
                self.drink_vote = self.label_Dew_Winner
                self.label_Current_Voter.setText(f'{name} you voted for')
                self.label_Current_Voter.show()
                self.shop_vote.show()
                self.pizza_vote.show()
                self.drink_vote.show()
                self.label_Thanks.show()
                self.pushButton_Enter.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "l":
                name = self.lineEdit_Name.text()
                self.drink4 += 1
                self.label_Drink_Options.hide()
                self.pushButton_Drink_1.hide()
                self.pushButton_Drink_2.hide()
                self.pushButton_Drink_3.hide()
                self.pushButton_Drink_4.hide()
                self.drink_vote = self.label_Pepper_Winner
                self.label_Current_Voter.setText(f'{name} you voted for')
                self.label_Current_Voter.show()
                self.shop_vote.show()
                self.pizza_vote.show()
                self.drink_vote.show()
                self.label_Thanks.show()
                self.pushButton_Enter.show()
                self.lineEdit_Choice.setText("p")

            elif vote == "m":
                self.shop_vote.hide()
                self.pizza_vote.hide()
                self.drink_vote.hide()
                self.label_Title.show()
                self.label_Vote.show()
                self.label_Exit.show()
                self.label_Thanks.hide()
                self.lineEdit_Name.clear()
                self.lineEdit_Choice.show()
                self.pushButton_Start.show()
                self.label_Error.hide()
                self.label_Error.setText("Please only enter v or x:")

        elif ans == "x":
            if self.total_votes == 0:
                print("no votes collected")
                self.label_Current_Voter.hide()
                self.label_Error.hide()
                self.label_Title.hide()
                self.lineEdit_Choice.hide()
                self.pushButton_Enter.hide()
                self.pushButton_Start.hide()
                self.label_No_Votes.show()
            else:
                val = (self.shop1 / self.total_votes) * 100
                dom = (self.shop2 / self.total_votes) * 100
                hut = (self.shop3 / self.total_votes) * 100
                papa = (self.shop4 / self.total_votes) * 100
                sup = (self.pizza1 / self.total_votes) * 100
                haw = (self.pizza2 / self.total_votes) * 100
                pep = (self.pizza3 / self.total_votes) * 100
                sau = (self.pizza4 / self.total_votes) * 100
                bar = (self.drink1 / self.total_votes) * 100
                cok = (self.drink2 / self.total_votes) * 100
                dew = (self.drink3 / self.total_votes) * 100
                dr = (self.drink4 / self.total_votes) * 100

                if val > dom and val > hut and val > papa:
                    self.label_Current_Voter.hide()
                    self.label_Error.hide()
                    self.label_Title.hide()
                    self.lineEdit_Choice.hide()
                    self.pushButton_Enter.hide()
                    self.pushButton_Start.hide()
                    self.shop_vote.hide()
                    self.pizza_vote.hide()
                    self.drink_vote.hide()
                    self.label_Winners_Per.setText(f'Out of {self.total_votes} votes collected')
                    self.label_Winners.show()
                    self.label_Winners_Per.show()
                    self.label_Shop_Winner_Val.show()
                    self.label_Shop_Perc.setText(f'{val:.2f}%')
                    self.label_Shop_Perc.show()
                elif dom > val and dom > hut and dom > papa:
                    self.label_Current_Voter.hide()
                    self.label_Error.hide()
                    self.label_Title.hide()
                    self.lineEdit_Choice.hide()
                    self.pushButton_Enter.hide()
                    self.pushButton_Start.hide()
                    self.shop_vote.hide()
                    self.pizza_vote.hide()
                    self.drink_vote.hide()
                    self.label_Winners_Per.setText(f'Out of {self.total_votes} votes collected')
                    self.label_Winners.show()
                    self.label_Winners_Per.show()
                    self.label_Shop_Winner_Dom.show()
                    self.label_Shop_Perc.setText(f'{dom:.2f}%')
                    self.label_Shop_Perc.show()
                elif hut > val and hut > papa and hut > dom:
                    self.label_Current_Voter.hide()
                    self.label_Error.hide()
                    self.label_Title.hide()
                    self.lineEdit_Choice.hide()
                    self.pushButton_Enter.hide()
                    self.pushButton_Start.hide()
                    self.shop_vote.hide()
                    self.pizza_vote.hide()
                    self.drink_vote.hide()
                    self.label_Winners_Per.setText(f'Out of {self.total_votes} votes collected')
                    self.label_Winners.show()
                    self.label_Winners_Per.show()
                    self.label_Shop_Winner_Hut.show()
                    self.label_Shop_Perc.setText(f'{hut:.2f}%')
                    self.label_Shop_Perc.show()
                else:
                    self.label_Current_Voter.hide()
                    self.label_Error.hide()
                    self.label_Title.hide()
                    self.lineEdit_Choice.hide()
                    self.pushButton_Enter.hide()
                    self.pushButton_Start.hide()
                    self.shop_vote.hide()
                    self.pizza_vote.hide()
                    self.drink_vote.hide()
                    self.label_Winners_Per.setText(f'Out of {self.total_votes} votes collected')
                    self.label_Winners.show()
                    self.label_Winners_Per.show()
                    self.label_Shop_Winner_Papa.show()
                    self.label_Shop_Perc.setText(f'{papa:.2f}%')
                    self.label_Shop_Perc.show()

                if dew > dr and dew > cok and dew > bar:
                    self.label_Drink_Winner_Dew.show()
                    self.label_Drink_Perc.setText(f'{dew:.2f}%')
                    self.label_Drink_Perc.show()
                elif dr > dew and dr > cok and dr > bar:
                    self.label_Drink_Winner_Pepper.show()
                    self.label_Drink_Perc.setText(f'{dr:.2f}%')
                    self.label_Drink_Perc.show()
                elif cok > dew and cok > dr and cok > bar:
                    self.label_Drink_Winner_Coke.show()
                    self.label_Drink_Perc.setText(f'{cok:.2f}%')
                    self.label_Drink_Perc.show()
                else:
                    self.label_Drink_Winner_Barg.show()
                    self.label_Drink_Perc.setText(f'{bar:.2f}%')
                    self.label_Drink_Perc.show()

                if sup > haw and sup > pep and sup > sau:
                    self.label_Pizza_Winner_Supreme.show()
                    self.label_Pizza_Perc.setText(f'{sup:.2f}%')
                    self.label_Pizza_Perc.show()
                elif haw > sup and haw > pep and haw > sau:
                    self.label_Pizza_Winner_Hawaiian.show()
                    self.label_Pizza_Perc.setText(f'{haw:.2f}%')
                    self.label_Pizza_Perc.show()
                elif sau > sup and sau > pep and sau > haw:
                    self.label_Pizza_Winner_Sausage.show()
                    self.label_Pizza_Perc.setText(f'{sau:.2f}%')
                    self.label_Pizza_Perc.show()
                else:
                    self.label_Pizza_Winner_Pepperoni.show()
                    self.label_Pizza_Perc.setText(f'{pep:.2f}%')
                    self.label_Pizza_Perc.show()
