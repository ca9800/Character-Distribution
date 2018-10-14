"""
distribution.py
Author: Claire Adner
Credit: Mr. Dennison

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""


t = str(input("Please enter a string of text (the bigger the better):"))
origanal = t
z = []
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

t = t.lower()
for x in abc:
    z.append(t.count(x))
w = list(zip(z,abc))
q = sorted(w)


q.reverse()

q = sorted(w, key=lambda zsd:(-zsd[0], zsd[1]))

x=0
z=[]

print(' The distribution of characters in "'+origanal+'" is:')
while x<len(q):
    print(q[x][0]*q[x][1])
    x=x+1







