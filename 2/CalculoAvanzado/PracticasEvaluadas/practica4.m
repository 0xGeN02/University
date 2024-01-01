% (a) Esfera de centro 0 y radio 2
[theta, phi] = meshgrid(linspace(0, 2*pi, 40), linspace(0, pi, 40));
x = 2 * cos(theta) .* sin(phi);
y = 2 * sin(theta) .* sin(phi);
z = 2 * cos(phi);
figure;
surf(x, y, z);
title('Esfera de centro 0 y radio 2');

% (b) Cilindro vertical de altura 2 y radio 1
[theta, z] = meshgrid(linspace(0, 2*pi, 40), linspace(-1, 1, 40));
x = cos(theta);
y = sin(theta);
figure;
surf(x, y, z);
title('Cilindro vertical de altura 2 y radio 1');

% (c) Plano x=0 para y,z en [-1,1]x[-1,1]
[y, z] = meshgrid(linspace(-1, 1, 40), linspace(-1, 1, 40));
x = zeros(size(y));
figure;
surf(x, y, z);
title('Plano x=0 para y,z en [-1,1]x[-1,1]');
