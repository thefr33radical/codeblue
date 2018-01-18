//On(n2)

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int binsearch(vector<pair<pair<int,int>,int> > jobs, int index)
{
    int low=0,high=index-1,mid;

    while(high>=low)
    {
        mid=(low+high)/2;
        if(jobs[mid].first.second<=jobs[index].first.first)
        {
            if(jobs[mid+1].first.second<=jobs[index].first.first)
                low=mid+1;
            else
                return mid;
        }
        else
            high=mid-1;
    }


    return -1;
}
void compute();
bool cmp(const pair<pair<int,int>,int>  & a, const pair<pair<int,int>,int> &b)
{
    return a.first.second<b.first.second;
}
int main()
{
    compute();
    return 0;
}

void compute()
{   int temp,n,s,e,p;
    vector<pair<pair<int,int>,int> > jobs;
    

    cout<<"\n Enter number of jobs";
    cin>>n;
    temp=n;
    cout<<"\n Enter start_time end_time profit";
    while(temp)
    {   cin>>s>>e>>p;
        jobs.push_back(make_pair(make_pair(s,e),p));

        temp--;
    }

   // for(vector<pair<pair<int,int>,int> > ::iterator it=jobs.begin();it!=jobs.end();it++)
    //   cout<<"\n"<<(*it).first.first<<(*it).first.second<<(*it).second;
    vector<pair<pair<int,int>,int> > ::iterator it;
    sort(jobs.begin(),jobs.end(),cmp);

   int res[n];
   res[0]=jobs[0].second;

   for(int i=1;i<jobs.size();i++)
   {    temp=jobs[i].second;
        int l=binsearch(jobs,i);// find the lowest conflicting elemsrnt

        if(l!=-1)
            temp=temp+res[l];
        res[i]=max(temp,res[i-1]);
   }

   cout<<"\n result:"<<res[n-1];


   }


