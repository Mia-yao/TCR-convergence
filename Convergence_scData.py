import pandas as pd
import os

#Put the sample names into one file 'sample_name.csv'
name=open(r'\sample_name.csv','r')
names=name.readlines()
names=[i.strip() for i in names]


for SRA in names:
    #Process the raw TCR-seq file
    a=pd.read_csv(r'\filtered_contig_annotations_%s'%(SRA)+'.csv')
    a=a[['barcode','chain','v_gene','cdr3','cdr3_nt']]
    a=a.dropna(how='any')
    TRA=a.loc[a['chain']=='TRA',]
    TRB=a.loc[a['chain']=='TRB',]
    TRA=TRA.drop_duplicates(subset='barcode',keep=False)
    TRB=TRB.drop_duplicates(subset='barcode',keep=False)
    TCR=pd.concat([TRA,TRB])
    TCR=TCR.loc[TCR.duplicated(subset='barcode',keep=False),]
    TRA=TCR.loc[TCR['chain']=='TRA',]
    TRB=TCR.loc[TCR['chain']=='TRB',]
    TRA=TRA.set_index('barcode',drop=True)
    TRB=TRB.set_index('barcode',drop=True)
    TRA.sort_values(by='barcode')
    TRB.sort_values(by='barcode')
    TRA.reset_index()
    TRB.reset_index()
    TCR=pd.concat([TRA,TRB],axis=1,ignore_index=True)
    TCR.to_csv(r'\tcr.csv')

    #Conbine the CDR3 sequence and variable gene of both alpha and beta chains
    a=open(r'\tcr.csv','r')
    b=open(r'\tcr_processed_%s'%(SRA)+'.csv','w')
    c=a.readlines()
    c=c[1:]
    first='barcode,TCR_nt,TCR_aa'+'\n'
    b.write(first)
    for i in c:
        i=i.strip()
        barcode,TRA,TRA_v,TRA_cdr3,TRA_cdr3nt,TRB,TRB_v,TRB_cdr3,TRB_cdr3nt=i.split(',')
        new=barcode+','+TRA+':'+TRA_cdr3nt+'_'+TRB+':'+TRB_cdr3nt+','+TRA+':'+TRA_v+'/'+TRA_cdr3+'_'+TRB+':'+TRB_v+'/'+TRB_cdr3+'\n'
        b.write(new)
    a.close()
    b.close()

    b=pd.read_csv(r'\tcr_processed_%s'%(SRA)+'.csv')
    TCR=b.sort_values(by='TCR_aa')
    TCR=TCR.loc[TCR.duplicated(subset='TCR_aa',keep=False),]
    TCR.to_csv(r'\tcr_di.csv',index=0)
    os.remove(r'\tcr.csv')

    #Select out convergent TCR 
    a=open(r'\tcr_di.csv','r') #Contain TCR amino acid detected in more than one cell
    al=open(r'\tcr_processed_%s'%(SRA)+'.csv','r') #Contain all the TCR reads
    b=open(r'\Convergence_%s'%(SRA)+'.csv','w') #Convergent TCRs files
    rev=open(r'\Convergence_%s'%(SRA)+'_rev.csv','w') #Non-convergent TCRs files
    c=a.readlines()
    b.write(first)
    rev.write(first)
    aa=[]
    nt=[]
    tmp=[]
    for i in c: 
        q=i.strip()
        barcode,TCR_nt,TCR_aa=q.split(',')
        if aa==[]:
            aa.append(TCR_aa)
            nt.append(TCR_nt)
            tmp.append(i)
        elif aa!=[] and TCR_aa in aa:
            if TCR_nt not in nt:
                nt.append(TCR_nt)
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
    os.remove(r'\tcr_di.csv')

    #Select non-convergent TCRs
    b=open(r'\Convergence_%s'%(SRA)+'.csv','r')
    p=b.readlines()
    l=al.readlines()
    for i in l:
        if i not in p:
            rev.write(i)
    al.close()
    rev.close()
    os.remove(r'tcr_processed_%s'%(SRA)+'.csv')
