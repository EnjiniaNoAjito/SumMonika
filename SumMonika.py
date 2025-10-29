from tkinter import *
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
import nltk
from time import sleep
from PIL import Image, ImageTk
import re
#  --Создание окна--
root = Tk()
root.geometry('900x710')
canvas = Canvas(root, width=900, height=710)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
TEXT_SUMM = ""
OPTIONS = {}
SUMMARY = ''
pil_image = Image.open("Dot.png")
piece1_image = Image.open("PIECE.png")
sh_image = Image.open("SHEET.png")
mon_image = Image.open("Monika.png")
new1_size = (890, 330)
new_img = sh_image.resize(new1_size, Image.Resampling.LANCZOS)
new_img.save("SHEET_resized.png")
new_size = (820, 400)
new_size2 = (500, 710)
piece_image = piece1_image.resize(new_size2, Image.Resampling.LANCZOS)
piece_image.save("PIECE_resized.png")
resized_img = pil_image.resize(new_size, Image.Resampling.LANCZOS)
resized_img.save("Dot_resized.png")
imageent = Image.open("Без имени.png")
mon1_image = Image.open("Monika_hand_up.png")
bg0_image = ImageTk.PhotoImage(piece_image)
bg1_image = ImageTk.PhotoImage(new_img)
bg_image = ImageTk.PhotoImage(resized_img)
bg3_image = ImageTk.PhotoImage(imageent)
bg4_image = ImageTk.PhotoImage(mon_image)
bg5_image = ImageTk.PhotoImage(mon1_image)

# --Создание элементов--
canvas.create_image(440, 0, anchor=NW, image=bg0_image)
canvas.create_image(0, 0, anchor=NW, image=bg_image)
canvas.create_image(5, 300, anchor=NW, image=bg1_image)
canvas.create_image(360, 10, anchor=NW, image=bg3_image)
canvas.place(x=0, y=0)
image = Image.open("Button.png")
image1 = Image.open("Button1.png")
pen_image = Image.open("Pen.png")
new2_size = (580, 43)
resized_img2 = pen_image.resize(new2_size, Image.Resampling.LANCZOS)
resized_img2.save("Pen_resized.png")
p_p_image = Image.open("Pen_open.png")
pen_wait_image = ImageTk.PhotoImage(p_p_image)
image_pen = ImageTk.PhotoImage(resized_img2)
photo = ImageTk.PhotoImage(image)
photo1 = ImageTk.PhotoImage(image1)

def submit_all():
   global SUMMARY
   print(OPTIONS)
   print('эта информация будет использоваться для суммаризации текста')
   
   prepared_text = re.sub(r'[?.!]{2,}', ".", TEXT_SUMM)
   sentences = prepared_text.count(".")
   sentences_final = round((int(OPTIONS['percent'].replace("%", ""))/100)*sentences) - (round((int(OPTIONS['percent'].replace("%", ""))/100)*sentences) == sentences)
   
   methods = {"TextRankSummarizer" : TextRankSummarizer, "LsaSummarizer" : LsaSummarizer, "LuhnSummarizer" : LuhnSummarizer, "EdmundsonSummarizer" : EdmundsonSummarizer}
   parser = PlaintextParser.from_string(TEXT_SUMM, Tokenizer(OPTIONS['language']))
   summarizer = TextRankSummarizer()
   summary = summarizer(parser.document, sentences_final)
   li = [str(s)+"\n" for s in summary]
   o = "".join(li)
   ready = []
   for s in li:
      chunks = [s[i:i+47]+'\n' if not(s[i:i+47].endswith('\n')) else s[i:i+47] for i in range(0, len(s), 47)]
      ready = ready + chunks
   r1 = ''.join(ready[:12])
   copy_button.config(text=r1)
   SUMMARY = ''.join(ready)
def copy():
   root.clipboard_clear()
   root.clipboard_append(SUMMARY)

# ----Логика кнопок-----
def submit(obj):
   global TEXT_SUMM
   canvas.delete("mytext")
   text_content = obj.get("1.0", "end-1c")
   ready = []
   for s in text_content.split('\n'):
      chunks = [s[i:i+76] for i in range(0, len(s), 76)]
      ready = ready + chunks
   r = '\n'.join(ready)
   if len(ready) >= 12:
      r1 = '\n'.join(ready[:11])+"..."
   else:
      r1 = '\n'.join(ready)
   canvas.create_text(110, 320, text=r1, fill='black', tags="mytext", anchor='nw', font=("Segoe Print", 12))
   TEXT_SUMM = text_content

def write_poem():
   root_write = Toplevel(root)
   root_write.geometry('850x450')
   root_write.title('SumMonika!')
   text = Text(root_write, width=64, height=12, font=("Segoe Print", 14))
   text.place(x=0, y=0)
   sub = Image.open("Submit.png")
   sub_image = ImageTk.PhotoImage(sub)
   button_write = Button(root_write, image=sub_image, command=lambda: submit(text), borderwidth=0)
   button_write.image = sub_image
   button_write.place(x=30, y=400)

