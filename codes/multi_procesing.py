import multiprocessing
import requests
import concurrent.futures

def download(url,name):
    print(f"Started Downloading {name}")
    re=requests.get(url)
    open(f"{name}.jpg","wb").write(re.content)
    print(f"Finished Downloading {name}")
    
    
url="https://picsum.photos/200/300"    
# one of the process to call multiprocessing
# pros=[]
# for i in range(5):
#    # download(url,i)
#    p=multiprocessing.Process(target=download,args=[url,i])
#    p.start()
#    pros.append(p)
   
#    for p in pros:
#        p.join()
   

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    l1=[i for i in range(5)]
    l2=[url for i in range(5)]
    results=executor.map(download,l2,l1)
    for r in results:
        print(r)