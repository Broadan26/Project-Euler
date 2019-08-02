#include <stdio.h>
#include <iostream>

using namespace std;

/* Determines the sum of each square of n */
long long squareEach(const int &number)
{
	long sum = 0;

	for(int i = 0; i <= number; i ++)
	{
		sum = sum + (i*i);
	}
	
	return sum;
}

/* Determines the square of the sum of n */
long long sumSquare(const int &number)
{
	long sum = 0;

	for(int i = 0; i <= number; i++)
	{
		sum = sum + i;
	}
	sum = (sum * sum);
	
	return sum;
}

/* Determines the difference between squaring the sum of n and the sum of each square of n */
/* Solution 1 */
long long sumSquareDifference(const int &number) //Runs in Big(O) of n time
{
	return (sumSquare(number) - squareEach(number));
}

/* Solution 2: Using a form of Gaussian Sum for squared numbers */
long long solution2(const int &number) //Runs in Big(O) of n time
{
	long sumSquare = 0, squareEach = 0;

	sumSquare = (number * (number + 1) / 2); //For the sum of each number n
	squareEach = ((number * (number + 1) * (2 * number + 1)) / 6); //For the square of each number summed together
	
	return ((sumSquare * sumSquare) - squareEach);
}

/* Answer should be 25164150 */
int main(int argc, char** argv)
{
	int number = 100;
	char exit = '1';

	while (exit != '0')
	{
		cout << sumSquareDifference(number) << endl;
		cout << solution2(number) << endl;
		
		cin >> exit;
	}

	return 0;
}