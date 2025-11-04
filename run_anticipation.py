import sys, os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
INNER_ANTICIPATION = os.path.join(PROJECT_ROOT, "anticipation", "anticipation")

for p in (PROJECT_ROOT, INNER_ANTICIPATION):
    if p not in sys.path:
        sys.path.insert(0, p)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if INNER_ANTICIPATION not in sys.path:
    sys.path.insert(0, INNER_ANTICIPATION)

from transformers import AutoModelForCausalLM
from midi2audio import FluidSynth
from anticipation.sample import generate
from anticipation.convert import events_to_midi

# Direct import from the inner anticipation package
#from sample import generate
#from convert import events_to_midi



# Load model
model = AutoModelForCausalLM.from_pretrained("stanford-crfm/music-small-800k")

# SoundFont path on macOS
soundfont_path = "/Library/Audio/Sounds/Banks/FluidR3_GM.sf2"
fs = FluidSynth(soundfont_path)

# Generate 10 seconds of music
tokens = generate(model, start_time=0, end_time=10, top_p=0.98)

# Save to MIDI
midi_path = "output.mid"
mid = events_to_midi(tokens)
mid.save(midi_path)

# Synthesize audio
fs.midi_to_audio(midi_path, "output.wav")

print("Done! Your audio is saved as 'output.wav'")

