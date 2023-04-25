#include <stdio.h>

int main(){
    char v1;
    unsigned char  v2;
    short 	v3;
    unsigned short v4;
    int 	v5;
    unsigned int	v6;
    long	v7;
    unsigned long v8;
    float 	v9;
    double	v10;
    long double 	v11;
    long long 	v12;
    printf("\t\tTIPO DE DATO\t\tTama%co (bytes)\n",164);
    printf("\tchar          : %d\n",sizeof(v1));
    printf("\tunsigned char : %d\n",sizeof(v2));
    printf("\tshort         : %d\n",sizeof(v3));
    printf("\tunsigned short: %d\n",sizeof(v4));
    printf("\tint           : %d\n",sizeof(v5));
    printf("\tunsigned int  : %d\n",sizeof(v6));
    printf("\tlong          : %d\n",sizeof(v7));
    printf("\tunsigned long : %d\n",sizeof(v8));
    printf("\tfloat         : %d\n",sizeof(v9));
    printf("\tdouble        : %d\n",sizeof(v10));
    printf("\tlong double   : %d\n",sizeof(v11));
    printf("\tlong long     : %d\n",sizeof(v12));
    return 0;
}