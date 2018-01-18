/*
roll no. = 16cs10001
question e1
file name 16cs10001e1.c
*/





#include<stdio.h>
#include<math.h>
int main()
{

  int a,b,c,y;
  float x;

  printf("enter the value of side a\n");
  scanf("%d",&a);

  printf("enter the value of side b\n");
  scanf("%d",&b);

  printf("enter the value of side c\n");
  scanf("%d",&c);

  if(a*a==b*b+c*c)
    {
      printf("yes\n");

      x=sqrt(2*b*c/1.7323);

      printf("the side of equilateral triangle is %f\n",x);

    }
 else if(b*b==a*a+c*c)
    {
      printf("yes\n");

      x=sqrt(2*a*c/1.7323);

      printf("the side of equilateral triangle is %f\n",x);

    }
  else if(c*c==a*a+b*b)
    {
      printf("yes\n");

      x=sqrt(2*a*b/1.7323);

      printf("the side of equilateral triangle is %f\n",x);

    }
      else
	{
      printf("no\n");
	}

  printf("the side length rounded up to integer is %d\n",(int)x+1);

}
      
