#include <iostream>
#include <stdio.h>

using namespace std;

int solutionOne(const int &total)
{
	int sum = 0;
	int	number; //n
	int nm1 = 0; //n-2
	int nm2 = 1; //n-1
	
	while(nm2 <= total)
	{
		number = nm1 + nm2; 
		if((number % 2) == 0)
			sum = sum + number;
		nm1 = nm2; 
		nm2 = number; 
	}
	
	return sum;
}

int solutionTwo(const int &total)
{
	int sum = 0;
	int number; //n
	int nm1 = 0; //n-3
	int nm2 = 2; //n-6

	while(nm2 <= total)
	{
		number = nm1 + nm2;
		nm1 = nm2;
		nm2 = number;
	}

	return sum;
}

int main(char argv, int** argc)
{
	int total = 4000000;
	char exit = '1';
	
	while (exit != '0')
	{
		cout << "Solution 1: " << solutionOne(total) << endl;
		cout << "Solution 2: " << solutionOne(total) << endl;
		cin >> exit;
	}

	return 0;
}