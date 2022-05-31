#Process the raw TCR-seq file, conbine the CDR3 sequence and variable gene of both alpha and beta chains
a=open(r'\filtered_contig_annotations.csv','r')
b=open(r'\tcr_po.csv','w')
c=a.readlines()
first='barcode,TCR_nt,TCR_aa'+'\n'
b.write(first)
for i in c:
    i=i.strip()
    barcode,TRA,TRA_v,TRA_cdr3,TRA_cdr3nt,TRB,TRB_v,TRB_cdr3,TRB_cdr3nt=i.split(',')
    new=barcode+','+TRA+':'+TRA_cdr3nt+'_'+TRB+':'+TRB_cdr3nt+','+TRA+':'+TRA_v+'/'+TRA_cdr3+'_'+TRB+':'+TRB_v+'/'+TRB_cdr3+'\n'
    b.write(new)
a.close()
b.close()

#Select out convergent TCR 
a=open(r'\tcr_di.csv','r') #Contain TCR amino acid detected in more than one cell
al=open(r'\tcr.csv','r') #Contain all the TCR reads
b=open(r'\Convergence.csv','w') #Convergent TCRs files
rev=open(r'\Convergence_rev.csv','w') #Non-convergent TCRs files
c=a.readlines()
aa=[]
nt=[]
tmp=[]
for i in c:
    q=i.strip()
    barcode,TCR_nt,TCR_aa,state,seurat_clusters,celltype=q.split(',')
    if aa==[]:
        aa.append(TCR_aa)
        nt.append(TCR_nt)
        tmp.append(i)
    elif aa!=[] and TCR_aa in aa:
        if TCR_nt not in nt:
            nt.append(TCR_nt)
            i=q+',T'+'\n'
            tmp.append(i)
        else:
            tmp.append(i)
    elif aa!=[] and TCR_aa not in aa:
        if len(nt)>1:
            b.writelines(tmp)
        tmp=[]
        nt=[]
        aa.append(TCR_aa)
        nt.append(TCR_nt)
        tmp.append(i)
a.close()
b.close()

#Select non-convergent TCRs
b=open(r'\Convergence_rev.csv','r')
p=b.readlines()
l=al.readlines()
for i in l:
    if i not in p:
        rev.write(i)
al.close()
rev.close()
        
