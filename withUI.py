import sys
import fitz
import PyQt6.QtWidgets as widget
import PyQt6.QtGui as gui

"""
def start():
    userInput = input(What do you want to do?:
        1. Merge 2 PDFs
        2. Split a PDF
        )
    match userInput:
        case 1:
            merge_pdfs()
        case 2:
            split_pdf()
"""

def input_pdf(input_count):
    pdf_list = []
    if input_count <= 0:
        print("No need to open a PDF.")
    elif input_count == 1:
        pdf_list[0] = input("Enter the path to PDF file: ")
    else:
        for i in range(0, input_count):
            pdf_list[i] = input(f"Enter the path to PDF file #{i}: ")



def merge_pdfs():
    count = input("How many PDFs to merge?")
    input_paths = input_pdf(count)

    try:
        pdf_document = []
        for i in range(0, count):
            pdf_document[i] = fitz.open(input_paths[i])
    except FileNotFoundError as e:
        print("File not found. Error: ", e)
        sys.exit()

    merged_pdf_document = fitz.open()

    for i in range(0, count):
        merged_pdf_document.insert_pdf(pdf_document[i])

    merged_pdf_document.save("result.pdf")
    merged_pdf_document.close()
    print("PDF created successfully!")

def split_pdf():
    input_paths = input_pdf(1)

def abc():
    input_paths = input_pdf(1)



# The main part of the program
app = widget.QApplication(sys.argv)

# Setting up the window
window = widget.QMainWindow()
window.setWindowIcon(gui.QIcon('L:/Fishy - Logo/2x/V2@2x.png'))
window.setWindowTitle("PDF Manager")
window.setGeometry(960, 540, 400, 300)
central_widget = widget.QLabel("")
window.setCentralWidget(central_widget)
window.show()



# Creating widgets
mergeButton = widget.QPushButton("Merge PDFs")
mergeButton.clicked.connect(merge_pdfs)
splitButton = widget.QPushButton("Split PDF")
splitButton.clicked.connect(split_pdf)
abcButton = widget.QPushButton("abc")
abcButton.clicked.connect(abc)

# Defining Layout Structure
hLayout1 = widget.QHBoxLayout()
hLayout2 = widget.QHBoxLayout()
vLayout = widget.QVBoxLayout()

# Adding widgets to layouts
hLayout1.addWidget(mergeButton)
hLayout1.addWidget(splitButton)
hLayout2.addWidget(abcButton)

vLayout.addLayout(hLayout1)
vLayout.addLayout(hLayout2)

central_widget.setLayout(vLayout)

sys.exit(app.exec())
