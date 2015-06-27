from pprint import pprint
def dijkstra(graph,start,target):
    inf = float('inf')
##    for u in graph:
##        for v ,w in graph[u]:
##           inf = inf + w                    #menghitung panjang seluruh jarak antar vertex
    dist = dict([(u,inf) for u in graph])   #buat semua jarak antar vertex menjadi infinity/sama dengan jumlah seluruh jarak antar vertex
    prev = dict([(u,None) for u in graph])  #buat dictionary, semua titik vertex dan bernilai None
    q = graph.keys()                        #buat List q, berisi semua Node
    dist[start] = 0                         #dist[start]=0, Deklarasi Asal dengan nilai 0
    #helper function
    def x(v):
        return dist[v]                      #untuk mengembalikan Node yang bernilai paling kecil
    #
    while q != []:                          #selama q tidak kosong!
        u = min(q, key=x)                   #mengambil node yang ada di q dengan jarak yang paling pendek
        q.remove(u)                         #Menghapus Node u
        for v,w in graph[u]:                #Node,Jarak yang ada di graph[u]
            alt = dist[u] + w               #Menyimpan jarak dari Node asal ke Node Selanjutnya
            if alt < dist[v]:               #Cek, apakah alt lebih kecil dari destination V
                dist[v] = alt               #Ubah nilai Distination B degan Alt
                prev[v] = u                 #Ganti Node Asal dari si Next(dist[v])/Menyimpan asal node sebelumnya yang terpendek
    #?way?
    trav = []                               #Array Travel
    jarak=[]
    temp = target                           #temp = tujuan
    while temp != start:                    #Selama temp tidak sama dengan Asal
        if prev[temp]==None:
            break
        trav.append(prev[temp])             #simpan Node sebelumnya dari temp
        jarak.append(dist[temp]-dist[prev[temp]])
        temp = prev[temp]                   #temp = Node sebelumnya,datang dari mana\
    trav.reverse()                          #balikkan List travel
    trav.append(target)                     #tambhkan Node Tujuan
    jarak.reverse()
    return trav,jarak,dist[target]

def PrintTravel(graph,start,end):
    node,jarak,total=dijkstra(graph,start,end)    #memanggil fungsi Dijkstra
    hasil=""                                #deklarasi hasil
    if len(node)==1:                        #jika panjang dari node==1?,panjang node satu jika dari asal ke tujuan tidak ada jalan, maka yang di simpan hanya node tujuan
        hasil="Tidak ada rute dari {0} ke {1}".format(start,end)
    else:
        for i in range(0,len(node)):        #perulangan List node
            if i==0:                        #jika i==0
                hasil=hasil+node[i]         #hasil=hasil+node yang ke i
            else:
                hasil=hasil+" "+str(jarak[i-1])+"-> "+node[i]
    hasil=hasil+"  = "+str(total)
    return hasil

graph = {
    "A" : [('B',20), ('D', 80), ('G', 90)],
    'B' : [('F', 60),('D', 70)],
    'C' : [('F', 50), ('H', 20)],
    'D' : [('G', 20), ('C', 10)],
    'E' : [('B', 50),('G', 30)],
    'F' : [('D', 40),('C', 30)],
    'G' : [('A', 20)],
    'H' : []
    }



##pprint(graph)
#traverse, dist = dijkstra(graph,'A','D')
#dijkstra(graph,'A','D')
#print traverse
#print 'Distance:',dist

a=PrintTravel(graph,'E','H')
print(a)




graph2 = {
    "A" : [('B',2), ('D', 3), ('C', 1)],
    'B' : [('G', 5)],
    'C' : [('F', 8), ('G', 11)],
    'D' : [('C', 10), ('E', 4)],
    'E' : [('H', 13)],
    'F' : [('E', 6),('H', 9)],
    'G' : [('A', 7)],
    'H' : [('D', 12),('G', 14)]
    }

##print(PrintTravel(graph2,'A','D'))



graph3 = {
    "A" : [('B',7.8)],
    'B' : [('C', 8.7),('F', 9.1),('G', 2.3)],
    'C' : [('D', 10.1)],
    'D' : [('H', 7.3)],
    'E' : [('D', 7.7),('I', 6.9)],
    'F' : [('C', 3.6),('E', 10.1),('I', 16.8),('J', 5.9)],
    'G' : [('F', 8.4),('K', 7.6)],
    'H' : [('N', 11.8)],
    'I' : [('H', 9.2),('N', 16.8),('L', 26.8)],
    'J' : [('I', 6.1),('M', 11.6)],
    'K' : [('J', 10.3)],
    'L' : [('N', 14)],
    'M' : [('L', 32.5)],
    'N' : []
    }
##print(PrintTravel(graph3,'A','N'))