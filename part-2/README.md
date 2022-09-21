![Formatting](../../../actions/workflows/part-1.yml/badge.svg)

# Unit Conversion

Finish part 1 before you start part 2.

In this part, you will write a program that converts a measurement of volume from milliliters in the metric system, to various units in the US customary system (teaspoons, tablespoons, ounces, and cups).

The conversion ratios between these units of measure are given below.

<p align="center">
4.929 ml ("milliliter") = 1 tsp ("teaspoon")
<br>3 tsp = 1 tbsp ("tablespoon")
<br>2 tbsp = 1 oz ("ounce")
<br>8 oz = 1 cup
</p>

Your program should implement the following algorithm:
1. Declare a `double` variable to store the number of milliliters.
1. Use [`cout`](https://www.learncpp.com/cpp-tutorial/introduction-to-iostream-cout-cin-and-endl/)  and [`cin`](https://www.learncpp.com/cpp-tutorial/introduction-to-iostream-cout-cin-and-endl/) to read the number of milliliters from stantard input, with a prompt. 
1. Declare and initialize a `double` variable that stores the equivalent number of teaspoons.
1. Declare and initialize a `double` variable that stores the equivalent number of tablespoons.
1. Declare and initialize a `double` variable that stores the equivalent number of ounces.
1. Declare and initialize a `double` variable that stores the equivalent number of cups.
1. Use a `cout` statement to print out the message
  ```
  <ML> ml = <TSP> tsp = <TBSP> tbsp = <OZ> oz = <CUPS> cups
  ```

## Example Input and Output

A complete run of the program, with input and output, is given below. The user typed the input after the `:` prompt.

```
Enter ml: 100
100 ml = 20.2881 tsp  = 6.7627 tbsp  = 3.38135 oz  = 0.422669 cups
```

## Test Cases

Follow the black box testing procedure to test your program against the test suite below.
(This procedure was described in detail in part 1.)

Due to the limits of [floating point precision](https://www.learncpp.com/cpp-tutorial/floating-point-numbers/), your program may output numbers that are very slightly different than the ones below. Treat numbers as matching if they are within .001 of each other. For example, if your program prints out that `1 ml = 0.203`, that is close enough to match `0.202881`.

| Test Case | Input                              | Expected Output                                                        |
|-----------|------------------------------------|------------------------------------------------------------------------|
| 1         | 1 ml                               | `1 ml = 0.202881 tsp = 0.067627 tbsp = 0.0338135 oz = 0.00422669 cups` |
| 2         | 0 ml                               | `0 ml = 0 tsp = 0 tbsp = 0 oz = 0 cups`                                |
| 3         | 355 ml (volume of a soda can)      | `355 ml = 72.0227 tsp = 24.0076 tbsp = 12.0038 oz = 1.50047 cups`      |

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

After you have pushed your code, move on to part 3.
