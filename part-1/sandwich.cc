// Christian Alton Bonilla
// CPSC 120-01
// 2022-08-21
// tuffy.titan@csu.fullerton.edu
// @tuffytitan
//
// Lab 03-01
//
// Print out a description of a sandwich.
//

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[]) {
  string portein;
  cout << "Enter protein: ";
  cin >> portein;
  string bread;
  cout << "Enter bread: ";
  cin >> bread;
  string condiment;
  cout << "Enrer condiment: ";
  cin >> condiment;
  cout << "Your order:\n"
       << "A " << portein << " sandwich on " << bread << " with " << condiment
       << "\n";

  return 0;
}