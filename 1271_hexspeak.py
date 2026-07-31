class Solution:
    def to_hexspeak(self, num: str) -> str:
        """
        Convert a decimal number string to its Hexspeak representation.
        :param str num: The decimal number as a string.
        :return: The Hexspeak representation if valid, otherwise "ERROR".
        :rtype: str
        """
        # Add your code here
        
        # can use hex() as well
            # "0x" represents "this is hex value", "0b" binary "0o" octal
        # hex_num = hex(num)[2:].upper()
            # alt: format(num, "X") uppercase of hexadecimal value
        def to_hex(num_str: str) -> str:
            num = int(num_str)
            result = ""
            
            hex_digits = "0123456789ABCDEF"
            while num > 0:
                remainder = num % 16
                result = hex_digits[remainder] + result
                num = num // 16 
                
            return result
            
        # def to_binary(num):
        #     result = ""
        #     while num > 0:
        #         remainder = num % 2
        #         result = str(remainder) + result
        #         num = num // 2
        #     return result        
        

            
        hex_num = to_hex(num)
        allowed = set("ABCDEF10")
        result = ""
        for i, char in enumerate(hex_num):
            if char not in allowed:
                return "ERROR"
            if char == "1":
                result += "I"
            elif char == "0":
                result += "O"
            else:
                result += char
                
        return result
    