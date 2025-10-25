def isOdd(param):
    # 先判断是否为整数类型
    if not isinstance(param, int):
        return False
    # 再判断是否为奇数
    return param % 2 == 1
