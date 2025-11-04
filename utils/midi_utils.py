from note_seq import midi_io

def midi_to_note_sequence(path):
    return midi_io.midi_file_to_note_sequence(path)

def note_sequence_to_midi(sequence, out_path):
    midi_io.sequence_proto_to_midi_file(sequence, out_path)
