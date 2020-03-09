def rabbits_fib(offspring, mouth):
    if(mouth in (1,2)):
        return(1)
    else:
        return(rabbits_fib(offspring, mouth-1) + offspring*rabbits_fib(offspring, mouth-2))

offspri = int(input('offspring：'))
mth = int(input('mouth：'))
rabbits_fib(offspri,mth)

#每一对两代前存活的兔子会繁殖出offspring只兔子，是这代唯一的新兔子来源，同时一代前存活的兔子依然存在。
#递归为程序的自身调用，直到能直接得出结果的层，再返还计算结果，包含大量重复运算。迭代为从已知项开始逐层循环求值。后者占用内存较少运行较快。