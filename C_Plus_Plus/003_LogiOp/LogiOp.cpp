#include <iostream>
using namespace std;

int main()
{
   int a = 5;
   int b = 20;
   int c;

   if(a && b)
   {
      cout << "Line 1 - The condition is true." << endl;
   }

   if(a || b)
   {
      cout << "Line 2 - The condition is true." << endl;
   }

   /* Change the value of a and b*/
   a = 0;
   b = 10;
   
   if(a && b)
   {
      cout << "Line 3 - The condition is true." << endl;
   }
   else
   {
      cout << "Line 4 - The condition is false." << endl;
   }

   if(!(a && b))
   {
      cout << "Line 5 - The condition is true." << endl;
   }
   else
   {
      cout << "Line 6 - The condition is false." << endl;
   }
   
   return 0;
}
