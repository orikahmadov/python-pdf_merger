"""GUI Program to merge PDF files."""


import PySimpleGUI as sg
import os, sys, datetime
from PyPDF2 import PdfFileMerger
import hashlib


def merge_pdfs(pdf_files, output_file):
    """Merge PDF files."""
    path = os.path.dirname(output_file)
    if not os.path.exists(path):
        os.makedirs(path)
    merger = PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()


# Create the window
def create_window():
    """This function creates the window for the GUI program"""
    sg.theme('DarkAmber')
    layout = layout_gui()
    window = sg.Window('Merge PDF Files', layout, size=(600, 300), element_justification='center')
    return window

def layout_gui():
    """This function defines the layout of the GUI program"""
    layout = [
        [sg.Text('Merge PDF Files', font=('Helvetica', 24))],
        [sg.Text('Select PDF Files to Merge', font=('Helvetica', 15))],
        [sg.InputText(key='-IN-'), sg.FilesBrowse('Select PDF Files', file_types=(('PDF Files', '*.pdf'),))],
        [sg.Text('Name your export folder', font=('Helvetica', 15))], # Export file name label
        [sg.InputText(key='-OUT-'), sg.FolderBrowse('Select Output Folder')],
        [sg.Button('Merge PDF Files', font=('Helvetica', 15)), sg.Button('Exit', font=('Helvetica', 15))]
    ]
    return layout



def main():
    """ Main function for GUI program will run until user exits program.
     User will select PDF files to merge and name the output file """
    window = create_window()
    random_hash = hashlib.sha256(str(datetime.datetime.now()).encode('utf-8')).hexdigest()[:25]
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Merge PDF Files':
            files = values['-IN-']
            output = values['-OUT-'] 
            if output: #if output folder selected,
                output = os.path.join(output, '{}.pdf'.format(random_hash))
            else: #if no output folder selected, write to current working directory
                output = os.path.join(os.getcwd(), '{}.pdf'.format(random_hash))
            if files:#if files selected
                files = files.split(';')
                merge_pdfs(files, output)
                sg.popup('PDF Files Merged', 'PDF Files saved to: {}'.format(output))
            else:
                sg.popup('No Files Selected', 'Please select PDF files to merge')
            
        


if __name__ == '__main__':
    main()
