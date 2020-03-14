class Temperature:
    str_format = ''
    def __init__(self, degree, unit = 'C'):
        if type(degree) not in {int, float}:
            raise TypeError
        else:
            self._degree = float(degree)
        if unit.upper() not in {'C', 'F'}:
            raise ValueError
        else:
            self._unit = unit
    def set_degree(self, degree):
        if type(degree) not in {int, float}:
           raise TypeError
        else:
            self._degree = degree
    def get_degree(self):
        return self._degree
    def set_unit(self, unit):
        if unit.upper() not in {'C', 'F'}:
            raise ValueError
        else:
            final_deg, final_unit = self.get_temp(unit) #obtain the degree and unit after transformation
            self.set_degree(final_deg)
            self._unit = final_unit
    def get_unit(self):
        return self._unit
    def __repr__(self):
        #deg = self.get_degree
        #unit = self.get_unit
        #ans = f'{deg} {unit}'
        return f'{self._degree} {self._unit}'
    def get_temp(self, sel_unit = 'C'):
        if sel_unit.upper() not in {'C', 'F'}:
            raise ValueError
        if self._unit == 'C' and sel_unit == 'F':
            #self._unit = sel_unit
            return (((self._degree * 9) / 5 + 32), sel_unit)
        elif self._unit == 'F' and sel_unit == 'C':
            #self._unit = sel_unit
            return ((self._degree - 32) * 5 / 9, sel_unit)
        else:
            return (self._degree, self._unit)
    degree = property(lambda self: self.get_degree(), lambda self, deg: self.set_degree(deg))
    unit = property(lambda self: self.get_unit(), lambda self, unit: self.set_unit(unit))
    #@classmethod
    #def set_format(cls, str_format):
        #str_format.replace('%', ':')
        #cls.str_format = str_format

class NewTemp(Temperature):
    def __repr__(self):
        return __class__.__name__ + f'({self._degree}, {self._unit})'
    def __add__(self, RHS):
        if isinstance(RHS, Temperature):
            RHS_degree, RHS_unit = RHS.get_temp(self._unit)
            return NewTemp(self._degree + RHS_degree, self._unit)
        elif type(RHS) in {int, float}:
            return NewTemp(self._degree + RHS, self._unit)
    def __sub__(self, RHS):
        if isinstance(RHS, Temperature):
            RHS_degree, RHS_unit = RHS.get_temp(self._unit)
            return NewTemp(self._degree - RHS_degree, self._unit)
        elif type(RHS) in {int, float}:
            return NewTemp(self._degree - RHS, self._unit)
        
