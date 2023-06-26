import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x300")

        # Initialize Pygame mixer
        pygame.init()
        pygame.mixer.init()

        # Create playlist
        self.playlist = []

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Create playlist listbox
        self.playlist_box = tk.Listbox(self.root, bg="lightyellow", selectbackground="orange")
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        # Create buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        self.addButton = tk.Button(button_frame, text="Add Song", command=self.add_song)
        self.addButton.grid(row=0, column=0, padx=10)

        self.removeButton = tk.Button(button_frame, text="Remove Song", command=self.remove_song)
        self.removeButton.grid(row=0, column=1, padx=10)

        self.playButton = tk.Button(button_frame, text="Play", command=self.play_music)
        self.playButton.grid(row=1, column=0, padx=10)

        self.pauseButton = tk.Button(button_frame, text="Pause", command=self.pause_music)
        self.pauseButton.grid(row=1, column=1, padx=10)

        self.stopButton = tk.Button(button_frame, text="Stop", command=self.stop_music)
        self.stopButton.grid(row=1, column=2, padx=10)

        # Create volume slider
        self.volumeLabel = tk.Label(self.root, text="Volume")
        self.volumeLabel.pack()

        self.volumeSlider = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volumeSlider.set(0.5)  # Set default volume to 0.5
        self.volumeSlider.pack()

    def add_song(self):
        song_path = filedialog.askopenfilename(title="Select Song", filetypes=(("MP3 Files", "*.mp3"),))
        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist_box.insert(tk.END, song_name)
            self.playlist.append(song_path)

    def remove_song(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            self.playlist_box.delete(selected_song)
            self.playlist.pop(selected_song[0])

    def play_music(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            song_path = self.playlist[selected_song[0]]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

# Create the Tkinter window
root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
