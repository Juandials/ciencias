#include <iostream>
using namespace std;
int main() {
  int cases=1;
  string cad = "";
  while(cin>>cad){
    cout<<"Case "<<cases++<<":"<<endl;
    int n;
    cin>>n;
    for(int q=0;q<n;q++){
      int i,j;
      cin>>i>>j;
      int aux = i;
      i=min(i,j);
      j=max(aux,j);
      char a=cad[i];
      bool Same=true;
      for(int pos=i+1;pos<=j;pos++){
        if(a!=cad[pos]){
          Same=false;
          break;
        }
      }
      if(Same){
        cout<<"Yes"<<endl;
      }else{
        cout<<"No"<<endl;
      }
    }
  }
}
