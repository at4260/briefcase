class Solution:
    def reformatDate(self, date: str) -> str:
        # O1 space and time - bounded by a constant

        month_lookup = {
            "Jan": "01", 
            "Feb": "02", 
            "Mar": "03", 
            "Apr": "04", 
            "May": "05", 
            "Jun": "06", 
            "Jul": "07",
            "Aug": "08", 
            "Sep": "09", 
            "Oct": "10",
            "Nov": "11", 
            "Dec": "12"
        }

        day, month, year = date.split(" ")

        day_num = (day[:-2]).zfill(2)
        # "{:02}".format() is not great because it expects an int and day is a string
        month_num = month_lookup[month]

        return f"{year}-{month_num}-{day_num}"
        