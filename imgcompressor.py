from PIL import Image
from tkinter import Tk, filedialog

def compress_image(input_path, output_path, quality=85):
    try:
        
        with Image.open(input_path) as img:
            
            img.save(output_path, 'JPEG', quality=quality)
            print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    root = Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"))]
    )

    return file_path


input_image_path = open_file_dialog()

if input_image_path:
    output_image_path = 'path/to/your/output/compressed_image.jpg'
    compress_image(input_image_path, output_image_path)
else:
    print("No file selected.")
