// ---------------------------------------------------------------
// Programming Assignment:	Project Week 7
// Developer:			    Kamil Moralewski
// Date Written:			8/24/2021
// Purpose:				    Adding one additional feature
// ---------------------------------------------------------------
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include "CAR.h"


using namespace std;

//Defining variables with CAR type
CAR car1("2012 Ford Mustang", 13560);
CAR car2("2010 Ford Explorer", 7550);
CAR car3("2018 Ford Escape", 15280);
CAR car4("2007 Jeep Grand Cherokee", 6880);
CAR car5("2004 Jeep Liberty", 3490);
CAR car6("2014 Jeep Wrangler", 14830);
CAR car7("2019 Honda Accord", 21250);
CAR car8("2010 Honda CRV", 11290);
CAR car9("2011 Honda Pilot", 11800);
CAR car10("2008 Nissan 350z", 8200);
CAR car11("2012 Nissan Rouge", 16870);
CAR car12("2017 Nissan Sentra", 14520);
CAR car13("2020 Toytota Camry", 18670);
CAR car14("1999 Toyota Corolla", 1900);
CAR car15("2004 Toyota Highlander", 3500);

//Defining variables with ADDON type
ADDON add1("Bike Rack", 1200);
ADDON add2("Trailer Hitch", 2400);
ADDON add3("Tints", 300);
ADDON add4("Premium Wheels", 800);
ADDON add5("Detail", 310);

const string FILE_NAME = "CarSales.csv";
void PickAndWrite(void);
void ReadAndDisplay(void);


//Defining functions
void addMenu();
void carMenu();


//Function for addons menu	
void addMenu()
{
	cout << "Here is a list of addons we offer:" << endl;
	cout << "______________________________________" << endl;
	cout << "1 Bike Rack $1200" << endl;
	cout << "-----------------------" << endl;
	cout << "2 Trailer Hitch $2400" << endl;
	cout << "-----------------------" << endl;
	cout << "3 Tints $300" << endl;
	cout << "-----------------------" << endl;
	cout << "4 Premium Wheels $800" << endl;
	cout << "-----------------------" << endl;
	cout << "5 Detail $310" << endl;
	cout << "-----------------------" << endl;
	cout << "0 None or Done" << endl;
	cout << "-----------------------" << endl;

}

//Function for car menu
void carMenu()
{
	cout << "Here is our inventory at the moment:" << endl; //Listing inventory for user to see
	cout << "______________________________________" << endl;
	cout << "-1- 2012 Ford Mustang $13560" << endl;
	cout << "-------------------------------" << endl;
	cout << "-2- 2010 Ford Explorer $7550" << endl;
	cout << "-------------------------------" << endl;
	cout << "-3- 2018 Ford Escape $15280" << endl;
	cout << "-------------------------------" << endl;
	cout << "-4- 2007 Jeep Grand Cherokee $6880" << endl;
	cout << "-------------------------------" << endl;
	cout << "-5- 2004 Jeep Liberty $3490" << endl;
	cout << "-------------------------------" << endl;
	cout << "-6- 2014 Jeep Wrangler $14830" << endl;
	cout << "-------------------------------" << endl;
	cout << "-7- 2019 Honda Accord $21250" << endl;
	cout << "-------------------------------" << endl;
	cout << "-8- 2010 Honda CRV $11290" << endl;
	cout << "-------------------------------" << endl;
	cout << "-9- 2011 Honda Pilot $11800" << endl;
	cout << "-------------------------------" << endl;
	cout << "-10- 2008 Nissan 350z $8200" << endl;
	cout << "-------------------------------" << endl;
	cout << "-11- 2012 Nissan Rouge $16870" << endl;
	cout << "-------------------------------" << endl;
	cout << "-12- 2017 Nissan Sentra $14520" << endl;
	cout << "-------------------------------" << endl;
	cout << "-13- 2020 Toyota Camry $18670" << endl;
	cout << "-------------------------------" << endl;
	cout << "-14- 1999 Toyota Corolla $1900" << endl;
	cout << "-------------------------------" << endl;
	cout << "-15- 2004 Toyota Highlander $3500" << endl;
	cout << "-------------------------------" << endl;
	cout << "-0- None or Done" << endl;
	cout << "-------------------------------" << endl;
}


