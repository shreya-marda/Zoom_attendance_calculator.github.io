def Histogram(L):
    num_bin = 3
    bin_size = (max(L) - min(L))/(num_bin)
    Dict = {}
    m = min(L)
        
    for i in L:
         r=[]
    d={}
    x=max(L)
    y=min(L)
    bin_size=(x-y)/num_bin
    start=y
    end=y+bin_size
    while(end<=x):
        r.append((start,end))      #Using a tuple so that it is hashable and thus can be used as key in the dictionary
        start+=bin_size
        end=start+bin_size
    L.sort()       #Sorting the list
    count=0
    j=0
    for i in L:
        if(r[j][0]<=i<r[j][1]):
            count+=1
        else:
            d['<'+str(r[j][1])]=count
            count=1
            j+=1
        if(j==len(r)):
            break
    return d


    
    

