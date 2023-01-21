# include <iostream>
using namespace std;
int main(){

    // INPUTS
    double base;
    double height;

    cout << "Enter the base: ";
    cin >> base;
    cout << "\nEnter the height: ";
    cin >> height;

    // PROCESS
    double area;
    area = base * height;

    // OUTPUT 
    cout <<"The area of this parallelogram = " << area;

    return 0;
}