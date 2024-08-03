import fitz  # PyMuPDF
import os

def save_pdf_pages_as_png(pdf_path, output_folder):
    # Check if the PDF file exists
    if not os.path.isfile(pdf_path):
        print(f"The file {pdf_path} does not exist.")
        return
    
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        # Render page to an image
        pix = page.get_pixmap()
        # Save the image as PNG
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(image_path)
        print(f"Saved {image_path}")
    
    # Close the PDF file
    pdf_document.close()
    print("All pages have been saved as PNG images.")

if __name__ == "__main__":
    # pdf_path = input("Enter the path to the PDF file: ")
    # output_folder = input("Enter the output folder path: ")
    pdf_path = r"C:\Users\razer\Downloads\DRONE.pdf"
    output_folder = r"C:\Users\razer\Desktop\DRONE"
    save_pdf_pages_as_png(pdf_path, output_folder)
