from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image,ImageTk

class Music_player:
    def __init__(self, base):
        base.title("Music Player")
        base.geometry("700x600")
        base.configure(bg="#F5FFFA")
        load = Image.open("music.png")
        render = ImageTk.PhotoImage(load, width=80, height=50)
        img = Label(base, image=render)
        img.image = render
        img.place(x=200, y=70)

        l = Label(base, bg="#F5FFFA", text="Music Player", font=('Tempus Sans ITC', 40))
        l.place(x=200, y=0)

        play_img = Image.open("play.png")
        play_reader = ImageTk.PhotoImage(play_img)
        play = Button(base, bg="#F5FFFA", image=play_reader,command=self.play_song,width=50,height=50)
        play.place(x=330, y=430)

        load_label = Button(base, text="Load Songs", bg='#F5FFFA', font=('Arial Bold', 15),command=self.load_songs,bd=5)
        load_label.place(x=50, y=370)

        pause = Button(base, text="Pause", bg='#F5FFFA', font=('Tempus Sans ITC', 15),command=self.pause_song,bd=5)
        pause.place(x=210,y=430)

        self.music_file = False
        self.playing_state = False

        base.mainloop()


    def load_songs(self):
        self.music_file = filedialog.askopenfilename()

    def play_song(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause_song(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False




window = Tk()
music = Music_player(window)


