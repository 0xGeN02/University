%Préambulo
%Vector de coste
c=[6 6];
%Matriz de coeficientes de las restricciones
A=[10 20; 30 20; 15 70];
%Vector de restricciones
b=transpose([800 1600 1800]);
%Cota inferior de las variables
lb=[0 0];
%Cota superior de las variables
ub=[];
%Tipo de restricciones
ctype="LLL";
%Tipo de variables de decisión
vartype="CC";
%Sentido de la optimización (minimización)
s=1;
%Parámetros de computación
param.msglev=3;
param.itlim=10;
%Optimización
%xmin punto donde se alcanza el valor mínimo de la función objetivo fmin
[xmin,fmin]=glpk(c,A,b,lb,ub,ctype,vartype,s,param);
disp(xmin)
disp(fmin)
