/*
This program uses array-base lists to allow user to select items, input quantity, make changes
to quantity or unit price, and displays as a receipt.
*/

#include <iostream>
#include "fruit.h"
#include "arrayListType.h"
#include "fruitArrayType.h"
#include <string>
#include <iomanip>

using namespace std;

//prototypes
void displayHeader();
void menuSelection();
int userChoice();
double userQ();
void showSelection();

const int mSize = 5;
const int maxAmt = 100;
string menuName[mSize] = {"Apple","Banana", "Grapes", "Orange", "Pear"};
double menuPrice[mSize] = {0.99, 1.49, 1.29, 2.29, 1.99};


int main()
{
    int choice;
    double q;
    char changeQ;
    char changeP;


    fruitArrayType shoppingList;


    displayHeader();
    do {
        menuSelection();
        showSelection();
        choice = userChoice();

        //if user enters invalid number
        while (choice > mSize || choice < 0)
        {
            cout << "Error. Enter a valid choice (0--5): ";
            choice = userChoice();
        }
        if (choice != 0)
        {
            fruitType newItem;
            newItem.setName(menuName[choice-1]);
            newItem.setPrice(menuPrice[choice-1]);
            newItem.setQuantity(userQ());
            shoppingList.insertEnd(newItem);
        }
        else
        {
            cout << "\nThanks for shopping with us! See receipt below" << endl << endl;
            shoppingList.print();
            cout << "\nTotal is $" << shoppingList.getTotal() << endl;
            break;
        }



    }while (choice != 0);//end do

    cout << "\nWould you like to change the Unit Price for an item? Y/N";
    cin >> changeP;
        if (changeP == 'Y' || 'y')
        {
            string name;
            double newP;
            cout << "Enter the name of the fruit: ";
            cin >> name;
            cout << "Enter the new unit price: ";
            cin >> newP;
            shoppingList.updateP(name, newP);
        }
    cout << "\nWould you like to change the quantity of any item? Y/N: ";
    cin >> changeQ;
        if (changeQ == 'Y')
        {
            cout << "Select the item number you wish to update: ";
            cin >> choice;
            cout << "\nEnter new quantity: ";
            cin >> q;
            shoppingList.updateQ(choice, q);
        }
        else if (changeQ == 'N')
            cout << "Have a good day";
        else
            cout << "Invalid option, try again";


    cout << "\nFinal list: " << endl;
    shoppingList.print();
    cout << endl;
    cout << "Total is $" << shoppingList.getTotal() << endl;

    return 0;
}//end main


void displayHeader()
{
    cout << "Welcome to the Fresh Fruit Store" << endl;
    cout << "*****************************************"<< endl;
}

int userChoice()
{
    int choice;
    cin >> choice;
    return choice;
}

double userQ()
{
    double q;
    cout << "Enter the Quantity: ";
    cin >> q;
    return q;
}

void menuSelection()
{
    cout << "\nPlease enter your selection (0--5): " << endl;
    cout << "0 -- Exit" << endl;
}



void showSelection()
{
    for (int i = 0; i < mSize; i++)
        {

            cout<<i+1 << " -- "<< setw(20) << left << menuName[i]<< "$" << menuPrice[i] << "/lb" << endl;
        }
}


/*
OUTPUT:

Welcome to the Fresh Fruit Store
*****************************************

Please enter your selection (0--5):
0 -- Exit
1 -- Apple               $0.99/lb
2 -- Banana              $1.49/lb
3 -- Grapes              $1.29/lb
4 -- Orange              $2.29/lb
5 -- Pear                $1.99/lb
1
Enter the Quantity: 4

Please enter your selection (0--5):
0 -- Exit
1 -- Apple               $0.99/lb
2 -- Banana              $1.49/lb
3 -- Grapes              $1.29/lb
4 -- Orange              $2.29/lb
5 -- Pear                $1.99/lb
7
Error. Enter a valid choice (0--5): 5
Enter the Quantity: 3

Please enter your selection (0--5):
0 -- Exit
1 -- Apple               $0.99/lb
2 -- Banana              $1.49/lb
3 -- Grapes              $1.29/lb
4 -- Orange              $2.29/lb
5 -- Pear                $1.99/lb
0

Thanks for shopping with us! See receipt below

Item:               Name:               Unit Price:         Quantity:           Cost:
1                   Apple               $0.99/lb                 4 lb                 $3.96
2                   Pear                $1.99/lb                 3 lb                 $5.97

Total is $9.93

Would you like to change the Unit Price for an item? Y/N Y
Enter the name of the fruit: Apple
Enter the new unit price: 1.29

New unit price is: 1.29

Would you like to change the quantity of any item? Y/N: Y
Select the item number you wish to update: 2

Enter new quantity: 6

New quantity for 2 is 6

Final list:
Item:               Name:               Unit Price:         Quantity:           Cost:
1                   Apple               $1.29/lb                 4 lb                 $5.16
2                   Pear                $1.99/lb                 6 lb                 $11.94

Total is $17.10

Process returned 0 (0x0)   execution time : 29.316 s
Press any key to continue.


*/

