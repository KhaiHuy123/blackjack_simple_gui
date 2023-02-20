from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
class MP:
    def __init__(self,win):
        #create Tkinter window
        win.geometry('300x300')
        #win.title('MUSIC GAME')
        win.config(background='green')
        win.resizable(0,0)

        self.play_restart=tk.StringVar()
        self.pause_resume=tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        load_button=Button(win,text="Load",width=10,font=("Consolas",14),command=self.load,border=5,borderwidth=10)
        load_button.place(x=100,y=40,anchor='center')

        play_button = Button(win, textvariable=self.play_restart, width=10, font=("Consolas", 14), command=self.play,border=5,borderwidth=10)
        play_button.place(x=100, y=80, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=("Consolas", 14), command=self.pause,border=5,borderwidth=10)
        pause_button.place(x=100, y=120, anchor='center')

        stop_button = Button(win, text="Stop", width=10, font=("Consolas", 14), command=self.stop,border=5,borderwidth=10)
        stop_button.place(x=100, y=160, anchor='center')

        self.music_file=False
        self.playing_state=False

    def load(self):
        self.music_file=filedialog.askopenfilename()
        print('Loaded:',self.music_file)
        self.play_restart.set("Play")
        pass
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state=False
            self.play_restart.set("Restart")
            self.pause_resume.set("Pause")
        pass
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
            self.pause_resume.set("Resume")
        else:
            mixer.music.unpause()
            self.playing_state=False
            self.pause_resume.set('Pause')
        pass
    def stop(self):
        mixer.music.stop()
        pass
    pass

#play_music=Tk()
#MP(play_music)
#play_music.mainloop()

