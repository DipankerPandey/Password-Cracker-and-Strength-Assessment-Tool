import tkinter as tk
from tkinter import filedialog


# Function to selected file
def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        file_label.config(text="Selected file: " + filename)
        print("Selected file:", filename)

# Function to selected file
def select_wordlist():
    wordlist = filedialog.askopenfilename()
    if wordlist:
        wordlist_label.config(text="Selected wordlist: " + wordlist)
        print("Selected wordlist:", wordlist)

root = tk.Tk()
root.title("Password Analysis Tool")
root.configure(bg="#f0f0f0")

# Function to create a label with custom style
def create_label(parent, text, font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="black"):
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    return label

# Function to create a button with custom style
def create_button(parent, text, command=None, font=("Helvetica", 10), bg="#4CAF50", fg="white"):
    button = tk.Button(parent, text=text, command=command, font=font, bg=bg, fg=fg)
    return button

# Create frame for file selection
file_frame = tk.Frame(root, bg="#f0f0f0")
file_frame.pack(pady=20)

file_label = create_label(file_frame, "Select a hash file:")
file_label.grid(row=0, column=0, padx=5)

file_button = create_button(file_frame, "Browse", command=select_file)
file_button.grid(row=0, column=1, padx=5)

# Create frame for hash type selection
hash_frame = tk.Frame(root, bg="#f0f0f0")
hash_frame.pack(pady=10)

hash_label = create_label(hash_frame, "Select hash type:")
hash_label.grid(row=0, column=0, padx=5)

hash_types = ["MD5", "SHA-1", "SHA-256"]
hash_type_var = tk.StringVar(value="MD5")
for i, hash_type in enumerate(hash_types):
    rb = tk.Radiobutton(hash_frame, text=hash_type, variable=hash_type_var, value=hash_type, bg="#f0f0f0")
    rb.grid(row=0, column=i+1, padx=5)

# Create frame for wordlist selection
wordlist_frame = tk.Frame(root, bg="#f0f0f0")
wordlist_frame.pack(pady=10)

wordlist_label = create_label(wordlist_frame, "Select a wordlist:")
wordlist_label.grid(row=0, column=0, padx=5)

wordlist_button = create_button(wordlist_frame, "Browse", command=select_wordlist)
wordlist_button.grid(row=0, column=1, padx=5)

# Create frame for attack type selection
attack_frame = tk.Frame(root, bg="#f0f0f0")
attack_frame.pack(pady=10)

attack_label = create_label(attack_frame, "Select attack types:")
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
analyze_button = create_button(root, "Analyze", font=("Helvetica", 12), bg="#4CAF50", fg="white")
analyze_button.pack(pady=20)

root.mainloop()
