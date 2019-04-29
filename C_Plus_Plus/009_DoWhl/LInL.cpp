#include <iostream>
using namespace std;

int main()
{
   int i, j;

   for(i = 2; i < 100; i ++)
   {
      for(j = 2; j <= (i / j); j ++)
      {
         if(!(i % j))
         {
            break; //if not find, this value is not.
         }
      }
      
      if(j > (i / j))
      {
         cout << i << " is the value." << endl;
      }
   }

   return 0;
}
