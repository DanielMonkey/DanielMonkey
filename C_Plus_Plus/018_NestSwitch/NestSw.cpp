#include <iostream>
using namespace std;

int main()
{
   //local variable declaration
   int a = 100;
   int b = 200;

   switch(a)
   {
   case 100:
      cout <<"This is a part of external switch" << endl;
      switch(b)
      {
      case 200:
         cout <<"This is a part of inside switch" << endl;
      }
   }
   cout <<"The value of a is " << a <<endl;
   cout <<"The value of b is " << b <<endl;

   return 0;
}
