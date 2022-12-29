from random import choice, shuffle, randint
import PySimpleGUI as sg
from copy import copy
# go into venv to run 
 
sg.theme('DarkTeal3')
 
keys = {
    "C":["C","D","E","F","G","A","B"], # key of C
    "F":["F","G","A","Bb","C","D","E"], # key of F
    "G":["G","A","B","C","D","E","F#"], # key of G
    "Bb":["Bb","C","D","Eb","F","G","A"], # key of Bb
    "D":["D","E","F#","G","A","B","C#"], # key of D
    "Eb":["Eb","F","G","Ab","Bb","C","D"], # key of Eb
    "A":["A","B","C#","D","E","F#","G#"], # key of A
    } 

 
# chord inversion practice, they all have everything twice this way the odds of them appearing in conjunction with sus chords becomes more even, otherwise the sus chords get called too often. this is a not so good bandage situation
inversions_1 = ["no 7", "first inversion no 7", "second inversion no 7"]
inversions_2 = ["no 5", "first inversion no 5", "third inversion no 5"]
inversions_3 = ["no 7", "no 5", "first inversion no 5", "first inversion no 7", "second inversion no 7", "third inversion no 5"] 
# sus chords
sus_inversions = ["sus 2", "sus 4", "sus 2 first inversion", "sus 4 first inversion", "sus 2 second inversion", "sus 4 second inversion", "no 7", "no 5", "first inversion no 5", "first inversion no 7", "second inversion no 7", "third inversion no 5", "no 7", "no 5", "first inversion no 5", "first inversion no 7", "second inversion no 7", "third inversion no 5"]
 
# layout for chord inversion page
chord_inversion_practice = [ 
    [sg.Text("Choose a key:")],
    [sg.Radio("Key of C", "radio_1",default=False)],
    [sg.Radio("Key of F", "radio_1",default=False)],
    [sg.Radio("Key of G", "radio_1",default=False)],
    [sg.Radio("Key of Bb", "radio_1",default=False)],
    [sg.Radio("Key of D", "radio_1",default=False)],
    [sg.Radio("Key of Eb", "radio_1",default=False)],
    [sg.Radio("Key of A", "radio_1",default=False)],
    [sg.Radio("Random", "radio_1",default=False)],
    [sg.Text("Select which inversions you want included:")],
    [sg.Radio("No inversion, first, second", "radio_2",default=False)],
    [sg.Radio("No inversion, first, third", "radio_2",default=False)],
    [sg.Radio("No inversion, first, second, third", "radio_2",default=False)],
    [sg.Radio("Choice 3 + Sus 2 and Sus 4 Chords", "radio_2", default=False)],
    [sg.Button("Generate Chord"), sg.Button("Easy Mode"), sg.Button("Back")],
    [
    sg.Text(key="display_key",font=("Courier", 25)),
    sg.Text(key="first_half",font=("Courier", 25)),
    sg.Text(key="note",font=("Courier", 25)),
    sg.Text(key="second_half", font=("Courier",25))
    ],
    [sg.Text(key='chord',font=("Courier", 25))]
    ]
 
# main function of chord generator 
def generate_chord(values):
    # get our key
    if values[0]:
        key, scale = "C",keys["C"] #C 
    elif values[1]:
        key, scale = "F",keys["F"] #F 
    elif values[2]:
        key, scale = "G",keys["G"] #G
    elif values[3]:
        key, scale = "Bb",keys["Bb"] #Bb
    elif values[4]:
        key, scale = "D",keys["D"] #D
    elif values[5]:
        key, scale = "Eb",keys["Eb"] #Eb
    elif values[6]:
        key, scale = "A",keys["A"] #A
    elif values[7]: # gets a key/value pair in the form of a tupe (key,value)
        key, scale = choice(list(keys.items()))
 
    # get which inversions to choose from
    if values[8]:
        inversion = inversions_1
    elif values[9]:
        inversion = inversions_2
    elif values[10]:
        inversion = inversions_3
    elif values[11]:
        inversion = sus_inversions

    note = choice(scale)

    return f"{note} {choice(inversion)}", key, '  '.join(scale), note  # choose a random note from the key and which inversion 
 

