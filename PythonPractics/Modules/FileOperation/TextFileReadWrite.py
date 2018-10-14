
# coding: utf-8

# In[33]:


from datetime import datetime


#_____________________________________________________
#Read a file
#_____________________________________________________
def ReadFile(filePath):
    file = open(filePath, "r") 
    for line in file: 
        print (line)
        
#ReadFile("C:\\Users\ppradha7\\Desktop\\Desktop\\hyderabad_tours.txt");        

#_____________________________________________________
#Write a file
#_____________________________________________________
def WriteFile(fileContent):
    FilePath=datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S.%f')[:-3]+".txt"
    Content = open(FilePath,'w')
    Content.write(fileContent)
  
#WriteFile("sample text to write");
        

