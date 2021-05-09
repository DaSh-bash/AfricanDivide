## PCA analysis walkthrough

**Preliminary results**

First, PCA analysis was preformed for the data with only necessary filtering to retain maximum coverage.

Short summary of filtering:
- Input file from Aurora: `cardui_migrdiv_indv.vcf.gz`
- Maximum missing % of individuals: 0.3
- Minor allele frequency cutoff fixed to 0.006: which corresponds to removing singletons and doubletons in dataset of 347 individuals
- Variant depth set to: 4 (see justification in Evernote)

We use custom functions (python: pandas, seaborn) to plot first exploratory graph:
![](PCA_fullSFS_all.png)

We observe distinct outliers in Southern Hemisphere, all belonging to Namibia sampling site. Such pattern, along with excessive grouping of other populations may be an effect of LD in the sample.

Here we attempt to correct for LD, removing SNPs, where r^2>0.2 on 50Kb overlapping blocks (performed in plink).

![](PCA_fullSFS_noLD.png)
LD pruning introduced minimal change in marker positions, several individuals are more spaced apart.

We will continue exploring this graph.

Samples from Northern Hemisphere are overlapping with majority of the rest, on the following graph we don't show them (NOTE: it's purely for visualization purposes, eigenvalues stay the same):
![](PCA_fullSFS_noNHE.png)

On this plot outliers from SH are even more obvious. We return to the table to extract exact IDs:
TBA

Let's explore "Hemisphere's" separately, starting from Southern Hemisphere:
![](PCA_fullSFS_SouthPC123.png)

We color plots by sampling location for further investigation:
![](PCA_fullSFS_SouthLocs.png)

Repeat the same plotting for Northern Hemisphere:
![](PCA_fullSFS_North.png)
![](PCA_fullSFS_NorthLocs.png)


No structure is observed in Northern Hemisphere sample set, which agrees with hypothesis of shared migratory cycle.
We zoom in to the center of plot space, ignoring three outliers.
