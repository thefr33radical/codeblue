#include<bits/stdc++.h>

using namespace std;


class single{

    int issingle=0;
    single(){
        cout<<"single class instance created \n";
            }

public:
single getinstance()
{   if(this->issingle==0)
    {    this->issingle=1;
        return new &single();
    }
    else
        {   cout<<"only one instance allowed ";
            return this.single();
        }

}



};

int main()

{   single a=single.getinstance();
    single b=single.getinstance();

return 0;
}
