from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
import os
from util.sample_data.seq import SampleData

class PathError(Exception):
    pass

class BLAST():
    def __init__(self,raw_string=None,path=None):
        self.__path = path
        if(path is not None):
            self.__filename, self.__file_ext = os.path.splitext(self.__path)
        self.__raw_string = raw_string

    def blast(self,search_type,seq_type):
        if(self.__path is not None):
            record = SeqIO.read(self.__path, format=self.__file_ext.replace(".",""))
            result_handle = NCBIWWW.qblast(search_type, seq_type, record.seq)

            blast_result = open(os.path.dirname(__file__)+self.__filename.replace("\\","_")+".xml", "w")
            blast_result.write(result_handle.read())
            blast_result.close()
            result_handle.close()
        else:
            PathError("The path is None, please provide a file path")

    def get_seq(self,seq_string=None):
        if(self.__raw_string is not None):
            return Seq(self.__raw_string)
        return Seq(seq_string)

    ## TODO Getters and Setters for instance fields


def main():
    dna = BLAST(path="open_biopipeline\\util\\sample_data\\example_seq\\Gene A -- DNA nucleotide sequence.fasta")
    dna.blast("blastn","nt")


if __name__ == '__main__':
    main()
