// Christian Alton Bonilla
// CPSC 120-01
// 2022-08-21
// Alton7@csu.fullerton.edu
// @Alton7759
//
// Lab 03-01
// Partners: @peteranteater
//
// Convert milliliters to units of the US customary system.
//

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[]) {
  double milliliters{69};
  cout << "Ender Ml: ";
  cin >> milliliters;
  double teaspoon{milliliters / 4.929};
  double tablespoon{teaspoon / 3};
  double ounce{tablespoon / 2};
  double cup{ounce / 8};
  cout << milliliters << " ml = " << teaspoon << " tsp = " << tablespoon
       << " tbsp = " << ounce << " oz = " << cup << " cups\n";

  return 0;
}
