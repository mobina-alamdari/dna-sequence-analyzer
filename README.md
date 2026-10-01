# DNA Sequence Analyzer

A simple Python script that reads a DNA sequence from a FASTA file and reports its length, nucleotide composition and GC content.

## Why GC content?
GC content (the percentage of guanine and cytosine bases) is one of the most basic properties of a genome. It varies widely between bacterial species and is often used in genome comparison and quality checks of sequencing data.

## What it does
- Reads a FASTA file and skips header lines (lines starting with `>`)
- Counts the number of A, T, C and G bases (case-insensitive)
- Calculates GC content as a percentage of the total sequence length

## Requirements
- Python 3 (no external libraries needed)

## How to use
1. Place your FASTA file in the same folder as the script.
2. Open `dna_analyzer.py` and set the file name:
```python
   filename = "example.fasta"
```
3. Run:
```bash
   python dna_analyzer.py
```

## Example
Input (`example.fasta`):
```
>example_sequence
ATGCGTACGTTAGCCGATCGATCGGCTAAGCTAGCTAGGCTA
```

Output:
```
Sequence length: 42
Nucleotide counts: {'A': 10, 'T': 10, 'C': 10, 'G': 12}
GC content: 52.38%
```

## Limitations
- If a FASTA file contains several sequences, they are joined and analysed as one.
- Ambiguous bases (such as N) are included in the total length but not in the nucleotide counts, which can slightly lower the GC percentage.

## Possible improvements
- Analyse each sequence in a multi-sequence FASTA file separately
- Accept the file name as a command-line argument
- Plot nucleotide composition with matplotlib

## Author
Mobina Alamdari – microbiology graduate learning Python for genomic data analysis
