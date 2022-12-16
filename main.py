import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QVBoxLayout,QFileDialog
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
import csv
import pywhatkit



class CreateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.window_title = "Process File.."
        self.label_file_name=QLineEdit('Select a file...')
        self.label_image_file_name=QLineEdit('Select a image...')
        verticalbox = QVBoxLayout()
        verticalbox.addWidget(QLabel("Files:"))
        verticalbox.addWidget(self.label_file_name)
        verticalbox.addWidget(self.label_image_file_name)

        horizontalbox = QHBoxLayout()
        horizontalbox.addStretch()  # aligns other box contents to the right
        button_open = QPushButton("Open file..")
        button_open.clicked.connect(self.select_file)
        button_open.setFixedWidth(120)

        button_open_image = QPushButton("Open image..")
        button_open_image.clicked.connect(self.select_image_file)
        button_open_image.setFixedWidth(120)
        
        
        horizontalbox.addWidget(button_open)
        horizontalbox.addWidget(button_open_image)
        self.button_send = QPushButton("Send..")
        self.button_send.setFixedWidth(120)
        self.button_send.clicked.connect(self.load_file)
        horizontalbox.addWidget(self.button_send)

        verticalbox.addLayout(horizontalbox)
        verticalbox.addStretch()  # aligns other box contents to the top

        self.setLayout(verticalbox)

    def select_file(self):
        self.Dialog=QFileDialog()
        self.file_name=self.Dialog.getOpenFileName(self,("Select a text file"), "/home/", ("CSV Files (*.csv)"))        
        self.label_file_name.setDisabled(True)
        self.button_send.setEnabled(True)
        self.full_filename=self.file_name[0]
        self.label_file_name.setText(self.full_filename)

    def select_image_file(self):
        self.Dialog=QFileDialog()
        self.image_file_name=self.Dialog.getOpenFileName(self,("Select a image"), "/home/", ("Image Files (*.png *.jpg *.bmp)"))        
        self.label_image_file_name.setDisabled(True)
        self.button_send.setEnabled(True)
        self.full_image_filename=self.image_file_name[0]
        self.label_image_file_name.setText(self.full_image_filename)

    def load_file(self):
        with open(self.full_filename, 'r', encoding='utf-8-sig') as csvfile:
            fields = []
            rows = []
            csvreader = csv.reader(csvfile)
            # extracting each data row one by one
            for row in csvreader:


                rows.append(row)
                phone_number='+52' + row[0]
                message=row[1]
                #pywhatkit.sendwhatmsg('+' + row[0], row[1], 18, 55, 15, True, 2)
                print(phone_number +' -> ' + message )
                print(self.full_image_filename)
               # pywhatkit.sendwhatmsg_instantly('+52' + phone_number,message,5,True,2)
                pywhatkit.sendwhats_image(phone_number, self.full_image_filename,message)

        self.label_file_name.setText("Done")
        self.label_image_file_name.setText("This too")
        self.button_send.setDisabled(True)

app = QApplication(sys.argv)
dialog = CreateDialog()
dialog.show()

app.exec_()