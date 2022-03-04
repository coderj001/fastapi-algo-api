//------------------------------------------------------------------//
//                       nth Fibonacci Number                       //
//------------------------------------------------------------------//

#include <iostream>
#include <string>

using namespace std;

int fibonacci_number(int num);

int main(int argc, char *argv[]) {
  if (argc > 0) {
    int fib_num = fibonacci_number(stoi(argv[1]));
    cout << fib_num << endl;
  } else
    throw "Please Enter Params";

  return 0;
}

int fibonacci_number(int n) {
  int t1 = 0, t2 = 1, nxtItem = 0;
  while (n--) {
    if (n < 1)
      break;

    nxtItem = t1 + t2;
    t1 = t2;
    t2 = nxtItem;
  }
  return nxtItem;
}
