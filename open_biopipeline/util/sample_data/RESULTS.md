## Results
Starting with an unknown sequence of nucleotides the program is fed into the BLAST algorithm to pairwise match the nucleotides for a specific gene. Refer to [gene_items.md](gene_items.md) for the gene name and accession number of the example genes given.

The next step is to understand the gene/protein function by using the UniProt database. By inputting a gene name, we can look for the specific amino acid sequence AND the protein function. You can see here that we don't use gene ontologogy (GO) directly in our analysis since functional annotation is not only partially given by UniProt, but one can retrieve GO information from UniProt links.

Next, we preform pathway analysis on the targeted gene so one can identify the cellular response of the specific cell cascade. This helps us gain understanding of the upstream and downstream molecules; moreover, this can aid in therapeutic drug research. Refer to figure 1 for the pathway interactions of vascular endothelial growth factor A (VEGFA) gene.

<p align="center">
  <img width="500" height="400" src="pathway_img/VEGFA_pathway.jpg">
</p>
<p align="center"><b>Figure 1.</b> Cell signaling cascade of the VEGFA protein (Note the specific link to angiogenesis, making it a target for cancer research)</p>

Lastly, we pass through the gene name into Protein Atlas which gives us valuable and relevant information on the protein expression in patients. This proves very desirable since one can now look at specific RNA cancer expression or the description of the protein within the clinical context. Below is an example of the Protein Atlas output:
```
0 Protein Name: VEGFA
  Tissue expression summary:  Most cancers showed strong cytoplasmic immunoreactivity. Lymphomas were in general moderately stained.
  Description:  Antibody staining mainly consistent with RNA expression data. At least one protein variant secreted, tissue location of RNA and protein might differ and correlation is complex.  
  RNA Cancer Specificity: Low cancer specificity

...
```
