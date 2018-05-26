# TREAP visualization

Feed the script from std_in, see Test.txt for example syntax

try

```py3 treap.py < Test.txt > Test.dot```


Output is GraphViz dot syntax, see Test.png for the result of Test.txt

## A short note on treaps

Treap basic operations are a joy to implement, the data structure is amazing.

Split/join (and by extension excission) are ez-pz due to natural balance of treaps.
Self-adjustment was strange, due to missing literature.

Finger search is super simple if done by parallel searches (see Gerth paper).

Overall, amazing data structure

## Literature

https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf

https://faculty.washington.edu/aragon/pubs/rst96.pdf

http://www.cs.au.dk/~gerth/papers/finger05.pdf
