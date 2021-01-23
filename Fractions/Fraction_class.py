from math import gcd

class Fraction:  # input numerator, input denominator
    def __init__(self, numerator, denominator):
        """Init two inputs"""
        self.numerator = numerator
        self.denominator = denominator
        # self.dec = round(self.numerator/self.denominator, 3)
            # but this is another attribute and i dont think that
            # what they want
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
            # numerator is smaller than denominatornow
            # numerator - denominator times the whole number from floor division
            # numerator smaller

            if new_numerator == 0:
                frac = f"{whole_number}"
                # if the numerator is 0 now, frac is the whole number

            else:
                greatestcd = gcd(new_numerator,self.denominator)
                # gcd returns the number to divide each part by
                new_numerator = new_numerator//greatestcd
                # numerator is now divided by the gcd
                new_denominator = self.denominator//greatestcd
                frac = f"{whole_number}-{int(new_numerator)}/{int(new_denominator)}"

        else: 
            greatestcd = gcd(self.numerator,self.denominator) 
            # reduce to the smallest fraction
            new_numerator = self.numerator//greatestcd
            new_denominator = self.denominator//greatestcd
            frac = f"{new_numerator}/{new_denominator}"
        return frac

    def __add__(self, frac_2): 
        """ Add the self and the second fraction """
        if self.denominator == frac_2.denominator:
            # same denominators
            new_numerator = self.numerator + frac_2.numerator
            denominator = self.denominator
            frac = Fraction(new_numerator,denominator)

        else:
            # different denominators
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
            # print(new_numerator)
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
        # just multiply
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
        # error handling


# f1 = Fraction(1,2) 
# f2 = Fraction(2,1) 

# total = f1/f2
# total_2 = f1-f2
# print(total.__str__())
# print(total_2.__str__())


# numerator2 = 2
# denominator2 = 5


# print(gcd(f2.numerator,f2.denominator))

# f1 = Fraction(1,2)
# f2 = Fraction(2,1)

# # hello = f1/f2
# # print(hello)

# f1 = Fraction(1,2) 
# f2 = Fraction(2,1) 

# total = f1/f2
# print(total)

# if f.__str__() == "5/8":
#     print(True)
# print(f)
# print(type(f))
# print(f+f)
# assert f == "5/8"
# assert f.as_decimal() == 0.625
# f2 = Fraction(numerator2,denominator2)

# print(f1+f2)
# print(f1*f2)
# print(f1-f2)
# print(f1/f2)
# print((f1+f2).as_decimal())

# be able to do greater than and less than

# expand on the given test suite

# print(f1.as_decimal()<f2.as_decimal()) # works!
# print(f1.as_decimal()>f2.as_decimal()) # works!