from parse_beep_music.py import return_voices
import os

def convert_to_file(file_name, array): 
    # Outputs the array into a file with the specified fileName for the bash script to read
    with open(file_name, "a+") as f:
        for note in array:
            string = note_to_string(note)
            f.write(string)
    f.close()


def note_to_string(note): 
    # Helper function to convert.
    # Takes a tuple and writes it into the correct form. See the test file
    freq, duration = note[1], note[2]
    string = str(freq) + ","  + str(duration) + "\n"
    return string

if __name__== "__main__":
    # Run the array and collect them
    if len(sys.argv) != 2: 
       print("Incorrect Arguments, check to see if the midi file exists in the given directory.")
       sys.exit()    
    low, mid, high = return_voices(sys.argv[1])
    convert_to_file("low", low)
    convert_to_file("mid", mid)
    convert_to_file("high", high)
 
