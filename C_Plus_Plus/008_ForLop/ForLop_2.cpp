#include <iostream>
using namespace std;

int main()
{
   int my_array[5] = {1, 2, 3, 4, 5};
   /* Every element multiply with 2 */
   for(int &x: my_array)
   {
      x *= 2;
      cout << x << endl;
   }

   /* Auto Type */
   for(auto &x : my_array)
   {
      x *= 2;
      cout << x << endl;
   }
 
   return 0;
}
