import os, sys, windnd
import base64
import magic
import tkinter as tk
from tkinter import messagebox, font, filedialog
from tkinter.ttk import *

def text_2_Base64():
    '''文本编码成Base64'''
    page_1_Base64_text.delete("1.0", tk.END)
    base64Value = base64.b64encode(page_1_Origin_text.get('1.0', 'end').encode('utf-8')).decode('utf-8')
    page_1_Base64_text.insert('1.0', base64Value)  

def Base64_2_text():
    '''Base64解码成文本'''
    page_1_Origin_text.delete("1.0", tk.END)
    try:
        originValue = base64.b64decode(page_1_Base64_text.get('1.0', 'end').encode('utf-8')).decode('utf-8')
        page_1_Origin_text.insert('1.0', originValue)
    except:messagebox.showinfo("结果", "解码后不是文本")

def file_2_Base64(file_path):
    '''文件编码成Base64'''
    source_file = open(file_path, "rb")
    base_64_file = base64.b64encode(source_file.read())
    source_file.close()
    return base_64_file

def Base64_2_file(text):
    '''Base64解码成文件'''
    return base64.b64decode(text)


def clear_page_1_Origin_text(event=None):
    '''清空文本解码后的文本'''
    page_1_Origin_text.delete("1.0", tk.END)

def clear_page_1_Base64_text(event=None):
    '''清空文件路径'''
    page_1_Base64_text.delete("1.0", tk.END)

def clear_page_3_Base64_text(event=None):
    '''清空Base64解码后的文本'''
    page_3_Base64_text.delete("1.0", tk.END)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def save_data(data, file_name):
    file = open(file_name, "wb")
    file.write(data)

def dragged_files(files):
    msg = '\n'.join(item.decode('gbk') for item in files)
    if len(files) > 1:
        messagebox.showerror('Oops!', '拖入的文件太多啦\n只能拖一个哦')
    else:
        # messagebox.showinfo('您拖动的文件', msg)
        data = file_2_Base64(msg)
        save_data(data, os.path.splitext(msg)[0] + '.txt')
        messagebox.showinfo(
            'Done!', '存储到 ' + os.path.splitext(msg)[0] + '.txt')
        os.system('start ' + os.path.splitext(msg)[0] + '.txt')

def clicked_files():
    files = filedialog.askopenfilename()

    if len(files) > 0:
        msg = files
        data = file_2_Base64(msg)
        save_data(data, os.path.splitext(msg)[0] + '.txt')
        messagebox.showinfo(
            'Done!', '存储到 ' + os.path.splitext(msg)[0] + '.txt')
        os.system('start ' + os.path.splitext(msg)[0] + '.txt')
    else:
        pass

