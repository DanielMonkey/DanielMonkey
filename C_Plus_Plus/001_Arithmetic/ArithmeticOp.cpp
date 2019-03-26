#include <iostream>
using namespace std;

int main()
{
   int a = 21;
   int b = 10;
   int c;

   c = a + b;
   cout << "Line 1 - the value of c is " << c << endl;
   c = a - b;
   cout << "Line 2 - the value of c is " << c << endl;
   c = a * b;
   cout << "Line 3 - the value of c is " << c << endl;
   c = a /b ;
   cout << "Line 4 - the value of c is " << c << endl;
   c = a % b;
   cout << "Line 5 - the value of c is " << c << endl;
  
   int d = 10;    //test self adding, mining

   c = d ++;
   cout << "Line 6 - the value of c is " << c << endl;
   
   d = 10;
   c = d --;
   cout << "Line 7 - the value of c is " << c << endl;
   
   d = 10;
   c = ++d;
   cout << "Line 8 - the value of c is " << c << endl;

   d = 10;
   c = --d;
   cout << "Line 9 - the value of c is " << c << endl;
   return 0;
}
