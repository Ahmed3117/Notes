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
---
## varibles :
* value data type : short, int, char, float, double etc
* reference data type : String, Class, Object and Interface
* Pointer Data Type :Pointers
---------
## type conversion :

-   **Implicit Casting** (automatically) - converting a smaller type to a larger type size  
    `char` -> `int` -> `long` -> `float` -> `double`  
```csharp
int myInt = 9;
double myDouble = myInt;       // Automatic casting: int to double
```

-   **Explicit Casting** (manually) - converting a larger type to a smaller size type  
    `double` -> `float` -> `long` -> `int` -> `char`

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
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));    // convert int to string
Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
Console.WriteLine(Convert.ToString(myBool));   // convert bool to string
```
-------
## const :
```csharp
// const prevents the override
// You cannot declare a constant variable without assigning the value
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