def decode_and_save_files():
    '''解码并保存为文件'''
    base64Code = page_3_Base64_text.get('1.0', 'end')
    data = Base64_2_file(base64Code)
    file_Suffix_name = ''
    try:
        fileType = magic.Magic(mime=True).from_buffer(data)
        if fileType == 'text/plain':file_Suffix_name = '.txt'
        elif fileType == 'text/x-python':file_Suffix_name = '.py'

        elif fileType == 'application/pdf':file_Suffix_name = '.pdf'
        elif fileType == 'application/zip':file_Suffix_name = '.zip'
        elif fileType == 'application/x-7z-compressed':file_Suffix_name = '.7z'
        elif fileType == 'application/x-tar':file_Suffix_name = '.tar'
        elif fileType == 'application/x-rar':file_Suffix_name = '.rar'
        elif fileType == 'application/x-bzip2':file_Suffix_name = '.bz2'
        elif fileType == 'application/x-gzip':file_Suffix_name = '.gz'
        elif fileType == 'image/jpeg':file_Suffix_name = '.jpg'
        elif fileType == 'image/png':file_Suffix_name = '.png'
        elif fileType == 'image/gif':file_Suffix_name = '.gif'
        elif fileType == 'image/tiff':file_Suffix_name = '.tiff'
        elif fileType == 'image/bmp':file_Suffix_name = '.bmp'
        elif fileType == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':file_Suffix_name = '.docx'
        elif fileType == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':file_Suffix_name = '.xlsx'
        elif fileType == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':file_Suffix_name = '.pptx'
        elif fileType == 'application/vnd.ms-excel':file_Suffix_name = '.xls'
        elif fileType == 'application/vnd.ms-powerpoint':file_Suffix_name = '.ppt'
        elif fileType == 'audio/mpeg':file_Suffix_name = '.mp3'
        elif fileType == 'audio/x-wav':file_Suffix_name = '.wav'
        elif fileType == 'audio/x-ms-wma':file_Suffix_name = '.wma'
        elif fileType == 'audio/x-ms-wax':file_Suffix_name = '.wax'
        elif fileType == 'video/x-ms-asf':file_Suffix_name = '.asf'
        elif fileType == 'video/x-ms-wmv':file_Suffix_name = '.wmv'
        elif fileType == 'video/x-ms-wmx':file_Suffix_name = '.wmx'
        elif fileType == 'video/x-ms-wvx':file_Suffix_name = '.wvx'
        elif fileType == 'video/x-msvideo':file_Suffix_name = '.avi'
        elif fileType == 'video/mp4':file_Suffix_name = '.mp4'
        elif fileType == 'video/mpeg':file_Suffix_name = '.mpeg'
        elif fileType == 'video/x-matroska':file_Suffix_name = '.mkv'
        elif fileType == 'video/quicktime':file_Suffix_name = '.mov'
        elif fileType == 'video/x-flv':file_Suffix_name = '.flv'
        elif fileType == 'application/x-shockwave-flash':file_Suffix_name = '.swf'
        elif fileType == 'text/x-msdos-batch':file_Suffix_name = '.bat'
        elif fileType == 'application/x-dosexec':file_Suffix_name = '.exe'
        elif fileType == 'application/x-msdownload':file_Suffix_name = '.dll'
        elif fileType == 'application/x-msi':file_Suffix_name = '.msi'
        elif fileType == 'application/x-ms-dos-executable':file_Suffix_name = '.com'
        elif fileType == 'application/x-ms-shortcut':file_Suffix_name = '.lnk'
        elif fileType == 'application/octet-stream':file_Suffix_name = '.unknown_file_type.txt'
        else:file_Suffix_name = f'.{fileType.replace("/", "#")}.txt'
    except:file_Suffix_name = '.unknown_file_type.txt'
    outputFileName = 'decode_output' + file_Suffix_name
    save_data(data, outputFileName)
    messagebox.showinfo(
        'Done!', '存储到 ' + outputFileName)
    os.system('start ' + outputFileName)


root = tk.Tk()
root.resizable(False, False)
title_font = font.Font(family="SimSun", size=16, weight="bold")
button_font = font.Font(family="SimSun", size=16, weight="bold")
text_font = font.Font(family="SimSun", size=16)

root.title("Base64编 / 解码工具")
notebook = Notebook(root)
notebook.pack(fill="both", expand=1)

page_1_text_2_Base64 = tk.Frame(notebook)
page_2_file_2_Base64 = tk.Frame(notebook)
page_3_Base64_2_file = tk.Frame(notebook)
notebook.add(page_1_text_2_Base64, text="文本Base64互转")
notebook.add(page_2_file_2_Base64, text="文件转Base64")
notebook.add(page_3_Base64_2_file, text="Base64转文件")

######################## Page 1 ########################

page_1_title_label = tk.Label(page_1_text_2_Base64, text="文本转换Base64", font=title_font)
page_1_title_label.pack(side='top', fill="both", expand=1)

page_1_Origin_frame = tk.Frame(page_1_text_2_Base64)
page_1_Origin_frame.pack(side='left', fill="both", expand=1)
page_1_Origin_label = tk.Label(page_1_Origin_frame, text=f"{' '*10}文本{' '*10}", font=title_font)
page_1_Origin_label.grid(row=0, column=0)
page_1_Origin_label.bind("<Button-1>", clear_page_1_Origin_text)
page_1_Origin_text = tk.Text(page_1_Origin_frame, width=30, font=text_font, wrap=tk.WORD)
page_1_Origin_text.grid(row=1, column=0)
page_1_Origin_text_scrollbar = tk.Scrollbar(page_1_Origin_frame)
page_1_Origin_text_scrollbar.grid(row=1, column=2, sticky="ns")
page_1_Origin_text_scrollbar.configure(command=page_1_Origin_text.yview)
page_1_Origin_text.configure(yscrollcommand=page_1_Origin_text_scrollbar.set)

