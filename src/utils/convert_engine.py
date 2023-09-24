from PIL import Image
from src.ui.error import erroors as error_page
from src.utils.vars import COMPATIBLE_FORMAT as FORMATS
from random import choice
from threading import Thread


def generate() -> str:
    """Generate random string for file name"""
    return "".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6))



def convert_threaded(file_path: str, save_path: str, secrets:str) -> None:
    """SAME AS convert_image() BUT RUNS IN A THREAD"""
    try:
        worker1 = Thread(target=convert_image, args=(file_path, save_path, secrets))
        worker1.start()
        worker1.join()
    except Exception as E:
        error_page(str(E))


def convert_image(file_path: str, save_path: str, secrets:str) -> None: 
    """Converts image to desired format

    Args:
        file_path (str): Path to file to convert
        file_format (str): Format to convert to
        save_path (str): Path to save converted file
    """
    
    name: str = generate()
    print(secrets)
    save_path = save_path + "/" + name + "_Transf" + secrets
    try:
        img = Image.open(file_path)
        extension = img.format
        if extension not in FORMATS:
            error_page("Invalid file format | File format not supported")
        else:
            img.save(save_path)
            del img 
            del save_path
    except Exception as E:
        error_page(str(E))