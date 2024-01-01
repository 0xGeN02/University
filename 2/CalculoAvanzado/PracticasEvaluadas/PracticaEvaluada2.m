% Definición de las funciones
f = @(x) exp(abs(x));
g = @(x) 1;
h = @(x) exp(-x.^2);
I = @(x) x;

% Cálculo y representación de las transformadas de Fourier
figure;

% Caso (a) - f(x) en [-1,1], con 20 puntos para x y 50 puntos para 𝜔.
subplot(6,2,1);
x = linspace(-1, 1, 20);
F = fft(f(x), 50);
w = linspace(-1, 1, length(F));
plot(w, real(F));
title('Transformada de Fourier de f en [-1,1]');

% Caso (b) - f(x) en [0,5], con 10 puntos para x y 20 puntos para 𝜔.
subplot(6,2,2);
x = linspace(0, 5, 10);
F = fft(f(x), 20);
w = linspace(-1, 1, length(F));
plot(w, real(F));
title('Transformada de Fourier de f en [0,5]');

% Caso (c) - g(x) en [-1,1], con 10 puntos para x y 100 puntos para 𝜔.
subplot(6,2,3);
x = linspace(-1, 1, 10);
G = fft(g(x), 100);
w = linspace(-1, 1, length(G));
plot(w, real(G));
title('Transformada de Fourier de g en [-1,1]');

% Caso (d) - h(x) en [0,5], con 10 puntos para x y 10 puntos para 𝜔.
subplot(6,2,4);
x = linspace(0, 5, 10);
H = fft(h(x), 10);
w = linspace(-1, 1, length(H));
plot(w, real(H));
title('Transformada de Fourier de h en [0,5]');

% Caso (e) - I(x) en [-2,2] con 2 puntos para x y 100 puntos para 𝜔.
subplot(6,2,5);
x = linspace(-2, 2, 2);
I = fft(I(x), 100);
w = linspace(-1, 1, length(I));
plot(w, real(I));
title('Transformada de Fourier de I en [-2,2] con 2 puntos para x');

% Caso (f) - I(x) en [-2,2] con 25 puntos para x y 100 puntos para 𝜔.
subplot(6,2,6);
x = linspace(-2, 2, 25);
I = fft(I(x), 100);
w = linspace(-1, 1, length(I));
plot(w, real(I));
title('Transformada de Fourier de I en [-2,2] con 25 puntos para x');

