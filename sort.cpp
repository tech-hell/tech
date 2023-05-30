#include <iostream>
using namespace std;
void selectionsort(int arr[],int n);
int main()
{
    int i,n;
    cout<<"Enter The Size Of Array \n";
    cin>>n;
    int arr[n];
    cout<<"Enter The Element Of Array \n";
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    selectionsort(arr,n);
    return 0;
}

void selectionsort(int arr[],int n)
{
    int i,j,k,temp,min;
    for(i=0;i<n-1;i++)
    {
        min=i;
        for(j=i+1;j<n;j++)
        {
            if(arr[j]<arr[min])
            {
                min=j;
            }
        }
        cout<<"Pass "<<i+1<<":";
        for(k=0; k<n; k++)
        {
            cout<<" ";
            cout<<arr[k];
        }
        cout<<"\n";
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
    cout<<"\nSORTED ARRAY\n\n";
    for(i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}
