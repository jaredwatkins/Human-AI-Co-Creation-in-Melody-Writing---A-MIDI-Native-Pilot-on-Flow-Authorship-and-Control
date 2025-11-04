""" Infrastructure for constructing anticipatory infilling models.

This model provides infrastructure to preprocess Midi music datasets
for training anticipatory music infilling models. For more context, see:

    Anticipatory Music Transformer
    John Thickstun, David Hall, Chris Donahue, Percy Liang
    Preprint Report, 2023
"""

# expose renamed tokenizer to existing imports
from . import tokenize_custom as tokenize

# expose sample module to top-level anticipation import
from . import sample
