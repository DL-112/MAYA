import tkinter as tk
from tkinter import scrolledtext
import train_bigram as tb
import train_bigram_v2 as tb2
from word_breaker.word_segment_v5 import WordSegment

wordSegmenter = WordSegment()

def bigram_predict():
    file_path = "books/shwe_u_daung.txt"
    probabilities = tb.train_bigram(file_path)
    output_text = tb.generate_text(probabilities, "ကြွယ်", 50)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

def bigram_predict_v2():
    file_path = "books/shwe_u_daung.txt"
    probabilities = tb2.train_bigram(file_path)
    output_text = tb2.generate_text(probabilities, "ကြွယ်", 50)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

def word_break():
    input_string = "၎င်း နည်းလမ်းများသည် တဦး တယောက်သော သူ၏ စိတ်ကူးဉာဏ်ဖြင့် ကုလားထိုင်ပေါ်မှ တွေးတောကြံစည် ရေးသားချက်များမဟုတ်၊ လက်ဖဝါး, ခြေဖဝါးမှ တိုင်းကျော်, ပြည်ကျော် သူဌေးကြီးများအဖြစ်သို့တိုင် ရောက်ကြပြီးသော ပုဂ္ဂိုလ်ကြီးပေါင်း ၅၀၀ ကျော်တို့၏ စီးပွားရှာပုံ စနစ် နည်းနာတို့ကို စစ်ဆေးမေးမြန်း စုံစမ်းနှီးနှောပြီးသည့်နောက်၊ ၎င်းတို့၏ ပြောဆိုချက်များကို တခုနှင့်တခု တိုက်ညှိနှိုင်းချိန်၍ အဆီအနှစ် ထုတ်နုတ်စီစဉ် စီရင် ရေးသားထားခြင်း ဖြစ်လေသည်။"
    # input_string = "၎င်း နည်းလမ်းများသည်"
    output_text = wordSegmenter.normalize_break(input_string, 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility)
    output_text_area.delete("1.0", tk.END)  # Clear previous output
    output_text_area.insert(tk.END, output_text)  # Insert new output

# Create the main window
root = tk.Tk()
root.title("MAYA")
root.geometry("400x300")

# Create button for bigram prediction
bigram_btn = tk.Button(root, text="Bigram", command=bigram_predict)
bigram_btn.pack()

# Create button for bigram prediction
bigram_btn_v2 = tk.Button(root, text="Bigram v2", command=bigram_predict_v2)
bigram_btn_v2.pack()

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