page_1_button_frame = tk.Frame(page_1_text_2_Base64)
page_1_button_frame.pack(side='left', fill="both", expand=1, padx=10, pady=200)
text_2_Base64_button = tk.Button(page_1_button_frame, text="   >>   ", command=text_2_Base64, font=button_font)
text_2_Base64_button.pack(pady=10)
Base64_2_text_button = tk.Button(page_1_button_frame, text="   <<   ", command=Base64_2_text, font=button_font)
Base64_2_text_button.pack(pady=10)

page_1_Base64_frame = tk.Frame(page_1_text_2_Base64)
page_1_Base64_frame.pack(side='left', fill="both", expand=1)
page_1_Base64_label = tk.Label(page_1_Base64_frame, text=f"{' '*10}Base64{' '*10}", font=title_font)
page_1_Base64_label.grid(row=0, column=0)
page_1_Base64_label.bind("<Button-1>", clear_page_1_Base64_text)
page_1_Base64_text = tk.Text(page_1_Base64_frame, width=30, font=text_font, wrap=tk.WORD)
page_1_Base64_text.grid(row=1, column=0)
page_1_Base64_text_scrollbar = tk.Scrollbar(page_1_Base64_frame)
page_1_Base64_text_scrollbar.grid(row=1, column=2, sticky="ns")
page_1_Base64_text_scrollbar.configure(command=page_1_Base64_text.yview)
page_1_Base64_text.configure(yscrollcommand=page_1_Base64_text_scrollbar.set)

######################## Page 2 ########################

page_2_title_label = tk.Label(page_2_file_2_Base64, text="文件编码为Base64", font=title_font)
page_2_title_label.pack(side="top", fill="x")

page_2_main_frame = tk.Frame(page_2_file_2_Base64)
page_2_main_frame.pack(side="top", fill="x")
f1 = tk.Frame(page_2_main_frame)
f2 = tk.Frame(page_2_main_frame)
f1.pack(side="top", fill="y")
f2.pack(side="top", fill="y")

page_2_label_00 = tk.Label(f1, text='\n\n', font=title_font)
page_2_label_00.pack(side="top", fill="x")
page_2_label = tk.Label(f1, text='\n\n     将文件拖到这里     \n\n', font=title_font, background='yellow')
page_2_label.pack(side="top", fill="x")
page_2_label_01 = tk.Label(f1, text='\n或', font=title_font)
page_2_label_01.pack(side="top", fill="x")
page_2_button = tk.Button(f2, text='打开文件...', command=clicked_files, font=title_font)
page_2_button.pack(side="top", fill="x")

windnd.hook_dropfiles(f1, func=dragged_files)

######################## Page 3 ########################

page_3_title_label = tk.Label(page_3_Base64_2_file, text="Base64解码为文件", font=title_font)
page_3_title_label.grid(row=0, column=0, columnspan=3)

page_3_Base64_frame = tk.Frame(page_3_Base64_2_file)
page_3_Base64_frame.grid(row=1, column=0)

page_3_button_frame = tk.Frame(page_3_Base64_frame)
page_3_button_frame.pack(side="top")
page_3_button = tk.Button(page_3_button_frame, text='解码并保存文件...', command=decode_and_save_files, font=title_font)
page_3_button.grid(row=0, column=0, padx=5)
page_3_clear_text_button = tk.Button(page_3_button_frame, text='清空', command=clear_page_3_Base64_text, font=title_font)
page_3_clear_text_button.grid(row=0, column=1, padx=5)

page_3_Base64_text = tk.Text(page_3_Base64_frame, width=75, font=text_font, wrap=tk.WORD)
page_3_Base64_text.pack(side="top", fill="both")
######################## E N D ########################

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure((0, 1), weight=1)

root.mainloop()
