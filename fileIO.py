import * from parse-beep-music.py

def convert_to_file(file_name, array): 
    # Outputs the array into a file with the specified fileName for the bash script to read
    with open(file_name, "a+") as f:
        for note in array:
            string = note_to_string(note)
            f.write(string)
    


def note_to_string(note): 
    # Helper function to convert.
    # Takes a tuple and writes it into the correct form. See the test file
    freq, duration = note
    string = str(freq) + ","  + str(duration) + "\n"
    return string

if __name__== "__main__":
    # Run the array and collect them
    if len(sys.argv) != 2: 
        print("Incorrect Arguments, check to see if the midi file exists in the given directory.")
        sys.exit()
    low, mid, high = parse-beep-music.py
    convert_to_file(low)
    convert_to_file(mid)
    convert_to_file(high)

