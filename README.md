# Part of a portfolio of Python projects developed by Brian Spangler

### Crossword class demonstration  
Demonstration of understanding of Python, classes, OOP, JSON, grid parsing

This is not the entire project. This is just a sample of the class I am using in a larger crossword project.  
This is just demonstrating my understanding of data structures.   

### What it does  
- read a JSON file to pull a crossword grid, size and other information  
- extract all the AROSS and DOWN nodes, starting cells and other info for a crossword puzzle  
- collect all the data into a class for external access  

### Data structure:  
In the Xword class, I have the following values available:
- puzzle: (input) This is the 1-based integer index from the JSON file  
- grid: (from JSON) string representing the squares of the puzzle with '*' representing cells and '.' representing black squares  
- gridsize: (from JSON) A string representing the size of the puzzle, horizontal x vertical  
- cols: (from JSON or extracted from gridsize if not supplied) integer number of columns in the crosssword
- rows: (from JSON or extracted from gridsize if not supplied) integer number of rows in the crossword  
- nodes: calculated list lists of all the connected cells (clues or words)
- gridlets:(optionally initially supplied by JSON) dictionary of cellnumber (as string): letter of initial letters to pad the puzzle to help solve or create a theme. Can also be used for the completion of the puzzle  
- stacklets: initially populated by gridlets. list of cells Used to create an initialize a LIFO stack to recursively solve the puzzle. Not used in this demonstration.  
- wordstarts:list of cells that will have numbers on the crossword puzzle
- acrossd: dictionary of numbered cell:list of cells in the word. The cells of the across words
- downd:dictionary of numbered cell:list of cells in the word. The cells of the down words

### Input JSON:  
can be in any order  
- grid (required): string representing the squares of the puzzle with '*' representing cells and '.' representing black squares  
- gridsize: (required): string representing the size of the puzzle, horizontal x vertical
- cols (optional): columns of the crossword. If not supplied, can be extracted from gridsize  
- rows (optional): rows of the crossword. If not supplied, can be extracted from gridsize     
- gridlets (optional): dictionary of initial letters
- any other information can be used for information or future expansion

### Requirements:
Python 3.7+

### Sample JSON:
<pre>
{ 
  "grid": "*******************.****.",  
  "gridsize": "5x5"  
}  
{
  "grid": "*************************************************",  
  "gridsize": "7x7"  
}  
{
 "gridsize": "5x5",  
 "grid": "***************.***..***.",  
 "date": "10/23",  
 "solution": "ANISECIDERKNEES.JAY..ALA.",  
 "perms": "reed|right",  
 "city": "Tucson"  
}  
{
 "gridsize": "15x15",  
 "source": "Games Magazine, Aug 2011, p 19",  
 "grid": "*****.*****.********.*****.**************.***..****.***.***********.***********.****.****.***.****.***....*************....***.****.***.****.****.***********.***********.***.****..***.**************.*****.********.*****.*****",  
 "gridlets": {
    "21": "B",
    "50": "N",
    "172": "Z",
    "150": "C",
    "136": "T",
    "141": "F",
    "123": "V",
    "74": "E",
    "12": "Q",
    "27": "U",
    "42": "I",
    "56": "H",
    "111": "O"
 }  
}  
</pre>
  
### File structure: 
<pre>
Crossword/  
|- xwordclass.py  
|- README.md  
|- json/  
|-- puzzdata.json  
</pre>
### Sample output:  
>Small demonstration  
>  
>Puzzle number: 4  
>Number of columns: 15  
>Number of rows: 15  
>Total words: 78  
>  
>Current puzzle with initial letters filled in:  
>░░░░░█░░░░░█Q░░  
>░░░░░█B░░░░█U░░  
>░░░░░░░░░░░█I░░  
>██░░░N█░░░█H░░░  
>░░░░░░░█░░░░░░E  
>░░░░█░░░░█░░░░█  
>░░░█░░░░█░░░███  
>█░░░░░O░░░░░░░█  
>███V░░█░░░░█░░░  
>█T░░░█F░░░█░░░░  
>C░░░░░░█░░░░░░░  
>░░░░█░░Z█░░░░██  
>░░░█░░░░░░░░░░░  
>░░░█░░░░░█░░░░░  
>░░░█░░░░░█░░░░░  
>  
>Clues:  
>  
>Across:  
> 1: (5 letters) [0, 1, 2, 3, 4]  
> 6: (5 letters) [6, 7, 8, 9, 10]  
>11: (3 letters) [12, 13, 14]  
>14: (5 letters) [15, 16, 17, 18, 19]  
>15: (5 letters) [21, 22, 23, 24, 25]  
>16: (3 letters) [27, 28, 29]  
>17: (11 letters) [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]  
>.  
>.  
>.   
>  
>
>Down:  
> 1: (3 letters) [0, 15, 30]  
> 2: (3 letters) [1, 16, 31]  
> 3: (8 letters) [2, 17, 32, 47, 62, 77, 92, 107]  
> 4: (6 letters) [3, 18, 33, 48, 63, 78]  
> 5: (5 letters) [4, 19, 34, 49, 64]  
> 6: (3 letters) [6, 21, 36]  
> 7: (4 letters) [7, 22, 37, 52]  
> 8: (6 letters) [8, 23, 38, 53, 68, 83]  
> 9: (5 letters) [9, 24, 39, 54, 69]  
>10: (3 letters) [10, 25, 40]  
>11: (6 letters) [12, 27, 42, 57, 72, 87]  
>12: (6 letters) [13, 28, 43, 58, 73, 88]  
>13: (5 letters) [14, 29, 44, 59, 74]  
>18: (7 letters) [35, 50, 65, 80, 95, 110, 125]  
>22: (5 letters) [56, 71, 86, 101, 116]  
>23: (3 letters) [60, 75, 90]  
>.  
>.
>.



