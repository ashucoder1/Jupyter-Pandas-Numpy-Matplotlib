import tkinter as tk
import random 
import string

def generate_password():
    length = length_entry.get()
    complexity = complexity_var.get()

    if not length.isdigit():
        result_label.config(text="Enter a valid Length")
        return
    
    length = int(length)
    if length <= 0:
        result_label.config(text="Password length should be more than 0")
        return
    
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated password: " + password)


########################################################################
window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()  

#############################    Complexity    ###############################
complexity_label = tk.Label(window, text="Complexity:")
complexity_label.pack()

complexity_var = tk.IntVar()
complexity_var.set(1)

option1 = tk.Radiobutton(window, text="Letters", variable=complexity_var, value=1)
option1.pack()

option2 = tk.Radiobutton(window, text="Letters + Digits", variable=complexity_var, value=2)
option2.pack()

option3 = tk.Radiobutton(window, text="Letters + Digits + Special Characters", variable=complexity_var, value=3)
option3.pack()

###########################    Buttons   ##############################
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

##Start
window.mainloop()
