

## varibles :



![csharp-data-type1](E:\my_important_notes\typora images\c#\csharp-data-type1.png)

* value data type : short, int, char, float, double etc
* reference data type : String, Class, Object and Interface
* Pointer Data Type :Pointers

-------------

## difference between | , || :

```c#
int x = 5;
int y = 5;
bool z = x == y;
static bool check()
{
    Console.WriteLine("ahmed issa");
    return true;
}

Console.WriteLine(z || check());  // True 
// when it found z = true , it was enough and didn't execute check()
// if z = false , it will execute check()
// if we use || , false || false = false , true || false = true , ....

Console.ReadKey();
```

---------------------------------------------

## Array :

- Random Access

*  index starts from 0
* types :
  1. Single Dimensional Array
  2. Multidimensional Array
  3. Jagged Array

* reference type

* explicitly defining data type :

```c#
int[] arr = { 10, 20, 30, 40, 50 }; // right
var arr = { 10, 20, 30, 40, 50 }; //rong
var arr = new int[5]{ 10, 20, 30, 40, 50 };// right
```

### Single Dimensional Array :

```c#
int[] arr = new int[5];
arr[0] = 10;
arr[2] = 20;  
arr[4] = 30;  
// array with for
for (int i = 0; i < arr.Length; i++)  
{  
            Console.WriteLine(arr[i]);  
}  
// array with foreach
foreach (int i in arr)  
{  
            Console.WriteLine(i);  
} 
```

```c#
// we can initialize the arrasy at the time of declaration
int[] arr = new int[5]{ 
		10,
		20,
		30,
		40,
		50
					}
```

```c#
// we can ignore the size of the array
int[] arr = new int[]{ 10, 20, 30, 40, 50 };
```

```c#
//We can omit the new operator
int[] arr = { 10, 20, 30, 40, 50 };
```

```c#
//We can omit the new operator
int[] arr = { 10, 20, 30, 40, 50 };
```

------------
