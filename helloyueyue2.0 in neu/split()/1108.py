#time.space: O(n)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        list_address = list(address)
        for i, char in enumerate(list_address):
            if char == ".":
                list_address[i] = "[.]"
        return "".join(list_address)

#更简洁 time.space: O(n)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        list_address = address.split(".")
        new_address = "[.]".join(list_address)
        return new_address