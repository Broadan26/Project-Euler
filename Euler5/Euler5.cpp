#include <stdio.h>
#include <iostream>

using namespace std;

/* Looks for the largest number divisible by integer values between 1-20 */
long long divisible() //Big(O) n^2
{
	long number = 0, divisible = 19;
	char check = '0', check2 = '0';
	
	while(check != '1')
	{
		number = number + 20;
		while(divisible > 10 && check2 != '1') //Check if number is divisible by 1-20
		{
			if (number % divisible != 0)
				check2 = '1';
			
			divisible = divisible - 1;
		}

		if (check2 == '1') //If the number is not divisible by 1-20
		{
			divisible = 19;
			check2 = '0';
		}
		else //If the number was divisible by 1-20
			check = '1';
	}
	
	return number;
}

/* Answer should be 232792560 */
int main(int argc, char** argv)
{
	char exit = '1';
	
	while(exit != '0')
	{
		cout << divisible() << endl;
		
		cin >> exit;
	}
	
	return 0;
}