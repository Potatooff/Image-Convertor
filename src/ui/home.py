# Crates
import customtkinter as c
from src.ui.error import erroors as error_page
from src.utils.vars import COMPATIBLE_FORMAT as FORMAT
from src.ui.file_explorer import open_file_explorer, open_folder_explorer
from src.utils.convert_engine import convert_threaded


class ConvertingFrame(c.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=120, corner_radius=10)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=0)

        self.secret = ""
        self.convert_from_file = c.StringVar()
        self.convert_to_file = c.StringVar()
        self.convert_to_fil = c.StringVar()

        self.convert_from = c.CTkOptionMenu(self, dynamic_resizing=False, values=FORMAT, corner_radius=10, fg_color="black", button_color="black",
                                            button_hover_color="black", height=35)
        self.convert_from.grid(row=0, column=0, padx=15, pady=(10, 10))


        self.label_indicator = c.CTkLabel(self, text="TO", font=("Arial", 15))
        self.label_indicator.grid(row=0, column=1, padx=15, pady=(10, 10))

        self.convert_to = c.CTkOptionMenu(self, dynamic_resizing=False, values=FORMAT, corner_radius=10, fg_color="black", button_color="black",
                                          button_hover_color="black", height=35, variable=self.convert_to_file)
        self.convert_to.grid(row=0, column=2, padx=15, pady=(10, 10))

        self.convert_from_path = c.CTkButton(self, text="FILE TO CONVERT", corner_radius=10, fg_color="black", hover_color="black", height=35, command=self.convert_from_event)
        self.convert_from_path.grid(row=1, column=0, padx=15, pady=10, sticky="nsew")

        self.label_indicator = c.CTkLabel(self, text="SAVE TO", font=("Arial", 15))
        self.label_indicator.grid(row=1, column=1, padx=15, pady=(10, 10))

        self.convert_to_path = c.CTkButton(self, text="SAVE FOLDER", corner_radius=10, fg_color="black", hover_color="black", height=35, command=self.convert_to_event)
        self.convert_to_path.grid(row=1, column=2, padx=15, pady=10, sticky="nsew")

        self.convert_all = c.CTkButton(self, text="CONVERT", corner_radius=10, fg_color="black", hover_color="black", height=35, command=self.convert_all_event)
        self.convert_all.grid(row=2, column=1, padx=15, pady=10, sticky="nsew")


    def convert_from_event(self):
        """FILE PATH FOR FILE TO CONVERT FROM"""

        try:
            self.convert_from_file.set(open_file_explorer())            
        except Exception as E:
            error_page(str(E))


    def convert_to_event(self):
        """FILE PATH FOR FILE TO CONVERT TO"""

        try:
            foo = []
            foo.append(open_folder_explorer())
            self.secret = "." + self.convert_to_file.get().lower()
            path = "".join(foo)
            self.convert_to_fil.set(path)
        except Exception as E:
            error_page(str(E))

    def convert_all_event(self):
        """CONVERT CHOSEN IMAGE"""

        um = self.convert_from_file.get()
        u1 = self.convert_to_fil.get()
        if um == "NO FILE SELECTED":
            error_page("Please select a file to convert!")
        elif u1 == "NO FOLDER SELECTED":
            error_page("Please select a folder to save converted file!")
        else:
            try:
                convert_threaded(file_path=um, save_path=u1, secrets=self.secret)
            except Exception as E:
                error_page(str(E))

class MainWindow(c.CTk):
    def __init__(self) -> None:
        """ THIS IS THE MAIN WINDOW!"""

        super().__init__()

        self.title(f"POTATO Image Convertor v1.0.0") # Title of the window
        self.geometry(f"{560}x{205}") # Size of the window
        self.resizable(False, False) # Disable resizing window option
        self.grid_rowconfigure((0), weight=1) # forget this shet
        self.grid_columnconfigure((0), weight=1) # forget this shet


        self.main = c.CTkFrame(self) # A Frame to be able to change bg or something else
        self.main.grid(row=0, column=0, sticky="nsew")   # Position on grid
        self.main.grid_rowconfigure((0, 1, 2), weight=0) # row grid layout
        self.main.grid_columnconfigure((0, 1, 2), weight=0) # column grid layout

        self.ConvertingSettingF = ConvertingFrame(self.main)
        self.ConvertingSettingF.grid(row=0, column=0, columnspan=3, padx=25, pady=20, sticky="nsew")
