# Unknown Nucleotide Sequence BioPipeline
This project was inspired by my intro to biomedical engineering lab course. This fully automates and streamlines the process of analyzing unknown sequence data. You can view the python notebook below to see a working version. Parts of this pipeline is left out as to prevent future students from cheating.

## Demo
[Python Notebook](https://colab.research.google.com/drive/1lRdys_SpBH4HugSSRcW8S678T-r7NYXV)

Please note this is not the full pipeline, just simply the blastn search portion.

## Packages
- Biopython
- NCBI BLAST 2.10.0+
- KEGG
- UniProt
- Protein Atlas


## Installation
### Windows and MacOS
Go to NCBI website [here](ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/) and download the installer. Install as you would any .exe program

### Linux dependencies
```
uname -i
sudo apt-get install lftp
lftp -e "cd blast/executables/LATEST; dir; quit" ftp.ncbi.nlm.nih.gov | awk '{print $NF}'
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.10.0+-x64-linux.tar.gz

tar -xzvf ncbi-blast-2.10.0+-x64-linux.tar.gz

# remove tar file
rm ncbi-blast-2.10.0+-x64-linux.tar.gz

cd ncbi-blast-2.10.0+
```
```
# so you can run the bin commands without specifying directory
export PATH = $PATH:$PWD

# or

export PATH = $PATH:$HOME/content/ncbi-blast-2.10.0+/bin
```
BLAST commands should work now, the following command should return an output other than "Unknown command".

```
blastn -version
```

### Python dependencies
```
pip install virtualenv

pip install biopython

virtualenv bio_pipeline

env\scripts\activate
```


## Results
Refer to gene_items.md for sequence gene id and accession Number

Further insight is currently being developed

## Pipeline flow
Under construction

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
