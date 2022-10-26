#Put the file names into a list
name=open(r'/sample_name.csv','r')
names=name.readlines()
names=[i.strip() for i in names]

#Assign the degeneracy of each TCR amino aicd sequence by counting the number of TCR nucleotide sequences corresponding to it
b=open(r'/Degeneracy.csv','w')
b.write('Amino_acid,degeneracy\n')
for Sample in names:
    ee=open(r'/processed/%s'%Sample+'_po.csv','r')
    a=ee.readlines()
    a=a[1:]
    def aa(line):
        line=line.strip()
        con=[i for i in line.split(',')]
        return con[1]
    a.sort(key=aa,reverse=True)
    a.append('a,b,1,2')
    aa_all=[]
    for i in a:
        q=i.strip()
        nucleotide,aminoacid,n,frequency=q.split(',')
        if aa_all==[] and aminoacid not in aa_all:
            aa_all.append(aminoacid)
            count=1
        elif aminoacid in aa_all:
            count+=1
        elif aa_all!=[] and aminoacid not in aa_all:
            out=aa_all[-1]+','+str(count)+'\n'
            b.write(out)
            count=1
            aa_all.append(aminoacid)
    ee.close()
name.close()
b.close()
            
        
        
