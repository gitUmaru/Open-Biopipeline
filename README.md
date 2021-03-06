<img width="auto" height="auto" src ="https://i.imgur.com/yUFCu2Y.png"><br><br>

Open Biopipeline is an open source bioinformatics tool for general and broad purposes, specifically the goal of this project is to develop a tool for researchers or students to use in order to investigate genes. This tool combines several popular existing bioinformatic tools, such as BLAST, KEGG, GO, and Protein Atlas, by consolidating them into one singular location. By using this tool you are able to retrieve: function gene annotation, protein function, clinical relevance, specific patient case information, and much more.

This project was inspired by my intro to biomedical engineering lab course. This fully automates and streamlines the process of analyzing unknown sequence data. You can view the python notebook below to see a working version.

## Packages
- Biopython
- NCBI BLAST 2.10.0+
- KEGG
- UniProt
- Protein Atlas


## Installation
### Windows and MacOS
Go to NCBI website [here](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/) and download the installer. Install as you would any .exe program

### Linux dependencies
```bash
uname -i
sudo apt-get install lftp
lftp -e "cd blast/executables/LATEST; dir; quit" ftp.ncbi.nlm.nih.gov | awk '{print $NF}'
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.10.0+-x64-linux.tar.gz

tar -xzvf ncbi-blast-2.10.0+-x64-linux.tar.gz

# remove tar file
rm ncbi-blast-2.10.0+-x64-linux.tar.gz

cd ncbi-blast-2.10.0+
```
```bash
# so you can run the bin commands without specifying directory
export PATH = $PATH:$PWD

# or

export PATH = $PATH:$HOME/content/ncbi-blast-2.10.0+/bin
```
BLAST commands should work now, the following command should return an output other than "Unknown command".

```bash
blastn -version
```

### Python Setup
```bash
pip install virtualenv

virtualenv bio_pipeline

bio_pipeline\Scripts\activate

pip install open-biopipeline

```

## Example Pipeline Flow Chart
<p align="center">
  <img src="https://i.imgur.com/UWcFXx1.png">
</p>

<p align="center"><b>Figure 2.</b> Flow chart diagram of bioinformatic pipeline, displaying flow of input/outputs</p>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
