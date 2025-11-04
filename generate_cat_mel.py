import note_seq
from note_seq import midi_io
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import magenta
from magenta.models.performance_rnn import performance_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from magenta.music import sequence_proto_to_midi_file

# Load the model bundle
print("Loading model...")
bundle = sequence_generator_bundle.read_bundle_file('performance_with_dynamics.mag')
generator_map = performance_sequence_generator.get_generator_map()
generator = generator_map['performance_with_dynamics'](checkpoint=None, bundle=bundle)
generator.initialize()

# Load the seed
print("Loading seed...")
seed = midi_io.midi_file_to_note_sequence('seed.mid')

# Set generation options
seconds_to_generate = 30
generator_options = generator.generate_options
generator_options.args['temperature'].float_value = 1.0
generate_section = generator_options.generate_sections.add(
    start_time=seed.total_time,
    end_time=seed.total_time + seconds_to_generate
)

# Generate
print("Generating...")
generated_sequence = generator.generate(seed, generator_options)

# Save
sequence_proto_to_midi_file(generated_sequence, 'generated.mid')
print("Generated file saved to generated.mid")
