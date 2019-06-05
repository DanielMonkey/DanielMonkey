#include <iostream>
using namespace std;

//function declaration
void swap(int x, int y);

int main(void)
{
   //local variable declaration
   int a = 100;
   int b = 200;

   cout << "Before swap, the value of a is " << a << endl;
   cout << "Before swap, the value of b is " << b << endl;

   //call the function to swap the value
   swap(a, b);
   
   cout << "After swap, the value of a is " << a << endl;
   cout << "After swap, the value of b is " << b << endl;

   return 0;
}

//function definition
void swap(int x, int y)
{ 
   int temp;
   
   temp = x; //store the value of x
   x = y;    //give the value of y to x
   y = temp; //give the value of x to y
  
   return;
}
