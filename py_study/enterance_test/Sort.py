li = []
def put_in():
    mode = True
    while mode == True:
          Tip = "请输入一个数字，当你觉得足够多时输入out结束输入，稍后我会为你排列它："
          a = input(Tip)
          li.append(a)
          li.sort()
          if a == "out":
              mode = False