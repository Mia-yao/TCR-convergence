#Put the file names into a list
name=open(r'sample_name.csv','r')
names=name.readlines()
names=[i.strip() for i in names]

#Process the files, conbind CDR3 and variable gene of each read. Filter out four information: nucleotide sequence ,aminoacid sequence,count, and frequency
for i in names:
    a=open(r'/%s'%(i)+'.tsv','r')
    b=open(r'/processed/%s'%(i)+'_po.csv','w')
    c=a.readlines()
    c=c[1:]
    b.write('nucleotide,aminoacid,count,frequency\n')
    for l in c:
        each=[k for k in l.split('\t')]
        nucleotide=each[0]
        aminoacid=each[1]
        count=each[2]
        frequency=each[3]
        v_gene=each[6]
        if aminoacid !='' and '*' not in aminoacid:
            if v_gene!='':
                new_a=aminoacid+'_'+v_gene
                out=nucleotide+','+new_a+','+count+','+frequency+'\n'
                b.write(out)
    a.close()
    b.close()

#Select convergent TCR by finding same TCR amino acid sequence with multiple different TCR nucleotide reads
for i in names:
    a=open(r'/processed/%s'%(i)+'_po.csv','r')
    b=open(r'/duplicate/%s'%(i)+'_di.csv','w')
    c=a.readlines()
    c=c[1:]
    c.append('a,b,1,2')
    b.write('nucleotide,aminoacid,count,frequency\n')    
    def aa(line):
        line=line.strip()
        con=[i for i in line.split(',')]
        return con[1]
    c.sort(key=aa,reverse=True)
    aa=[]
    tmp=[]
    for i in c:
        p=i.strip()
        nucleotide,aminoacid,count,frequency=p.split(',')
        if aa==[]:
            aa.append(aminoacid)
            tmp.append(i)
        elif aa!=[] and aminoacid in aa:
            tmp.append(i)
        elif aa!=[] and aminoacid not in aa:
            if len(tmp)>1:
                b.writelines(tmp)
            tmp=[]
            aa.append(aminoacid)
            tmp.append(i)
    a.close()
    b.close()
                


