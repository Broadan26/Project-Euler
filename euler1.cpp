#include <iostream>
#include <stdio.h>

using namespace std;

int findSumOne(int count)
{
	int sum = 0, countUp = 1;
	
	while (countUp < count)
	{
		if ((countUp % 3) == 0)
			sum = sum + countUp; //sum += countUp
		else if ((countUp % 5) == 0)
			sum = sum + countUp; //sum += countUp
		countUp++;
	}
	return sum;
}

int findSumTwo(int count)
{
	int sum = 0, multiple = 3;

	while(multiple < count)
	{
		sum = sum + multiple;
		multiple = multiple + 3; //multiple += 3
	}
	multiple = 5;
	while(multiple < count)
	{
		sum = sum + multiple;
		multiple = multiple + 5; //multiple += 5
	}
	multiple = 15;
	while(multiple < count)
	{
		sum = sum - multiple;
		multiple = multiple + 15; //multiple += 15
	}
	
	return sum;
}

int main(char argv, int** argc)
{
	char exit = '1';
	
	while (exit != '0') 
	{
		cout << "Solution 1: " << findSumOne(1000) << endl;
		cout << "Solution 2: " << findSumTwo(1000) << endl;
		cin >> exit;
	}
	return 0;
}