import mido

mid = mido.MidiFile('Mario-Sheet-Music-Overworld-Main-Theme.mid')

time = 0

note_arr = []

notes_on = {}

for msg in mid:

    sentence = str(msg).split(" ")

    if not sentence[0].startswith("note"):
        continue

    note_on = sentence[0] == "note_on"
    note = int(sentence[2].replace('note=', ''))
    velocity = int(sentence[3].replace('velocity=', ''))
    note_time = float(sentence[4].replace('time=', ''))

    if note_time != time and note_time != 0:
        time = time + note_time

    if note_on:
        if velocity == 0:
            n = [time, -1, 0]
        else:
            n = [time, -1, note]
        note_arr = note_arr + [n]
        notes_on[note] = n

    if not note_on:
        n = notes_on[note]
        notes_on.pop(note, None)
        n[1] = time - n[0]

note_arr = sorted(note_arr, key=lambda x: x[0])

sid = [];
vincent = [];
peter = [];

for note in note_arr:
    if len(sid) == 0:
        sid.append(note)
        continue

    elif sid[-1][0] + sid[-1][1] <= note[0]:
        sid.append(note)

    elif len(vincent) == 0:
        vincent.append(note)
        continue

    elif vincent[-1][0] + vincent[-1][1] <= note[0]:
        vincent.append(note)

    elif len(peter) == 0:
        peter.append(note)
        continue

    elif peter[-1][0] + peter[-1][1] <= note[0]:
        peter.append(note)

    else:
        print("BEEEEEEEEP")

def add_rests(l):
    r_l = []

    for i in range(len(l) - 2):
        rest = l[i+1][0] - (l[i][0] + l[i][1])
        r = [l[i][0] + l[i][1], rest, 0]
        r_l.append(l[i])
        r_l.append(r)

    r_l.append(l[len(l) - 1])

    return r_l

sid_r = add_rests(sid)
vincent_r = add_rests(vincent)
peter_r = add_rests(peter)

for p in peter_r:
    print(p)

# use sid_r
# use vincent_r
# use peter_r
