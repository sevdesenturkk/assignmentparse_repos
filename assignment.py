from Bio import SeqIO

file_paths = ['/home/senturks/assignment_parse_deneme/casseq1.fasta',
              '/home/senturks/assignment_parse_deneme/ccr51seq.fasta',
              '/home/senturks/assignment_parse_deneme/hemoglobin1seq.fasta' ]

genbank_file = "/home/senturks/assignment_parse_deneme/outputfiles.gb"

def parse_fasta(file_paths):
    for file_path in file_paths:
        with open(file_path, "r") as fasta_file:
            for record in SeqIO.parse(fasta_file, "fasta"):
                print(f"SeqID for {file_path}: {record.id}")
                


def convert_fasta_to_genbank(file_paths):
    for file_path in file_paths:
        genbank_file = file_path.replace(".fasta", ".gb")
        with open(file_path, "r") as input_handle, open(genbank_file, "w") as output_handle:
            SeqIO.convert(input_handle, "fasta", output_handle, "genbank")
        print(f"Converted fasta file {file_path} to genbank file {genbank_file}")


parse_fasta(file_paths)
convert_fasta_to_genbank(file_paths)
