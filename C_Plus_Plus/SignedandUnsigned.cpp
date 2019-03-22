#include <iostream>
using namespace std;

/* This program shows the difference between signed and unsigned integers.*/

int main()
{
   short int i;    //signed short int
   short unsigned j;    //unsigned short int

   j = 50000;
  
   i = j;
   
   cout << i << " " << j << endl;

   return 0;
}
