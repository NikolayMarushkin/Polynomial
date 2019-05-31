class Polynomial:

    def __init__(self, coeffs):
        if not isinstance(coeffs, list):
            raise TypeError("Coeffs not list or constant")
        for i in coeffs:
            if type(i) is not int and type(i) is not float:
                raise TypeError("Coeffs not int or float")

        self.coeffs = coeffs[:]
        if len(coeffs) != 0:
            while self.coeffs[0] == 0 and len(self.coeffs) > 1:
                del self.coeffs[0]
        else:
            self.coeffs.append(0)

    def __add__(self, poly_coef):
        if isinstance(poly_coef, Polynomial):
            result = []
            self_len = len(self.coeffs)
            poly_coef_len = len(poly_coef.coeffs)

            if self_len > poly_coef_len:
                result = self.coeffs[:]
                for i in range(0, len(poly_coef.coeffs)):
                    result[self_len - poly_coef_len + i] += poly_coef.coeffs[i]
            else:
               result = poly_coef.coeffs[:]
               for i in range(0, len(self.coeffs)):
                   result[-(self_len - poly_coef_len) + i] += self.coeffs[i]                   
        else:
            if self.coeffs:
                result = self.coeffs[:]
                result[-1] += poly_coef
            else:
                result = poly_coef
        return Polynomial(result)

    def __radd__(self, poly_coef):
        return self + poly_coef  

    def __negative__(self):
        return Polynomial([ -n_coef for n_coef in self.coeffs])
    
    def __sub__(self, poly_coef):
        if not isinstance(poly_coef, (Polynomial, int, float)):
            raise TypeError("Error type")
        if isinstance(poly_coef, (int, float)):
            return self.__add__(-poly_coef)
        elif isinstance(poly_coef, Polynomial):
            return self.__add__(poly_coef.__negative__())
  
    def __rsub__(self, poly_coef):
        if not isinstance(poly_coef, (Polynomial, int, float)):
            raise TypeError("Error type")   
        
        temp = []
        if type(poly_coef) is type(self):
            temp = poly_coef.coeffs
        else:
            temp.append(poly_coef)

        self_len = len(self.coeffs)
        poly_coef_len = len(temp)

        result = []
        
        ext = [0] * (self_len - poly_coef_len)
        ext.extend(temp)
        for i in range(self_len):
            result.append(ext[i] - self.coeffs[i])

        while result[0] == 0 and len(result) > 1:
            result.pop(0)
                
        return Polynomial(result)
               
    def __mul__(self, poly_coef):
        if isinstance(poly_coef, Polynomial):
            result = [0] * (len(self.coeffs) + len(poly_coef.coeffs) - 1)
            for i, j in enumerate(self.coeffs):
                for k, l in enumerate(poly_coef.coeffs):
                    result[i + k] += j * l
        elif isinstance(poly_coef, int) or isinstance(poly_coef, float):
            result = [i * poly_coef for i in self.coeffs]
        else:
            raise TypeError("Coeffs not int or float")
        return Polynomial(result)

    def __rmul__(self, poly_coef):
        return self * poly_coef

    def __eq__(self, poly_coef):
        if isinstance(poly_coef, Polynomial):
            return poly_coef.coeffs == self.coeffs
        elif isinstance(poly_coef, int) or isinstance(poly_coef, float):
            return len(self.coeffs) == 1 and self.coeffs[0] == poly_coef
        else:
            raise TypeError("Not equal")

    def __ne__(self, poly_coef):
        if not isinstance(poly_coef, (Polynomial, int, float)):
            raise TypeError("Error type")
        if isinstance(poly_coef, (int, float)):
            if len(self.coeffs) > 1:
                return True
            else:
                return poly_coef != self.coeffs[0]
        elif isinstance(poly_coef, Polynomial):
            return self.coeffs != poly_coef.coeffs

    def __str__(self):
        str_poly = ""
        lenght = len(self.coeffs)
        if lenght == 1 and self.coeffs[0] == 0:
            return str(0)
        for i in self.coeffs:
            lenght = lenght - 1

            if (i == 1 or i == -1) and lenght != 0:
                if lenght == len(self.coeffs) - 1 and i > 0:
                    str_poly = str_poly + "x^" + str(lenght)
                elif lenght == len(self.coeffs) - 1 and i < 0 or (lenght != 1 and i < 0):
                    str_poly = str_poly + "-" + "x^" + str(lenght)
                elif lenght != len(self.coeffs) - 1 and lenght != 1 and i > 0:
                    str_poly = str_poly + "+" + "x^" + str(lenght)

            if i != 1 and i != -1 and lenght != 0:
                if lenght == len(self.coeffs) - 1 or (lenght != 1 and i < 0):
                    str_poly = str_poly + str(i) + "x^" + str(lenght)
                elif lenght != len(self.coeffs) - 1 and lenght != 1 and i > 0:
                    str_poly = str_poly + "+"+str(i) + "x^" + str(lenght)

            if lenght == 1 and i > 0:
                str_poly = str_poly + "+" + "x"
            elif lenght == 1 and i < 0:
                str_poly = str_poly + "-" + "x"     
            
            if lenght == 0 and i < 0:
                str_poly = str_poly + str(i)
            elif lenght == 0 and i > 0:
                str_poly = str_poly + "+" + str(i)

        return str_poly

