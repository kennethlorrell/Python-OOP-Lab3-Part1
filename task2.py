class Calendar(object): 
    def __init__(self, day=1, month=1, year=0):
        self.months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
 
        if day > self.months[month % 12 -1] and not self.leapyear(year):    
            print('Перехід на наступний місяць')
            while day > self.months[month % 12 - 1]:
                day -= self.months[month % 12 - 1]
                month += 1
        if month > 12:
            print('Перехід на наступний рік')
            while month > 12:
                year += 1
                month -= 12
           
        self.__day = day
        self.__month = month
        self.__year = year

    def leapyear(self,y):
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            return True
        else:
            return False

    def get(self):
        return (self.__day, self.__month, self.__year)

    def __iadd__(self, other):
        return Calendar(self.__day + other.__day, self.__month + other.__month,\
                        self.__year + other.__year)

    def __isub__(self, other):
        return Calendar(self.__day - other.__day, self.__month - other.__month,\
                        self.__year - other.__year)

    def __eq__(self, other):
        return all([self.__year == other.__year, self.__month==other.__month,\
                    self.__day==other.__day])

    def __ne__(self, other):
        return any([self.__year != other.__year, self.__month!=other.__month,\
                    self.__day!=other.__day])

    def __ge__(self, other):
        if self.__year >= other.__year:
            return True
        elif self.__month >= other.__month:
            return True
        elif self.__day >= other.__day: 
            return True
        return False

    def __gt__(self, other):
        if self.__year > other.__year:
            return True
        elif self.__month > other.__month:
            return True
        elif self.__day > other.__day: 
            return True
        return False   

    def __lt__(self, other): 
        if self.__year < other.__year:
            return True
        elif self.__month < other.__month:
            return True
        elif self.__day < other.__day: 
            return True
        return False   

    def __le__(self, other): 
       if self.__year <= other.__year:
            return True
       elif self.__month <= other.__month:
            return True
       elif self.__day <= other.__day: 
            return True
       return False   
 
    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

    def __str__(self):
       return '''{}.{}.{}'''.format(self.__day, self.__month, self.__year)
