import re
import os
import shutil
from PIL import Image


def resize_images(dir: str, output_dir: str, size: int, quality: int) -> None:
    pattern = re.compile(r"(-|_).*(\.jpg|\.jpeg)$")
    os.chdir(dir)
    for filename in os.scandir(dir):
        if filename.is_file() and re.search(pattern, filename.name):
            check_image_size(filename.name, size, quality)
            shutil.move(
                os.path.join(dir, filename.name),
                os.path.join(output_dir, filename.name),
            )


def check_image_size(file_path: str, size: int, quality: int) -> None:
    current_size = os.stat(file_path).st_size
    while current_size > size or quality == 0:
        if quality == 0:
            os.remove(file_path)
            print("File cannot be compressed to defined size")
            break

        compress_image(file_path, quality)
        current_size = os.stat(file_path).st_size
        quality -= 5


def compress_image(file_path: str, quality: int) -> int:
    image = Image.open(file_path)
    image.save(file_path, "JPEG", optimize=True, quality=quality)
    compressed_size = os.stat(file_path).st_size
    return compressed_size
