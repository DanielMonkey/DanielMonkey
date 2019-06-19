#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main()
{
   int i, j;

   //she the timer
   srand((unsigned)time(NULL));
   
   //generate 10 random numbers
   for(i = 0; i < 10; i ++)
   {
      //generate random number
      j = rand();
      cout << "Random number is "  << j << endl;
   }

   return 0;
}
