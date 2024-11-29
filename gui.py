import tkinter as tk
from tkinter import scrolledtext
import bigram

def process_text():
    # Assuming sylbreak.py has a function named 'break_syllables' for processing
    # output_text = sylbreak.break_syllables(input_text)
    file_path = "book.txt"
    output_text = bigram.build_bigram_model(file_path)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

# Create the main window
root = tk.Tk()
root.title("Syllable Breaker GUI")
root.geometry("400x300")

# Create process button
process_button = tk.Button(root, text="Break Syllables", command=process_text)
process_button.pack()

# Create output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_text_area.pack()

# Run the application
root.mainloop()