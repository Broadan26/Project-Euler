#include <stdio.h>
#include <iostream>

using namespace std;

/* Function reverses potential palindrome numbers and compares them; Returns 1 for palindrome, 0 for not */
/* Helper function for palindrome */
char compare(const int &n1, const int &n2) // Big(O) n
{
	int number1 = n1 * n2, number2 = 0, remainder;
	char check = '0';

	while(number1 != 0)
	{
		remainder = number1 % 10;
		number2 = (number2 * 10) + remainder;
		number1 /= 10;
	}
	number1 = n1 * n2;

	if (number1 == number2) 
	{
		check = '1';
	}
	
	return check;
}

/* Function is used to iterate through numbers and calls compare for palindrome comparison */
int palindrome() //Big(O) n^2
{
	int one = 999, two = 999, palindrome = 0;
	while(one >= 750)
	{
		while(two >= 750)
		{
			if (compare(one, two) == '1' && (one*two) > palindrome) //Perform comparison
			{
				palindrome = one * two;
			}
			
			two = two - 1;
		}
		one = one - 1;
		two = 999;
	}
	return palindrome;
}

/* Answer should be 906609 as the largest palindrome */
int main(int argc, char** argv)
{
	char exit = '1';
	
	while (exit != '0')
	{
		cout << palindrome();
		cin >> exit;
	}
	
	return 0;
}