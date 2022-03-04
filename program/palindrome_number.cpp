//------------------------------------------------------------------//
//                Check if palindrome number or not                 //
//------------------------------------------------------------------//

#include <iostream>
#include <string>

bool check_palindrome_number(int num);

int main(int argc, char *argv[]) {
  if (argc) {
    bool pall_num = check_palindrome_number(std::stoi(argv[1]));
    std::cout << pall_num << std::endl;
  } else
    throw "Please Enter Params";

  return 0;
}

bool check_palindrome_number(int num) {
  int s = 0, cpynum = num;
  while (num > 0)
  {
    int r = num % 10;
    s = (s * 10) + r;
    num /= 10;
  }
  if (cpynum == s)
    return true;
  return false;
}
