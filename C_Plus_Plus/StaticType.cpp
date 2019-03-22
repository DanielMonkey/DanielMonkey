#include <iostream>

//function declaration
void func(void);

static int count = 10; /*Global Variable */

int main()
{
   while(count --)
   {
      func();
   }
   return 0;
}

//function definition
void func(void)
{
   static int i = 5;   //Local static variable
   i ++;

   std::cout << "Variable i is " << i;
   std::cout <<", Variable count is " << count << std::endl;

}
