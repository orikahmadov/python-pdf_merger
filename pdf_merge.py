
import argparse, os 
from PyPDF2 import PdfFileMerger
import hashlib
import datetime


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
    

    



def main():
    random_hash = hashlib.sha256(str(datetime.datetime.now()).encode('utf-8')).hexdigest()[:25]
    parser = argparse.ArgumentParser(description='Merge 2 or more pdfs', add_help=True, prog="merge_pdfs.py", usage='%(prog)s [options] pdf1 pdf2 . . .' )
    parser.add_argument("-f", "--file", help="pdf files to merge", required=True, nargs='+')
    parser.add_argument("-o", "--output", help="output file name", required=False,default=str(random_hash)+".pdf")
    parser.add_argument("-p", "--path", help="path to pdf files", required=False)

    args = parser.parse_args()
    files = args.file
    output = args.output
    path = args.path

    if path:
        files = [os.path.join(path, file) for file in files]
        output = os.path.join(path, output)
    else:
        files = [os.path.abspath(file) for file in files]
        output = os.path.abspath(output)

    merge_pdfs(files, output)

    




if __name__ == '__main__':
    main()