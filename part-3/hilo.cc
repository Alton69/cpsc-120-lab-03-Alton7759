// Christian Alton Bonilla
// CPSC 120-01
// 2022-08-21
// Alton7@csu.fullerton.edu
// @Alton7759
//
// Lab 03-01
// Partners: @peteranteater
//
// Play a hi/lo guessing game.
//

#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  int p1{69};
  int p2{169};
  cout << "before we play would you like to hide player one's number? \n"
       << "Y/N: ";
  string hide;
  cin >> hide;
  if (hide == "Y" || hide == "y") {
    cout << "remember we play with full numbers!\n"
         << "Player 1, enter the secret number: ";
    cin >> p1;
    for (int i{0}; i < 300; i++) {
      cout << "\n";
    }
  } else if (hide == "N" || hide == "n") {
    cout << "too bad they might cheat!\n";
    cout << "remember we play with full numbers!\n"
         << "Player 1, enter the secret number: ";
    cin >> p1;
  } else {
    cout << "I think I'll take that as no? \n";
    cout << "remember we play with full numbers!\n"
         << "Player 1, enter the secret number: ";
    cin >> p1;
  }
  cout << "Player 2, enter your first guess: ";
  cin >> p2;
  if (p2 > p1) {
    cout << "Too High\n";
    cout << "Player 2, enter your second guess: ";
    cin >> p2;
    if (p2 == p1) {
      cout << "Correct, you win!\n";
    } else {
      cout << "Incorrect, the secret number was " << p1 << ", you lose.\n";
    }
  } else if (p2 < p1) {
    cout << "Too Low\n";
    cout << "Player 2, enter your second guess: ";
    cin >> p2;
    if (p2 == p1) {
      cout << "Correct, you win!\n";
    } else {
      cout << "Incorrect, the secret number was " << p1 << ", you lose.\n";
    }
  } else {
    cout << "Correct, you win!\n";
  }
  // I broke I didnt know how to do it but this :<
  return 0;
}