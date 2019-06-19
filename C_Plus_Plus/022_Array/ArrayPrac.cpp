#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

int main()
{
   int n[10]; // n is an array which have 10 int numbers

   //initial the array n
   for(int i = 0; i < 10; i ++)
   {
      n[i] = i + 100; //set the value of element i to i + 100
   }

   cout << "Element" << setw(13) << "Value" << endl;

   //print out the value of every element
   for(int j = 0; j < 10; j ++)
   {
      cout << setw(7) << j << setw(13) << n[j] << endl;
   }

   return 0;
}