pentatonics = ["major pentatonic", "egyptian", "blues minor", "blues major", "minor pentatonic"]
pent_keys = {
    "C":["C","D","E","G","A"],
    "F":["F","G","A","C","D"],
    "G":["G","A","B","D","E"],
    "Bb":["Bb","C","D","F","G"],
    "D":["D","E","F#","A","B"],
    "Eb":["Eb","F","G","Bb","C"],
    "A":["A","B","C#","E","F#"]
}
pentatonic_practice = [
    [sg.Text("Choose a key:")],
    [sg.Radio("Key of C", "radio_1",default=False, key="pentatonic_c")],
    [sg.Radio("Key of F", "radio_1",default=False, key="pentatonic_f")],
    [sg.Radio("Key of G", "radio_1",default=False, key="pentatonic_g")],
    [sg.Radio("Key of Bb", "radio_1",default=False, key="pentatonic_bb")],
    [sg.Radio("Key of D", "radio_1",default=False, key="pentatonic_d")],
    [sg.Radio("Key of Eb", "radio_1",default=False, key="pentatonic_eb")],
    [sg.Radio("Key of A", "radio_1",default=False, key="pentatonic_a")],
    [sg.Radio("Random", "radio_1",default=False, key="pentatonic_random_key")],
    [sg.Text("Choose a mode:")],
    [sg.Radio("major pentatonic", "pentatonic_mode", key="major_pent")],
    [sg.Radio("egyptian        ", "pentatonic_mode", key="egyptian")],
    [sg.Radio("blues minor     ", "pentatonic_mode", key="blues minor")],
    [sg.Radio("blues major     ", "pentatonic_mode", key="blues major")],
    [sg.Radio("minor pentatonic", "pentatonic_mode", key="minor_pent")],
    [sg.Radio("Random          ", "pentatonic_mode", key="random_pentatonic_mode")],
    [sg.Button("Generate Pentatonic Scale"), sg.Button("Halp"), sg.Button("Recall")],
    [sg.Text(key="scale_to_show_2", font=("Courier",25))],
    [sg.Text(key="scale_hint_2", font=("Courier",25))],
]

