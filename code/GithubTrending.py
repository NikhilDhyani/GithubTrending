from bs4 import BeautifulSoup
import requests
import webbrowser
i=0
response =requests.get("https://github.com/trending")
data= response.text
soup = BeautifulSoup(data,"lxml") 
reponame =[]
language =[]
description = []
print("\t\t***Trending Repos***\n")

for li in soup.find_all("ol",{"class":"repo-list"}):
    language = li.find_all("span",{"class":"mr-3"})
    
    for h in li.find_all("h3"): 
        link = h.find("a")
        name = link.get("href")
        reponame.insert(i,name)
        i=i+1
    i=0    
    for lan in li.find_all("span",{"class":"mr-3"}):
        language.insert(i,lan.next)
        
        i=i+1
    
    i=0
    for desc in li.find_all("p",{"class":"col-9 d-inline-block text-gray m-0 pr-4"}):
        
        description.insert(i,desc.next)
        i=i+1

   
length = len(reponame)
for li in soup.find_all("ol",{"class":"repo-list"}):
    i=0    
    for lan in li.find_all("span",{"class":"mr-3"}):
        
       
        language.insert(i,lan.next)
       
        i=i+1

print("Total Repos = %s\n"%(length))   
for p in range(0,length):
        
        
        print("REPO[%s] = %s"%(p,reponame[p]))
        print("%s"%(description[p]))
        print("%s"%(language[p]))
        print("\n")
option = int(raw_input("want to open any repo else -1 "))
if option!=-1:
   webbrowser.open("https://github.com"+reponame[option])
     
    
