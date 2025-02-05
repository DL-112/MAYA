from basic_bur import BasicTokenizer
from base import Tokenizer

import tkinter as tk
from tkinter import scrolledtext

# Assume BasicTokenizer is already defined or imported from another module
# Initialize the tokenizer
tokenizer = BasicTokenizer()
tokenizeBase = Tokenizer()
# Train the tokenizer with some text and vocab size
text = "၎င်းနည်းလမ်းများသည် တဦး တယောက်သော သူ၏ စိတ်ကူးဉာဏ်ဖြင့် ကုလားထိုင်ပေါ်မှ တွေးတောကြံစည် ရေးသားချက်များမဟုတ်၊ လက်ဖဝါး, ခြေဖဝါးမှ တိုင်းကျော်, ပြည်ကျော် သူဌေးကြီးများအဖြစ်သို့တိုင် ရောက်ကြပြီးသော ပုဂ္ဂိုလ်ကြီးပေါင်း ၅၀၀ ကျော်တို့၏ စီးပွားရှာပုံ စနစ် နည်းနာတို့ကို စစ်ဆေးမေးမြန်း စုံစမ်းနှီးနှောပြီးသည့်နောက်၊ ၎င်းတို့၏ ပြောဆိုချက်များကို တခုနှင့်တခု တိုက်ညှိနှိုင်းချိန်၍ အဆီအနှစ် ထုတ်နုတ်စီစဉ် စီရင် ရေးသားထားခြင်း ဖြစ်လေသည်။ Hello"
tokenizer.train(text, vocab_size=500, verbose=True)  # Will print the merges during training

# Encode the text into token IDs
encoded_ids = tokenizer.encode(text)
decoded_text = tokenizer.decode(encoded_ids)  # Decoded text

# Tkinter GUI to display the decoded text
def display_decoded_text():
    # Display the decoded text in the label
    # Clear previous output in the text area and insert new result
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, decoded_text)
    
tokenizeBase.save("lala")

# Create a Tkinter window
root = tk.Tk()
root.title("MAYA - BPE Tokenizer")
root.geometry("800x600")

# Create buttons for decode
decode_btn = tk.Button(root, text="Syl break and UTF-8", command=display_decoded_text)
decode_btn.pack()



# Create output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
output_text_area.pack()

# Run the application
root.mainloop()


# tokenizer = BasicTokenizer()
# tokenize = Tokenizer()

# text = "၎င်းနည်းလမ်းများသည် တဦး တယောက်သော သူ၏ စိတ်ကူးဉာဏ်ဖြင့် ကုလားထိုင်ပေါ်မှ တွေးတောကြံစည် ရေးသားချက်များမဟုတ်၊ လက်ဖဝါး, ခြေဖဝါးမှ တိုင်းကျော်, ပြည်ကျော် သူဌေးကြီးများအဖြစ်သို့တိုင် ရောက်ကြပြီးသော ပုဂ္ဂိုလ်ကြီးပေါင်း ၅၀၀ ကျော်တို့၏ စီးပွားရှာပုံ စနစ် နည်းနာတို့ကို စစ်ဆေးမေးမြန်း စုံစမ်းနှီးနှောပြီးသည့်နောက်၊ ၎င်းတို့၏ ပြောဆိုချက်များကို တခုနှင့်တခု တိုက်ညှိနှိုင်းချိန်၍ အဆီအနှစ် ထုတ်နုတ်စီစဉ် စီရင် ရေးသားထားခြင်း ဖြစ်လေသည်။ Hello"
# tokenizer.train(text, vocab_size=300, verbose=True)
# tokenize.save("trained_tokenizer")

# # Encode the text into token IDs
# encoded_ids = tokenizer.encode(text)
# print("Encoded IDs:", encoded_ids)

# # Decode the token IDs back to text
# decoded_text = tokenizer.decode(encoded_ids)
# print("Decoded Text:", decoded_text)  # Will print the reconstructed text