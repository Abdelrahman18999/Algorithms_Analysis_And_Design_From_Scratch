# include <iostream>
using namespace std;
int main (){

    // INPUTS
    double smaller_base;
    double larger_base;
    double height;

    cout << "Enter the smaller base: ";
    cin >> smaller_base;
    cout << "\nEnter the larger base: ";
    cin >> larger_base;
    cout << "\nEnter the height: ";
    cin >> height;

    // PROCESS
    double area;
    area = ((smaller_base + larger_base) / 2) * height;

    //OUTPUT
    cout << "The area of Trapezoid = " << area << endl;

    return 0;
}