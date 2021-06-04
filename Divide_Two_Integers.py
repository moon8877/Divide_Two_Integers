class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #輸入字串，從大數至小數進行減法
        def mul(str_divisor,str_dividend):
            ans = []
            count = 0
            divisor = int(str_divisor)
            dividend = int(str_dividend)
            bonus_char = ""
            for i in str_dividend:
                temp = bonus_char
                temp = bonus_char+i
                temp = int(temp)
                while(divisor <= temp):
                    temp = temp - divisor 
                    count = count + 1
                bonus_char = str(temp)
                ans.append(str(count))
                count = 0
            return ans
        temp = 0
        flag = 1
        #判斷輸出是否為負
        if((dividend < 0) and (divisor < 0)):
            flag = 1
            dividend = abs(dividend) 
            divisor = abs(divisor) 
        elif(dividend < 0):
            dividend = abs(dividend) 
            flag = 0
        elif(divisor < 0):
            divisor = abs(divisor) 
            flag = 0
        #無效值過濾
        if(dividend == 0 or dividend<divisor):
            return 0
        
        ans = mul(str(divisor),str(dividend))
        #字串轉數字
        ans_char = ""
        for j in range(len(ans)):
            if(j==0 and ans[j]=="0"):
                pass
            else:
                ans_char = ans_char + ans[j]
        
        ans_int = int(ans_char)
        if(flag == 0):
            temp = ans_int
            ans_int = ans_int - temp
            ans_int = ans_int - temp
            if(ans_int<-2147483648):
                ans_int = -2147483648
            return ans_int
        else:
            if(ans_int>=2147483648):
                ans_int = 2147483647
            return ans_int