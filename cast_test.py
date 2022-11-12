from typing import Optional, cast

x: Optional[int] = None

def AddOne(num: int) -> int:
    return num + 1

# mypyに怒られる
#y = AddOne(x)
#print(y)

# mypyに怒られないけど実行時エラー
#y = AddOne(cast(int, x))
#print(y)

# mypyに怒られないし実行時にちゃんと例外処理できる
if x is not None:
    y = AddOne(cast(int, x))
    print(y)