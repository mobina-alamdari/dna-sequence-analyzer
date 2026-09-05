def read_fasta(filename):
    """Reads a FASTA file and returns the sequence as a string."""
    sequence = ""
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line.startswith(">"):  # skip header lines
                sequence += line
    return sequence


def count_nucleotides(sequence):
    """Counts how many times each nucleotide appears."""
    counts = {"A": 0, "T": 0, "C": 0, "G": 0}
    for base in sequence:
        base = base.upper()
        if base in counts:
            counts[base] += 1
    return counts


def gc_content(counts, total_length):
    """Calculates the percentage of G and C in the sequence."""
    gc = counts["G"] + counts["C"]
    return (gc / total_length) * 100 if total_length > 0 else 0


if __name__ == "__main__":
    filename = "example.fasta"  # change this to your file name
    sequence = read_fasta(filename)
    total_length = len(sequence)
    counts = count_nucleotides(sequence)
    gc = gc_content(counts, total_length)

    print(f"Sequence length: {total_length}")
    print(f"Nucleotide counts: {counts}")
    print(f"GC content: {gc:.2f}%")
