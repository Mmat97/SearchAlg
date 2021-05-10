import operator
import collections ########ADD

class InputClass:
    algorithmName = ""
    w=0
    h=0
    x=0
    y=0
    maxHDiff=0
    numSites=0
    sites=[]
    cells=[]
 
class Node(object):
    def __init__(self, location, path, distance):
        self.location = location
        self.path = path 
        self.distance = distance


        

def heuristicFunction(cost,currLocation,targetLocation):
    x,y=currLocation
    tx,ty=targetLocation
    h_diagonal = min(abs(x-tx), abs(y-ty))
    h_straight = (abs(x-tx) + abs(t-ty))
        
    return (diagonalCost * h_diagonal) + (cost * (h_straight - (2*h_diagonal)))
        
        
def solutionProcess(inputProc, targetPaths):
    f = open('output.txt', 'w')
    if(targetPaths==[]):
        for coordinate in inputProc.sites:
            f.write('FAIL')
            if(coordinate!=inputProc.sites[-1]):
                f.write('\n')
           
    else:
      
       for coordinate in inputProc.sites:#targetPaths=[[(,), (,)..each with path info]  ...... ] and sites=[(, ), (, )] 
            
            for p in targetPaths:
                print_value='FAIL'
                if(coordinate==p.location):
                    print_value=p.path
                    break
            #s=str(print_value).replace('[','').replace(']','')
            #s=s.replace('(','').replace(')','')
            
            if(print_value!='FAIL'):
                for i in range(len(print_value)):
                    for j in range(len(print_value[i])):
                       s=str(print_value[i][j]) 
                       if j==0:
                           f.write(s)
                           f.write(',')
                       else:
                           f.write(s)
                           if(i!=(len(print_value)-1)):
                               f.write(' ')
                        
                  
            else:
                
                f.write('FAIL')
            if(coordinate!=inputProc.sites[-1]):
                f.write('\n')
    f.close()

       
    
        
        
        
        
        
def listMoves(inputProc, currNode):
    limit=inputProc.maxHDiff
    w=inputProc.w
    h=inputProc.h
    cells=inputProc.cells
    x,y=currNode.location
    listOfMoves=[]
    
    #make sure no out of bounds also since x y are indices
    
    z=0
    
    if(cells[y][x]<0):#negative means rock
        z=abs(cells[y][x])
       
    
    
    
    
    
    
    a=0    
    if((x-1)!=-1 and (y-1)!=-1 ):
        if(cells[y-1][x-1]<0):
            a=abs(cells[y-1][x-1])
        if((abs(a - z) <= limit)):
            listOfMoves.append((x-1,y-1))
    
        
    b=0    
    if((y-1)!=-1):  
        if(cells[y-1][x]<0):
            b=abs(cells[y-1][x])
        if((abs(b - z) <= limit)):
            listOfMoves.append((x,y-1))
    
    c=0
    if((y-1)!=-1 and (x+1)!=w):
        if(cells[y-1][x+1]<0):
            c=abs(cells[y-1][x+1])
        if( (abs(c - z) <= limit)):
            listOfMoves.append((x+1,y-1))
        
        
        
    d=0
    if((x+1)!=w):
        if(cells[y][x+1]<0):
            d=abs(cells[y][x+1])
        if(abs(d - z) <= limit):
            listOfMoves.append((x+1,y))
    e=0
    if((x-1)!=-1):
        if(cells[y][x-1]<0):
            e=abs(cells[y][x-1])
        if((abs(e - z) <= limit)):
            listOfMoves.append((x-1,y))
    
    
    f=0
    if((x-1)!=-1 and (y+1)!=h  ):
        if(cells[y+1][x-1]<0):
            f=abs(cells[y+1][x-1])
        if((abs(f - z) <= limit)):
            listOfMoves.append((x-1,y+1))
    
    g=0
    if((y+1)!=h  ):
        if(cells[y+1][x]<0):
            g=abs(cells[y+1][x])
        if(abs(g - z) <= limit):
            listOfMoves.append((x,y+1))
    j=0
    if((x+1)!=w and (y+1)!=h):
        if(cells[y+1][x+1]<0):
            j=abs(cells[y+1][x+1])
        if(abs(j - z) <= limit):
            listOfMoves.append((x+1,y+1))  
    
    
    
    
    
    
    
    
    
            
    
    
    
    
    
            
    
    
   
            
    

    
            
    
    

    
            
    

    
    
    #print(listOfMoves)
    return listOfMoves

    
    
    
    
    
    
    

        
        
        
        