def options():
   global OPTIONS
   root_options = Toplevel(root)
   root_options.geometry('450x450')
   root_options.title('SumMonika!')
   canvas = Canvas(root_options, width=450, height=450, bg="pink")
   canvas.create_image(0, 0, anchor=NW, image=bg_image)
   Monika = canvas.create_image(20, 390, anchor=NW, image=bg4_image)
   def monika1(g):
      canvas.itemconfig(Monika, image=bg5_image)
   def monika2(g):
      canvas.itemconfig(Monika, image=bg4_image)
   canvas.place(x=0, y=0)
   canvas.create_text(170, 10, text='Language', fill='black', tags="opts", anchor='nw', font=("Segoe Print", 12))
   var_l = StringVar()
   rb1 = Radiobutton(root_options, text="English", variable=var_l, value="english", bg='pink')
   rb2 = Radiobutton(root_options, text="Russian", variable=var_l, value="russian", bg='pink')
   rb1.config(fg='black', font=('Segoe Print', 12))
   rb2.config(fg='black', font=('Segoe Print', 12))
   rb1.place(x=100, y=38)
   rb2.place(x=250, y=38)
   canvas.create_text(12, 78, text='Length of a summarized text (in % from the original)', fill='black', tags="opts", anchor='nw', font=("Segoe Print", 12))
   label = Label(root_options, text='20%', width=5, height=1, bg='white', font=('Segoe Print', 10))
   label.place(x=170, y=128)
   def more():
      current = label.cget('text')
      current = f'{int(current.replace("%", ""))+(10*(int(current.replace("%", "")) <= 80))}%'
      return label.config(text=current)
   def less():
      current = label.cget('text')
      current = f'{int(current.replace("%", ""))-(10*(int(current.replace("%", "")) > 20))}%'
      return label.config(text=current)
   canvas.create_rectangle(160, 115, 270, 165, fill='pink', outline='pink')
   up = Button(root_options, text='🠉', command=more, width=1, height=1, bg='white')
   up.place(x=222, y=125)
   down = Button(root_options, text='🠋', command=less, width=1, height=1, bg='white')
   down.place(x=239, y=125)
   canvas.create_text(110, 175, text='Summarizing method', fill='black', tags="opts", anchor='nw', font=("Segoe Print", 12))
   var_m = StringVar()
   rb3 = Radiobutton(root_options, text="TextRank", variable=var_m, value="TextRankSummarizer", bg='pink')
   rb4 = Radiobutton(root_options, text="LsaSummarizer", variable=var_m, value="LsaSummarizer", bg='pink')
   rb5 = Radiobutton(root_options, text="LuhnSummarizer", variable=var_m, value="LuhnSummarizer", bg='pink')
   rb6 = Radiobutton(root_options, text="EdmundsonSummarizer", variable=var_m, value="EdmundsonSummarizer", bg='pink')
   rb3.config(fg='black', font=('Segoe Print', 10))
   rb4.config(fg='black', font=('Segoe Print', 10))
   rb5.config(fg='black', font=('Segoe Print', 10))
   rb6.config(fg='black', font=('Segoe Print', 10))
   rb3.place(x=80, y=210)
   rb4.place(x=80, y=250)
   rb5.place(x=80, y=290)
   rb6.place(x=80, y=330)
   def submit():
      OPTIONS['language'] = var_l.get()
      OPTIONS['percent'] = label.cget('text')
      OPTIONS['method'] = var_m.get()
   submit = Button(root_options, text='Submit', command=submit, width=6, height=1, bg='pink', font=('Segoe Print', 12), borderwidth=0)
   submit.bind("<Enter>", monika1)
   submit.bind("<Leave>", monika2)
   submit.place(x=70, y=400)


button = Button(root, image=photo, command=submit_all, borderwidth=0)
button1 = Button(root, image=photo1, command=options, borderwidth=0)
button_pen = Button(root, image=image_pen, command=write_poem, borderwidth=0, width=620, height=100, bg='white')
def on_enter(event):
    button_pen.config(image=pen_wait_image)
def on_leave(event):
    button_pen.config(image=image_pen)
button_pen.bind("<Enter>", on_enter)
button_pen.bind("<Leave>", on_leave)
copy_button = Button(root, bg="#ffcfde", text='', anchor='nw', command=copy, borderwidth=0, width=46, height=12, wraplength=360, justify='left', font=("Segoe Print", 9))
copy_button.place(x=410, y=20)
button.place(x=8, y=400)
button1.place(x=8, y=483)
button_pen.place(x=0, y=620)

#  canvas_enter = Canvas(root, width=460, height=270, bg='pink', bd=8, relief="ridge")
#  canvas_enter.place(x=350, y=10)
root.mainloop()
