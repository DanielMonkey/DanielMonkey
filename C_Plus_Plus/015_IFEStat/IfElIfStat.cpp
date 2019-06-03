#include <iostream>
using namespace std;

int main()
{
   //local variable declaration
   int a = 100;

   //check boolean condition
   if(a == 10)
   {
      // if condition is true, then print the following state
      cout << "The value of a is 10." << endl;
   }
   else if(a == 20)
   {
      //if else if condition is ture, then print the following state
      cout << "The value of a is 20." << endl;
   }
   else if(a == 30)
   {
      //if else if condition is true, then print the following state
      cout << "The value of a is 30." << endl;
   }
   else
   {
      //if all the conditions above are false, then print the following state
      cout << "There is no match value of a." << endl;
   }
   
   cout << "The value of a is " << a << endl;

   return 0;
}
