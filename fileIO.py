def convert(file_name, array): 
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
