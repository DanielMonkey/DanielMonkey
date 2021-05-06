#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

//generate and return random number
int *getRandom()
{
   static int r[10];

   //set the key
   srand((unsigned)time(NULL));
   
   for(int i = 0; i < 10; i ++)
   {
      r[i] = rand();
      cout << r[i] << endl;
   }

   return r;
}

//the main function which calls the defined function above
int main()
{
   //a pointer point to int
   int *p;

   p = getRandom();

   for(int i = 0; i < 10; i ++)
   {
      cout << "*(p + " << i << "): ";
      cout << *(p + i) << endl;
   }

   return 0;
}
