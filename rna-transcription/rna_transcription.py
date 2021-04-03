translation = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand):
    r = ""
    for caracter in dna_strand:
        r += translation[caracter]
    return r