int main()
{
	char user3;
	bool answer;
	while (answer = true)
	{
		cout << "Welcome to Millz Autos!" << endl; //Welcome message followed by menu choices
		cout << "Please choose an option: (Enter number)" << endl;
		cout << "-1- Start transaction" << endl;
		cout << "-2- Display all sales" << endl;
		cout << "-3- Exit" << endl;
		cin >> user3;
		switch (user3) { //Switch statement for menu choices
		case '1':
			PickAndWrite(); //Call for PickAndWrite function
			continue;
		case '2':
			ReadAndDisplay(); //Call for ReadAndDisplay Function
			continue;
		case '3':
			cout << "Have a good day." << endl;
			break;
		default:
			cout << "Invalid choice--please enter 1, 2, or 3" << endl;
			continue;
		}
		break;
	}
	return 0;
}


void PickAndWrite(void)
{
	//Defining variables
	int carPrice, anscar;
	char ansadd, ansadd2, ask;
	bool answer;
	float totalSale;
	float totalCar, totalAdd, totalAdd1, totalAdd2, totalAdd3, totalAdd4, totalAdd5;
	float addFee1, addFee2, addFee3, addFee4, addFee5, addFee, totalFee, carFee;
	float addTax1, addTax2, addTax3, addTax4, addTax5, addTax, totalTax, carTax;
	float addPrice1, addPrice2, addPrice3, addPrice4, addPrice5, totalNofee;
	string user1, user2;




	//Opening output file
	ofstream FILE_NAME;
	FILE_NAME.open("CarSales.csv");

	while (answer = true)
	{
		while (answer = true)
			//While loop for looking at inventory
		{
			cout << "Would you like to look at our inventory? (y or n)" << endl;
			cin >> user1;
			if (user1 == "y" || user1 == "Y")
			{
				break;

			}
			else if (user1 == "n" || user1 == "N")
			{
				cout << "Have a good day" << endl;

			}
			else
				cout << "Invalid input" << endl;
			continue;
			break;

		}

		carMenu();

		while (answer = true)  //While loop for choosing car
		{

			cout << "Which car would you like?(Enter number to left of vehicle)" << endl;
			cin >> anscar;
			if (anscar >= 0 && anscar < 16) {
				switch (anscar) {
				case 0: cout << "Have a good day." << endl;

				case 1: car1.calculatetotalCar();
					car1.PrintCarInfo();
					totalCar = car1.gettotalCar();
					carFee = car1.getcarPrice();
					carTax = car1.getcarTax();
					carPrice = car1.getcarPrice();
					break;
				case 2: car2.calculatetotalCar();
					car2.PrintCarInfo();
					totalCar = car2.gettotalCar();
					carFee = car2.getcarPrice();
					carTax = car2.getcarTax();
					carPrice = car2.getcarPrice();
					break;
				case 3: car3.calculatetotalCar();
					car3.PrintCarInfo();
					totalCar = car3.gettotalCar();
					carFee = car3.getcarPrice();
					carTax = car3.getcarTax();
					carPrice = car3.getcarPrice();
					break;
				case 4: car4.calculatetotalCar();
					car4.PrintCarInfo();
					totalCar = car4.gettotalCar();
					carFee = car4.getcarPrice();
					carTax = car4.getcarTax();
					carPrice = car4.getcarPrice();
					break;
				case 5: car5.calculatetotalCar();
					car5.PrintCarInfo();
					totalCar = car5.gettotalCar();
					carFee = car5.getcarPrice();
					carTax = car5.getcarTax();
					carPrice = car5.getcarPrice();
					break;
				case 6: car6.calculatetotalCar();
					car6.PrintCarInfo();
					totalCar = car6.gettotalCar();
					carFee = car6.getcarPrice();
					carTax = car6.getcarTax();
					carPrice = car6.getcarPrice();
					break;
				case 7: car7.calculatetotalCar();
					car7.PrintCarInfo();
					carFee = car7.getcarPrice();
					carTax = car7.getcarTax();
					totalCar = car7.gettotalCar();
					carPrice = car7.getcarPrice();
					break;
				case 8: car8.calculatetotalCar();
					car8.PrintCarInfo();
					totalCar = car8.gettotalCar();
					carFee = car8.getcarPrice();
					carTax = car8.getcarTax();
					break;
				case 9: car9.calculatetotalCar();
					car9.PrintCarInfo();
					totalCar = car9.gettotalCar();
					carFee = car9.getcarPrice();
					carTax = car9.getcarTax();
					carPrice = car9.getcarPrice();
					break;
				case 10: car10.calculatetotalCar();
					car10.PrintCarInfo();
					totalCar = car10.gettotalCar();
					carFee = car10.getcarPrice();
					carTax = car10.getcarTax();
					carPrice = car10.getcarPrice();
					break;
				case 11: car11.calculatetotalCar();
					car11.PrintCarInfo();
					totalCar = car11.gettotalCar();
					carFee = car11.getcarPrice();
					carTax = car11.getcarTax();
					carPrice = car11.getcarPrice();
					break;
				case 12: car12.calculatetotalCar();
					car12.PrintCarInfo();
					totalCar = car12.gettotalCar();
					carFee = car12.getcarPrice();
					carTax = car12.getcarTax();
					carPrice = car12.getcarPrice();
					break;
				case 13: car13.calculatetotalCar();
					car13.PrintCarInfo();
					totalCar = car13.gettotalCar();
					carFee = car13.getcarPrice();
					carTax = car13.getcarTax();
					carPrice = car13.getcarPrice();
					break;
				case 14: car14.calculatetotalCar();
					car14.PrintCarInfo();
					totalCar = car14.gettotalCar();
					carFee = car14.getcarPrice();
					carTax = car14.getcarTax();
					carPrice = car14.getcarPrice();
					break;
				case 15: car15.calculatetotalCar();
					car15.PrintCarInfo();
					totalCar = car15.gettotalCar();
					carFee = car15.getcarPrice();
					carTax = car15.getcarTax();
					carPrice = car15.getcarPrice();
					break;
				default: cout << "Invalid input." << endl;
					continue;
				}
				break;
			}
			else
				cout << "Wrong input." << endl;
			continue;
			break;
		}

		while (answer = true)
		{
			//While loop to look at addons
			cout << "Would you like to look at our addons? (y or n)" << endl;
			cin >> user2;
			if (user2 == "Y" || user2 == "y")
			{
				//While loops for choosing addons
				while (answer = true)
					//While loop for first addon
				{
					addMenu();
					cout << "Which addon would you like? (Enter number to left of addon or 0 for none)" << endl;
					cin >> ansadd;
					if (ansadd >= '0' && ansadd < '6') {
						switch (ansadd) {
						case '0': cout << "Lets continue." << endl;
							totalAdd1 = 0; addFee1 = 0; addTax1 = 0; addPrice1 = 0;
							totalAdd2 = 0; addFee2 = 0; addTax2 = 0; addPrice2 = 0;
							totalAdd3 = 0; addFee3 = 0; addTax3 = 0; addPrice3 = 0;
							totalAdd4 = 0; addFee4 = 0; addTax4 = 0; addPrice4 = 0;
							totalAdd5 = 0; addFee5 = 0; addTax5 = 0; addPrice5 = 0;
							break;
						case '1': add1.calculateaddonPrice();
							add1.PrintAddonInfo();
							totalAdd1 = add1.gettotalPrice();
							addFee1 = add1.gettotalFee();
							addTax1 = add1.gettotalTax();
							addPrice1 = add1.getaddonPrice();
							break;
						case '2': add2.calculateaddonPrice();
							add2.PrintAddonInfo();
							totalAdd1 = add2.gettotalPrice();
							addFee1 = add2.gettotalFee();
							addTax1 = add2.gettotalTax();
							addPrice1 = add2.getaddonPrice();
							break;
						case '3': add3.calculateaddonPrice();
							add3.PrintAddonInfo();
							totalAdd1 = add3.gettotalPrice();
							addFee1 = add3.gettotalFee();
							addTax1 = add3.gettotalTax();
							addPrice1 = add3.getaddonPrice();
							break;
						case '4': add4.calculateaddonPrice();
							add4.PrintAddonInfo();
							totalAdd1 = add4.gettotalPrice();
							addFee1 = add4.gettotalFee();
							addTax1 = add4.gettotalTax();
							addPrice1 = add4.getaddonPrice();
							break;
						case '5': add5.calculateaddonPrice();
							add5.PrintAddonInfo();
							totalAdd1 = add5.gettotalPrice();
							addFee1 = add5.gettotalFee();
							addTax1 = add5.gettotalTax();
							addPrice1 = add5.getaddonPrice();
							break;
						default: cout << "Wrong" << endl;
						}
						break;
					}
					else
						cout << "Wrong input. Try again." << endl;
					continue;

				}
				while (answer = true)
					//While loop for second addon
				{
					cout << "Would you like any other addon? (Choose one by entering number to left of addon or 0 for done)" << endl;
					cin >> ansadd;
					if (ansadd >= '0' && ansadd < '6') {
						switch (ansadd) {
						case '0': cout << "Lets continue." << endl;
							totalAdd2 = 0; addFee2 = 0; addTax2 = 0; addPrice2 = 0;
							totalAdd3 = 0; addFee3 = 0; addTax3 = 0; addPrice3 = 0;
							totalAdd4 = 0; addFee4 = 0; addTax4 = 0; addPrice4 = 0;
							totalAdd5 = 0; addFee5 = 0; addTax5 = 0; addPrice5 = 0;
							break;
						case '1': add1.calculateaddonPrice();
							add1.PrintAddonInfo();
							totalAdd2 = add1.gettotalPrice();
							addFee2 = add1.gettotalFee();
							addTax2 = add1.gettotalTax();
							addPrice2 = add1.getaddonPrice();
							break;
						case '2': add2.calculateaddonPrice();
							add2.PrintAddonInfo();
							totalAdd2 = add2.gettotalPrice();
							addFee2 = add2.gettotalFee();
							addTax2 = add2.gettotalTax();
							addPrice2 = add2.getaddonPrice();
							break;
						case '3': add3.calculateaddonPrice();
							add3.PrintAddonInfo();
							totalAdd2 = add3.gettotalPrice();
							addFee2 = add3.gettotalFee();
							addTax2 = add3.gettotalTax();
							addPrice2 = add3.getaddonPrice();
							break;
						case '4': add4.calculateaddonPrice();
							add4.PrintAddonInfo();
							totalAdd2 = add4.gettotalPrice();
							addFee2 = add4.gettotalFee();
							addTax2 = add4.gettotalTax();
							addPrice2 = add4.getaddonPrice();
							break;
						case '5': add5.calculateaddonPrice();
							add5.PrintAddonInfo();
							totalAdd2 = add5.gettotalPrice();
							addFee2 = add5.gettotalFee();
							addTax2 = add5.gettotalTax();
							addPrice2 = add5.getaddonPrice();
							break;
						default: cout << "Wrong" << endl;
						}
						break;
					}
					else
						cout << "Wrong input. Try again." << endl;
					continue;

				}
				while (answer = true)
					//While loop for third addon
				{
					cout << "Would you like any other addon? (Choose one by entering number to left of addon or 0 for done)" << endl;
					cin >> ansadd;
					if (ansadd >= '0' && ansadd < '6') {
						switch (ansadd) {
						case '0': cout << "Lets continue." << endl;
							totalAdd3 = 0; addFee3 = 0; addTax3 = 0; addPrice3 = 0;
							totalAdd4 = 0; addFee4 = 0; addTax4 = 0; addPrice4 = 0;
							totalAdd5 = 0; addFee5 = 0; addTax5 = 0; addPrice5 = 0;
							break;
						case '1': add1.calculateaddonPrice();
							add1.PrintAddonInfo();
							totalAdd3 = add1.gettotalPrice();
							addFee3 = add1.gettotalFee();
							addTax3 = add1.gettotalTax();
							addPrice3 = add1.getaddonPrice();
							break;
						case '2': add2.calculateaddonPrice();
							add2.PrintAddonInfo();
							totalAdd3 = add2.gettotalPrice();
							addFee3 = add2.gettotalFee();
							addTax3 = add2.gettotalTax();
							addPrice3 = add2.getaddonPrice();
							break;
						case '3': add3.calculateaddonPrice();
							add3.PrintAddonInfo();
							totalAdd3 = add3.gettotalPrice();
							addFee3 = add3.gettotalFee();
							addTax3 = add3.gettotalTax();
							addPrice3 = add3.getaddonPrice();
							break;
						case '4': add4.calculateaddonPrice();
							add4.PrintAddonInfo();
							totalAdd3 = add4.gettotalPrice();
							addFee3 = add4.gettotalFee();
							addTax3 = add4.gettotalTax();
							addPrice3 = add4.getaddonPrice();
							break;
						case '5': add5.calculateaddonPrice();
							add5.PrintAddonInfo();
							totalAdd3 = add5.gettotalPrice();
							addFee3 = add5.gettotalFee();
							addTax3 = add5.gettotalTax();
							addPrice3 = add5.getaddonPrice();
							break;
						default: cout << "Wrong" << endl;
						}
						break;
					}
					else
						cout << "Wrong input. Try again." << endl;
					continue;

				}
				while (answer = true)
					//While loop for fourth addon
				{
					cout << "Would you like any other addon? (Choose one by entering number to left of addon or 0 for done)" << endl;
					cin >> ansadd;
					if (ansadd >= '0' && ansadd < '6') {
						switch (ansadd) {
						case '0': cout << "Lets continue." << endl;
							totalAdd4 = 0; addFee4 = 0; addTax4 = 0; addPrice4 = 0;
							totalAdd5 = 0; addFee5 = 0; addTax5 = 0; addPrice5 = 0;
							break;
						case '1': add1.calculateaddonPrice();
							add1.PrintAddonInfo();
							totalAdd4 = add1.gettotalPrice();
							addFee4 = add1.gettotalFee();
							addTax4 = add1.gettotalTax();
							addPrice4 = add1.getaddonPrice();
							break;
						case '2': add2.calculateaddonPrice();
							add2.PrintAddonInfo();
							totalAdd4 = add2.gettotalPrice();
							addFee4 = add2.gettotalFee();
							addTax4 = add2.gettotalTax();
							addPrice4 = add2.getaddonPrice();
							break;
						case '3': add3.calculateaddonPrice();
							add3.PrintAddonInfo();
							totalAdd4 = add3.gettotalPrice();
							addFee4 = add3.gettotalFee();
							addTax4 = add3.gettotalTax();
							addPrice4 = add3.getaddonPrice();
							break;
						case '4': add4.calculateaddonPrice();
							add4.PrintAddonInfo();
							totalAdd4 = add4.gettotalPrice();
							addFee4 = add4.gettotalFee();
							addTax4 = add4.gettotalTax();
							addPrice4 = add4.getaddonPrice();
							break;
						case '5': add5.calculateaddonPrice();
							add5.PrintAddonInfo();
							totalAdd4 = add5.gettotalPrice();
							addFee4 = add5.gettotalFee();
							addTax4 = add5.gettotalTax();
							addPrice4 = add5.getaddonPrice();
							break;
						default: cout << "Wrong" << endl;
						}
						break;
					}
					else
						cout << "Wrong input. Try again." << endl;
					continue;

				}
				while (answer = true)
					//While loop for fifth addon
				{
					cout << "Would you like any other addon? (Choose one by entering number to left of addon or 0 for done)" << endl;
					cin >> ansadd;
					if (ansadd >= '0' && ansadd < '6') {
						switch (ansadd) {
						case '0': cout << "Lets continue." << endl;
							totalAdd5 = 0; addFee5 = 0; addTax5 = 0; addPrice5 = 0;
							break;
						case '1': add1.calculateaddonPrice();
							add1.PrintAddonInfo();
							totalAdd5 = add1.gettotalPrice();
							addFee5 = add1.gettotalFee();
							addTax5 = add1.gettotalTax();
							addPrice5 = add1.getaddonPrice();
							break;
						case '2': add2.calculateaddonPrice();
							add2.PrintAddonInfo();
							totalAdd5 = add2.gettotalPrice();
							addFee5 = add2.gettotalFee();
							addTax5 = add2.gettotalTax();
							addPrice5 = add2.getaddonPrice();
							break;
						case '3': add3.calculateaddonPrice();
							add3.PrintAddonInfo();
							totalAdd5 = add3.gettotalPrice();
							addFee5 = add3.gettotalFee();
							addTax5 = add3.gettotalTax();
							addPrice5 = add3.getaddonPrice();
							break;
						case '4': add4.calculateaddonPrice();
							add4.PrintAddonInfo();
							totalAdd5 = add4.gettotalPrice();
							addFee5 = add4.gettotalFee();
							addTax5 = add4.gettotalTax();
							addPrice5 = add4.getaddonPrice();
						case '5': add5.calculateaddonPrice();
							add5.PrintAddonInfo();
							totalAdd5 = add5.gettotalPrice();
							addFee5 = add5.gettotalFee();
							addTax5 = add5.gettotalTax();
							addPrice5 = add5.getaddonPrice();
							break;
						default: cout << "Wrong" << endl;
						}
						break;
					}
					else
						cout << "Wrong input. Try again." << endl;
					continue;
					break;

				}
				break;

			}
			else if (user2 == "N" || user2 == "n")
			{
				break;
			}
			else
				cout << "Invalid input.";
			continue;
			break;
		}



		totalSale = totalCar + totalAdd1 + totalAdd2 + totalAdd3 + totalAdd4 + totalAdd5; //Calculation for totalSale
		addFee = addFee1 + addFee2 + addFee3 + addFee4 + addFee5;
		addTax = addTax1 + addTax2 + addTax3 + addTax4 + addTax5;
		totalFee = carFee + addFee;
		totalTax = carTax + addTax;
		totalNofee = carPrice + addPrice1 + addPrice2 + addPrice3 + addPrice4 + addPrice5;



		cout << fixed << setprecision(2) << "Your total cost before fees is $" << totalNofee << endl; //Total sale cost message with precision set at 2
		cout << fixed << setprecision(2) << "Your total dealer fees are $" << totalFee << endl; //Total Dealer Fee message with precision set at 2
		cout << fixed << setprecision(2) << "Your total sales tax is $" << totalTax << endl; //Total Sales Tax message with precision set at 2
		cout << fixed << setprecision(2) << "Your total cost is $" << totalSale << endl; //Total sale cost message with precision set at 2
		cout << "Would you like another car? (y or n)";

		//Writing to output file
		FILE_NAME << totalNofee;
		FILE_NAME << ", " << totalFee;
		FILE_NAME << ", " << totalTax;
		FILE_NAME << ", " << totalSale << endl;

		cin >> ask;
		if (ask == 'Y' || ask == 'y')
		{
			continue;
		}
		else if (ask == 'N' || ask == 'n')
		{
			break;
		}
		else
			break;


		break;
	}
	//Close output file
	FILE_NAME.close();

}
void ReadAndDisplay(void)
{
	//Defining variables
	string totalSale, totalFee, totalTax, totalNofee;
	//Opening input file
	ifstream input(FILE_NAME);
	//Getting values from file
	if (input.is_open()) {

		while (getline(input, totalNofee, ',')) {
			getline(input, totalFee, ',');
			getline(input, totalTax, ',');
			getline(input, totalSale, '\n');

			//Output from file
			cout << "--Sale--" << endl;
			cout << fixed << setprecision(2) << "Your total cost before fees is $" << totalNofee << endl; //Total sale cost message with precision set at 2
			cout << fixed << setprecision(2) << "Your total dealer fees were $" << totalFee << endl;
			cout << fixed << setprecision(2) << "Your total sales tax was $" << totalTax << endl;
			cout << fixed << setprecision(2) << "Your total cost was $" << totalSale << endl; //Total sale cost message with precision set at 2
		}
		//Close input file
		input.close();




	}
}
