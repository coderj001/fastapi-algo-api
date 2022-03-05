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
  int t1 = 1, t2 = 2, nxtItem = 0;
  if (n == 1)
    nxtItem = t1;
  else if (n == 2)
    nxtItem = t2;
  else {
    n -= 2;
    while (n--) {
      nxtItem = t1 + t2;
      t1 = t2;
      t2 = nxtItem;

      if (n < 1)
        break;
    }
  }
  return nxtItem;
}
