#include <iostream>
using namespace std;

//function declaration
double getAverage(int arr[], int size);

int main()
{
   //the int array with five elements
   int balance[5] = {1000, 2, 3, 17, 50};
   double avg;

   //send the pointer of an array as the parameter
   avg = getAverage(balance, 5);

   //print the return value
   cout << "The average value is " << avg << endl;

   return 0;
}

double getAverage(int arr[], int size)
{
   int i, sum = 0;
   double avg;

   for(i = 0; i < size; i ++)
   {
      sum += arr[i];
   }

   avg = double(sum) / size;

   return avg;
}
