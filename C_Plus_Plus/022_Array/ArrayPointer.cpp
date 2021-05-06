#include <iostream>
using namespace std;

int main()
{
   // a double float array with 5 elements
   double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
   double *p;

   p = balance;

   //print every element of the array
   cout << "use the pointer of array element " << endl;
   for(int i = 0; i < 5; i ++)
   {
      cout << "*(p + " << i << "): ";
      cout << *(p + i) << endl;
   }

   cout << "use balance as the address of array element " << endl;
   for(int i = 0; i < 5; i ++)
   {
      cout << "*(balance + " << i << "): ";
      cout << *(balance + i) << endl;
   }

   return 0;
}
