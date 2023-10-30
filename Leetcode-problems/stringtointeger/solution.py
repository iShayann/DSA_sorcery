class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        l=""
        res=""
        num=False

        for i in s:
            if i=='-' and num!= True:
                sign*=-1
                l+=i
            elif i=='+' and num!=True:
                l+=i
                continue
            elif ord('0')<=ord(i)<=ord('9'):
                res+=i
                num=True
            elif not ord('0')<=ord(i)<=ord('9'):
                break
            
        print(res)
        if res=="" or len(l)>1:
            return 0
        else:

            if (int(res)*sign)>2**31 -1:
                return 2**31 - 1
            elif (int(res)*sign)<(-2)**31:
                return (-2)**31
            return int(res)*sign
