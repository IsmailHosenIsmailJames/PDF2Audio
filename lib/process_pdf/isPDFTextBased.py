import fitz  # PyMuPDF

def is_PDF_text_based(path:str)-> dict:
    pdf_file = fitz.open(path)
    isPageContainsText = dict()
    for page_no in range(len(pdf_file)):
        text = pdf_file[page_no].get_text("text")
        isTextLong = len(text) > 50
        if text:
            isPageContainsText[page_no] = {
                "isTextContains" : True,
                "text":text,
                "isTextLong":isTextLong
                }
            
        else:
            isPageContainsText[page_no] = {
                "isTextContains" : False,
                "text":"",
                "isTextLong":isTextLong
            }
    
    return isPageContainsText
