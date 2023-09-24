# CRATES
from tkinter import filedialog
from src.utils.vars import COMPATIBLE_FORMAT_TUPLE as FORMAT
from src.ui.error import erroors as error_page


def open_file_explorer()->str | int:

    """Function to open the file explorer only image files + folders"""
    try:
        file_path = filedialog.askopenfilename(title="CHOOSE AN IMAGE", filetypes=[FORMAT])
        if file_path:
            return file_path
        else:
            return "NO FILE SELECTED"
    except Exception as E:
            error_page(str(E))


def open_folder_explorer() -> str | int :
    
    """Function to open the file explorer only folders"""
    try:
        folder_path = filedialog.askdirectory()
        if folder_path:
            return folder_path
        else:
            return "NO FOLDER SELECTED"
    except Exception as E:
            error_page(str(E))