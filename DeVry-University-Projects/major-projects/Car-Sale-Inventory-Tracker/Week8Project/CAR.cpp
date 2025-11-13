// ---------------------------------------------------------------
// Programming Assignment:	Project Week 8
// Developer:			    Kamil Moralewski
// Date Written:			8/24/2021
// Purpose:				    Adding one additional feature
// ---------------------------------------------------------------
#include <iostream>
#include <iomanip>
#include <string>
#include "CAR.h"


using namespace std;



CAR::CAR(string det, int pe)
{
	carDetails = det;
	carPrice = pe;
}
string CAR::getcarDetails()
{
	return carDetails;
}
int CAR::getcarPrice()
{
	return carPrice;
}
float CAR::gettotalCar() {
	return totalCar;
}
float CAR::getcarFee() {
	return carFee;
}
float CAR::getcarTax() {
	return carTax;
}
float CAR::calculatetotalCar() {
	carFee = carPrice * (3.0 / 100.0);
	carTax = carPrice * (1.0 / 16.0);
	totalCar = carFee + carTax + carPrice;
	return totalCar, carFee, carTax, carPrice;

}
void CAR::PrintCarInfo()
{
	cout << "You chose: " << carDetails << endl;
	cout << fixed << setprecision(2) << "Price: $" << totalCar << endl;
	cout << fixed << setprecision(2) << "Fee: $" << carFee << endl;
	cout << fixed << setprecision(2) << "Tax: $" << carTax << endl;
}

ADDON::ADDON(string add, int adp)
{
	addOn = add;
	addPrice = adp;
}
void ADDON::setaddonPrice(int adp) {
	addPrice = adp;
}
string ADDON::getaddonDetails()
{
	return addOn;
}
int ADDON::getaddonPrice()
{
	return addPrice;
}
float ADDON::gettotalPrice() {
	return totalAdd;
}
float ADDON::gettotalFee() {
	return addFee;
}
float ADDON::gettotalTax() {
	return addTax;
}
float ADDON::calculateaddonPrice() {
	addFee = addPrice * (3.0 / 100.0);
	addTax = addPrice * (1.0 / 16.0);
	totalAdd = addFee + addTax + addPrice;
	return totalAdd, addFee, addTax, addPrice;
}
void ADDON::PrintAddonInfo()
{
	cout << "Your addon choice is: " << addOn << endl;
	cout << fixed << setprecision(2) << "Price: $" << totalAdd << endl;
	cout << fixed << setprecision(2) << "Fee: $" << addFee << endl;
	cout << fixed << setprecision(2) << "Tax: $" << addTax << endl;
}