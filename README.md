# python-pdf_merger
A simple command-line tool to merge two or more PDF files into a single PDF file. 

Installation
To install the required dependencies, run:

Copy code
pip install -r requirements.txt
Usage
To merge two or more PDF files, run:


python merge_pdfs.py -f pdf1 pdf2 ...
This will generate a random hash as the output file name. To specify a custom output file name, use the -o or --output option:


python merge_pdfs.py -f pdf1 pdf2 ... -o output.pdf
You can also specify a path to the PDF files using the -p or --path option:


python merge_pdfs.py -f pdf1 pdf2 ... -o output.pdf -p path/to/pdfs
Arguments
The merge_pdfs.py script accepts the following arguments:

-f, --file: Required. The PDF files to merge.
-o, --output: Optional. The name of the output PDF file. If not specified, a random hash will be generated as the output file name.
-p, --path: Optional. The path to the PDF files.
Dependencies
This script requires the following Python packages:

argparse
PyPDF2
datetime
hashlib
