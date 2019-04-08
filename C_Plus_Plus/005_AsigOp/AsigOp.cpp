#include <iostream>
using namespace std;

int main()
{
   int a = 21;
   int c;

   c = a;
   cout << "Line 1 - = Assign Operator Example, the value of c is " << c << endl;

   c += a;
   cout << "Line 2 - += Assign Operator Example, the value of c is " << c << endl;

   c -= a;
   cout << "Line 3 - -= Assign Operator Example, the value of c is " << c << endl;

   c *= a;
   cout << "Line 4 - *= Assign Operator Example, the value of c is " << c << endl;

   c /= a;
   cout << "Line 5 - /= Assign Operator Example, the value of c is " << c << endl;

   c = 200;
   c %= a;
   cout << "Line 6 - %= Assign Operator Example, the value of c is "  << c << endl;

   c <<= 2;
   cout << "Line 7 - <<= Assign Operator Example, the value of c is " << c << endl;

   c >>= 2;
   cout << "Line 8 - >>= Assign Operator Example, the value of c is " << c << endl;

   c &= 2;
   cout << "Line 9 - &= Assign Operator Example, the value of c is "  << c << endl;

   c ^= 2;
   cout << "Line 10 - ^= Assign Operator Example, the value of c is "  << c << endl;

   c |= 2;
   cout << "Line 11 - |= Assign Operator Example, the value of c is "  << c << endl;

   return 0;
}
