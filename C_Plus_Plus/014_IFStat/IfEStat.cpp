#include <iostream>
using namespace std;

int main()
{
   //local variable declaration
   int a = 100;

   // check boolean condition
   if(a < 20)
   {
      //if condition is true, then print following statements
      cout << "a is less than 20." << endl;
   }
   else
   {
      //if condition is false, then print following statements
      cout << "a is greater than 20." << endl;
   }

   cout << "The value of a is " << a << endl;

   return 0;
}
