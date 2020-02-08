import pcka
from pcka import test_module
from p108t2 import sx


print("输出pcka包中的变量", pcka.name)
print("调用pcka中的函数", end="")
pcka.pck_test_fun()
print("调用test_module中的函数")
test_module.test_module_fun()
sx.sushu(37)
