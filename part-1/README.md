![Formatting](../../../actions/workflows/part-1.yml/badge.svg)

# Sandwich Mad Lib

[Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs) are a word game that involves a sentence with blanks. Players fill in the blanks in amusing ways. In this part, you will write a program that fills in the blanks for a sentence about a sandwich order:

"A *PROTEIN* sandwich on *BREAD* with *CONDIMENT*."

The italics *PROTEIN*, *BREAD*, and *CONDIMENT* are fill-in-the blanks. For example, if you fill in *PROTEIN*=tuna, *BREAD*=wheat, and *CONDIMENT*=lettuce, the sentence becomes:

"A tuna sandwich on wheat with lettuce."

As you know, computer programs are very good at following patterns. The `sandwich` program will follow a pattern to read the components of a sandwich from standard input, and write out a sentence describing an order for that sandwich as output. A program like this could be a part of a cash register software or ordering app.

Your program should implement the following algorithm:
1. Declare three [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string) variables to store the *PROTEIN*, *BREAD*, and *CONDIMENT* fill-ins.
1. Use [`cout`](https://www.learncpp.com/cpp-tutorial/introduction-to-iostream-cout-cin-and-endl/) to print a prompt for the protein. The prompt must be "Enter protein: ".
1. Use [`cin`](https://www.learncpp.com/cpp-tutorial/introduction-to-iostream-cout-cin-and-endl/) to read a word into the protein variable.
1. Repeat steps 2-3 to prompt and read into the bread variable. The prompt must be "Enter bread: ".
1. Repeat steps 2-3 to prompt and read into the condiment variable.  The prompt must be "Enter condiment: ".
1. Print out a sentence that fits the pattern "A *PROTEIN* sandwich on *BREAD* with *CONDIMENT*."
1. Return exit code 0, to signal success.

## Example Input and Output

When you run your program with `./a.out`, if should first print a prompt that tells the user that they need to enter a protein. The output should resemble:

```
Enter protein: 
```

The program will then pause, and the cursor will blink to the right of the `:` colon. Your prompt does not need to be entirely identical to what is shown above, but it does need to clearly communicate what the user should do.

This example will follow the tuna, wheat, lettuce example described above. So the next step is for the user to type `tuna` and press Enter. Then, the next prompt should appear:

```
Enter protein: tuna
Enter bread: 
```

After the user types `wheat` and Enter, the last prompt appears:

```
Enter protein: tuna
Enter bread: wheat
Enter condiment: 
```

After the user types `lettuce`, the output sentence appears:

```
Enter protein: tuna
Enter bread: wheat
Enter condiment: lettuce
Your order:
A tuna sandwich on wheat with lettuce.
```

The order needs to appear on its own line of output.

## Test Cases

Test your program before moving on. For each of the test cases below,

1. Look at the test suite, and identify the first test case, its input, and expected output.
1. Run your program with `./a.out` .
1. Provide the program with the test case input.
1. If the program crashes, use the **debug runtime error** flowchart to debug the error.
1. Observe the program output and decide whether the actual output matches the expected output.
1. If the output **does not match**, declare that the program fails the test. Use the **debug logic error** flowchart to debug the error.
1. Otherwise (the output **does match**), repeat step 2 with the next test case.

If the program works correctly (meaning no runtime or logic errors) for every test case, declare that the program passes the test. You can move on to releasing your code for part 1.

| Test Case | Input                              | Expected Output                          |
|-----------|------------------------------------|------------------------------------------|
| 1         | tuna, wheat, lettuce               | `A tuna sandwich on wheat with lettuce.` |
| 2         | tomato, rye, mayo                  | `A tomato sandwich on rye with mayo.`    |

## Format Check

As usual, use the `check_lint_and_format` program to check your source code for formatting or lint errors. These formatting requirements are part of the grading rubric.

If you make significant changes to your source file, test it again to confirm that it still passes the test suite. Sometimes a small change that looks benign can actually create a bug.

## Push Your Code

After you have certified that your code passes the test suite and format check, release the code by pushing it to GitHub.

As usualy, you need to
1. Use a computer that is authenticated to git. If your computer is not already authenticated, use the `gcf.sh` script in the **Git Configuration & Authentication* page in Canvas.
1. Add modified file(s) with the `git add` shell command.
1. Create a git commit with the `git commit -m "<MESSAGE>"` shell command.
1. Send the commit to GitHub.com with the `git push` shell command.
1. Refresh the web view of your repo and confirm that your push went through.

If any of these steps trigger an error message, use the **debug command error** flowchart to resolve the problem.

## Next Steps

After you have pushed your code, move on to part 2.
