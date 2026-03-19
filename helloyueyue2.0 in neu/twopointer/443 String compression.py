class Solution:
    def compress(self, chars: List[str]) -> int:
        """
    modify in_place:count the number of each char and replace the last char with the number
         i	    scan through the list
        write	写入压缩结果的位置
        count	当前字符连续出现次数
        return: length of new input array
        """
        i = 0
        write = 0
        while i < len(chars):
            curr_char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == curr_char:
                i += 1
                count += 1
            chars[write] = curr_char #先写入curr_char
            write += 1
            if count > 1:#考虑多位数情况
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write