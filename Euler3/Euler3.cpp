#include <iostream>
#include <stdio.h>

using namespace std;

long solutionOne(const long long &number)
{
	long long factorCheck = number, count = 2, largestFactor = 0;

	while((count * count) <= factorCheck) // The square root of the initial number is the loop ceiling
	{
		if ((factorCheck % count) == 0) //Check for a prime factor
		{
			factorCheck = factorCheck / count; //Break off smaller factors
			largestFactor = count; 
		}
		else
			count++;
	}
	if (factorCheck > largestFactor) //Determine which remaining prime factor is larger
		largestFactor = factorCheck;
	
	return largestFactor;
}

int main(char argv, int** argc)
{
	long long number = 600851475143;
	long long prime = 0;
	char exit = '1';
	
	while(exit != '0')
	{
		prime = solutionOne(number);
		cout << "Solution 1: " << prime << endl;
		cin >> exit;
	}
	
	return 0;
}