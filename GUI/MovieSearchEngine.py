import bs4
import urllib.request as url
import PIL
from PIL import ImageTk

import tkinter
from tkinter import *

window = Tk()
window.geometry('1000x600')

# movie = input("Enter movie name : ")
text_box = Entry(window, width=30, font=('Arial', 20, 'bold'))
text_box.place(x=10, y=70)

label = Label(window, text="Movie Search Engine", fg='red',
              font=('Arial',28,'bold'))
label.pack()

label_1 = Label(window, text="Movie Name : ", fg='blue',
              font=('Arial',18,'bold'), wraplength=500)
label_1.place(x=10, y=160)

label_2 = Label(window, text="Movie Rating : ", fg='blue',
              font=('Arial',18,'bold'))
label_2.place(x=10, y=260)

label_3 = Label(window, text="Movie Summary : ", fg='blue',
              font=('Arial',18,'bold'), wraplength=800)
label_3.place(x=10, y=360)

def get_data():
    label_1.configure(text="Movie Name : ")
    label_2.configure(text="Movie Rating : ")
    label_3.configure(text="Movie Summary : ")

    movie = text_box.get()
    movie = movie.replace(' ', '+')
    path = 'https://www.imdb.com/find?q={}&ref_=nv_sr_sm'.format(movie)

    res = url.urlopen(path)
    page = bs4.BeautifulSoup(res, 'lxml')
    td = page.find('td', class_='result_text')
    a_tag = td.find('a')
    href = a_tag.attrs['href']
    path = 'https://www.imdb.com/' + href
    response = url.urlopen(path)
    page_source = bs4.BeautifulSoup(response, 'lxml')
    title = page_source.find('h1')
    rating = page_source.find('div', class_='ratingValue')
    summary = page_source.find('div', class_='summary_text')
    image = page_source.find('div', class_='poster')
    img_src = image.find('img').attrs['src']
    url.urlretrieve(img_src, 'img.jpg')

    title = label_1['text'] + title.text.replace("\n","")
    rating = label_2['text'] + rating.text.replace("\n","")
    summary = label_3['text'] + summary.text.replace("\n","").strip()

    label_1.configure(text=title)
    label_2.configure(text=rating)
    label_3.configure(text=summary)

    load_img = PIL.Image.open('img.jpg')
    load_img = load_img.resize((200,200))
    render = ImageTk.PhotoImage(load_img)

    img_label = Label(window, image=render)
    img_label.image = render
    img_label.place(x=600, y=60)

btn = Button(window, text="Click Here", command=get_data)
btn.place(x=10,y=130)

window.mainloop()