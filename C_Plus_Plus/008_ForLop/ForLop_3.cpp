#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main()
{
   string str("some string");
   /* range for statements */
   for(auto &c : str)
   {
      c = toupper(c);
   }

   cout << str << endl;

   return 0;
}
