from Bio import SeqIO
from Bio.Blast import NCBIWWW
import os

fasta_file = []

def main():
    for file in os.listdir('fasta'):
         filename = os.fsdecode(file)
         if filename.endswith(".fasta"):
             print(filename)
             fasta_file.append(filename)


    record = SeqIO.read('fasta/'+fasta_file[0], format="fasta")

    result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)


    blast_result = open("0.xml", "w")
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()

if __name__ == '__main__':
    main()
