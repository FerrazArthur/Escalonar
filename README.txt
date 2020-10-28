Fell free to use as you want and if you add some new utilities, make sure to do a commit so i can get it too! 
##
ENGLISH MENU:
1-Multiply line by constant
2-Transform first element non 0 of line into pivot
3-Add to a line the multiple of another line
4-Swap lines
5-Swap collumns
6-Show system
7-Show registry of swap's in collumns
9-Change system
10-Exit
##
To insert data, you will need to use a ',' to separate elements in the line like a, b, c and a ';' to separate lines, like a, b, c;d, e, f; g,h,i
this will create a matriz
a b c
d e f
g h i
Easiest way to use:
for each line, use option '2' do define a 'pivo' then use option '4' in all other lines to reduze the collumns bellow 'pivo' to zero;
repeat this processes line by line until you reach the end, so you'll have a identity matriz as 'A' and the 'b' matriz(vector) is going to be the 'x' values to this system.
NOTE: when you use 'swap collumns', you must keep in mind that you also swap the 'x' order. So i wrote a register of collumns change. If you want to contribute to this proj., please do something to inform the currect order of x based on that! it'll be so cool...
IMPORTANT TO NOTE, THIS CODE IS FOR LINEAR SISTEMS LIKE Ax=b so A MUST be NxN(square matriz) and b must be a single line with N elements.
Arthur Ferraz
to send your feedback, contact me on
arthursnc@gmail.com
