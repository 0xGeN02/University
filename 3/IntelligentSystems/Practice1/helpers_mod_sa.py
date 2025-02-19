from inspect import getsource
from IPython.display import HTML
from IPython.display import display
import math

def psource(*functions):
    """Print the source code for the given function(s)."""
    source_code = '\n\n'.join(getsource(fn) for fn in functions)
    try:
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import PythonLexer
        from pygments import highlight

        display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))

    except ImportError:
        print(source_code)
        
class Localizaciones ():

    def __init__ (self, filename='./data/grafo8cidades.txt'):
        self.filename = filename
        file = open(filename, 'r')
        Lines = file.readlines()

        count = -1
        self.nciudades = 0 
        self.tablaciudades = dict()
        for line in Lines:
            if count == -1:
                self.nciudades = int(line.strip().split()[0])        
            else:
                tokens = line.strip().split()
                self.tablaciudades[count]=tuple((float(tokens[0]),float(tokens[1])))                

            count+=1
    
        self.matriz = []
        for c1 in range(self.nciudades):
            a = [0]*self.nciudades
            self.matriz.append(a)
            for c2 in range(self.nciudades):
                self.matriz[c1][c2] = self.__distancia_semiverseno__(c1, c2)
    
    def __distancia_semiverseno__ (self, c1, c2):
        radioTierra = 6371
        lat1 = math.radians(self.tablaciudades[c1][0]);
        lon1 = math.radians(self.tablaciudades[c1][1]);
        lat2 = math.radians(self.tablaciudades[c2][0]);
        lon2 = math.radians(self.tablaciudades[c2][1]);
        
        sinChi = math.sin((lat2 - lat1) / 2);
        sinLambda = math.sin((lon2 - lon1) / 2);

        raiz = (sinChi * sinChi) + math.cos(lat1) * math.cos(lat2) * (sinLambda * sinLambda);

        return 2 * radioTierra * math.asin(math.sqrt(raiz));
    
    def distancia (self, c1, c2):        
        return self.matriz [c1][c2]
    