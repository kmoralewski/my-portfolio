// ---------------------------------------------------------------
// Programming Assignment:	Project Week 8
// Developer:			    Kamil Moralewski
// Date Written:			8/24/2021
// Purpose:				    Adding one additional feature
// ---------------------------------------------------------------
#include <iostream>
#include <iomanip>
#include <string>


using namespace std;



class CAR {
private:
	string carDetails;
	int carPrice;
	float totalCar, carFee, carTax;
	float feesDealer = 0.03;
	float taxSales = 0.0625;
public:
	CAR(string, int);
	string getcarDetails();
	int getcarPrice();
	float gettotalCar();
	float getcarFee();
	float getcarTax();
	float calculatetotalCar();
	void PrintCarInfo();
};

class ADDON {
private:
	string addOn;
	int addPrice;
	float feesDealer = 0.03;
	float taxSales = 0.0625;
	float totalAdd1, totalAdd2, totalAdd3, totalAdd4, totalAdd5, totalAdd;\
		float addFee, addTax;

public:
	ADDON(string add, int adp);
	void setaddonPrice(int);
	string getaddonDetails();
	int getaddonPrice();
	float gettotalPrice();
	float gettotalFee();
	float gettotalTax();
	float calculateaddonPrice();
	void PrintAddonInfo();
};