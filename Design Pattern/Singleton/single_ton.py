class Singleton:
    __instance = None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is singleton.Already have an instance')
    
    @staticmethod
    def get_instanc():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

first = Singleton.get_instanc()
second = Singleton.get_instanc()
third = Singleton.get_instanc()

print(first)
print(second)
print(third)