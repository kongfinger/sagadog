from yahoofinancials import YahooFinancials

def divy(x,y):
        return x/y

def rund(e):
        w={}
        for x in e:
                if x:
                        r=divy(float(x[1]),float(x[2]))
                        if w.has_key(r):
                                w[r].append(x[0])
                        else:
                                w[r]=[]
                                w[r].append(x[0])
        return w

o = open('nasdaq100e')
r = o.read()
r=r.replace('"','')
print r
e=r.split(' ')

i=open('dog')
kl=i.read()
pok=kl.split('\n')
il=len(pok)
print kl
uo=kl
i.close()

sto = []

for x in e:
#       i=open('scf','w')
#       uo=i.read()
#       try:
        #x='AAPL'
#       try:
        print x
        yf=YahooFinancials(x)
#       except:
#               print 'err'
#               continue
        m=yf.get_financial_stmts('quarter','balance')
        z=m.keys()
        w=z[0]
        r=m[w]
        u=r.keys()
        f=r[u[0]]
        try:
                h=f[0]
                        except:
                continue
        j=h.keys()
        k=h[j[0]]
        l=k['totalAssets']
        c=yf.get_ebit()
        uo=uo+x+','+str(c)+','+str(l)+'\n'
        #bb=bb+uo
#       i.write(bb)
#       i.close()
        s = []
        s.append(x)
        s.append(c)
        s.append(l)
        sto.append(s)
        print x,c,l,'\n'
#       except:
#       continue
print sto
print rund(sto)
h=rund(sto)
b=h.keys()
b.sort()
for x in b:
        print x,h[x]
print len(b)
o=open('nasdog','w')
o.write(uo)
o.close()
