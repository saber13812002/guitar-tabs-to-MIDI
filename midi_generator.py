#!/usr/bin/python3
from midiutil import MIDIFile
from read_tabs import Tabs

class Track():
    def __init__(self,tempo):
        self.track    = 0
        self.channel  = 0
        self.time     = 0.125    # In beats
        self.duration = 0.1     # In beats
        self.tempo    = tempo   # In BPM
        self.volume   = 100  # 0-127, as per the MIDI standard


    def midiGenerator(self,a):
        # One track, defaults to format 1 (tempo track is created automatically)
        MyMIDI = MIDIFile(1)

        #Change Instrument
        MyMIDI.addProgramChange(self.track, self.channel, self.time,2)

        MyMIDI.addTempo(self.track, self.time, self.tempo)
        time=0
        for i in range(len(a[0])):
            for j in range(len(a)):
                duration = self.duration
                if a[j][i]!='-':
                    #print(int(a[j][i]),end="")
                    if a[j][i+1]=='-':
                        duration = self.duration+1
                    MyMIDI.addNote(self.track,self.channel,int(a[j][i]),time,duration,self.volume)
                #else:
                    #MyMIDI.addNote(self.track,self.channel,0,time,self.duration,0)
            time+=self.time

        with open("output.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)