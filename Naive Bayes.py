file=open("tic-tac-toe.data",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    for i in range(9):
        q=r.find(',',p+1)
        temp.append(r[p+1:q])
        p=q
    temp.append(r[p+1:-1])
    p=-1
    q=0
    a1.append(temp)

p=0
n=0
for i in range(len(l)):
    if a1[i][-1]=="positive":
        p+=1
n=len(l)-p
pos=p/len(l)
neg=1-pos
ac=0
for nod in range(len(l)):
    pp=pos
    np=neg
    for i in range(9):
        sp=0
        sn=0
        for c in range(len(l)):
            if c!=nod:
                if a1[c][-1]=="positive":
                    if a1[nod][i]==a1[c][i]:
                        sp+=1
                else:
                    if a1[nod][i]==a1[c][i]:
                        sn+=1
        sp/=p
        sn/=n
        pp*=sp
        np*=sn
    if pp>np:
        fd="positive"
    else:
        fd="negative"
    if a1[nod][-1]==fd:
        ac+=1

ac/=(len(l))
print("Tic-Tac-Toe Endgame Data Set: "+str(ac))
        
file=open("SPECT.train",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    for i in range(22):
        q=r.find(',',p+1)
        temp.append(r[p+1:q])
        p=q
    temp.append(r[p+1:-1])
    p=-1
    q=0
    a1.append(temp)
    
nop=0
n=0
for i in range(len(l)):
    if a1[i][0]=='1':
        nop+=1
n=len(l)-nop
pos=nop/len(l)
neg=1-pos
ac=0

file=open("SPECT.test",'r')
m=file.readlines()
a2=[]
p=-1
q=0
for r in m:
    temp=[]
    for i in range(22):
        q=r.find(',',p+1)
        temp.append(r[p+1:q])
        p=q
    temp.append(r[p+1:-1])
    p=-1
    q=0
    a2.append(temp)
    
for c in range(len(m)):
    pp=pos
    np=neg
    for i in range(1,23):
        sp=0
        sn=0
        for j in range(len(l)):
            if a1[j][0]=='1':
                if a1[j][i]==a2[c][i]:
                    sp+=1
            else:
                if a1[j][i]==a2[c][i]:
                    sn+=1
        sp/=nop
        sn/=n
        pp*=sp
        np*=sn
    if pp>np:
        fd='1'
    else:
        fd='0'
    if a2[c][0]==fd:
        ac+=1

ac/=(len(m))
print("SPECT Heart Data Set: "+str(ac))

file=open("soybean-small.data",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    for i in range(35):
        q=r.find(',',p+1)
        temp.append(r[p+1:q])
        p=q
    temp.append(r[p+1:-1])
    p=-1
    q=0
    a1.append(temp)
    
d1=0
d2=0
d3=0
d4=0
for i in range(len(l)):
    if a1[i][-1]=="D1":
        d1+=1
    elif a1[i][-1]=="D2":
        d2+=1
    elif a1[i][-1]=="D3":
        d3+=1
    elif a1[i][-1]=="D4":
        d4+=1
ac=0

for nod in range(len(l)):
    pd1=d1/len(l)
    pd2=d2/len(l)
    pd3=d3/len(l)
    pd4=d4/len(l)
    for i in range(35):
        sd1=0
        sd2=0
        sd3=0
        sd4=0
        for c in range(len(l)):
            if c!=nod:
                if a1[c][-1]=="D1":
                    if a1[nod][i]==a1[c][i]:
                        sd1+=1
                elif a1[c][-1]=="D2":
                    if a1[nod][i]==a1[c][i]:
                        sd2+=1
                elif a1[c][-1]=="D3":
                    if a1[nod][i]==a1[c][i]:
                        sd3+=1
                elif a1[c][-1]=="D4":
                    if a1[nod][i]==a1[c][i]:
                        sd4+=1
        sd1/=d1
        sd2/=d2
        sd3/=d3
        sd4/=d4
        pd1*=sd1
        pd2*=sd2
        pd3*=sd3
        pd4*=sd4
        
    if not(pd1==0 and pd2==0 and pd3==0 and pd4==0):
        k=max(pd1,pd2,pd3,pd4)
        fl=0
        if k==pd1:
            if a1[nod][-1]=="D1":
                ac+=1
                fl=1
        if k==pd2 and fl==0:
            if a1[nod][-1]=="D2":
                ac+=1
                fl=1
        if k==pd3 and fl==0:
            if a1[nod][-1]=="D3":
                ac+=1
                fl=1
        if k==pd4 and fl==0:
            if a1[nod][-1]=="D4":
                ac+=1
                fl=1
    
ac/=(len(l))
print("Soybean(Small) Data Set: "+str(ac))

file=open("shuttle-landing-control.data",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    for i in range(6):
        q=r.find(',',p+1)
        temp.append(r[p+1:q])
        p=q
    temp.append(r[p+1:-1])
    p=-1
    q=0
    a1.append(temp)

p=0
n=0
for i in range(len(l)):
    if a1[i][0]=='2':
        p+=1
n=len(l)-p
pos=p/len(l)
neg=1-pos
ac=0

for nod in range(len(l)):
    pp=pos
    np=neg
    for i in range(1,7):
        sp=0
        sn=0
        for c in range(len(l)):
            if c!=nod:
                if a1[c][0]=='2':
                    if a1[c][i]!='*' and a1[nod][i]==a1[c][i]:
                        sp+=1
                else:
                    if a1[c][i]!='*' and a1[nod][i]==a1[c][i]:
                        sn+=1
        sp/=p
        sn/=n
        pp*=sp
        np*=sn
        
    if pp>np:
        fd='2'
    else:
        fd='1'
    if a1[nod][0]==fd:
        ac+=1

ac/=(len(l))
print("Shuttle Landing Control Data Set: "+str(ac))




import random
file=open("monks-1.train",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a1.append(temp)
    
nop=0
n=0
for i in range(len(l)):
    if a1[i][0]=='1':
        nop+=1
n=len(l)-nop
pos=nop/len(l)
neg=1-pos
ac=0

file=open("monks-1.test",'r')
m=file.readlines()
a2=[]
p=-1
q=0
for r in m:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a2.append(temp)

for c in range(len(m)):
    pp=pos
    np=neg
    for i in range(1,7):
        sp=0
        sn=0
        for j in range(len(l)):
            if a1[j][0]=='1':
                if a1[j][i]==a2[c][i]:
                    sp+=1
            else:
                if a1[j][i]==a2[c][i]:
                    sn+=1
        sp/=nop
        sn/=n
        pp*=sp
        np*=sn
    if pp>np:
        fd='1'
    else:
        fd='0'
    if a2[c][0]==fd:
        ac+=1

ac/=(len(m))
print("MONK's Problems Data Set 1: "+str(ac))
        
import random
file=open("monks-2.train",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a1.append(temp)
    
nop=0
n=0
for i in range(len(l)):
    if a1[i][0]=='1':
        nop+=1
n=len(l)-nop
pos=nop/len(l)
neg=1-pos
ac=0

file=open("monks-2.test",'r')
m=file.readlines()
a2=[]
p=-1
q=0
for r in m:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a2.append(temp)

for c in range(len(m)):
    pp=pos
    np=neg
    for i in range(1,7):
        sp=0
        sn=0
        for j in range(len(l)):
            if a1[j][0]=='1':
                if a1[j][i]==a2[c][i]:
                    sp+=1
            else:
                if a1[j][i]==a2[c][i]:
                    sn+=1
        sp/=nop
        sn/=n
        pp*=sp
        np*=sn
    if pp>np:
        fd='1'
    else:
        fd='0'
    if a2[c][0]==fd:
        ac+=1

ac/=(len(m))
print("MONK's Problems Data Set 2: "+str(ac))
        
                
import random
file=open("monks-3.train",'r')
l=file.readlines()

a1=[]
temp=[]
p=-1
q=0
for r in l:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a1.append(temp)
    
nop=0
n=0
for i in range(len(l)):
    if a1[i][0]=='1':
        nop+=1
n=len(l)-nop
pos=nop/len(l)
neg=1-pos
ac=0

file=open("monks-3.test",'r')
m=file.readlines()
a2=[]
p=-1
q=0
for r in m:
    temp=[]
    q=r.find(' ',p+1)
    p=q
    for i in range(7):
        q=r.find(' ',p+1)
        temp.append(r[p+1:q])
        p=q
    p=-1
    q=0
    a2.append(temp)

for c in range(len(m)):
    pp=pos
    np=neg
    for i in range(1,7):
        sp=0
        sn=0
        for j in range(len(l)):
            if a1[j][0]=='1':
                if a1[j][i]==a2[c][i]:
                    sp+=1
            else:
                if a1[j][i]==a2[c][i]:
                    sn+=1
        sp/=nop
        sn/=n
        pp*=sp
        np*=sn
    if pp>np:
        fd='1'
    else:
        fd='0'
    if a2[c][0]==fd:
        ac+=1

ac/=(len(m))
print("MONK's Problems Data Set 3: "+str(ac))
        
                
                    
            
        
        
        
        
        
    
    
    
        
    
    
        
        
        
    
    
    
        
    
    

        
                
                    
            
        
        
        
        
        
    
    
    
        
    
    

        
                 
                    
            
        
        
        
        
        
    
    
    
        
    
    

        
                
                    
            
        
        
        
        
        
    
    
    
        
    
    
    
        
        
        
    
    
    
        
    
    
