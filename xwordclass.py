""" Crossword Class demonstration"""

#########
# CONSTANTS
#########
#input grid
BLACKSQ='.'
WHITESQ='*'
#in working grid
FILLED='#'
EMPTYSQ=''


############
# Class
############


class Xword:
    def __init__(self,puzzle):
        #list all the variables this class will calculate and use
        self.puzzle:int=puzzle
        self.stacklets:list=[]
        self.grid:str=''
        self.gridsize:str=''
        self.cols:int=0
        self.rows:int=0
        self.gridlets:list=[] #entire output crossword grid with some possible filled letters
        self.nodes:list=[] #'words' of the puzzle represented by cell numbers
        self.acrossd:dict={}
        self.downd:dict={}
        self.wordstarts:list=[]
        
        #calculate grid,gridsize,cols,rows,gridlets
        self.getvars(puzzle)
        #calculate nodes,acrosssqs,downsqs
        self.makenodes(self.grid,self.cols,self.rows)
        
    def getvars(self,puzzle:int):
        #calculate grid,gridsize,cols,rows,gridlets
        with open("./json/puzzdata.json","r") as f:
            datain=json.loads(list(f)[puzzle-1])
        
        self.grid=datain["grid"]
        self.gridsize=datain["gridsize"]
        self.cols=int(datain["cols"]) if "cols" in datain \
                                      else int(self.gridsize[(self.gridsize.upper().index('X'))+1:])
        self.rows=int(datain["rows"]) if "rows" in datain \
                                      else int(self.gridsize[:(self.gridsize.upper().index('X'))])
        self.gridlets=[(FILLED if self.grid[i]==BLACKSQ
                       else EMPTYSQ)
                       for i in range(len(self.grid))]
        if "gridlets" in datain:
            for cell,letter in (datain["gridlets"]).items():
                self.gridlets[int(cell)]=letter
                self.stacklets.append(int(cell))

    def makenodes(self,grid,cols,rows):
        nodes:list[list]=[]
        acrosssqs:list=[]
        downsqs:list=[]
        counter:int=0
        acrossd:dict={}
        downd:dict={}
        tmpnode:list[int]
        #wordstarts:list=[] #cells where words start
                
        #across
        tmpnode=[]
        for cell in range(len(grid)):
            if not (cell)%cols: #beginning of row
                if len(tmpnode)>1: #hanging
                #if tmpnode!=[]:
                    nodes.append(tmpnode)
                tmpnode=[]
            if grid[cell]==BLACKSQ:
                if len(tmpnode)>1: #hanging
                #if tmpnode!=[]:
                    nodes.append(tmpnode)
                tmpnode=[]
            else: #WHITESQ
                if len(tmpnode)==0:
                    acrosssqs.append(cell)
                tmpnode.append(cell)
        if len(tmpnode)>1: #hanging
        #if tmpnode!=[]:
            nodes.append(tmpnode)

        #down
        tmpnode=[]
        for count in range(len(grid)):
            #count through the grid down
            cell=((count%rows)*cols) +(count//rows)
            if (cell)<cols:
                if len(tmpnode)>1: #hanging
                    nodes.append(tmpnode)
                tmpnode=[]
            if grid[cell]==BLACKSQ:
                if len(tmpnode)>1: #hanging
                    nodes.append(tmpnode)
                tmpnode=[]
            else: #WHITE
                if len(tmpnode)==0:
                    downsqs.append(cell)
                tmpnode.append(cell)
        if len(tmpnode)>1: #hanging
            nodes.append(tmpnode)
        
        self.nodes=nodes
        acrosssqs=sorted(acrosssqs)
        downsqs=sorted(downsqs)
        self.wordstarts=list(sorted(set(acrosssqs+downsqs)))

        #Make dictionaries of across and down clues
        for cell in range(len(self.gridlets)):
            if cell in self.wordstarts:
                counter+=1
                if cell in acrosssqs:
                    w=[n for n in self.nodes if n[0]==cell and n[1]==cell+1][0]
                    acrossd.update({counter:w})
                if cell in downsqs:
                    w=[n for n in self.nodes if n[0]==cell and n[1]==cell+self.cols][0]
                    downd.update({counter:w})
        self.acrossd=acrossd
        self.downd=downd


#####
#sample program
######
import json

puzzle=4 # 1-based index
puzzledata=Xword(puzzle)

#do something with the data
#actual program will recursively solve the puzzle
#For demonstration, we will just display some of the information
print("Small demonstration\n")
print("Puzzle number: "+str(puzzledata.puzzle))
print("Number of columns: "+str(puzzledata.cols))
print("Number of rows: "+str(puzzledata.rows))
print("Total words: "+str(len(puzzledata.nodes)))

#print the grid
print("\nCurrent puzzle with initial letters filled in:")
patterns={FILLED:"\u2588",
          EMPTYSQ:"\u2591",
         }
for i in range(0,len(puzzledata.gridlets),puzzledata.cols):
    print(''.join([patterns.get(puzzledata.gridlets[cell],puzzledata.gridlets[cell])
           for cell in range(i,i+puzzledata.cols)
          ]))
    
#print the clue boxes
print("\nClues:")    
print('\nAcross:')
for cluenum,cells in puzzledata.acrossd.items():
    print(f'{cluenum:2}: ({len(cells)} letters) {str(cells)}')

print('\nDown:')    
for cluenum,cells in puzzledata.downd.items():
    print(f'{cluenum:2}: ({len(cells)} letters) {str(cells)}')

