#include <stdio.h>

int main(void) {
	int T,i,X;
	scanf("%d",&T);
	for(i=0; i<T; i++){
	    scanf("%d",&X);
	    if(X>30){
	        printf("YES\n");
	    }
	    else{
	        printf("NO\n");
	    }
	}
	return 0;
}

