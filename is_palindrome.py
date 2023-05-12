chain = "somos o no somos"
chain2 = list(range(1, 10))

def is_palindrome(chain: str | list):
    if type(chain) == str:
        chain = list(chain.replace(" ", ""))
        reversed_chain = chain.copy()
    else:
        reversed_chain = chain.copy()
    
    reversed_chain.reverse()
    
    if chain == reversed_chain:
        return True
    
    return False
        
print(palindrome(chain))