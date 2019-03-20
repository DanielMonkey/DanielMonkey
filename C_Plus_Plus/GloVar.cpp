#include <iostream>
using namespace std;

//global variable declaration
int g;

int main()
{
   //Local variable declaration
   int a, b;
   
   cout <<"Global g is " <<g <<endl;
   cout <<"Local a, b are " <<a <<", "<<b << endl;

   //Actually initialization
   a = 10;
   b = 20;
   g = a + b;
   
   cout << g << endl;

   return 0;
}