def findBFS(inputProc):
    explored=[]
    queue=[]
    targets=(inputProc.sites).copy()
    targetCount=len(targets)
    start=Node((inputProc.x, inputProc.y),[(inputProc.x, inputProc.y)], 0)
    queue.append(start)
    explored.append(start.location)
    targetPaths=[]
    explored, queue = set(start.location), collections.deque([start]) ###########ADD
    while len(queue) > 0:
                
        #####DELETEcurrNode=queue[0]
        #####DELETEqueue.pop(0)
        currNode = queue.popleft()######ADD
        if(currNode.location in targets): 
            
            
            
            
            
            targetPaths.append(currNode) 
            targetCount=targetCount-1
            targets.remove(currNode.location)
            if(targetCount==0):          
                return solutionProcess(inputProc, targetPaths )
        for newLocation in listMoves(inputProc,currNode):                      
            if newLocation not in explored:
                
                
                
                    
                ####DELETEexplored.append(newLocation)
                explored.add(newLocation)###ADD
                newpath=(currNode.path).copy()
                newpath.append(newLocation)
                newNode=Node(newLocation,newpath,currNode.distance+1)#1 for BFS
                queue.append(newNode)
                
        
         
                
                
                

    return solutionProcess(inputProc,targetPaths) 











def ucsDistance(currLocation, newLocation):
    x,y=currLocation
    if (x-1, y-1)== newLocation or (x-1, y+1)== newLocation or (x+1, y-1)== newLocation or (x+1, y+1)== newLocation:
        return 14
    else:
        return 10


def aStarDistance(cells,currLocation, newLocation):
    x,y=currLocation
    a,b=newLocation
    
    if(cells[b][a]<0):
        mLevel=0
    else:
        mLevel=abs(cells[b][a])
    
    
    
    z=0
    if(cells[y][x]<0):
        z=abs(cells[y][x])
    n=0
    if(cells[b][a]<0):
            n=abs(cells[b][a])
    hDiff=abs(n - z)
    
    total=mLevel+hDiff
    
    return total
    
    
    
def myFunc(e):
  return e.distance


#####################################################
def findUCS(inputProc):
    explored=[]
    queue=[]
    targets=(inputProc.sites).copy()
    targetCount=len(targets)
    start=Node((inputProc.x, inputProc.y),[(inputProc.x, inputProc.y)], 0)
    queue.append(start)
    explored.append(start.location)
    targetPaths=[]

    ####ADD
    explored, queue = set(start.location), collections.deque([start])


    while len(queue) > 0:
                
        #currNode=queue[0]
        #queue.pop(0)
        currNode = queue.popleft()



        if(currNode.location in targets): 
            
            
            
            
            
            targetPaths.append(currNode) 
            targetCount=targetCount-1
            targets.remove(currNode.location)
            if(targetCount==0):          
                return solutionProcess(inputProc, targetPaths )
        elementsToSort=[]
        for newLocation in listMoves(inputProc,currNode):                      
            if newLocation not in explored:
                
                
                
                    
                #explored.append(newLocation)

                ####ADD
                explored.add(newLocation)




                newpath=(currNode.path).copy()
                newpath.append(newLocation)
                #newNode=Node(newLocation,newpath,currNode.distance+1)#1 for BFS
                newNode=Node(newLocation,newpath,currNode.distance+ucsDistance(currNode.location,newLocation))#1 for BFS
                elementsToSort.append(newNode)
                
        ####DELETEqueue.extend(sorted(elementsToSort, key=operator.attrgetter("distance")))

        ####ADD
        m=queue
        for ii in elementsToSort:
            m.append(ii)

        m=sorted(m, key=operator.attrgetter('distance'))

        if(len(m)>0):
            queue = collections.deque([m[0]])
        for iii in m:
            if(iii!=m[0]):
                queue.append(iii)
        #queue.sort(key=operator.attrgetter('distance'))

     
        
    
    return solutionProcess(inputProc,targetPaths) 
