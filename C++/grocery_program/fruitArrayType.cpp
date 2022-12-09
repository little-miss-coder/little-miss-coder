#include "fruit.h"
#include "arrayListType.h"
#include "fruitArrayType.h"

#include <iostream>
#include <string>
using namespace std;

void fruitArrayType::print() const
{
    cout << left<< setw(20) << "Item:"<<setw(20)<<"Name:"<<setw(20)<< "Unit Price:" <<setw(20)
            << "Quantity:"<<setw(20) << "Cost:" << endl;

    for (int i = 0; i < length; i++)
    {
        cout << left<< setw(20) << i+1 << list[i];
    }

}

void fruitArrayType::printByItem(int num) const
{
    cout << list[num-1] << endl;
}

void fruitArrayType::printByName(string name) const
{
    for (int i = 0; i < length; i++)
    {
        if (list[i].getName()== name)
            cout << list[i] << endl;
    }
}

void fruitArrayType::updateQ(int num, double quantity)
{

    list[num-1].setQuantity(quantity);
    cout << "\nNew quantity for " << num << " is " << list[num-1].getQuantity() << endl;

}

void fruitArrayType::updateP(string name, double price)
{
    bool isName = false;

    for (int i = 0; i < length; i++)
    {
        if (list[i].getName()== name)
        {
            list[i].setPrice(price);
            cout << "\nNew unit price is: " << list[i].getPrice() << endl;
            isName = true;
            break;
        }

    }

    if (isName = false)
        cout << "Item is not in list" << endl;

}

double fruitArrayType::getTotal()
{
    double grandTotal = 0;

        for (int i = 0; i < length; i ++)
        {
            grandTotal += list[i].getPrice() * list[i].getQuantity();

        }
    return grandTotal;
}
