/*
This program was a homework assignment that included:
1) A recursive function (The star pattern)
2) Selection sort. MinLocation and swap functions are for the sort.
3) Binary search. Two methods are shown, one is commented out for functionality.
*/

#include <iostream>
using namespace std;

void starFunc(int num);
void selectionSort(int list[], int length);
int minLocation(int list[], int first, int last);
void swap(int list[], int first, int second);
int binarySearch(int list[], int item, int first, int last);



int main()
{
    int number=0;

    while (number <= 0) // while loop to ask for number until user enters a positive number
    {
        cout << "Enter a positive number to create your star pattern: ";
        cin >> number;
    }

    starFunc(number); //call func after positive number is inputted

    const int SIZE = 5;
    int intList[SIZE];
    cout << "\nEnter 5 numbers for your array, in any order: ";
    for (int i=0; i<SIZE; i++)
       cin>>intList[i];

    selectionSort(intList, SIZE);

    cout << endl;
    cout << "After sorting, the list is: ";
    for (int i = 0; i < SIZE; i++)
        cout << intList[i] << " ";
    cout << endl;

    int searchItem;
    cout << "\nEnter the number you would like to search: ";
    cin >> searchItem;
    cout << endl;

    int position;
    position = binarySearch(intList, searchItem, 0, SIZE);

    if (position != -1)
        cout << searchItem <<" is found at position " << position << endl;
    else
        cout << searchItem << " is not in your array." << endl;



    return 0;
}

void starFunc(int num)
{

    if (num >0)
    {
        for (int i = 1; i <= num; i++)
            cout << "*";
        cout << endl;
        starFunc(num - 1);
        for (int i = 1; i <= num; i++) //print stars back up to num amount
            cout << "*";
        cout << endl;
    }
}

//next 3 are for selection sort
void selectionSort(int list[], int length)
{
    int minIndex;

    for (int index = 0; index < length; index++)
    {
        minIndex = minLocation(list, index, length-1);
        swap(list, index, minIndex);
    }
}

int minLocation(int list[], int first, int last)
{
    int minIndex = first;

    for (int loc = first + 1; loc <= last; loc++)
        if (list[loc] < list[minIndex])
            minIndex = loc;

    return minIndex;
}


void swap(int list[], int first, int second)
{
    int temp;

	temp = list[first];
    list[first] = list[second];
    list[second] = temp;
}


//other binary search
/*int binarySearch(const int list[],  int length, const int& item)
{
    int first = 0, mid, last = length - 1;

    bool found = false;

    while (first <= last && ! found)
    {
        mid = (first + last)/2;

	 if (list[mid] == item)
            found = true;
        else if (list[mid] > item)
            last = mid - 1;
        else
            first = mid + 1;
    }

    if (found)
        return mid;
    else
        return -1;
}*/


//recursive binary search
int binarySearch(int list[], int item, int first, int last)
{
    int mid = (first+last/2);

    if (first > last)
        return -1;
    else if (list[mid] == item)
        return mid;
    else if (item < list[mid])
        binarySearch(list, item, first, mid-1);
    else if (item > list[mid])
        binarySearch(list, item, mid+1, last);

}


/*
OUTPUT:
Enter a positive number to create your star pattern: 7
*******
******
*****
****
***
**
*
*
**
***
****
*****
******
*******

Enter 5 numbers for your array, in any order: 34 67 4 33 18

After sorting, the list is: 4 18 33 34 67

Enter the number you would like to search: 33

33 is found at position 2

Process returned 0 (0x0)   execution time : 34.711 s
Press any key to continue.

*/
