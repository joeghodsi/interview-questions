'''
Problem: Design a musical jukebox using OOP

start: 4.30
total time: ...
'''
from queue import Queue
import circular_queue
import llist


class Jukebox:
    money = 0
    playing_song = None
    play_queue = Queue()
    focused_song = None
    focused_album = None
    albums = circular_queue()

    def __init__(self):
        '''add all albums with all songs and init focused_* to first respective element'''
        pass

    def add_money(self, money):
        self.money += money

    def can_queue(self, song):
        return self.money >= song.cost

    def queue_song(self, song):
        if self.can_queue(song):
            self.play_queue.enqueue(song)
            self.money -= song.cost

    def next_album(self):
        self.focused_album = self.focused_album.next()

    def next_song(self):
        next_song = self.focused_song.next()
        if not next_song:
            self.next_album()
            next_song = self.focused_album.songs[0]
        self.focused_song = next_song

    def song_end_receiver(self, song):
        self.play_queue.remove(song)
        self.playing_song = self.play_queue.dequeue()


class Album:
    songs = llist()
    metadata = None  # title, length, artist, etc


class Song:
    album = None
    cost = 0.75  # some songs might cost more?
    metadata = None  # title, length, artist, etc
