//------------------------------------------------------------------//
//                       Largest prime factor                       //
//         The prime factors of 13195 are 5, 7, 13 and 29.          //
//          What is the largest prime factor of the number          //
//                          600851475143 ?                          //
//------------------------------------------------------------------//

#include <iostream>
#include <string>

using namespace std;
typedef unsigned long long int ulli;

bool isprime(ulli n);
ulli largest_prime_factor(ulli n);

int main(int argc, char *argv[]) {
  if (argc > 0) {
    ulli num = stoi(argv[1], nullptr, 0);
    cout << num << endl;
  } else
    throw "Please Enter Params";
  return 0;
}

bool isprime(ulli n) {
  bool flag = true;
  for (int i = 2; i < n / 2; i++) {
    if (n % 2 == 0) {
      flag = false;
      break;
    }
  }
  return flag;
}

ulli largest_prime_factor(ulli n) {
  ulli cn = n;
  while (n > 1) {
    n--;
    if (cn % n == 0 && isprime(n))
      break;
  }
  return n;
}
