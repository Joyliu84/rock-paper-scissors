# 求平方根
def square_root(numb, acc):
    """求平方根函数

    Args:
        numb (int): 要求的数
        acc (int): 精确度

    Raises:
        ZeroDivisionError: 输入负数则抛出此异常

    Returns:
        float: 所求的平方根值
    """
    if numb < 0:
        raise ZeroDivisionError

    def tmp_root(bottom, upper):
        while True:
            root = (upper+bottom)/2
            print(bottom, upper)
            if abs(root*root-numb) <= acc/1000000:
                return root
            elif root*root > numb:
                upper = root
            else:
                bottom = root

    if numb > 1:
        bottom, upper = 0, numb
        return tmp_root(bottom, upper)
    elif numb < 1:
        bottom, upper = numb, 1
        return tmp_root(bottom, upper)
    else:
        return 1

x = square_root(4, 1)
print(x)