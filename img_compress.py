import re
import os
import shutil
from PIL import Image


def resize_images(dir: str, output_dir: str, size: int, quality: int) -> None:
    # Define a regular expression pattern to match filenames ending with .jpg or .jpeg
    pattern = re.compile(r"(-|_).*(\.jpg|\.jpeg)$")
    # Change the current directory to the directory containing the images
    os.chdir(dir)
    # Iterate over all files in the current directory
    for filename in os.scandir(dir):
        # Check if the current item is a file and its name matches the defined pattern
        if filename.is_file() and re.search(pattern, filename.name):
            # Check the size of the image file and compress it if necessary
            check_image_size(filename.name, size, quality)
            # Move the compressed image file to the output directory
            shutil.move(
                os.path.join(dir, filename.name),
                os.path.join(output_dir, filename.name),
            )


def check_image_size(file_path: str, size: int, quality: int) -> None:
    # Get the current size of the image file
    current_size = os.stat(file_path).st_size
    # Continue compressing as long as the image size is greater than the target size or quality is zero
    while current_size > size or quality == 0:
        # If quality is zero, delete the image file and print a message
        if quality == 0:
            os.remove(file_path)
            print("File cannot be compressed to defined size")
            break
        # Compress the image file with the current quality
        compress_image(file_path, quality)
        # Update the current size of the image file
        current_size = os.stat(file_path).st_size
        # Reduce the quality for the next compression iteration
        quality -= 5


def compress_image(file_path: str, quality: int) -> int:
    # Open the image file
    image = Image.open(file_path)
    # Save the image in JPEG format with optimization enabled and the specified quality
    image.save(file_path, "JPEG", optimize=True, quality=quality)
    # Get the size of the compressed image file
    compressed_size = os.stat(file_path).st_size
    # Return the size of the compressed image file
    return compressed_size