#####################################################         
                
                
                

    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
    '''    
              
        
        
        currNode=queue[0]
        
        queue.pop(0)
        if(currNode.location in targets):
            
            
            
            if(not any(x.location == currNode.location for x in targetPaths)):
                targetPaths.append(currNode) 
                

            else:
                for q in range(len(targetPaths)):
                
                    if currNode.distance <= targetPaths[q].distance and currNode.location==targetPaths[q].location:
                    
                        targetPaths[q]=Node(currNode.location, (currNode.path).copy(), currNode.distance)
                    
                   
                        break 
            
            #targetPaths.append(currNode) 
            #targetCount=targetCount-1
            #targets.remove(currNode.location)
            #if(targetCount==0):        
                #return solutionProcess(inputProc, targetPaths )
        elementsToSort=[]
        
       
        value=''
        l=0
        if(len(targetPaths)==len(targets)):
            l=l+1
            value='Skip'
            total=currNode.distance
            for t in targetPaths:
                if total < t.distance:
                    value='notSkip'
      
        
        if(len(targetPaths)==len(targets) ):#heuristic
            return solutionProcess(inputProc,targetPaths) 
        
        for newLocation in listMoves(inputProc,currNode):
         
            if(value=='Skip'):
                    break
            
            
            
            
            
            
            if newLocation not in currNode.path:
                #if(newLocation not in targets):
                   #explored.append(newLocation)
                
                newpath=(currNode.path).copy()
                newpath.append(newLocation)
                newNode=Node(newLocation,newpath,currNode.distance+ucsDistance(currNode.location,newLocation))#1 for BFS
                #queue.append(newNode)
                elementsToSort.append(newNode)
        
    '''     
        
    


    
    
    
    
    
    
    
    
def findAstar(inputProc):
    explored=[]
    queue=[]
    targets=(inputProc.sites).copy()
    targetCount=len(targets)
    start=Node((inputProc.x, inputProc.y),[(inputProc.x, inputProc.y)], 0)
    queue.append(start)
    explored.append(start.location)
    targetPaths=[]

    ####ADD
    explored, queue = set(start.location), collections.deque([start])


    while len(queue) > 0:
                
        #currNode=queue[0]
        #queue.pop(0)
        currNode = queue.popleft()



        if(currNode.location in targets): 
            
            
            
            
            
            targetPaths.append(currNode) 
            targetCount=targetCount-1
            targets.remove(currNode.location)
            if(targetCount==0):          
                return solutionProcess(inputProc, targetPaths )
        elementsToSort=[]
        for newLocation in listMoves(inputProc,currNode):                      
            if newLocation not in explored:
                
                
                
                    
                #explored.append(newLocation)

                ####ADD
                explored.add(newLocation)




                newpath=(currNode.path).copy()
                newpath.append(newLocation)
                #newNode=Node(newLocation,newpath,currNode.distance+1)#1 for BFS
                newNode=Node(newLocation,newpath,currNode.distance+ucsDistance(currNode.location,newLocation)+aStarDistance(inputProc.cells,currNode.location,newLocation))#1 for BFS
                elementsToSort.append(newNode)
                
        ####DELETEqueue.extend(sorted(elementsToSort, key=operator.attrgetter("distance")))

        ####ADD
        m=queue
        for ii in elementsToSort:
            m.append(ii)

        m=sorted(m, key=operator.attrgetter('distance'))

        if(len(m)>0):
            queue = collections.deque([m[0]])
        for iii in m:
            if(iii!=m[0]):
                queue.append(iii)
            #queue.sort(key=operator.attrgetter('distance'))

     
        
    
    return solutionProcess(inputProc,targetPaths) 
    
    
    
    
    
    
    
    
        
        
def getInput(filename):
    file =  open(filename, "r")
    inputProc = InputClass()
    
    lines = file.readlines() 
    
    
    inputProc.algorithmName = lines[0].replace('\n', '')
    w,h = lines[1].split()
    inputProc.w, inputProc.h = int(w),int(h)
    x, y = lines[2].split()
    inputProc.x, inputProc.y = int(x),int(y)
    inputProc.maxHDiff=int(lines[3])
    inputProc.numSites=int(lines[4])
    for i in range(inputProc.numSites):
        x, y =  lines[i+5].split()
        (inputProc.sites).append((int(x),int(y)))
        
        
    for i in range(inputProc.h):

        (inputProc.cells).append(list(map(int, (lines[i+5+inputProc.numSites].replace('\n', '')).split())))
    
    
    file.close()
    
    
    return inputProc
    
    
    
    
    
    
def main():
    # algorithm name
    #w h 
    #x y for party coord
    #limit height
    # number of settling sites
    
    # ....each with site coordinates
    
    #... each with W numbers
    
    inputProc=getInput('input.txt')
    
    
   
    
                                        
    if(inputProc.algorithmName=="BFS"):
        findBFS(inputProc)
    elif(inputProc.algorithmName=="UCS"):
        findUCS(inputProc)
    elif(inputProc.algorithmName=="A*"):
        findAstar(inputProc)



if __name__ == '__main__':
    main()       
    
    
    
    
