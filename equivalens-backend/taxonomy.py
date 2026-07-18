# taxonomy.py

UCP_CATEGORIES = {
    "multiword_unit": {
        "label": "Multiword unit",
        "subcategories": [
            "compound",
            "fixed_expression",
            "idiomatic_expression",
            "light_verb_construction",
            "verb_particle_construction",
        ],
        "definition": (
            "A multiword expression that may not have a straightforward "
            "or routine equivalent in the target language."
        ),
    },
    "complex_structure": {
        "label": "Complex structure",
        "subcategories": [
            "complex_noun_phrase",
            "complex_syntactic_structure",
        ],
        "definition": (
            "A complex phrase or syntactic construction that may require "
            "a non-routine translation solution."
        ),
    },
    "cultural_linguistic_variant": {
        "label": "Cultural and linguistic variant",
        "subcategories": [
            "cultural_reference",
            "linguistic_variant",
        ],
        "definition": (
            "A culturally specific element or linguistic variation that may "
            "not be directly reproducible in the target language."
        ),
    },
    "colloquial_language": {
        "label": "Colloquial language",
        "subcategories": [],
        "definition": "Informal, conversational, dialectal, or slang language.",
    },
    "metaphor_original_image": {
        "label": "Metaphor and original image",
        "subcategories": [],
        "definition": (
            "A metaphorical expression or original image whose effect may "
            "need a creative translation solution."
        ),
    },
}

TRANSLATION_TECHNIQUES = {
    "literal": "A direct, close rendering that preserves the source expression and meaning.",
    "equivalence": (
        "A different target-language expression with equivalent meaning, "
        "especially for fixed expressions, idioms, or proverbs."
    ),
    "particularization": (
        "A more specific or concrete target-language expression than the source."
    ),
    "generalization": (
        "A broader or more general target-language expression than the source."
    ),
    "modulation_other": (
        "A change of viewpoint, perspective, or form to produce a natural "
        "target-language expression, excluding particularization and generalization."
    ),
    "transposition": (
        "A change of grammatical category or part of speech without materially "
        "changing the meaning."
    ),
    "modulation_plus_transposition": (
        "A combination of modulation and transposition in the same unit."
    ),
    "metaphor": (
        "Use of a metaphorical or idiomatic target-language expression."
    ),
    "reduction": (
        "Source-text information is omitted or has no aligned target-text equivalent."
    ),
    "explicitation": (
        "Target-text information is added or made explicit without a direct "
        "source-text equivalent."
    ),
    "no_type_attributed": (
        "No technique is attributed, usually because the unaligned element does "
        "not affect the message."
    ),
    "erroneous": "The proposed translation of the unit contains an error.",
    "untranslated": "The source-text unit has been left untranslated.",
    "uncertain": "The annotator cannot confidently assign a technique.",
}