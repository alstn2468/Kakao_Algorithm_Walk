# 010.py
def shell() :
    입력값 = input('#')

    if 입력값 == 'exit' :
        return None

    shell()

shell()        
