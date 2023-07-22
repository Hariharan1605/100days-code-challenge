#include<iostream>
using namespace std;
main()
{
	int i,j,n;
	cout << "Enter n : ";
	cin >> n;
	for(i=0; i<n; i++){
        for(j=0; j<2*n; j++){
            if (j<n){
                if(j<i+1){
                    cout << j+1 << " ";
                    }
                else{
                    cout<<" ";
                    }
                }
            else{
                if(j<2*n-i-1){
                    cout << "   ";
                    }
                else{
                    cout << 2*n-j<<" ";
                   }
                }
            }
            cout<<"\n";
        }
}
