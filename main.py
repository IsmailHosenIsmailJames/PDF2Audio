from lib.processAudio.processAudio import combineAudioFiles
from lib.process_pdf.isPDFTextBased import is_PDF_text_based
from lib.process_pdf.convertPDFtoImage import converFullPDFToImage
from lib.tesseract.getTextFromImage import getTestFromImage
import gtts
import os
import time
import shutil

def main():
    pdfPath = input("Give the path of PDF : ")
    info = is_PDF_text_based(pdfPath)
    images = converFullPDFToImage(pdfPath)
    audios = []
    os.makedirs("tem/audio", exist_ok=True)
    for i in range(len(images)):
            text = getTestFromImage(images[i])
            text = text.replace("\n" , " ")
            if(len(text) < 5): continue 
            audio = gtts.gTTS(text=text, lang="bn", slow= False )
            audios.append(audio)
            audio.save(f"tem/audio/{i}.mp3")
            time.sleep(5)
            print(i, " Page is Done.")
            
    
    combineAudioFiles(folder_path= "tem/audio/",saveName= "অরক্ষিত_স্বাধীনতাই_পরাধীনতা")
    shutil.rmtree("tem/")

if __name__ == '__main__':
    main()
