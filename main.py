import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit,QDialog,QApplication,QApplication,QMessageBox,QFileDialog, QMainWindow, QSlider, QCheckBox, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QProcess
# from file_manager_ui import Ui_MainWindow

class Main(QDialog):
  def __init__(self):
    super(Main,self).__init__()
    loadUi("menu.ui",self)
    self.loginbutton.clicked.connect(self.loginfunction)
    self.loginbutton.clicked.connect(self.gotohomeinitial)
    self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    self.validity_checker.clear()
    self.loginbutton.setEnabled(False)  # Disable login button initially
    self.loginbutton.setAutoDefault(True)  # Set the login button as default (activated on Enter key)
    self.loginbutton.setDefault(True)

  # def gotohomeinitial(self):
  #       initial = HomeInitial()
  #       widget.addWidget(initial)
  #       widget.setCurrentIndex(widget.currentIndex() + 1)

  def loginfunction(self):
      input_username = self.username.text()
      input_password = self.password.text()

        # Check if both username and password are entered
      if input_username and input_password:
            # Check if the credentials are correct
            if input_username == "CAGE_DECODERS" and input_password == "HIRA1234": # Change the User Name and Password here
                self.validity_checker.clear()
                self.validity_checker.setText("Valid user")
                self.loginbutton.setEnabled(True)  # Enable login button
            else:
                self.validity_checker.clear()
                self.validity_checker.setText("Invalid user")
                self.loginbutton.setEnabled(False)  # Disable login button
      else:
            self.validity_checker.clear()
            self.validity_checker.setText("Invalid user")
            self.loginbutton.setEnabled(False)  # Disable login button

  def keyPressEvent(self, event):
        # Handle Enter key press
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.loginfunction()
            self.username.clear()
            self.password.clear()


  # def gotomenu(self):
  #   main=Main()
  #   widget.addWidget(main)
  #   widget.setCurrentIndex(widget.currentIndex()+1)  

# class Main(QDialog):
#   def __init__(self):
#     super(Main,self).__init__()
#     loadUi("menu.ui",self)
#     self.loginbutton2.clicked.connect(self.loginfunction2)
#     self.menubtn2.clicked.connect(self.gotomain)
#     self.loginbutton2.clicked.connect(self.gotohomeinitial)
#     self.shutbtn1.clicked.connect(self.hideWindow)
#     self.rstbtn1.clicked.connect(self.gotomain)

#   def gotohomeinitial(self):
#      initial=Home_initial()
#      widget.addWidget(initial)
#      widget.setCurrentIndex(widget.currentIndex()+1)  

#   def loginfunction2(self):
#     username=self.username.text()
#     password=self.password.text()
#     print("Successfully logged in with email:" ,username ,"and password:",password)

#   def hideWindow(self):
#     self.close()

#   def gotomain(self):
#     login=Login()
#     widget.addWidget(login)
#     widget.setCurrentIndex(widget.currentIndex()+1)

class Home_initial(QDialog):
  def __init__(self):
    super(Home_initial,self).__init__()
    loadUi("home_initial.ui",self)
    self.hmmenubtn_2.clicked.connect(self.gotohome)    

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  
  
