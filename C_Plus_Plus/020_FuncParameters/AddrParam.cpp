#include <iostream>
using namespace std;

//function declaraion
void swap(int &x, int &y);

int main(void)
{
   //local variable declaration
   int a = 100;
   int b = 200;

   cout << "Before swap, the value of a is " << a << endl;
   cout << "Before swap, the value of b is " << b << endl;

   /*Call the function to swap the value */
   swap(a, b);

   cout << "After swap, the value of a is " << a << endl;
   cout << "After swap, the value of b is " << b << endl;

   return 0;
}

//function definition
void swap(int &x, int &y)
{
   int temp;

   temp = x; /*Store the value of address at x*/
   x = y;    /*Give the value of y to x */
   y = temp; /*Give the value of x to y */

   return;
}

