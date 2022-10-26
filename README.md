# TCR-convergence

**Convergence_scData.py**

The python code used to select the convergent TCR in scTCR-seq data.

  Input file description: 
  
    'sample_name.csv': a file with only one column which contains the names of each sample file (e.g. SRA number of each sample)
    
    'filtered_contig_annotations.csv': the standard output file from the 10X cellranger pipeline.

  Output file description: 
  
    'Convergence_sample.csv': the file containing the information of convergent TCRs. It has three columns: barcode, CRD3 nucleotide sequences, and CDR3 amino acid sequences. Each sample input file will be outputted into a separate file.
    
    'Convergence_sample_rev.csv': the file containing the information of non-convergent TCRs. It has three columns: barcode, CRD3 nucleotide sequences, and CDR3 amino acid sequences. Each sample input file will be outputted into a separate file.

**Convergence_bulkData.py**

The python code used to select the convergent TCR in bulk TCRbeta-seq data.

  Input file description: 
  
    'sample_name.csv': a file with only one column which contains the names of each sample file
    
    'sample.tsv': the standerd .tsv file downloaded from InmuneAccess.
   
  Output file description: 
  
    'sample_po.cvs': a file containing the CDR3 CRD3 nucleotide sequences, CDR3 amino acid sequences, counts and frequency info of all the detected productive TCR rearrangements.
    
    'sample_di.cvs': a file containing the CDR3 CRD3 nucleotide sequences, CDR3 amino acid sequences, counts, and frequency info of convergent T cell clones.
    
**Degeneracy.py**

The python code used to assign the degeneracy of each TCR amino acid sequence in bulk TCRbeta-seq data.

  Input file description:

    'sample_name.csv': a file with only one column which contains the names of each sample file
    
    'sample_po.cvs': the output file of the above-mentioned 'Convergence_bulkData.py'.
  
  Output file description: 
  
    'Degeneracy.csv': a file with two columns, which are the TCR protein (amino acid sequence) and its corresponding degeneracy. The output of all the sample files will be put into this single file.

**Note**

Since convergent T cells constitute a small proportion of the entire T cell population, analysis of high-throughput data can generate more precise and informative results. To have an overall reflection of the sample, including predicting immunotherapy responses, bulk TCRbeta-seq is preferred over scTCR-seq, which usually has a lower throughput.



