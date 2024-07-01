import random
import customtkinter
import tkinter
""" password style : 
                    characters : 8 (1 Capitalized and 7 lowercase)
                    special symbols : one in this list : [!, @, #, $, %, ^, &, *, <, >, ?, /, |]
                    numbers : 3
"""
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Main(customtkinter.CTk):
    def __init__(self):
        self.password = ''
        super().__init__()

    def generate_password(self):
        # Ascii Values = A: 65 - Z: 90 and a:97 - z: 122
        cap_letter = chr(random.randint(65, 90))
        low_letter = [(chr(random.randint(97, 122))) for i in range (7)]
        special_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?', '/', '|', '_', '-', '~']
        num = [str(random.randint(0, 9)) for i in range (3)]
        self.password = cap_letter + ''.join(low_letter) + random.choice(special_symbol) + ''.join(num)

        self.entry.delete(0, tkinter.END)
        self.entry.insert(0, self.password)
    
    def GUI(self):
        self.title("Password Generator")
        width_of_window = 400
        height_of_window = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))                  #Open windows only center of screen

        self.resizable(False, False)
        self.configure(bg="black")

        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure((1), weight=0)
        self.grid_rowconfigure((0, 1), weight=0)
        
        self.label = customtkinter.CTkLabel(self, text="Password Generator", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label.grid(column=0, row=0, sticky='nsew', pady=10)

        self.entry = customtkinter.CTkEntry(self, corner_radius=15, border_width=2, show=self.password)
        self.entry.grid(column=1, row=0, sticky='nsew', pady=10)
        
        self.button = customtkinter.CTkButton(self, text="Generate Password", corner_radius=15, border_width=2, command=self.generate_password)
        self.button.grid(column=1, row=1, sticky='nsew', pady=10)
        self.mainloop()

Main().GUI()