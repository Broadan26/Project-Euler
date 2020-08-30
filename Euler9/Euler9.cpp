#include <iostream>

using namespace std;

/* A Pythagorean Triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2 */
/* For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2 */
/* There exists exactly one Pythagorean triplet for which a + b + c = 1000 */

/* Basic n^2 time function which iterates until it can find the correct pythagorean triplet */
int basic()
{
	const int num = 1000;
	int a = 1, b = 1, c = 998;

	for(a = 1; a < num - 501; a++) //Since a cannot be 500, n/2 time here
	{
		for(b = 1; b < num - a; b++) //b's value also determined by a
		{
			c = num - b - a; //c gets what is left
			if (((a * a) + (b * b) == (c * c))) //Check for triplet
			{
				cout << "A = " << a << endl;
				cout << "B = " << b << endl;
				cout << "C = " << c << endl;
				cout << "Product = " << (a * b * c) << endl;
				return 1;
			}
		}
	}
	return 0;
}

/* Driver Code */
/* Should produce A = 200, B = 375, C = 425 */
/* Product: 31875000*/
int main (int argc, char** argv)
{
	basic();

	return 0;
}