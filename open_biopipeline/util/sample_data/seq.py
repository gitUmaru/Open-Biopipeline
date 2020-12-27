import os
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import example_seq  # TODO make relative import work


class SampleData():
    def __init__(self):
        pass

    def get_fasta(self):
        fasta_files = []
        for file in os.listdir('./sample_data/example_seq'):
             fasta_files.append(file)
        print(fasta_files)
        return fasta_files
