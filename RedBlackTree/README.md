# RED-BLACK tree visualization

Feed the script from std_in, see test.txt for example syntax

try

```py3 RBTree.py < Test.txt > Test.dot```


Output is GraphViz dot syntax, see Test.png for the result of Test.txt

## A short note on Red-Black Trees

Red-Black Trees are nice and dandy in theory. Proving that they are sort of balanced is a breze.

Implementing them is hell, hell I tell you!

Insert is fairly straight-forward, but deletion is just pure insanity, and a gazillion rotating cases of fixing a broken tree. 

Also, never ever think 'I can just copy paste the left-case and swap the directions of the code', you can and will mess up.

## Literature

CLRS

FML http://stackoverflow.com/questions/6723488/red-black-tree-deletion-algorithm