def generate_pentatonic_scale(values):
    if values["pentatonic_c"] == True:
        key, temp_scale = "C",copy(pent_keys["C"]) #C 
    elif values["pentatonic_f"] == True:
        key, temp_scale = "F",copy(pent_keys["F"]) #F 
    elif values["pentatonic_g"] == True:
        key, temp_scale = "G",copy(pent_keys["G"]) #G
    elif values["pentatonic_bb"] == True:
        key, temp_scale = "Bb",copy(pent_keys["Bb"]) #Bb
    elif values["pentatonic_d"] == True:
        key, temp_scale = "D",copy(pent_keys["D"]) #D
    elif values["pentatonic_eb"] == True:
        key, temp_scale = "Eb",copy(pent_keys["Eb"]) #Eb
    elif values["pentatonic_a"] == True:
        key, temp_scale = "A",copy(pent_keys["A"]) #A
    elif values["pentatonic_random_key"] == True: 
        key, temp_scale = copy(choice(list(pent_keys.items())))

    if values["major_pent"] == True:
        mode = "major pentatonic"
    elif values["egyptian"] == True:
        mode = "egyptian"
    elif values["blues minor"] == True:
        mode = "blues minor"
    elif values["blues major"] == True:
        mode = "blues major"
    elif values["minor_pent"] == True:
        mode = "minor pentatonic"
    elif values["random_pentatonic_mode"] == True:
        mode = choice(pentatonics)

    if mode == "major pentatonic":
        scale = temp_scale
    elif mode == "egyptian":
        scale = temp_scale[1:]
        scale.append(temp_scale[0])
    elif mode == "blues minor":
        scale = temp_scale[2:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
    elif mode == "blues major":
        scale = temp_scale[3:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
    elif mode == "minor pentatonic":
        scale = temp_scale[4:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
        scale.append(temp_scale[3])
    scale = ' '.join(scale)
        
    return key, scale, mode

diatonics = ["ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]
# diatonic practice layout
diatonic_practice = [
    [sg.Text("Choose a key:")],
    [sg.Radio("Key of C", "radio_1",default=False, key="diatonic_c")],
    [sg.Radio("Key of F", "radio_1",default=False, key="diatonic_f")],
    [sg.Radio("Key of G", "radio_1",default=False, key="diatonic_g")],
    [sg.Radio("Key of Bb", "radio_1",default=False, key="diatonic_bb")],
    [sg.Radio("Key of D", "radio_1",default=False, key="diatonic_d")],
    [sg.Radio("Key of Eb", "radio_1",default=False, key="diatonic_eb")],
    [sg.Radio("Key of A", "radio_1",default=False, key="diatonic_a")],
    [sg.Radio("Random", "radio_1",default=False, key="diatonic_random_key")],
    [sg.Text("Choose a mode:")],
    [sg.Radio("ionnian   ", "diatonic_mode", key="ionian")],
    [sg.Radio("dorian    ", "diatonic_mode", key="dorian")],
    [sg.Radio("phrygian  ", "diatonic_mode", key="phrygian")],
    [sg.Radio("lydian    ", "diatonic_mode", key="lydian")],
    [sg.Radio("mixolydian", "diatonic_mode", key="mixolydian")],
    [sg.Radio("aeolian   ", "diatonic_mode", key="aeolian")],
    [sg.Radio("locrian   ", "diatonic_mode", key="locrian")],
    [sg.Radio("Random    ", "diatonic_mode", key="random_diatonic_mode")],
    [sg.Button("Generate Diatonic Scale"), sg.Button("Hint pls"), sg.Button("Return")],
    [sg.Text(key="scale_to_show", font=("Courier",25))],
    [sg.Text(key="scale_hint", font=("Courier",25))],
    [sg.Text(key="factoid", font=("Courier",18))]
    ]
 
# main function of scale practice 
def generate_diatonic_scale(values):
    if values["diatonic_c"] == True:
        key, temp_scale = "C",copy(keys["C"]) #C 
    elif values["diatonic_f"] == True:
        key, temp_scale = "F",copy(keys["F"]) #F 
    elif values["diatonic_g"] == True:
        key, temp_scale = "G",copy(keys["G"]) #G
    elif values["diatonic_bb"] == True:
        key, temp_scale = "Bb",copy(keys["Bb"]) #Bb
    elif values["diatonic_d"] == True:
        key, temp_scale = "D",copy(keys["D"]) #D
    elif values["diatonic_eb"] == True:
        key, temp_scale = "Eb",copy(keys["Eb"]) #Eb
    elif values["diatonic_a"] == True:
        key, temp_scale = "A",copy(keys["A"]) #A
    elif values["diatonic_random_key"] == True: 
        key, temp_scale = copy(choice(list(keys.items())))
 
    if values["ionian"] == True:
        mode = "ionian"
    elif values["dorian"] == True:
        mode = "dorian"
    elif values["phrygian"] == True:
        mode = "phrygian"
    elif values["lydian"] == True:
        mode = "lydian"
    elif values["mixolydian"] == True:
        mode = "mixolydian"
    elif values["aeolian"] == True:
        mode = "aeolian"
    elif values["locrian"] == True:
        mode = "locrian"
    elif values["random_diatonic_mode"] == True:
        mode = choice(diatonics)
    # reorder the scale
    if mode == "ionian":
        scale = temp_scale
        note = "original scale"
    elif mode == "dorian":
        scale = temp_scale[1:]
        scale.append(temp_scale[0])
        note = "flat 3, flat 7"
    elif mode == "phrygian":
        scale = temp_scale[2:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        note = "flat 2, flat 3, flat 6, flat 7"
    elif mode == "lydian":
        scale = temp_scale[3:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
        note = "sharp 4"
    elif mode == "mixolydian":
        scale = temp_scale[4:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
        scale.append(temp_scale[3])
        note = "flat 7"
    elif mode == "aeolian":
        scale = temp_scale[5:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
        scale.append(temp_scale[3])
        scale.append(temp_scale[4])
        note = "flat 3, flat 6, flat 7"
    elif mode == "locrian":
        scale = temp_scale[6:]
        scale.append(temp_scale[0])
        scale.append(temp_scale[1])
        scale.append(temp_scale[2])
        scale.append(temp_scale[3])
        scale.append(temp_scale[4])
        scale.append(temp_scale[5])
        note = "flat 2, flat 3, flat 5, flat 6, flat 7"
    scale = ' '.join(scale)
        
    return key, scale, mode, note
 

# timing practice
timing_practice = [
    [sg.Text("Choose if you want to work on 8 or 16 bit sequences")],
    [sg.Radio("8 bit",group_id="seqeunce"), sg.Radio("16 bit",group_id="seqeunce")], # represented by values 35 and 36
    [sg.Text("Enter how many beats you want to play:\nThis will be random if left blank or if the number is out of range"), sg.Input()],
    [sg.Text(key="sequence_marks", font=("Courier",25))],
    [sg.Text(key="sequence_guide", font=("Courier",25))],
    [sg.Button("Generate Sequence"), sg.Button("Menu")]
]

def generate_sequence(sequence,x): # the sequence list to modify and x is the number of strikes to insert into the sequence
    for i in range(0,x):
        sequence[i] = "X"
    shuffle(sequence)
    sequence = ' '.join(sequence)
    return sequence
 
 
# menu 
main_menu = [
    [sg.Text('Select a practice tool:')],
    [sg.Button('Chord Inversion Practice')],
    [sg.Button('Diatonic Scale Practice')],
    [sg.Button('Pentatonic Scale Practice')],
    [sg.Button('Timing Practice')],
    [sg.Button('Exit')]
    ]
 
layout = [
    [sg.Column(main_menu, key="screen_0"),
    sg.Column(chord_inversion_practice, key="screen_1",visible=False),
    sg.Column(diatonic_practice, key="screen_2",visible=False),
    sg.Column(pentatonic_practice, key="screen_3", visible=False),
    sg.Column(timing_practice, key="screen_4",visible=False)]
    ]
 
window = sg.Window("Music Practice Tool", layout,size=(625, 650), font="Courier")
 
 
while True:
    event, values = window.read()
    # choosing the modes
    if event == "Chord Inversion Practice":
        window["screen_0"].update(visible=False)
        window["screen_1"].update(visible=True)
    if event == "Diatonic Scale Practice":
        window["screen_0"].update(visible=False)
        window["screen_2"].update(visible=True)
    if event == "Pentatonic Scale Practice":
        window["screen_0"].update(visible=False)
        window["screen_3"].update(visible=True)
    if event == "Timing Practice":
        window["screen_0"].update(visible=False)
        window["screen_4"].update(visible=True)
 
    # activating the main function
    if event == "Generate Chord":
        try:
            chord_to_play, key_name, scale, note = generate_chord(values)
            window['display_key'].update(f'key:  {key_name}') # default show on harder mode
            window['chord'].update(f'chord:  {chord_to_play}')
            window['first_half'].update("")
            window['note'].update("")
            window['second_half'].update("") 
        except Exception as e:
            sg.popup_error("make sure two parameters are selected")
            continue
 
    if event == "Generate Diatonic Scale":
        try:
            key, scale, mode, note = generate_diatonic_scale(values)
            window["scale_to_show"].update(f"scale: {scale[0:2]} {mode}") # want to show scale: first note mode, hint 
            window['scale_hint'].update('')
            window['factoid'].update('')
        except Exception as e:
            sg.popup_error(e)
    
    if event == "Generate Pentatonic Scale":
        # try:
        key, scale, mode = generate_pentatonic_scale(values)
        window["scale_to_show_2"].update(f"scale: {scale[0:2]} {mode}") 
        window['scale_hint_2'].update('')
        # except Exception as e:
        #     sg.popup_error(e)


    
    if event == "Generate Sequence": # this needs to be fixed because the values index number will be off due to the split of pent/diatonic scales, just use keys for these though 
        if values[36] == True: # making 8 bit sequence 
            sequence_guide = "1 & 2 & 3 & 4 &"
            sequence = [" "," "," "," "," "," "," "," "]
            if values[38].isdigit():
                if int(values[38]) not in range(1,9):
                    nums_in_seq = randint(1,8)
                else:
                    nums_in_seq = int(values[38])
            else:
                nums_in_seq = randint(1,8)
        elif values[37] == True: # making 16 bit sequence
            sequence_guide = "1 e & a 2 e & a 3 e & a 4 e & a"
            sequence = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            if values[38].isdigit():
                if int(values[38]) not in range(1,17):
                    nums_in_seq = randint(1,16)
                else:
                    nums_in_seq = int(values[38])
            else:
                nums_in_seq = randint(1,16)
        sequence = generate_sequence(sequence,nums_in_seq)
        window['sequence_marks'].update(sequence)
        window['sequence_guide'].update(sequence_guide)

        
    # enabling easy modes
    if event == "Hint pls":
        try:
            window["scale_hint"].update(f"key: {key}\nscale: {scale}")
            window['factoid'].update(note)
        except Exception as e:
            sg.popup_error(e)
    
    if event == "Halp":
        try:
            window["scale_hint_2"].update(f"key: {key}\nscale: {scale}")
        except Exception as e:
            sg.popup_error(e)
 
    if event == "Easy Mode":
        try:
            note_index = scale.index(note) # index of the note
            if note_index > 0: 
                window['display_key'].update("key: ")
                window['first_half'].update(scale[:note_index-1])
            if note_index == 0:
                window['display_key'].update("key:")
            window['note'].update(value=scale[note_index:note_index+2], text_color="yellow")
            window['second_half'].update(scale[note_index+3:])
        except Exception as e:
            sg.popup_error(e)
            continue
 
    # returning back to the menu, idk why i can't use the same word for everything so this is a bit sloppy here but it works 
    if event == "Back":
        window['screen_1'].update(visible=False)
        window['screen_0'].update(visible=True)
    if event == "Return":
        window['screen_2'].update(visible=False)
        window['screen_0'].update(visible=True)
    if event == "Recall":
        window['screen_3'].update(visible=False)
        window['screen_0'].update(visible=True)
    if event == "Menu":
        window['screen_4'].update(visible=False)
        window['screen_0'].update(visible=True)
 
    elif event == sg.WIN_CLOSED or event == "Exit":
        break
 
window.close()
 