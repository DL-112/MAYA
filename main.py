import tkinter as tk
from tkinter import scrolledtext
import train_bigram as tb

def process_text():
    file_path = "shwe_u_daung.txt"
    probabilities = tb.train_bigram(file_path)
    output_text = tb.generate_text(probabilities, "ကြွယ်", 50)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

# Create the main window
root = tk.Tk()
root.title("MAYA")
root.geometry("400x300")

# Create process button
process_button = tk.Button(root, text="Process", command=process_text)
process_button.pack()

# Create output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_text_area.pack()

# Run the application
root.mainloop()