## print without new line :

```python
# ex:
print("geeks", end =" ") #in end=" " means a space , if it is end="\n" it makes a new line
print("geeksforgeeks")
```

```
out:
geeks geeksforgeeks
```

```python
#ex:
a = [1, 2, 3, 4]
for i in range(4):
    print(a[i], end =" ")
```

```
out:
1 2 3 4
```

```python
#ex:
l=[1,2,3,4]
print(*l) #  * used to loop the list without for , and the rusult in a single line
```

```
out:
1 2 3 4
```

## input :

receive multiple values from user and make them int and store them in a list:

```python
# ex:
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)
```

## print properties :

### sep:

to remove space or change it between words

```python
# ex
x='ahmed'
y='ibra'
z='issa'
print(x,y,z, sep='') # without sep will print ==> ahmed ibra issa
```

```
out:
ahmedibraissa
```



### flush:

when for work , memory wait until loop finishes then execute what next in code (print the result for example) but if flush=True this means that memory empty the current value in it then continue to loop and so on .

```python
import time
for i in reversed(range(4)):
    if i>0:
        print(i,flush=True)
        time.sleep(1)
    else:
        print('start')
```

## string format:

```python
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks'))
```

```
out:
I love Geeks for "Geeks!"
Geeks and Portal
Portal and Geeks
Number one portal is Geeks, For, and Geeks.
```

using dictionary with formate:

```python
data = dict(fun ="GeeksForGeeks", adj ="Portal")
print("I love {fun} computer {adj}".format(**data))
```

```
out:
I love GeeksForGeeks computer Portal
```

## global:

```python
# Python program processing
# global variable

count = 5
def some_method():
	global count
	count = count + 1
	print(count)
some_method()
```

## loops:

### loop without for or while ,...

```python
#ex:
l=[1,2,3,4]
print(*l) #  * used to loop the list without for , and the rusult in a single line
```

```
out:
1 2 3 4
```

## for with function:

```python
# ex:
def digitSum(n):
	dsum = 0
	for x in str(n):
		dsum += int(x)
	return dsum
List = [367, 111, 562, 945, 6726, 873]
newList = [digitSum(i) for i in List if i & 1]
print(newList)
```

## remove duplicates from a Python list :

Sometimes we have a list of objects we want to clean for duplicates. Here's how you do that.            

### Example

```
>>> # Create a list
>>> animals = ["Giraffe", "Lion", "Horse", "Lion", "Giraffe", "Hippo", "Cow"]
>>>
>>> # Remove duplicates
>>> animals = list(dict.fromkeys(animals))
>>>
>>> # Print the list
>>> print(animals)
['Giraffe', 'Lion', 'Horse', 'Lion', 'Giraffe', 'Hippo', 'Cow']
```

### What happened?

First, we create a list with animals. Some of those are duplicates.

Next, we create a new list, based on a dictionary we make from the list.

If we just run the "dict.fromkeys(animals)", we get this:

```
>>> animals = dict.fromkeys(animals)
>>> print(animals)
{'Giraffe': None, 'Lion': None, 'Horse': None, 'Hippo': None, 'Cow': None}
```

So here we have a dictionary with keys and values. Well, the values is None as you can see.

When we convert this to a list, the value will be removed and the key will be preserved.

The reason why the duplicates are removed is that a Python dictionary can't have duplicate keys, so they are just ignored.

​          
