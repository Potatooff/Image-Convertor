# Crates
from typing import  Tuple
import customtkinter as c


# Error var
error_text: list = []


class Errors(c.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        """ERROR WINDOW"""
        super().__init__(fg_color, **kwargs)

        self.title("ERROR PAGE")
        self.geometry(f"{500}x{300}")
        self.resizable(False, False)    
        
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = c.CTkLabel(self, text_color="red", text=error_text[-1])
        self.label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

        self.ok = c.CTkButton(self, text="OK", command=self.destroy, fg_color="transparent", hover_color="black")
        self.ok.grid(row=1, column=1, padx=20, pady=20, sticky="s")

    
def insert_newlines(text, line_length=48):
    """AFTER 48 CHARACTERS, IT WILL ADD A NEW LINE!"""

    lines = []
    for i in range(0, len(text), line_length):
        lines.append(text[i:i + line_length])
    return '\n'.join(lines)


def erroors(text: str) -> None:

    """THIS WILL THROW THE ERROR PAGE!"""
    text = f"AN ERROR OCCURED:\n{text}"
    error_text.append(insert_newlines(text))
    Errors().mainloop()
