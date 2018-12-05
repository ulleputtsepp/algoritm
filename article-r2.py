#leia tekstifailist pikim sõna, milles ükski täht ei kordu

f=open("article.txt", encoding="UTF-8")
fsisu=f.read() #kogu faili sisu ühe sõnena

fvaike=fsisu.lower().replace(",","").replace(".","").replace("\n","").replace("?","").replace("!","")
sonad=fvaike.split(" ") #list, kus iga sõna on eraldi element
#print(w)
f.close()

# listi elementide/sõnade seast ühekordsete tähtedega sõna leidmine
s=[]
k=0
for sona in sonad:
    for taht in sona: # käib sõna tähthaaval läbi
        k+=sona.count(taht) #summeerib tähtede arvu sõnas
    if k == len(sona): #ühkordselt esinevad tähed korjab välja
        s.append(sona) #korjab sõnad listi
    k=0 # tähtede loendamise lähtestus
#    print(s)
print("Pikim sõna, milles kõik tähed ühekordselt on "+"'"+max(s, key=len)+"'")
#list with maximum length using key function