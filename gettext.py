#!C:\Python27\python.exe
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

# main
def main(fname):
    # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    outdir = None
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = None

    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)

    outtype = 'text'
	
    #here i redirect the output to file
    f = open('file', 'w')
	
    if outtype == 'text':
        device = TextConverter(rsrcmgr, f, codec=codec, laparams=None)
   
    fp = file(fname, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True)
    fp.close()
    device.close()

    f.close()
    return

