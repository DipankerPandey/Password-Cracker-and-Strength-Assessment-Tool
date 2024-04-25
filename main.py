import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from checker import password_strength_checker
from dicto import dictionary_password
from brute import guess_password
from rainbow import rainbow_password

# Function for pop up
def popup():
    param= password_strength_checker(password_entry.get())
    messagebox.showinfo("Strength", param)


# Function to showcase wordlist selection
def show_wordlist_selection():
    wordlist = filedialog.askopenfilename()
    if wordlist:
        wordlist_label.config(text="Selected wordlist: " + wordlist)
        print("Selected wordlist:", wordlist)



# Function to show analysis details
def show_analysis_details():
    entered_password = password_entry.get()
    print("Entered password:", entered_password)
    
    entered_hash = hash_entry.get()
    print("Entered hash:", entered_hash)
    
    selected_hash_type = hash_type_var.get()
    if selected_hash_type == "MD5":
        type=0
    if selected_hash_type == "SHA-1":
        type=1
    if selected_hash_type == "SHA-256":
        type=2
    if selected_hash_type == "Try all":
        type=3
    
    selected_wordlist = wordlist_label.cget("text")
    print("Selected wordlist:", selected_wordlist)
    
    selected_attack_types = []
   
    if attack_var2.get() == 1:
        a= dictionary_password(entered_hash, type)
        if a != "Password not found":
            messagebox.showinfo("Analysis", a)
    if attack_var1.get() == 1:
        guess_password(entered_hash, 5, 12, type)
        if a != "Password not found":
            messagebox.showinfo("Analysis", a)
    """if attack_var3.get() == 1:
        rainbow_password(entered_hash, selected_wordlist)
        if a != "Password not found":
            messagebox.showinfo("Analysis", a)"""


# USER INTERFACE 

root = tk.Tk()
root.title("Password Analysis Tool")
root.configure(bg="#f0f0f0")



# Function to create a label with custom style                       ///// USER INTERFACE FUNCTION /////////////


def create_label(parent, text, font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black"):
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    return label



# Function to create a button with custom style                      ///// USER INTERFACE FUNCTION /////////////

def create_button(parent, text, command=None, font=("Helvetica", 10), bg="#4CAF50", fg="white"):
    button = tk.Button(parent, text=text, command=command, font=font, bg=bg, fg=fg)
    return button



# Function to create an entry with custom style                     ///// USER INTERFACE FUNCTION /////////////    

def create_entry(parent, font=("Helvetica", 10), bg="white", fg="black"):
    entry = tk.Entry(parent, font=font, bg=bg, fg=fg)
    return entry



# Create frame for input Password                             /////////////////// PASSWORD INPUT ////////////////////


password_input_frame = tk.Frame(root, bg="#f0f0f0")
password_input_frame.pack(pady=20)

password_label = create_label(password_input_frame, "Enter the Password")
password_label.grid(row=0, column=0, padx=5)

password_entry = create_entry(password_input_frame)
password_entry.grid(row=0, column=1, padx=5)

check_button = create_button(root, "Check", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=popup)
check_button.pack(pady=5)



# Create frame for inputing hash file                        ///////////////// HASH INPUT ////////////////////////


hash_input_frame = tk.Frame(root, bg="#f0f0f0")
hash_input_frame.pack(pady=20)

hash_label = create_label(hash_input_frame, "Enter a hash")
hash_label.grid(row=0, column=0, padx=5)

hash_entry = create_entry(hash_input_frame)
hash_entry.grid(row=0, column=1, padx=5)




# Create frame for hash type selection                          //////////////// RADIO BUTTON //////////////////////


hash_frame = tk.Frame(root, bg="#f0f0f0")
hash_frame.pack(pady=10)

hash_label = create_label(hash_frame, "Select hash type")
hash_label.grid(row=0, column=0, padx=5)

hash_types = ["MD5", "SHA-1", "SHA-256", "Try all"]
hash_type_var = tk.StringVar(value="MD5")
for i, hash_type in enumerate(hash_types):
    rb = tk.Radiobutton(hash_frame, text=hash_type, variable=hash_type_var, value=hash_type, bg="#f0f0f0")
    rb.grid(row=0, column=i+1, padx=5)



# Create frame for wordlist selection                          ///////////////// LIST INPUT ///////////////////////////


wordlist_frame = tk.Frame(root, bg="#f0f0f0")
wordlist_frame.pack(pady=10)

wordlist_label = create_label(wordlist_frame, "WordList Rainbow")
wordlist_label.grid(row=0, column=0, padx=5)

wordlist_button = create_button(wordlist_frame, "Browse", command=show_wordlist_selection)
wordlist_button.grid(row=0, column=1, padx=5)



# Create frame for attack type selection                      ///////////////////   CHECK BOX   //////////////////////////


attack_frame = tk.Frame(root, bg="#f0f0f0")
attack_frame.pack(pady=10)

attack_label = create_label(attack_frame, "Select attack types")
attack_label.grid(row=0, column=0, padx=5)

attack_var1 = tk.IntVar()
attack_var2 = tk.IntVar()
attack_var3 = tk.IntVar()

checkbox1 = tk.Checkbutton(attack_frame, text="Brute Force", variable=attack_var1, bg="#f0f0f0")
checkbox1.grid(row=1, column=0, padx=5, pady=2, sticky="w")

checkbox2 = tk.Checkbutton(attack_frame, text="Dictionary Attack", variable=attack_var2, bg="#f0f0f0")
checkbox2.grid(row=2, column=0, padx=5, pady=2, sticky="w")

checkbox3 = tk.Checkbutton(attack_frame, text="Rainbow Table Attack", variable=attack_var3, bg="#f0f0f0")
checkbox3.grid(row=3, column=0, padx=5, pady=2, sticky="w")

# Create analyze button
analyze_button = create_button(root, "Analyze", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=show_analysis_details)
analyze_button.pack(pady=20)

root.mainloop()
