from tkinter import *
import webbrowser
import datetime
import random
import time
import pyautogui

royaltyVideos = [
    'https://www.youtube.com/watch?v=eQo_tJdZMkI&ab_channel=BuildEmpire', 
    'https://www.youtube.com/watch?v=R4smaCJD-Oo', 
    "https://www.youtube.com/watch?v=tIygkCfDM4M", 
    'https://www.youtube.com/watch?v=kwz0BGm9Ze4&ab_channel=FreedomLifestyleVisualization', 
    'https://www.youtube.com/watch?v=P-q_iBTbZw8&ab_channel=LifeTimeWinners',
    'https://www.youtube.com/watch?v=AvstcGFeeu4&ab_channel=VirtualStudioInnovations',
    'https://www.youtube.com/watch?v=nog8WmTZl7A&ab_channel=LifeTimeWinners',
    'https://www.youtube.com/watch?v=NJrkz_A78QM&ab_channel=BuildEmpire'
]

motivational_speeches = ['https://www.youtube.com/watch?v=Z6T2P3KeSSU&ab_channel=LawofAttractionCoaching', 'https://www.youtube.com/watch?v=Z6T2P3KeSSU&ab_channel=LawofAttractionCoaching']

pianoSong = "https://www.youtube.com/watch?v=967DBySw8QA&ab_channel=PandoraJourney"#piano 
anotherone = "https://www.youtube.com/watch?v=RnkxLb2KaXA"
favorite_song = "https://open.spotify.com/playlist/7fihFmSzMxMDzK99scpOqb"
CapriCorn = "https://open.spotify.com/show/7q8OVMVcsTdJhg0AToajHs" # Astrology
interstellar = "https://www.youtube.com/watch?v=o_Ay_iDRAbc&ab_channel=Jennyni20%28EpicMusic%29"
experience = "https://www.youtube.com/watch?v=kjlu9RRHcbE&ab_channel=ibi"
misty_morning_cabbin = 'https://www.youtube.com/watch?v=1w6G37k8kv0'  # cabin with morningmist
banjoman = "https://www.youtube.com/watch?v=cIMKJ43TFLs"
japanmorningvibes = "https://www.youtube.com/watch?v=x7e2Dm5WdNg"
spotifyPlaylist = "https://open.spotify.com/playlist/0cUYNoMMsSKAcWNwYx7qAe" # spotify playlist
MagicMirror = "http://localhost:8080/"
ForestSoundsVideo = "https://www.youtube.com/watch?v=WarL4vURLYw"
nineteenth_century_villain = "https://www.youtube.com/watch?v=p7dqmROKGIo"
classical_tree = 'https://www.youtube.com/watch?v=SA7uXNeVRjs&ab_channel=PandoraJourney'

randomPick_royalty = random.choice(royaltyVideos)
randompick_motivationalspeech = random.choice(motivational_speeches)

class WakeProgram(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self['background'] = '#000000'
        self.initUI()

    def initUI(self):
        self.title("Wake Program")
        self.wake_url_label = Label(self, text="What should wake you?")
        self.wake_url_label.config(foreground='white', background='black')
        self.wake_url_label.pack(padx=10, pady=10, anchor='center')

        self.options = {"Spotify: MXQ": "https://open.spotify.com/playlist/0b9gboRxvPc3HRgJBuCH5c", 
                        "Morning Forest": "https://www.youtube.com/watch?v=WarL4vURLYw",
                        "Nineteenth Century Villain": "https://www.youtube.com/watch?v=p7dqmROKGIo",
                        "Classical Tree": 'https://www.youtube.com/watch?v=SA7uXNeVRjs&ab_channel=PandoraJourney',
                        "Misty Morning Cabbin" : 'https://www.youtube.com/watch?v=1w6G37k8kv0',
                        'Interstellar' : "https://www.youtube.com/watch?v=o_Ay_iDRAbc&ab_channel=Jennyni20%28EpicMusic%29",
                        'Royalty' : randomPick_royalty,
                        'The Experience' : "https://www.youtube.com/watch?v=kjlu9RRHcbE&ab_channel=ibi",
                        'Banjoman' : "https://www.youtube.com/watch?v=cIMKJ43TFLs"
                        }
        self.var = StringVar(value=list(self.options.keys())[0])

        self.wake_url_dropdown = OptionMenu(self, self.var, *self.options)
        self.wake_url_dropdown.config(foreground='white', background='black')
        self.wake_url_dropdown.pack(padx=10, pady=10, anchor='center')

        self.alarm_time_label = Label(self, text="Enter alarm time (HH:MM):")
        self.alarm_time_label.config(foreground='white', background='black')
        self.alarm_time_label.pack(padx=10, pady=10, anchor='center')

        self.alarm_time_entry = Entry(self, textvariable = StringVar(value="09:00"))
        self.alarm_time_entry.config(foreground='white', background='black')
        self.alarm_time_entry.pack(padx=10, pady=10, anchor='center')

        self.set_alarm_button = Button(self, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.config(foreground='white', background='black')
        self.set_alarm_button.pack(padx=10, pady=10, anchor='center')

    def set_alarm(self):
        wake_url = self.options[self.var.get()]
        alarm_time = datetime.datetime.strptime(self.alarm_time_entry.get(), "%H:%M")
        current_time = datetime.datetime.now()
        alarm_datetime = datetime.datetime.combine(datetime.date.today(), alarm_time.time())

        if alarm_datetime < current_time:
            alarm_datetime += datetime.timedelta(days=1)

        alarm_delta = alarm_datetime - current_time
            
        if "spotify" in wake_url.lower(): # check if spotify option is chosen
         self.after(int(alarm_delta.total_seconds() * 1000),self.play_spotify )

        else:
         self.after(int(alarm_delta.total_seconds() * 1000), self.play_video)

        self.alarm_set_label = Label(self, text=f"Alarm set to go off in {round(alarm_delta.total_seconds()/3600)} hours. \n Goodnight Wytse Punter!",fg="white")
        self.alarm_set_label.config(foreground='white', background='black')
        self.alarm_set_label.pack()

    def play_video(self):
        youtube = self.options[self.var.get()]
        webbrowser.open_new_tab(youtube)
        print("opening youtube")
        time.sleep(60)
        pyautogui.click(x=1196, y=828)
        while True: # Keep screen and user awake
            print("pressed 'a' key")
            pyautogui.press("a")
            time.sleep(60)

    def play_spotify(self):
        spotify = self.options[self.var.get()]
        webbrowser.open_new_tab(spotify)
        print("Opening spotify")
        time.sleep(60)
        pyautogui.click(x=375, y=624)
        print("click")
        time.sleep(5)
        pyautogui.click(x=1880, y=970)
        while True: # Keep screen and user awake
            print("pressed 'a' key")
            pyautogui.press("a")
            time.sleep(60)

if __name__ == '__main__':
    app = WakeProgram()
    app.mainloop()