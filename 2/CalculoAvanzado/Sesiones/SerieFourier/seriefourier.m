% Función para calcular y graficar la serie de Fourier de f(x)
function fourier()
    % Definir el intervalo y el número de términos a calcular
    x = linspace(0, 2, 100);
    n_terms = 10;
    result = zeros(size(x));

    % Calcular la serie de Fourier
    for n = 1:n_terms
        term = 3+(-1/(pi*n)+(-1)^n/(n*pi))*sin(pi*x*n)
        result = result + term;
    end

    % Agregar el término constante
    result = result + 3/2;

    % Graficar la función
    plot(x, result);
    title('Serie de Fourier para f(x)');
    xlabel('x');
    ylabel('f(x)');

    % Calcular y mostrar los valores
    a_0 = 3;
    a_n_values = zeros(1, n_terms);
    b_n_values = zeros(1, n_terms);

    for n = 1:n_terms
        a_n_values(n) = sin(n*pi/2)/(n*pi);
        b_n_values(n) = (2*sin(n*pi)/(n*pi));
    end

    disp(['a_0 = ', num2str(a_0)]);
    disp(['a_n = ', num2str(a_n_values)]);
    disp(['b_n = ', num2str(b_n_values)]);
end
