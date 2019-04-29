#include <iostream>
using namespace std;

int main()
{
   /*Local varialbe declaration */
   int a = 10;
   
   /* Do loop execution*/
   do
   {
      cout << "The value of a: " << a <<endl;
      a = a + 1;
      if(a > 15)
      {
         /* End the loop*/
         break;
      }
   }while(a < 20); 
 
   return 0;
}
