%Vector de coste
c=[500 1000 250 450 375 75 0 0 0];
%Matriz de coeficientes de las restricciones
A=[0 0 0 0 0 0 215 110 125;
   -5 -10 -2 -4 -4 -1 20 20 20;
   -6 -12 -3 -5 -4 -3 45 35 70;
   -4 -7 -4 -6 -1 -2 30 25 30;
   -7 -15 -2 -4 -4 -1 25 10 10;];
%Vector de restricciones
b=transpose([5000 0 0 0 0]);
%Cota inferior de las variables
lb=[5 3 8 3 4 9 0 0 0];
%Cota superior de las variables
ub=[];
%Tipo de restricciones
ctype="ULLLL";
%Tipo de variables de decisión
vartype="IIIIIIIII";
%Sentido de la optimización (minimización=1, maximización=-1)
s=-1;
%Parámetros de computación
param.msglev=3;
param.itlim=10;
%Optimización
%xmax punto donde se alcanza el valor óptimo de la función objetivo
[xmax,fmax]=glpk(c,A,b,lb,ub,ctype,vartype,s,param);
disp(xmax)
disp(fmax)
