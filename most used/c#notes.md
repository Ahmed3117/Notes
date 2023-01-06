## create c# project in vscode:

```text
* install dotnet : sudo apt install dotnet6
* in termenal :
1- dotnet new console -o test
2- cd test
3- dotnet run    ===> to run the content of the Program.cs file
4- dotnet restore
* open the main file (Program.cs) in the project
* in terminal :
dotnet 
```

----
## display :
```csharp
string name = "John";
Console.WriteLine("Hello " + name);
```

----
## input :
```csharp
string userName = Console.ReadLine(); // accept string by default

int age = Convert.ToInt32(Console.ReadLine());

```

----
## interpolation : ( $ )
```csharp
string firstName = "John";
string lastName = "Doe";
string name = $"My full name is: {firstName} {lastName}";
Console.WriteLine(name);
```

```c#
int num1 = 2;
int num2 = 4;
int sum = $"sum is: {num1+num2}";
Console.WriteLine(sum);
```

------
## difference between null and " "  :

```c#
string s ="";
// the variable s is stored in stack and point to a place in the heap that contains the "" value (the place is reserved bul has empty value)
string g = null; 
// the variable g is stored in stack but dosn't point to any thing in heap (null dosn't reserve a place in the heap) 
```

![[images/csharp/1.png]]

---------
## null check :  null coalescing operator (??)

```c#
string s = null;
s = s ?? "ahmed"  // if s=null , let s = "ahmed"
Console.WriteLine(s); // ahmed
```

## null condisional operator (?) :

```c#
string s = null;
s = s ?.ToUpper(); // convert s to uppercase if it is not null
Console.WriteLine(s);
```
---
## varibles :
* value data type : short, int, char, float, double etc
* reference data type : String, Class, Object and Interface
* Pointer Data Type :Pointers
---------
## type conversion :

-   **Implicit Casting** (automatically) 
	- converting a smaller type to a larger type size  
	    `char` -> `int` -> `long` -> `float` -> `double`  
	* value type to reference type (boxing operation)
*
```csharp
int myInt = 9;
double myDouble = myInt;       // Automatic casting: int to double
```

```csharp
int myInt = 9;
Object obj = myInt;       // Automatic casting: int to double
```

-   **Explicit Casting** (manually) 
	* converting a larger type to a smaller size type  
	    `double` -> `float` -> `long` -> `int` -> `char`
	* reference type to value type  (unboxing operation)

	*`Convert.ToBoolean`,
	`Convert.ToDouble`, 
	`Convert.ToString`,
	`Convert.ToInt32` 
	(`int`) 
	(`long`)
	`Convert.ToInt64`*
	  
```csharp
double myDouble = 9.78;
int myInt = (int) myDouble;    // Manual casting: double to int
```

```csharp
Object obj = 3;      
int i = (int)obj;
```

```csharp
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));    // convert int to string
Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
Console.WriteLine(Convert.ToString(myBool));   // convert bool to string
```

```c#
// convert string to any number type:

string myStr = "12";
int a = int.Parese(myStr);
double b = double.Parese(myStr);

// but if string is not number of out of range of int as "9999999999999999999" ?
// then we will have to check the conversion validation first using tryParse()
//-------------------------------------------

int a;
string myStr = "12";
if (int.TryParse(myStr, out a))
{
	Console.WriteLine("String is converted to: "+a);
}
else
{
	Console.WriteLine("invalid string ,can't be converted to number ");
}
     
```

-------
## Binary converting :

![[Pasted image 20221219043726.png]]

![[Pasted image 20221219043859.png]]

.PadLeft(8,'0')  => means make it 8 bit and fill the empty bits with 0  

there is more about asci ,binary, hexadecimal ,.... in DR : Issam video : 7 minute:40

-------
## const :
```csharp
// const prevents the override
// You cannot declare a constant variable without assigning the value
// in a class , if an attribute is defined as const , then this attribute can't be called by object name but must be called by class name
const int myNum = 15;
myNum = 20; // error
```

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

Console.WriteLine(z | check());  // True 
// when it found z = true , it was enough and didn't execute check()
// if z = false , it will execute check()
// if we use || , false || false = false , true || false = true , ....

Console.ReadKey();
```

------
## if else :
```csharp
int time = 22;
if (time < 10) 
{
  Console.WriteLine("Good morning.");
} 
else 
{
  Console.WriteLine("Good evening.");
}
```

```csharp
int time = 20;
string result = (time < 18) ? "Good day." : "Good evening.";
Console.WriteLine(result);
```

------------
## infinite loop :

```c#
for (;;)
{
	 Console.WriteLine("Good evening.");
}
```

----

## goto statement :

```c#
ineligible:
	Console.WriteLine("You are not eligible to vote!");

Console.WriteLine("Enter your age:\n");
int age = Convert.ToInt32(Console.ReadLine());
if (age < 18){
goto ineligible;
}
else
{
Console.WriteLine("You are eligible to vote!");
}
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

* explicitly (صراحة)defining data type :

```c#
int[] arr = { 10, 20, 30, 40, 50 }; // right
var arr = { 10, 20, 30, 40, 50 }; //wrong
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

```csharp
// Create an array of four elements, and add values later
string[] cars = new string[4];

// Create an array of four elements and add values right away 
string[] cars = new string[4] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements without specifying the size 
var cars = new string[] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements, omitting the new keyword, and without specifying the size
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
```

## jagged array : 

#### aray in array
```csharp
int[][] jagged_arr = new int[4][];
jagged_arr[0] = new int[] {1, 2, 3, 4};
jagged_arr[1] = new int[] {11, 34, 67};
jagged_arr[2] = new int[] {89, 23};
jagged_arr[3] = new int[] {0, 45, 78, 53, 99};
```

```csharp
int[][] jagged_arr = new int[][] 
{
    new int[] {1, 2, 3, 4},
    new int[] {11, 34, 67},
    new int[] {89, 23},
    new int[] {0, 45, 78, 53, 99}
};
```

```csharp
int[][] jagged_arr = 
{
    new int[] {1, 2, 3, 4},
    new int[] {11, 34, 67},
    new int[] {89, 23},
    new int[] {0, 45, 78, 53, 99}
};
```

## Array slicing :

```csharp
var cars = new string[] {"Volvo", "BMW", "Ford", "Mazda"};

var c = cars[..3]; // slice from 0 to 2  {"Volvo", "BMW", "Ford"}
var c = cars[3..]; // slice 3 items from the end  {"BMW", "Ford", "Mazda"} 
var c = cars[1..3]; //slice from 1 to 2  {"BMW", "Ford"}
var c = cars[1..^2]; //start from 1 and get 2 items from the end{"Ford", "Mazda"}
System.Console.WriteLine(c[2]);

```

------------
