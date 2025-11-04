from note_seq import midi_io, sequences_lib, music_pb2
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

# --- config & model ---
config = configs.CONFIG_MAP['cat-mel_2bar_big']
model = TrainedModel(config, batch_size=4, checkpoint_dir_or_path='cat-mel_2bar_big.ckpt')

# --- load seed ---
seed = midi_io.midi_file_to_note_sequence('seed.mid')

# --- normalize to a single tempo (MusicVAE quantizer needs this) ---
# If there are multiple tempos, replace with one at time=0.
if len(seed.tempos) == 0:
    t = seed.tempos.add(); t.qpm = 120.0; t.time = 0.0
elif len(seed.tempos) > 1:
    qpm = seed.tempos[0].qpm  # pick the first; or set your own constant (e.g., 120.0)
    del seed.tempos[:]
    t = seed.tempos.add(); t.qpm = qpm; t.time = 0.0
else:
    qpm = seed.tempos[0].qpm

# --- compute two-bar window in seconds BEFORE quantizing ---
# assume default 4/4 unless present
num = 4; den = 4
if len(seed.time_signatures) > 0:
    num = seed.time_signatures[0].numerator
    den = seed.time_signatures[0].denominator

quarters_per_bar = num * (4.0 / den)
seconds_per_quarter = 60.0 / qpm
two_bars_seconds = 2 * quarters_per_bar * seconds_per_quarter

# --- trim unquantized, then quantize ---
trimmed = sequences_lib.extract_subsequence(seed, 0.0, two_bars_seconds)
quantized = sequences_lib.quantize_note_sequence(trimmed, steps_per_quarter=4)

# --- generate ---
generated = model.sample(n=4, length=32, primer_sequence=quantized, temperature=1.0)

# --- save first result ---
midi_io.sequence_proto_to_midi_file(generated[0], 'output.mid')
print("✅ Generated melody saved as output.mid")