class Home(QDialog):
  def __init__(self):
    super(Home,self).__init__()
    loadUi("home.ui",self)
    # self.homemenubtn1.clicked.connect(self.gotoHomeMenu)
    self.autobtn.clicked.connect(self.show_message1)
    self.userbtn.clicked.connect(self.show_message2)
    self.disablebtn.clicked.connect(self.show_message3)
    self.userbtn.clicked.connect(self.gotohomeuser)
    self.autobtn.clicked.connect(self.gotoautouser)
    self.last_button_clicked = None
  #   self.userbtn.clicked.connect(self.change_button_color)

  # def change_button_color(self):
  #     self.userbtn.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  def gotohomeuser(self):
     hmmuser=homeuser()
     widget.addWidget(hmmuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotoautouser(self):
     autouuser=autouser()
     widget.addWidget(autouuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def show_message1(self):
        self.last_button_clicked = "AUTO MODE DEACTIVATED"
        msg = QMessageBox()
        msg.setWindowTitle("Auto Status")
        msg.setText("AUTO MODE ACTIVATED")
        msg.exec_()

  def show_message2(self):
        self.last_button_clicked = "USER MODE DEACTIVATED"
        msg = QMessageBox()
        msg.setWindowTitle("User Status")
        msg.setText("USER MODE ACTIVATED")
        msg.exec_()

  def show_message3(self):
        if self.last_button_clicked:
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText(f"STATUS: {self.last_button_clicked}")
            msg.exec_()

  def gotoHomeMenu(self):
    homemenu1=HomeMenu()
    widget.addWidget(homemenu1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

class homeuser(QDialog):
  def __init__(self):
    super(homeuser,self).__init__()
    loadUi("home_user.ui",self)
    self.homeusermenu1.clicked.connect(self.gotohomeusermenu)
    self.disablebtn2.clicked.connect(self.show_message3)
    self.disablebtn2.clicked.connect(self.gotohome)
    self.prguserbtn.clicked.connect(self.gotouserprogram)
    self.calibtn.clicked.connect(self.gotocaliber)
    self.jogybtn.clicked.connect(self.gotojogging)
    self.userbtn.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  
  
  # def gotoevent(self):
  #   eventing=Event()
  #   widget.addWidget(eventing)
  #   widget.setCurrentIndex(widget.currentIndex()+1)

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def show_message3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText("USER MODE DEACTIVATED")
            msg.exec_() 

  def gotohomeusermenu(self):
    homeusermenuu=homeusermenu()
    widget.addWidget(homeusermenuu)
    widget.setCurrentIndex(widget.currentIndex()+1) 

class autouser(QDialog):
  def __init__(self):
    super(autouser,self).__init__()
    loadUi("home_auto.ui",self)
    self.homeautomenu1.clicked.connect(self.gotoautousermenu)
    self.disablebtn4.clicked.connect(self.show_message3)
    self.disablebtn4.clicked.connect(self.gotohome)
    self.prgautobtn.clicked.connect(self.gotoevent)
    self.calibtn5.clicked.connect(self.gotocaliber)
    self.autobtn.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  


  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1) 
    # self.prguserbtn2.clicked.connect(self.gotouserprogram)

  def show_message3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText("USER MODE DEACTIVATED")
            msg.exec_() 

  def gotoautousermenu(self):
    homeautomenuu=homeautomenu()
    widget.addWidget(homeautomenuu)
    widget.setCurrentIndex(widget.currentIndex()+1)  

class homeusermenu(QDialog):
  def __init__(self):
    super(homeusermenu,self).__init__()
    loadUi("home_user_menu.ui",self)
    self.disablebtn3.clicked.connect(self.show_message3)
    self.disablebtn3.clicked.connect(self.gotohome)
    self.prguserbtn2.clicked.connect(self.gotouserprogram)
    self.calibtn2.clicked.connect(self.gotocaliber)
    self.jogybtn2.clicked.connect(self.gotojogging)
    self.prguserbtn3.clicked.connect(self.gotouserprogram)
    self.calibtn3.clicked.connect(self.gotocaliber)
    self.jogybtn3.clicked.connect(self.gotojogging)
    self.userbtn.setStyleSheet("background-color: #00FF00; color: #ffffff;")


  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  
  
  # def gotoevent(self):
  #   eventing=Event()
  #   widget.addWidget(eventing)
  #   widget.setCurrentIndex(widget.currentIndex()+1)

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def show_message3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText("USER MODE DEACTIVATED")
            msg.exec_() 

class homeautomenu(QDialog):
  def __init__(self):
    super(homeautomenu,self).__init__()
    loadUi("home_auto_menu.ui",self)
    self.disablebtn5.clicked.connect(self.show_message3)
    self.disablebtn5.clicked.connect(self.gotohome)
    self.prgautobtn2.clicked.connect(self.gotoevent)
    self.calibtn6.clicked.connect(self.gotocaliber)
    self.prgautobtn3.clicked.connect(self.gotoevent)
    self.calibtn7.clicked.connect(self.gotocaliber)
    self.autobtn.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def show_message3(self):
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText("USER MODE DEACTIVATED")
            msg.exec_() 

class HomeMenu(QDialog):
  def __init__(self):
    super(HomeMenu,self).__init__()
    loadUi("home-menu.ui",self)
    self.hmmenubtn2.clicked.connect(self.gotohome)
    self.autobtn2.clicked.connect(self.show_message1)
    self.userbtn2.clicked.connect(self.show_message2)
    self.disablebtn2.clicked.connect(self.show_message3)
    self.userbtn2.clicked.connect(self.gotohomeuser)
    self.autobtn2.clicked.connect(self.gotoautouser)

  def gotohomeuser(self):
     hmmuser=homeuser()
     widget.addWidget(hmmuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotoautouser(self):
     autouuser=autouser()
     widget.addWidget(autouuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def show_message1(self):
        self.last_button_clicked = "AUTO MODE DEACTIVATED"
        msg = QMessageBox()
        msg.setWindowTitle("Auto Status")
        msg.setText("AUTO MODE ACTIVATED")
        msg.exec_()

  def show_message2(self):
        self.last_button_clicked = "USER MODE DEACTIVATED"
        msg = QMessageBox()
        msg.setWindowTitle("User Status")
        msg.setText("USER MODE ACTIVATED")
        msg.exec_()

  def show_message3(self):
        if self.last_button_clicked:
            msg = QMessageBox()
            msg.setWindowTitle("Deactivation Status")
            msg.setText("USER MODE DEACTIVATED")
            msg.exec_()

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

class Calibrate(QDialog):
  def __init__(self):
    super(Calibrate,self).__init__()
    loadUi("calibrate.ui",self)
    self.calibratemenubtn1.clicked.connect(self.gotocalibrate_menu)
    self.hmmenubtn3.clicked.connect(self.gotohome)
    self.prgautobtn3.clicked.connect(self.gotoevent)
    self.jogybtn3.clicked.connect(self.gotojogging)
    self.prguserbtn3.clicked.connect(self.gotouserprogram)

  def gotocalibrate_menu(self):
    caliber1=Calibrate_menu()
    widget.addWidget(caliber1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

   
class Calibrate_menu(QDialog):
  def __init__(self):
    super(Calibrate_menu,self).__init__()
    loadUi("calibrate_menu.ui",self)
    self.joggingbtn2.clicked.connect(self.gotojogging)
    self.programbtn3.clicked.connect(self.gotouserprogram)
    self.hmmenubtn4.clicked.connect(self.gotohome)
    self.eventlogbtn2.clicked.connect(self.gotoevent)
    self.prgautobtn4.clicked.connect(self.gotoevent)
    self.jogybtn4.clicked.connect(self.gotojogging)
    self.prguserbtn4.clicked.connect(self.gotouserprogram)

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  
  
  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

  # def gotoaievent(self):
  #   aieventy=AIevent()
  #   widget.addWidget(aieventy)
  #   widget.setCurrentIndex(widget.currentIndex()+1) 


class Jogging(QDialog):
  def __init__(self):
    super(Jogging,self).__init__()
    loadUi("jogging.ui",self)
    self.jogmenubtn1.clicked.connect(self.gotojogmenu)
    self.hmmenubtn5.clicked.connect(self.gotohomeuser)
    self.jogybtn5.clicked.connect(self.gotojogging)
    self.prguserbtn5.clicked.connect(self.gotouserprogram)
    self.joggybtn.clicked.connect(self.gotojogmenu)
    self.userbtn7.setStyleSheet("background-color: #00FF00; color: #ffffff;")
    self.JOG1.setEnabled(False) 
    self.JOG2.setEnabled(False)
    self.JOG3.setEnabled(False)
    self.text.setEnabled(False) 
    self.slider.setEnabled(False) 
    self.text2.setEnabled(False) 
    self.slider_2.setEnabled(False) 
    self.text3.setEnabled(False) 
    self.slider_3.setEnabled(False) 
    self.text4.setEnabled(False) 
    self.slider_4.setEnabled(False) 
    self.text5.setEnabled(False) 
    self.slider_5.setEnabled(False) 
    self.text6.setEnabled(False) 
    self.slider_6.setEnabled(False) 
    self.text7.setEnabled(False) 
    self.slider_7.setEnabled(False) 
    self.text8.setEnabled(False) 
    self.slider_8.setEnabled(False) 
    self.text9.setEnabled(False) 
    self.slider_9.setEnabled(False) 
    self.text10.setEnabled(False) 
    self.slider_10.setEnabled(False)
    self.text11.setEnabled(False) 
    self.slider_11.setEnabled(False)
    self.text12.setEnabled(False) 
    self.slider_12.setEnabled(False)
    self.checkBox.setEnabled(False)
    self.checkBox_2.setEnabled(False)
    self.checkBox_3.setEnabled(False)
    self.checkBox_4.setEnabled(False)
    self.checkBox_5.setEnabled(False)
    self.checkBox_6.setEnabled(False)
    self.checkBox_7.setEnabled(False)
    self.checkBox_8.setEnabled(False)
    self.checkBox_9.setEnabled(False)
    self.checkBox_10.setEnabled(False)
    self.checkBox_11.setEnabled(False)
    self.checkBox_12.setEnabled(False)
    self.increment_1.setEnabled(False)
    self.increment_2.setEnabled(False)
    self.increment_3.setEnabled(False)

  def gotohomeuser(self):
     hmmuser=homeuser()
     widget.addWidget(hmmuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotojogmenu(self):
    jog1=jogging_menu()
    widget.addWidget(jog1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  


class jogging_menu(QDialog):
  def __init__(self):
    super(jogging_menu,self).__init__()
    loadUi("jogging_menu.ui",self)
    # self.aieventbtn3.clicked.connect(self.gotoaievent)
    self.hmmenubtn6.clicked.connect(self.gotohomeuser)
    self.JOG4.clicked.connect(self.gotojogaction)
    self.JOG5.clicked.connect(self.gotojoglinear)
    self.JOG6.clicked.connect(self.gotojogreorient)
    self.jogybtn6.clicked.connect(self.gotojogging)
    self.prguserbtn6.clicked.connect(self.gotouserprogram)
    self.userbtn5.setStyleSheet("background-color: #00FF00; color: #ffffff;")

    self.slider = self.findChild(QtWidgets.QSlider, 'slider')
    self.text = self.findChild(QtWidgets.QLineEdit, 'text')
    self.slider_2 = self.findChild(QtWidgets.QSlider, 'slider_2')
    self.text2 = self.findChild(QtWidgets.QLineEdit, 'text2')
    self.slider_3 = self.findChild(QtWidgets.QSlider, 'slider_3')
    self.text3 = self.findChild(QtWidgets.QLineEdit, 'text3')
    self.slider_4 = self.findChild(QtWidgets.QSlider, 'slider_4')
    self.text4 = self.findChild(QtWidgets.QLineEdit, 'text4')
    self.slider_5 = self.findChild(QtWidgets.QSlider, 'slider_5')
    self.text5 = self.findChild(QtWidgets.QLineEdit, 'text5')
    self.slider_6 = self.findChild(QtWidgets.QSlider, 'slider_6')
    self.text6 = self.findChild(QtWidgets.QLineEdit, 'text6')
    self.slider_7 = self.findChild(QtWidgets.QSlider, 'slider_7')
    self.text7 = self.findChild(QtWidgets.QLineEdit, 'text7')
    self.slider_8 = self.findChild(QtWidgets.QSlider, 'slider_8')
    self.text8 = self.findChild(QtWidgets.QLineEdit, 'text8')
    self.slider_9 = self.findChild(QtWidgets.QSlider, 'slider_9')
    self.text9 = self.findChild(QtWidgets.QLineEdit, 'text9')
    self.slider_10 = self.findChild(QtWidgets.QSlider, 'slider_10')
    self.text10 = self.findChild(QtWidgets.QLineEdit, 'text10')
    self.slider_11 = self.findChild(QtWidgets.QSlider, 'slider_11')
    self.text11 = self.findChild(QtWidgets.QLineEdit, 'text11')
    self.slider_12 = self.findChild(QtWidgets.QSlider, 'slider_12')
    self.text12 = self.findChild(QtWidgets.QLineEdit, 'text12')
    
    self.slider.valueChanged.connect(self.update_line_edit)
    self.slider_2.valueChanged.connect(self.update_line_edit2)
    self.slider_3.valueChanged.connect(self.update_line_edit3)
    self.slider_4.valueChanged.connect(self.update_line_edit4)
    self.slider_5.valueChanged.connect(self.update_line_edit5)
    self.slider_6.valueChanged.connect(self.update_line_edit6)
    self.slider_7.valueChanged.connect(self.update_line_edit7)
    self.slider_8.valueChanged.connect(self.update_line_edit8)
    self.slider_9.valueChanged.connect(self.update_line_edit9)
    self.slider_10.valueChanged.connect(self.update_line_edit10)
    self.slider_11.valueChanged.connect(self.update_line_edit11)
    self.slider_12.valueChanged.connect(self.update_line_edit12)

  def update_line_edit(self, value):
        float_value = float(value) / 100.0  
        self.text.setText('{:.2f}'.format(float_value)) 

  def update_line_edit2(self, value):
        float_value = float(value) / 100.0  
        self.text2.setText('{:.2f}'.format(float_value)) 

  def update_line_edit3(self, value):
        float_value = float(value) / 100.0  
        self.text3.setText('{:.2f}'.format(float_value)) 

  def update_line_edit4(self, value):
        float_value = float(value) / 100.0  
        self.text4.setText('{:.2f}'.format(float_value)) 

  def update_line_edit5(self, value):
        float_value = float(value) / 100.0  
        self.text5.setText('{:.2f}'.format(float_value)) 

  def update_line_edit6(self, value):
        float_value = float(value) / 100.0  
        self.text6.setText('{:.2f}'.format(float_value)) 

  def update_line_edit7(self, value):
        float_value = float(value) / 100.0  
        self.text7.setText('{:.2f}'.format(float_value)) 

  def update_line_edit8(self, value):
        float_value = float(value) / 100.0  
        self.text8.setText('{:.2f}'.format(float_value)) 

  def update_line_edit9(self, value):
        float_value = float(value) / 100.0  
        self.text9.setText('{:.2f}'.format(float_value)) 

  def update_line_edit10(self, value):
        float_value = float(value) / 100.0  
        self.text10.setText('{:.2f}'.format(float_value)) 

  def update_line_edit11(self, value):
        float_value = float(value) / 100.0  
        self.text11.setText('{:.2f}'.format(float_value)) 

  def update_line_edit12(self, value):
        float_value = float(value) / 100.0  
        self.text12.setText('{:.2f}'.format(float_value)) 
    
        # self.sliders = [self.findChild(QSlider, f'slider_{i+1}') for i in range(12)]
        # self.text_fields = [self.findChild(QLineEdit, f'text{i+1}') for i in range(12)]

        # # Connect sliders to update functions using a loop
        # for slider, text_field in zip(self.sliders, self.text_fields):
        #     slider.valueChanged.connect(lambda value, text_field=text_field: self.update_line_edit(value, text_field))

  # def update_line_edit(self, value, text_field):
  #       # Update the corresponding line edit based on the slider value
  #       float_value = float(value) / 100.0  # Adjust based on your range and precision
  #       text_field.setText('{:.2f}'.format(float_value))

    # self.slider.valueChanged.connect(self.slide)
    # self.slider_2.valueChanged.connect(self.slide)
    # self.slider_3.valueChanged.connect(self.slide)
    # self.slider_4.valueChanged.connect(self.slide)
    # self.slider_5.valueChanged.connect(self.slide)
    # self.slider_6.valueChanged.connect(self.slide)
    # self.slider_7.valueChanged.connect(self.slide)
    # self.slider_8.valueChanged.connect(self.slide)
    # self.slider_9.valueChanged.connect(self.slide)
    # self.slider_10.valueChanged.connect(self.slide)
    # self.slider_11.valueChanged.connect(self.slide)
    # self.slider_12.valueChanged.connect(self.slide)
    # self.checkBox.clicked.connect(self.on_checkbox_state_changed)
    # self.checkBox_2.clicked.connect(self.on_checkbox_state_changed2)
    # self.checkBox_3.clicked.connect(self.on_checkbox_state_changed3)
    # self.checkBox_4.clicked.connect(self.on_checkbox_state_changed4)
    # self.checkBox_5.clicked.connect(self.on_checkbox_state_changed5)
    # self.checkBox_6.clicked.connect(self.on_checkbox_state_changed6)
    # self.checkBox_7.clicked.connect(self.on_checkbox_state_changed7)
    # self.checkBox_8.clicked.connect(self.on_checkbox_state_changed8)
    # self.checkBox_9.clicked.connect(self.on_checkbox_state_changed9)
    # self.checkBox_10.clicked.connect(self.on_checkbox_state_changed10)
    # self.checkBox_11.clicked.connect(self.on_checkbox_state_changed11)
    # self.checkBox_12.clicked.connect(self.on_checkbox_state_changed12)
    # self.text.textChanged.connect(self.update_slider)
    # self.text2.textChanged.connect(self.update_slider)
    # self.text3.textChanged.connect(self.update_slider)
    # self.text4.textChanged.connect(self.update_slider)
    # self.text5.textChanged.connect(self.update_slider)
    # self.text6.textChanged.connect(self.update_slider)
    # self.text7.textChanged.connect(self.update_slider)
    # self.text8.textChanged.connect(self.update_slider)
    # self.text9.textChanged.connect(self.update_slider)
    # self.text10.textChanged.connect(self.update_slider)
    # self.text11.textChanged.connect(self.update_slider)
    # self.text12.textChanged.connect(self.update_slider)
    # self.value = 0 
    # self.value2 = 0 
    # self.value3 = 0 
    # self.value4 = 0 
    # self.value5 = 0 
    # self.value6 = 0 
    # self.value7 = 0 
    # self.value8 = 0 
    # self.value9 = 0 
    # self.value10 = 0 
    # self.value11 = 0 
    # self.value12 = 0 
    # self.increase_1.clicked.connect(self.increment_value)
    # self.increase_2.clicked.connect(self.increment_value2)
    # self.increase_3.clicked.connect(self.increment_value3)
    # self.increase_4.clicked.connect(self.increment_value4)
    # self.increase_5.clicked.connect(self.increment_value5)
    # self.increase_6.clicked.connect(self.increment_value6)
    # self.increase_7.clicked.connect(self.increment_value7)
    # self.increase_8.clicked.connect(self.increment_value8)
    # self.increase_9.clicked.connect(self.increment_value9)
    # self.increase_10.clicked.connect(self.increment_value10)
    # self.increase_11.clicked.connect(self.increment_value11)
    # self.increase_12.clicked.connect(self.increment_value12)
    # self.decrease_1.clicked.connect(self.decrement_value)
    # self.decrease_2.clicked.connect(self.decrement_value2)
    # self.decrease_3.clicked.connect(self.decrement_value3)
    # self.decrease_4.clicked.connect(self.decrement_value4)
    # self.decrease_5.clicked.connect(self.decrement_value5)
    # self.decrease_6.clicked.connect(self.decrement_value6)
    # self.decrease_7.clicked.connect(self.decrement_value7)
    # self.decrease_8.clicked.connect(self.decrement_value8)
    # self.decrease_9.clicked.connect(self.decrement_value9)
    # self.decrease_10.clicked.connect(self.decrement_value10)
    # self.decrease_11.clicked.connect(self.decrement_value11)
    # self.decrease_12.clicked.connect(self.decrement_value12)
    # self.increment_1.clicked.connect(self.increase)
    # self.increment_2.clicked.connect(self.increase1)
    # self.increment_3.clicked.connect(self.increase2)
  #   self.saveButton.clicked.connect(self.save_text)
  #   self.joggybtn.clicked.connect(self.display_text)

  #       # Create a variable to store the file content
  #   self.file_content = ""

  # def save_text(self):
  #       # Get the content from the QTextEdit widget
  #       content = self.text.toPlainText()

  #       if content:
  #           self.file_content = content

  # def display_text(self):
  #       self.text.setPlainText(self.file_content)

  def gotohomeuser(self):
     hmmuser=homeuser()
     widget.addWidget(hmmuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

  # def increase(self):
  #     self.value += 0.1
  #     self.text.setText(str(self.value))
  # def increase1(self):
  #     self.value += 1
  #     self.text.setText(str(self.value))
  # def increase2(self):
  #     self.value += 10
  #     self.text.setText(str(self.value))


  # def increment_value(self):
  #       self.value+= 1
  #       self.text.setText(str(self.value2))
  # def increment_value2(self):
  #       self.value2 += 1
  #       self.text2.setText(str(self.value2))
  # def increment_value3(self):
  #       self.value3 += 1
  #       self.text3.setText(str(self.value3))
  # def increment_value4(self):
  #       self.value4 += 1
  #       self.text4.setText(str(self.value4))
  # def increment_value5(self):
  #       self.value5 += 1
  #       self.text5.setText(str(self.value5))
  # def increment_value6(self):
  #       self.value6 += 1
  #       self.text6.setText(str(self.value6))     
  # def increment_value7(self):
  #       self.value7 += 1
  #       self.text7.setText(str(self.value7))
  # def increment_value8(self):
  #       self.value8 += 1
  #       self.text8.setText(str(self.value8))
  # def increment_value9(self):
  #       self.value9 += 1
  #       self.text9.setText(str(self.value9))
  # def increment_value10(self):
  #       self.value10 += 1
  #       self.text10.setText(str(self.value10))
  # def increment_value11(self):
  #       self.value11 += 1
  #       self.text11.setText(str(self.value11))
  # def increment_value12(self):
  #       self.value12 += 1
  #       self.text12.setText(str(self.value12))

  # def decrement_value(self):
  #       self.value -= 1
  #       self.text.setText(str(self.value))  
  # def decrement_value2(self):
  #       self.value2 -= 1
  #       self.text2.setText(str(self.value2))
  # def decrement_value3(self):
  #       self.value3 -= 1
  #       self.text3.setText(str(self.value3))
  # def decrement_value4(self):
  #       self.value4 -= 1
  #       self.text4.setText(str(self.value4))
  # def decrement_value5(self):
  #       self.value5 -= 1
  #       self.text5.setText(str(self.value5))
  # def decrement_value6(self):
  #       self.value6 -= 1
  #       self.text6.setText(str(self.value6))     
  # def decrement_value7(self):
  #       self.value7 -= 1
  #       self.text7.setText(str(self.value7))
  # def decrement_value8(self):
  #       self.value8 -= 1
  #       self.text8.setText(str(self.value8))
  # def decrement_value9(self):
  #       self.value9 -= 1
  #       self.text9.setText(str(self.value9))
  # def decrement_value10(self):
  #       self.value10 -= 1
  #       self.text10.setText(str(self.value10))
  # def decrement_value11(self):
  #       self.value11 -= 1
  #       self.text11.setText(str(self.value11))
  # def decrement_value12(self):
  #       self.value12 -= 1
  #       self.text12.setText(str(self.value12))

  #       self.slider = self.findChild(QtWidgets.QSlider, 'slider')
  #       self.text19 = self.findChild(QtWidgets.QLineEdit, 'lineEdit')

  #       # Step 5: Connect the slider to the line edit
  #       self.slider.valueChanged.connect(self.update_line_edit)

  # def update_line_edit(self, value):
  #       self.text19.setText(str(value))


  # def update_slider(self):
  #   try:
  #       # value = float(self.text.toPlainText())
  #       # self.slider.setValue(value)
  #       # value2 = float(self.text2.text())
  #       # self.slider_2.setValue(value2)
  #       # value3 = float(self.text3.text())
  #       # self.slider_3.setValue(value3)
  #       value = int(self.text4.text())
  #       self.slider_4.setValue(value)
  #       value = int(self.text5.text())
  #       self.slider_5.setValue(value)
  #       value = int(self.text6.text())
  #       self.slider_6.setValue(value)
  #       value = int(self.text7.text())
  #       self.slider_7.setValue(value)
  #       value = int(self.text8.text())
  #       self.slider_8.setValue(value)
  #       value = int(self.text9.text())
  #       self.slider_9.setValue(value)
  #       value = int(self.text10.text())
  #       self.slider_10.setValue(value)
  #       value = int(self.text11.text())
  #       self.slider_11.setValue(value)
  #       value = int(self.text12.text())
  #       self.slider_12.setValue(value)
  #   except ValueError:
  #       pass

  # def slide(self):
  #           sli1 = str(self.slider.value())
  #           sli2 = str(self.slider_2.value())
  #           sli3 = str(self.slider_3.value())
  #           sli4 = str(self.slider_4.value())
  #           sli5 = str(self.slider_5.value())
  #           sli6 = str(self.slider_6.value())
  #           sli7 = str(self.slider_7.value())
  #           sli8 = str(self.slider_8.value())
  #           sli9 = str(self.slider_9.value())
  #           sli10 = str(self.slider_10.value())
  #           sli11 = str(self.slider_11.value())
  #           sli12= str(self.slider_12.value())
  #           self.text.setText(sli1)
  #           self.text2.setText(sli2)
  #           self.text3.setText(sli3)
  #           self.text4.setText(sli4)
  #           self.text5.setText(sli5)
  #           self.text6.setText(sli6)
  #           self.text7.setText(sli7)
  #           self.text8.setText(sli8)
  #           self.text9.setText(sli9)
  #           self.text10.setText(sli10) 
  #           self.text11.setText(sli11)
  #           self.text12.setText(sli12)

  def gotojogaction(self):
    text=self.text.text()
    text2=self.text2.text()
    text3=self.text3.text()
    text4=self.text4.text()
    text5=self.text5.text()
    text6=self.text6.text()
    print("JOG AXIS :{",text,text2,text3,text4,text5,text6,"}")

  def gotojoglinear(self):
    text8=self.text8.text()
    text7=self.text7.text()
    text9=self.text9.text()
    print("JOG LINEAR :{",text7,text8,text9,"}")

  def gotojogreorient(self):
    text10=self.text10.text()
    text12=self.text11.text()
    text11=self.text12.text()
    print("JOG REORIENT :{",text10,text11,text12,"}")

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  # def gotoaievent(self):
  #   aieventy=AIevent()
  #   widget.addWidget(aieventy)
  #   widget.setCurrentIndex(widget.currentIndex()+1) 
  

class programuser(QDialog):
  def __init__(self):
    super(programuser,self).__init__()
    loadUi("user_auto.ui",self)
    self.hmmenubtn9.clicked.connect(self.gotohomeuser)
    self.prgautobtn9.clicked.connect(self.gotoevent)
    self.jogybtn9.clicked.connect(self.gotojogging)
    self.userbtn7.setStyleSheet("background-color: #00FF00; color: #ffffff;")
    self.saveButton.clicked.connect(self.save_text)
    self.loadButton.clicked.connect(self.load_text)
    self.file_content = ""
        # Create a variable to store the file content
   

  def save_text(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            # Get the content from the QTextEdit widget
            content = self.texting.toPlainText()

            if content:
                self.file_content = content
                # You can use self.file_content in your program as needed
                self.texting.clear()  # Clear the QTextEdit widget after saving
                
  def load_text(self):
        if self.file_content:
            # Set the content stored in self.file_content to the QTextEdit widget
            self.texting.setPlainText(self.file_content)

  #   self.saveButton.clicked.connect(self.save_file)
  #   self.openButton.clicked.connect(self.open_file)

  # def save_file(self):
  #       text = self.texting.toPlainText()
  #       options = QFileDialog.Options()
  #       file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
  #       if file_name:
  #           with open(file_name, 'w') as file:
  #               file.write(text)

  # def open_file(self):
  #       options = QFileDialog.Options()
  #       file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
  #       if file_name:
  #           with open(file_name, 'r') as file:
  #               text = file.read()
  #               self.texting.setPlainText(text)

  def gotohomeuser(self):
     hmmuser=homeuser()
     widget.addWidget(hmmuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  # def gotoautouser(self):
  #    autouuser=autouser()
  #    widget.addWidget(autouuser)
  #    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotoevent(self):
    eventing=Event()
    widget.addWidget(eventing)
    widget.setCurrentIndex(widget.currentIndex()+1)

class user_menu(QDialog):
  def __init__(self):
    super(user_menu,self).__init__()
    loadUi("program_user_menu.ui",self)
    self.calibratebtn6.clicked.connect(self.gotocaliber)
    self.joggingbtn3.clicked.connect(self.gotojogging)
    # self.aieventbtn4.clicked.connect(self.gotoaievent)
    self.hmmenubtn8.clicked.connect(self.gotohome)
    self.jogybtn8.clicked.connect(self.gotojogging)
    self.prguserbtn8.clicked.connect(self.gotouserprogram)
    self.userbtn9.setStyleSheet("background-color: #00FF00; color: #ffffff;")
   

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)
    
class Event(QDialog):
  def __init__(self):
    super(Event,self).__init__()
    loadUi("program_user.ui",self)
    self.programmenubtn3.clicked.connect(self.gotousermenu)
    self.hmmenubtn7.clicked.connect(self.gotoautouser)
    self.jogybtn7.clicked.connect(self.gotojogging)
    self.prguserbtn7.clicked.connect(self.gotouserprogram)
    self.autobtn8.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  #   self.hmmenubtn9.clicked.connect(self.gotoautouser)
  #   self.prgautobtn9.clicked.connect(self.gotoevent)
  #   self.jogybtn9.clicked.connect(self.gotojogging)
  #   self.autobtn7.setStyleSheet("background-color: #00FF00; color: #ffffff;")

  # def gotoautouser(self):
  #    autouuser=autouser()
  #    widget.addWidget(autouuser)
  #    widget.setCurrentIndex(widget.currentIndex()+1)  

  # def gotojogging(self):
  #   jog=Jogging()
  #   widget.addWidget(jog)
  #   widget.setCurrentIndex(widget.currentIndex()+1)  

  # def gotoevent(self):
  #   eventing=Event()
  #   widget.addWidget(eventing)
  #   widget.setCurrentIndex(widget.currentIndex()+1)

  def gotoautouser(self):
     autouuser=autouser()
     widget.addWidget(autouuser)
     widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotousermenu(self):
    prgmuser1=user_menu()
    widget.addWidget(prgmuser1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1)



# class event_menu(QDialog):
#   def __init__(self):
#     super(event_menu,self).__init__()
#     loadUi("eventlog_menu.ui",self)
#     self.programbtn5.clicked.connect(self.gotouserprogram)
#     self.calibratebtn7.clicked.connect(self.gotocaliber)
#     self.joggingbtn4.clicked.connect(self.gotojogging)
#     self.aieventbtn5.clicked.connect(self.gotoaievent)
#     self.hmmenubtn10.clicked.connect(self.gotohome)

#   def gotohome(self):
#     hoom1=Home()
#     widget.addWidget(hoom1)
#     widget.setCurrentIndex(widget.currentIndex()+1)  

#   def gotojogging(self):
#     jog=Jogging()
#     widget.addWidget(jog)
#     widget.setCurrentIndex(widget.currentIndex()+1) 

#   def gotocaliber(self):
#     caliber=Calibrate()
#     widget.addWidget(caliber)
#     widget.setCurrentIndex(widget.currentIndex()+1) 

#   def gotouserprogram(self):
#     prouser=programuser()
#     widget.addWidget(prouser)
#     widget.setCurrentIndex(widget.currentIndex()+1) 

  # def gotoaievent(self):
  #   aieventy=AIevent()
  #   widget.addWidget(aieventy)
    # widget.setCurrentIndex(widget.currentIndex()+1) 

class AIevent(QDialog):
  def __init__(self):
    super(AIevent,self).__init__()
    loadUi("AI.ui",self)
    self.aimenubtn3.clicked.connect(self.gotoaimenu)
    self.homebtn1.clicked.connect(self.gotohome)

  def gotoaimenu(self):
    aievent=ai_menu()
    widget.addWidget(aievent)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1) 


class ai_menu(QDialog):
  def __init__(self):
    super(ai_menu,self).__init__()
    loadUi("AI_menu.ui",self)
    self.programbtn6.clicked.connect(self.gotouserprogram)
    self.calibratebtn8.clicked.connect(self.gotocaliber)
    self.joggingbtn5.clicked.connect(self.gotojogging)
    # self.eventlogbtn6.clicked.connect(self.gotoevent)
    self.hmmenubtn11.clicked.connect(self.gotohome)

  def gotojogging(self):
    jog=Jogging()
    widget.addWidget(jog)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def gotohome(self):
    hoom1=Home()
    widget.addWidget(hoom1)
    widget.setCurrentIndex(widget.currentIndex()+1)  

  def gotocaliber(self):
    caliber=Calibrate()
    widget.addWidget(caliber)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  def gotouserprogram(self):
    prouser=programuser()
    widget.addWidget(prouser)
    widget.setCurrentIndex(widget.currentIndex()+1) 

  # def gotoevent(self):
  #   eventing=Event()
  #   widget.addWidget(eventing)
  #   widget.setCurrentIndex(widget.currentIndex()+1)

app=QApplication(sys.argv)
mainwindow=Main()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(2000)
widget.setFixedHeight(1000)
widget.show()
app.exec_()