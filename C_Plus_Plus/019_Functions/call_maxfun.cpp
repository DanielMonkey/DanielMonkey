#include <iostream>
using namespace std;

//function declaration
int max(int num1, int num2);

int main(void)
{
   //local variable declaration
   int a = 100;
   int b = 200;
   int ret;

   //call the function to get the max num.
   ret = max(a, b);

   cout << "Max value is: " << ret << endl;

   return 0;
}

//the function return the max one of the two numbers
int max(int num1, int num2)
{
   //local variable declaration
   int result;

   if(num1 > num2)
      result = num1;
   else
      result = num2;

   return result;
}
