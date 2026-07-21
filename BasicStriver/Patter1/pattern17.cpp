#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=n;j>i;j--){
             cout<<" ";
            }
        for(int j=0;j<i;j++){
            cout<<char(65+j);
        }
        for(int j=0;j<i+1;j++){
            cout<<char(65+i-j);
        }
        cout<<'\n';
    }
    return 0;
}