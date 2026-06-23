import os
import random
from music21 import instrument, note, chord, stream

def load_midi_or_fallback(folder_path="midi_songs"):
    """
    Attempts to load MIDI files from a directory and extract individual notes.
    Falls back to a structural musical scale if no files exist.
    """
    notes = []
    
    if os.path.exists(folder_path) and any(f.endswith('.mid') for f in os.listdir(folder_path)):
        print(f"Found MIDI files in '{folder_path}'. Parsing musical elements...")
        for file in os.listdir(folder_path):
            if file.endswith(".mid"):
                try:
                    from music21 import converter
                    midi = converter.parse(os.path.join(folder_path, file))
                    parts = instrument.partitionByInstrument(midi)
                    notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes
                    for element in notes_to_parse:
                        if isinstance(element, note.Note):
                            notes.append(str(element.pitch))
                        elif isinstance(element, chord.Chord):
                            notes.append('.'.join(str(n) for n in element.normalOrder))
                except Exception as e:
                    print(f"Skipping broken file {file}: {e}")
    else:
        print(f"No local MIDI dataset found. Initializing custom melody sequence patterns...")
        # A structural melody pattern representing a musical progression
        base_scale = ['C4', 'E4', 'G4', 'B4', 'C5', 'A4', 'F4', 'D4']
        for i in range(150):
            notes.append(base_scale[i % 8])
            if i % 4 == 0:
                notes.append("0.4.7") # Simulated basic chord structure
                
    return notes

def build_probabilistic_matrix(notes):
    """
    Builds a probabilistic note transition matrix (Markov Chain)
    to model sequence patterns mathematically.
    """
    transitions = {}
    for i in range(len(notes) - 1):
        current_note = notes[i]
        next_note = notes[i+1]
        if current_note not in transitions:
            transitions[current_note] = []
        transitions[current_note].append(next_note)
    return transitions

def generate_musical_sequence(transitions, unique_notes, num_generate=30):
    """Generates new note sequences based on structural matrix probabilities."""
    print("Generating new mathematical musical sequences...")
    current_note = random.choice(unique_notes)
    generation_output = [current_note]
    
    for _ in range(num_generate - 1):
        if current_note in transitions and transitions[current_note]:
            current_note = random.choice(transitions[current_note])
        else:
            current_note = random.choice(unique_notes)
        generation_output.append(current_note)
        
    return generation_output

def convert_to_midi(prediction_output, filename="output_generated_music.mid"):
    """Parses text pitch representations and compiles them into a physical MIDI audio file."""
    offset = 0
    output_notes = []
    
    for pattern in prediction_output:
        # If the element represents a chord sequence structure
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes_list = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                notes_list.append(new_note)
            new_chord = chord.Chord(notes_list)
            new_chord.offset = offset
            output_notes.append(new_chord)
        # If the element is a standalone note
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)
            
        offset += 0.5 # Step forwarding the timestamps
        
    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp=filename)
    print(f"\n[SUCCESS] Generated tracks compiled and saved as: '{filename}'")

if __name__ == "__main__":
    # 1. Load data
    raw_music_data = load_midi_or_fallback()
    
    # 2. Build statistical network model patterns
    print("Building Probabilistic Transition Networks...")
    transition_matrix = build_probabilistic_matrix(raw_music_data)
    
    # 3. Generate sequential note output paths
    melody_output = generate_musical_sequence(transition_matrix, list(set(raw_music_data)))
    
    # 4. Save file
    convert_to_midi(melody_output)