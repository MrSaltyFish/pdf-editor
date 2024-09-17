import fitz
import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("PyQt6 Example")

        # Set the window dimensions
        self.setGeometry(100, 100, 400, 300)

        # Create a QPushButton
        button = QPushButton("Click Me", self)
        button.setGeometry(100, 100, 200, 50)  # Position the button (x, y, width, height)

        # Connect the button to a function
        button.clicked.connect(start())


def start():
    userInput = input("""What do you want to do?:
        1. Merge 2 PDFs
        2. Split a PDF
        """)
    match userInput:
        case 1:
            merge_pdfs()
        case 2:
            split_pdf()


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



app = QApplication(sys.argv)

# Create an instance of MainWindow
window = QMainWindow()
window.show()

# Start the application's event loop
sys.exit(app.exec())