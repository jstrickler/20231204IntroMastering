import sys
import os
from subprocess import run  # for running external PDF viewer
import requests

url = 'https://smd-cms.nasa.gov/wp-content/uploads/2023/10/Exoplanets_Coloring_Book_07-22-2016.pdf'  # target URL
saved_pdf_file = 'nasa_coloring_book.pdf'  # name of PDF file for saving

response = requests.get(url)  # open the URL
if response.status_code == requests.codes.OK:  # check status code
    if response.headers.get('content-type').startswith('application/pdf'):
        with open(saved_pdf_file, 'wb') as pdf_out:  # open local file
            pdf_out.write(response.content)  # write data to a local file in binary mode; response.content is data from URL

        if sys.platform == 'win32':  # select platform and choose the app to open the PDF file
            cmd = saved_pdf_file
        elif sys.platform == 'darwin':
            cmd = 'open ' + saved_pdf_file
        else:
            cmd = 'acroread ' + saved_pdf_file

        run(cmd, shell=True)  # run command with command.exe or Mac/Linux shell
