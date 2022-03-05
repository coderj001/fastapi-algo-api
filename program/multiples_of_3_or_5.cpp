//------------------------------------------------------------------//
//                       Multiples of 3 or 5                        //
//         If we list all the natural numbers below 10 that         //
//        are multiples of 3 or 5, we get 3, 5, 6 and 9. The        //
//                  sum of these multiples is 23.                   //
//------------------------------------------------------------------//

#include <iostream>
#include <string>

using namespace std;

int multiples_of_3_or_5(int num);

int main(int argc, char *argv[]) {
  if (argc > 0) {
    int ml = multiples_of_3_or_5(stoi(argv[1]));
    cout << ml << endl;
  } else
    throw "Please Enter Params";

  return 0;
}

int multiples_of_3_or_5(int num){
  int sum = 0;
  for (int i = 3; i < num; i++) {
    if(i % 3 == 0 || i % 5 == 0)
      sum+=i;
  }
  return sum;
}
