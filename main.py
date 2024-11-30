import tkinter as tk
from tkinter import scrolledtext
import train_bigram as tb
import wordbreak as wb

def bigram_predict():
    file_path = "shwe_u_daung.txt"
    probabilities = tb.train_bigram(file_path)
    output_text = tb.generate_text(probabilities, "ကြွယ်", 50)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

def word_break():
    input_string = "သဘာဝဟာသဘာဝပါ"
    output_text = wb.wordbreak(input_string)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

# Create the main window
root = tk.Tk()
root.title("MAYA")
root.geometry("400x300")

# Create button for bigram prediction
bigram_btn = tk.Button(root, text="Bigram", command=bigram_predict)
bigram_btn.pack()

# Create button for word breaker
wordbreaker_btn = tk.Button(root, text="Word break", command=word_break)
wordbreaker_btn.pack()

# Create output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_text_area.pack()

# Run the application
root.mainloop()