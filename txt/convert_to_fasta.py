import os

def main():
    for file in os.listdir('txt'):
         filename = os.fsdecode(file)

         if filename.endswith(".txt"):
             print(filename)
             name = filename.split('.txt')
             print(name[0])
             with open('txt/'+ filename) as f:
                with open('fasta/' + name[0] + ".fasta", "w") as f1:
                    for line in f:
                        f1.write(line)
         else:
             continue

if __name__ == "__main__":
    main()
