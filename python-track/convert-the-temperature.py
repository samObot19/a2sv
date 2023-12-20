class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        Fahrenheit = celsius * 1.80 + 32.00

        kelvn = celsius + 273.15
        lst = []
        lst.append(kelvn)
        lst.append(Fahrenheit)
        return lst
        