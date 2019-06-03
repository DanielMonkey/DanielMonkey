#include <iostream>
using namespace std;

int main()
{
   //local variable declaration
   int a = 10;

   // do while exe
   do
   {
      if(a == 15)
      {
         //ignore this loop
         a = a + 1;
         continue;
      }

      cout << "The value of a is " << a << endl;
      a = a + 1;
   }while(a < 20);

   return 0;
}
