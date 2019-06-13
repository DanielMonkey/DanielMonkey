#include <iostream>
using namespace std;

int sum(int a, int b = 20)
{
   int result;

   result = a + b;

   return (result);
}

int main()
{
   //local variable declaration
   int a = 100;
   int b = 200;
   int result;

   //call the function to add value
   result = sum(a, b);
   cout << "Total value is " << result << endl;

   //call the function again
   result = sum(a);
   cout << "Total value is " << result << endl;

   return 0;
}
