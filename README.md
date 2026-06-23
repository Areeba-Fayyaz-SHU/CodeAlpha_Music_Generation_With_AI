# CodeAlpha - Music Generation with AI

A mathematical and probabilistic Music Generation system built as part of the CodeAlpha Artificial Intelligence Internship. This project establishes sequential transition models to dynamically create new, coherent melodic lines and chord patterns, exporting the generated outputs directly into standard physical MIDI audio structures.

## Features
- **Sequential Music Data Parsing:** Dynamically interacts with MIDI streams using the `music21` processing architecture to identify core musical note data and stacked chord objects.
- **Probabilistic Transition Matrices:** Utilizes a custom Markov Chain matrix model to map out the statistical likelihood of note sequences based on structural music theory inputs.
- **Dynamic Synthetic Melodic Fallbacks:** Embedded algorithmic safety measures allow the engine to generate structured major scales (C-Major progression variations) natively if external MIDI files are missing.
- **Direct MIDI Generation & Compiling:** Translates software sequence predictions and variable timestamp parameters directly into physical, playable `.mid` track extensions.

## How the Sequence Synthesis Model Works
Rather than relying on static loops, the system models music as a sequential probabilistic process:
1. **Note and Chord Extraction:** Individual pitches are tokenized as string identifiers, while simultaneous notes are down-sampled into string-delimited chord keys (e.g., `0.4.7`).
2. **Transition Probability Mapping:** The architecture runs linear look-aheads across raw data tracks, storing subsequent elements inside a matrix dictionary representing state space maps.
3. **Stochastic Generation Loop:** Taking a random architectural seed element, the sequence predictor crawls across transition maps, picking the next node via statistical variance patterns until the target file length is reached.

## Technologies Used
- Python 3
- Music21 Advanced Musical Toolkit Engine

## How to Run Locally

1. Clone this repository or download the files.
2. Install the necessary sound library packages:
```bash
   pip install music21
Run the tracking script:

Bash
   python music_generator.py
Find your generated audio output inside the root folder saved as output_generated_music.mid.
