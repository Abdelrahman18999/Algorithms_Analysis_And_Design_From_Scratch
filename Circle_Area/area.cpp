# include <iostream>
# include <cmath>
using namespace std;

int main(){

    double radius;
    double area;

    // INPUTS
    cout << "Enter the radius of the circle: ";
    cin >> radius;

    // PROCESS
    area = M_PI * (radius * radius);

    // OUTPUT
    cout << "Area = " << area;

    return 0;
}