import mido


class Note:
    def __init__(self, midi, start_time, duration=0):
        self.midi = midi
        self.duration = duration
        self.start_time = start_time

    def __repr__(self):
        return f'Note({self.midi}, {self.start_time}, {self.duration})'

    @property
    def end_time(self):
        return self.start_time + self.duration

    @property
    def freq(self):
        if self.midi == 0:
            return 1
        return int(2 ** ((self.midi - 69)/12) * 440)

    @property
    def scale_dur(self):
        return int(self.duration * 1000)

    @property
    def csv(self):
        return f'{self.freq},{self.scale_dur}\n'


def create_note_array(fp):
    narray = []
    notes = dict()
    time = 0
    for msg in mido.MidiFile(fp):
        print(msg)
        if msg.type == 'note_on':
            notes[msg.note] = Note(msg.note, time)
        elif msg.type == 'note_off':
            note = notes[msg.note]

            note.duration = time - note.start_time
            narray.append(note)
        time += msg.time

    return narray


def split_voices(notes, number):
    voices = [[[], 0] for i in range(number)]
    for note in notes:
        for voice in voices:
            if voice[1] < note.start_time:
                voice[0].append(note)
                voice[1] = note.end_time
                break
    return [v[0] for v in voices]


def write_csv(voice, filepath):
    csv = ""
    last_dur = 0
    zero_note = Note(0, 0)
    for note in voice:
        if note.start_time > last_dur:
            zero_note.start_time = last_dur
            zero_note.duration = note.start_time - last_dur
            csv += zero_note.csv
        csv += note.csv
        last_dur = note.end_time

    with open(filepath, 'w') as f:
        f.write(csv)

notes = create_note_array('Mario-Sheet-Music-Overworld-Main-Theme.mid')
notes = sorted(notes, key=lambda x:x.start_time)
notes = split_voices(notes, 3)

for voice, name in zip(notes, ['vincent.csv', 'peter.csv', 'sid.csv']):
    write_csv(voice, name)
print(notes)
