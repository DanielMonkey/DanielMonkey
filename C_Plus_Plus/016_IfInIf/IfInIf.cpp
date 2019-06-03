#include <iostream>
using namespace std;

int main()
{
   //declare local variable
   int a = 100;
   int b = 200;

   //check boolean expression
   if(a == 100)
   {
      //if the expression is true, then check the following expression
      if(b == 200)
      {
         //if the expression is true, then print the following state
         cout << "The value of a is 100, and the value of b is 200." << endl;
      }
   }
   cout << "The value of a is " << a << endl;
   cout << "The value of b is " << b << endl;

   return 0;
}
