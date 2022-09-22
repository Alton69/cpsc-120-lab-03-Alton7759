// Christian Alton Bonilla
// CPSC 120-01
// 2022-08-21
// Alton7@csu.fullerton.edu
// @Alton7759
//
// Lab 03-01
// Partners: @peteranteater
//
// you make a order for a sandwitch!
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