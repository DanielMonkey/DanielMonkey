#include <iostream>
using namespace std;

int main()
{
   //Local variable declaration
   char grade = 'D';

   switch(grade)
   {
   case 'A':
      cout <<"Great!" <<endl;
      break;
   case 'B':
   case 'C':
      cout <<"Good!" <<endl;
      break;
   case 'D':
      cout <<"Passed!" <<endl;
      break;
   case 'F':
      cout <<"Try again!" <<endl;
      break;
   default:
      cout <<"Invalid grade!" <<endl;
   }
   cout <<"Your grade is " <<grade <<endl;

   return 0;
}
