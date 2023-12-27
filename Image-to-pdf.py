
# Importing Modules
import img2pdf
from PIL import Image

# Due to logic issue. This program is only converting .png images to PDF.
 
try:
    # Giving Images Location in python list. You can add Single or Multiple Images path in the list based on your requirements.
    Images_Location = ["E:\Image-to-PDF\Boat.png", "E:\Image-to-PDF\Car.png"]
    
    # Giving Location to save PDF. And also give 'PDF file Name'..
    pdf_path = "E:\Image-to-PDF\ImagesPDF.pdf"
    
    # Opening Images
    for TotalImages in Images_Location:
        image = Image.open(TotalImages)
    
    # Converting Images into Chunks using img2pdf module.
    pdf_bytes = img2pdf.convert(Images_Location)
    
    # Opening and Creating PDF.
    file = open(pdf_path, "wb")
    
    # Writing PDF files with Chunks
    file.write(pdf_bytes)
    
    # Closing images
    image.close()
    
    # closing PDF file
    file.close()
    
    # Showing a message to the User.
    print("Images converted into PDF successfully")

except:
    print('Sorry unable to convert your images into PDF!')