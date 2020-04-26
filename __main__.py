"""

Verison: 0.0.1
Release Date:
Language:  Python
Author:  Sean Lyons
Email: slyons494@gmail.com

"""


"""

Import modules section.

"""

from bs4 import BeautifulSoup
import requests
import time
from tkinter import *
from lxml import html
import os
import openpyxl
#may replace modules below with -> from openpyxl import *
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import FORMULAE
from openpyxl.styles import colors
from openpyxl.styles import Font, Color


"""

Define web-scraping functions.
Define memory functions.

"""


input_memory = {"robots.txt_accepted" : None,
                "URL" : None,
                "variable_type" : None,
                "variable_name" : None,
                }

robots_memory = {}

set_page_memory = {}

html_variable_memory = None

variable_class_memory = None

data_batch_memory = {}

class data_batch:
    def __init__(self, date, collection):
        data_batch.date = date
        data_batch.collection = collection


"""

Define tkinter variables.

"""


root = Tk()
root.wm_title("Web Scraper")
root.geometry("470x280")
root.resizable(False,False)

e1 = Entry(root)
e1.place(x=160,y=20)
e1.insert(0,"Test text!")

e2 = Entry(root)
e2.place(x=320,y=20)

label_1 = Label(root,text="Status", fg="Blue")
label_1.place(x=320,y=40)

e3 = Entry(root)
e3.place(x=160,y=90)

e4 = Entry(root)
e4.place(x=320,y=90)

e5 = Entry(root)
e5.place(x=160,y=160)

e6 = Entry(root)
e6.place(x=320,y=160)

e7 = Entry(root)
e7.place(x=160,y=230)

e8 = Entry(root)
e8.place(x=320,y=230)


"""

Notice windows.

"""

class robots_window:
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("400x600")
        self.window.resizable(False,False)


"""

Define functions for entry boxes.

"""


def wunga():
    print(1)

def robots():
    try:
        robots_a = e1.get()
        robots_memory["URL"] = robots_a
        robots_b = requests.get(f"{robots_a}/robots.txt")
        robots_c = robots_b.text
        robots_d = BeautifulSoup(robots_c, features='lxml')
        robots_e = robots_d.find_all
        print(robots_e)
        e2.insert(0,"Found robots.txt.")
        label_1_green = Label(root,text="Status", fg="Green")
        label_1_green.place(x=320,y=40)
    except:
        e2.insert(0,"Robots.txt not found.")
        label_1_red = Label(root,text="Status", fg="Red")
        label_1_red.place(x=320,y=40)

def set_page():
    try:
        sp_a = e3.get()
        set_page_memory["URL"] = sp_a
        sp_b = requests.get(f"{sp_a}")
        #sp_c = html.fromstring(sp_b.content)
        sp_c = sp_b.text
        sp_d = BeautifulSoup(sp_c, features='lxml')
        sp_e = sp_d.find_all
        print(sp_e)
        e4.insert(0, "Success")
    except:
        e4.insert(0, "An error occurred.")
    
def html_variable():
    try:
        hv_a = e5.get()
        html_variable_memory = hv_a
        hv_b = None
        e6.insert(0, "Success")
        print(html_variable_memory)
    except:
        e6.insert(0, "an error occurred")

def variable_class():
    try:
        vc_a = e7.get()
        variable_class_memory = vc_a
        e8.insert(0, "Success")
        print(variable_class_memory)
    except:
        e8.insert(0, "an error occurred")


"""

Define menu bar functions.

"""


def scrape_data():
    try:
        sd_a = requests.get(f'{set_page_memory["URL"]}')
        sd_b = html.fromstring(sd_a.content)
        sd_c = sd_b.xpath(f'//{html_variable_memory}[@class="{variable_class_memory}"]/text()')
        for item in enumerate(sd_c):
            print(item)
    except:
        print("An error occurred.")

def create_txt():
    wunga()

def create_csv():
    wunga()

def create_xlsx():
    wunga()

def clear_cache():
    data_batch_memory.clear()


"""

Define GUI variables.

"""


def report_window():
    rw_window = Toplevel()
    rw_window.geometry("600x400")
    rw_window.resizable(False,False)
    #rw_window.Scrollbar(rw_window, orient="vertical", command=rw_window)

def export_window():
    e_window = Toplevel()
    e_window.geometry("600x400")
    e_window.resizable(False,False)
    #e_window.Scrollbar(e_window, orient="vertical", command=e_window)

def repeat_scrape_window():
    rs_window = Toplevel()
    rs_window.geometry("400x250")
    rs_window.resizable(False,False)
    rs_window.title("Repeat Scrape")
    rs_e = Entry(rs_window)
    rs_e.place(x=10,y=30)
    
    def rs_callback():
        print(rs_e.get())
        
    rs_b = Button(rs_window, text="yum", width=10,command=rs_callback)
    rs_b.place(x=30,y=100)

def about_window():
    a_window = Toplevel()
    a_window.geometry("300x200")
    a_window.title('About')
    a_window.resizable(False,False)
    #t = tkinter.Text(a_window)
    #t.insert(index=0,chars="Test text!!")
    #t.place(x=50,y=125)

class faq_window:
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("400x600")
        self.window.resizable(False,False)

def create_window():
    window = Toplevel()
    window.geometry("500x350")
    window.resizable(False,False)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
file_menu.add_command(label="New file", command=create_window)
file_menu.add_command(label="Scrape Data", command=scrape_data)
file_menu.add_command(label="Repeat Scrape", command=repeat_scrape_window)
menu.add_cascade(label="File", menu=file_menu)

data_menu = Menu(menu)
data_menu.add_command(label="View Cache", command=report_window)
data_menu.add_command(label="Export Cache", command=export_window)
data_menu.add_command(label="Clear Cache", command=clear_cache)
menu.add_cascade(label="Data", menu=data_menu)

reports_menu = Menu(menu)
reports_menu.add_command(label="Create .txt Report", command=create_txt)
reports_menu.add_command(label="Create .csv Report", command=create_csv)
reports_menu.add_command(label="Create .xlsx Report", command=create_xlsx)
menu.add_cascade(label="Reports", menu=reports_menu)

help_menu = Menu(menu)
help_menu.add_command(label="About", command=about_window)
help_menu.add_command(label="FAQ", command=faq_window)
menu.add_cascade(label="Help", menu=help_menu)


"""

Define tkinter button functions.

"""


b1 = Button(root, text="Find robots.txt", width=15,command=robots,activebackground="pink", activeforeground="blue")
b1.place(x=20,y=20)

b2 = Button(root, text="Set Webage", width=15,command=set_page,activebackground="pink", activeforeground="blue")
b2.place(x=20,y=90)

b3 = Button(root, text="Set HTML Variable", width=15,command=html_variable,activebackground="pink", activeforeground="blue")
b3.place(x=20,y=160)

b4 = Button(root, text="Set Class", width=15,command=variable_class,activebackground="pink", activeforeground="blue")
b4.place(x=20,y=230)

notice1 = Label(root, text="Wishing Well Computing")
notice1.place(x=10,y=260)


#Program launch section.

def main():
    root.mainloop()


"""
20.0424:

if __name__ == "__main__":
    root.mainloop()


"""