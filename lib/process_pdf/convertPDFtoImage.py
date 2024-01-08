from pdf2image import convert_from_path

def converFullPDFToImage(path:str):
    pages = convert_from_path(path, dpi=300)
    images = []
    for page in pages:
        images.append(page)
    
    return images
