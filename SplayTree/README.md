# SplayTree visualization

Feed the script from std_in, see Test.txt for example syntax

try

```py3 SplayTree.py < Test.txt > Test.dot```

## A short note on Splay Trees

Huh, that was kinda strange

Just implement a function bubbling a node to the top, and abuse that to do splits and jois for inserts and deletes
I expected more actually

Note that this implementation uses the simple, and slightly slower, inserts deletes that work by bubbling to the root. 
Faster, more in-place versions of these exist

We skip the explicit split/join operations, as they are fairly trivial using splays.

## Literature

https://www.cs.cmu.edu/~sleator/papers/self-adjusting.pdf

https://people.eecs.berkeley.edu/~jrs/61b/lec/36

http://courses.cs.washington.edu/courses/cse326/01au/lectures/SplayTrees.ppt

http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Trees/Splay.html