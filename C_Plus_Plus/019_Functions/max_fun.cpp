#include <iostream>
using namespace std;
//function return the max one of two numbers

int max(int num1, int num2)
{
   //local variable declaration
   int result;

   if(num1 > num2)
      result = num1;
   else
      result = num2;

   return result;
}

int main(void)
{
   int max(int num1, int num2);
   //local variable declaration
   int a = 122;
   int b = 133;
   int c;
   
   c = max(a, b);

   cout << "The value of a is " << a << endl;
   cout << "The value of b is " << b << endl;
   cout << "The bigger one is " << c << endl;

   return 0;
}
