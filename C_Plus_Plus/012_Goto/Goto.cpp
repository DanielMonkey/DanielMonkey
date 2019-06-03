#include <iostream>
using namespace std;

int main()
{
   //local variable declaration
   int a = 10;

   //do loop exe
   LOOP: do
   {
      if(a == 15)
      {
         // ingore this loop
         a = a + 1;
         goto LOOP;
      }
      
      cout << "The value of a is " << a << endl;
      a = a + 1;
   }while(a < 20);

   return 0;
}
