#include<stdio.h>
int main()
{
	int mat[30][30],m,n,i,j,left=0,right,top=0,bottom,k,num;
	printf("Enter n : ");
	scanf("%d",&n);
	right = 2*n-1;
	bottom  = 2*n-1;
	num=n;
	for(k=0; k<n; k++){
		for(i=left; i<right; i++){
			for(j=top; j<bottom; j++){
				if(j==left || j==right-1 || i==top || i==bottom-1){
					mat[i][j]=num;
				}
			}
		}
		left++;
		right--;
		top++;
		bottom--;	
		num--;
	}
	for(i=0; i<2*n-1; i++){
		for(j=0; j<2*n-1; j++){
			printf("%d ",mat[i][j]);
		}
		printf("\n");
	}
}
