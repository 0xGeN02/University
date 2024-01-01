% Define la función f(x) a trozos
function y = f(x)
    y = zeros(size(x)); % Inicializa y con valores cero para evitar errores

    for i = 1:length(x)
        if (x(i) >= 0 && x(i) < 1)
            y(i) = 1;
        elseif (x(i) >= 1 && x(i) <= 2)
            y(i) = 2;
        else
            y(i) = 0; % Fuera del intervalo [0,2]
        end
    end
endfunction

% Valores de x para el gráfico
x = linspace(0, 2, 1000); % Ajusta el intervalo según tu necesidad

% Número de términos para la Serie de Fourier
num_terminos = [1, 5, 20, 100, 1000];

% Longitud del intervalo (L)
L = 2;

% Calcula y grafica la Serie de Fourier para diferentes números de términos
for i = 1:length(num_terminos)
    n = num_terminos(i);

    % Calcula los coeficientes de la Serie de Fourier
    a0 = 0;
    an = zeros(1, n);
    bn = zeros(1, n);

    for j = 1:n
        an(j) = (1/L) * integral(@(x) f(x) .* cos(j*pi*x/L), 0, L);
        bn(j) = (1/L) * integral(@(x) f(x) .* sin(j*pi*x/L), 0, L);
    end

    % Calcula la suma de la Serie de Fourier
    suma_fourier = a0 / 2;
    for j = 1:n
        suma_fourier = suma_fourier + an(j) * cos(j*pi*x/L) + bn(j) * sin(j*pi*x/L);
    end

    % Grafica la Serie de Fourier
    figure;
    plot(x, f(x), 'b', x, suma_fourier, 'r');
    title(['Serie de Fourier con ', num2str(n), ' términos']);
    xlabel('x');
    ylabel('y');
    legend('Función original', 'Serie de Fourier');
    grid on;
end

