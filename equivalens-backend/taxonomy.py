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
    "literal": "word-for-word translation (including insertion or deletion of determiners, changes between singular and plural forms), or possible literal translation of some idioms; the underlying syntactic construction is similar in both languages",
    "equivalence": "Non-literal translation of proverbs, idioms, fixed expressions or syntactical constructioons (which  cannot be transferred as such into the target langauge) OR semantic equivalence at the supra-lexical level, translation of terms.",
    "modulation_particularization": "The translation is more precise or presents a more concrete sense.",
    "modulation_generalization": "The translation is more general or neutral OR translation of an idiom by a non-fixed expression OR removal of a metaphorical image.",
    "modulation_other": "Changing the point of view, either to circumvent a translation difficulty or to reveal a way of seeing things.",
    "transposition": "Translating words or expressions by using other grammatical categories (e.g., noun -> verb) than the ones used in the source language, without altering the meaning of the utterance.",
    "modulation_plus_transposition": "Any sub-type of Modulation combined with transposition",
    "metaphor": "Keep the same metaphorical image by using a non-literal translation OR introduce metaphorical expression to translate non-metaphor",
    "reduction": "Remove deliberately certain content words in translation",
    "explicitation": "Introduce clarifications that remain implicit in the source language.",
    "no_type_attributed": "Translated words which don't correspond to any source words",
    "erroneous": "Obvious translation error.",
    "untranslated": "Keep the source in the target to avoid the translation problem.",
    "uncertain": "Difficult example (not clear from attotation guidelines how to annotate this example).",
}