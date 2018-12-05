#milline täht tekstis esineb kõige sagedamini?
f=open("article.txt", encoding="UTF-8")
fsisu=(f.read()) #kogu faili sisu ühe sõnena
fvaike=fsisu.lower().replace(" ","").replace(",","").replace(".","").replace("\n","").replace("?","")
#kõik väiketähtedeks, kaotab sõnavahed, komad, punktid, reavahed
#print(fvaike)
f.close()

s=[]
for el in fvaike:
    s.append(el) #teeb listi

d=[]
for ele in s:
    k=s.count(ele)
    d.append(k)
##print(max(d))
index=d.index(max(d))
print("Kõige sagedasem täht "+"'"+s[index]+"'"+" esineb "+ str(max(d))+" korda")