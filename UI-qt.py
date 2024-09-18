import sys
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import fitz 

# Test PDF Paths - 
# D:/College/Branding/Assets/SIT Brand Specifications/SIT_NGPR_1.pdf
# D:/College/Branding/Assets/SIT Brand Specifications/SIT_NGPR_2.pdf
# 

# --------- Helper Functions -------------
def open_pdfs(file_paths):
    """ Open PDF files from the provided file paths. """
    pdf_list = []
    for path in file_paths:
        pdf_list.append(fitz.open(path))
    return pdf_list

def close_pdfs(pdf_list):
    """ Close the opened PDF files. """
    for pdf in pdf_list:
        pdf.close()

# --------- PDF Functions -------------

def merge_pdfs(file_paths):
    """ Merge multiple PDF files into one. """
    pdf_list = open_pdfs(file_paths)
    output_pdf = fitz.open()

    for pdf in pdf_list:
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            output_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)

    output_file = widgets.QFileDialog.getSaveFileName(
        caption="Save Merged PDF", filter="PDF Files (*.pdf)")[0]
    
    if output_file:
        output_pdf.save(output_file)
        output_pdf.close()
    close_pdfs(pdf_list)

def merge_pdfs(file_paths):
    pass



# -------------- UI -------------------
class MyApp(widgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PDF Manager")
        self.setWindowIcon(gui.QIcon("D:/Projects/Illustrator Projects/Fishy - Logo/2x/V2@2x.png"))
        self.setGeometry(100, 100, 400, 200)

        # Button for merging PDFs
        mergeButton = widgets.QPushButton("Merge PDFs", self)
        mergeButton.clicked.connect(lambda: self.browse_files("s to merge"))

        # Button for splitting a PDF
        splitButton = widgets.QPushButton("Split PDF", self)
        splitButton.clicked.connect(lambda: self.browse_files(" to split"))

        # Layout setup
        layout = widgets.QVBoxLayout()
        layout.addWidget(mergeButton)
        layout.addWidget(splitButton)

        container = widgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_files(self, trail):
        """ Browse for PDF files. """
        file_paths, _ = widgets.QFileDialog.getOpenFileNames(
            self, f"Select PDF{trail}", "", "PDF Files (*.pdf)"
        )
        if file_paths:
            merge_pdfs(file_paths)

# Main execution
if __name__ == '__main__':
    app = widgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
