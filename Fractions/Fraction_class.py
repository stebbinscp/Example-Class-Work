from math import gcd

class Fraction:  # input numerator, input denominator
    """Fraction class intended to overload python object classes"""
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def as_decimal(self):
        """Turns two given numbers into a decimal"""
        decimal = self.numerator/self.denominator
        decimal = round(decimal,3) 
        # round
        if int(self.numerator) != self.numerator:
            return ValueError
        elif int(self.denominator) != self.denominator:
            return ValueError
        elif self.denominator == 0:
            return ZeroDivisionError
        else:
            return decimal
    def __str__(self):
        """Turns two given numbers into a string"""
        whole_number = self.numerator//self.denominator
            
        if whole_number != 0: 
            new_numerator = self.numerator - (whole_number*self.denominator)

            if new_numerator == 0:
                frac = f"{whole_number}"


            else:
                greatestcd = gcd(new_numerator,self.denominator)
                new_numerator = new_numerator//greatestcd
                new_denominator = self.denominator//greatestcd
                frac = f"{whole_number}-{int(new_numerator)}/{int(new_denominator)}"

        else: 
            greatestcd = gcd(self.numerator,self.denominator) 
            new_numerator = self.numerator//greatestcd
            new_denominator = self.denominator//greatestcd
            frac = f"{new_numerator}/{new_denominator}"
        return frac

    def __add__(self, frac_2): 
        """ Add the self and the second fraction """
        if self.denominator == frac_2.denominator:
            new_numerator = self.numerator + frac_2.numerator
            denominator = self.denominator
            frac = Fraction(new_numerator,denominator)

        else:
            common_denominator = self.denominator*frac_2.denominator
            new_num = self.numerator*frac_2.denominator
            new_num_2 = frac_2.numerator*self.denominator
            new_numerator = new_num+new_num_2
            frac = Fraction(new_numerator,common_denominator)
        if int(frac.numerator) != frac.numerator:
            "Ope, that's not an integer!"
            return ValueError
        elif int(frac.denominator) != frac.denominator:
            "Ope, that's not an integer!"
            return ValueError
        elif frac.denominator == 0:
            print("Cannot divide by zero!")
            return ZeroDivisionError
        else:
            return frac

    def __sub__(self, frac_2):
        """ Subtract the self and the second fraction """
        if self.denominator == frac_2.denominator:
            new_numerator = self.numerator - frac_2.numerator
            denominator = self.denominator
            frac = Fraction(new_numerator,denominator)

        else:
            common_denominator = self.denominator*frac_2.denominator
            new_num = self.numerator*frac_2.denominator
            new_num_2 = frac_2.numerator*self.denominator
            new_numerator = new_num-new_num_2
            frac = Fraction(new_numerator,common_denominator)
        if int(frac.numerator) != frac.numerator:
            "Ope, that's not an integer!"
            return ValueError
        elif int(frac.denominator) != frac.denominator:
            "Ope, that's not an integer!"
            return ValueError
        elif frac.denominator == 0:
            print("Cannot divide by zero!")
            return ZeroDivisionError
        else:
            return frac

    def __mul__(self, frac_2):
        """ Multiply the self and the second fraction """
        new_numerator = self.numerator*frac_2.numerator
        new_denominator = self.denominator*frac_2.denominator
        frac = Fraction(new_numerator,new_denominator)
        if int(frac.numerator) != frac.numerator:
            "Ope, that's not an integer!"
            return ValueError
        elif int(frac.denominator) != frac.denominator:
            "Ope, that's not an integer!"
            return ValueError
        elif frac.denominator == 0:
            print("Cannot divide by zero!")
            return ZeroDivisionError
        else:
            return frac

    def __truediv__(self, frac_2):
        """ Divide the self by the second fraction """
        numerator_2 = frac_2.denominator 
        # flip the second fraction's numerator and denomiator
        denominator_2 = frac_2.numerator
        f_new = Fraction(numerator_2,denominator_2)
        # make a new instance
        new_numerator = self.numerator*f_new.numerator
        # multiple numerators and denominators
        new_denominator = self.denominator*f_new.denominator
        frac = Fraction(new_numerator,new_denominator)
        if int(frac.numerator) != frac.numerator:
            "Ope, that's not an integer!"
            return ValueError
        elif int(frac.denominator) != frac.denominator:
            "Ope, that's not an integer!"
            return ValueError
        elif frac.denominator == 0:
            print("Cannot divide by zero!")
            return ZeroDivisionError
        else:
            return frac