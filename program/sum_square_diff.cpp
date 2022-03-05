//------------------------------------------------------------------//
//                      Sum square difference                       //
//         The sum of the squares of the first ten natural          //
//                           numbers is,                            //
//          The square of the sum of the first ten natural          //
//                           numbers is,                            //
//           Hence the difference between the sum of the            //
//         squares of the first ten natural numbers and the         //
//                      square of the sum is.                       //
//------------------------------------------------------------------//

#include <iostream>
#include <string>

using namespace std;

long int sum_square_diff(int n);

int main(int argc, char *argv[]) {
  if (argc > 0) {
    cout << sum_square_diff(stoi(argv[1])) << endl;
  } else
    throw "Please Enter Params";

  return 0;
}

long int sum_square_diff(int n) {
  long int t1 = 0, t2 = 0;
  for (int i = 1; i <= n; i++) {
    t1 += i * i;
    t2 += i;
  }
  return t2 * t2 - t1;
}
