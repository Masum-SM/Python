class Furniture:
    def __init__(self) -> None:
        pass
    
class Chair(Furniture):
    def __init__(self) -> None:
        super().__init__()
    
wooden_chir = Chair()
print(issubclass(Chair,Furniture))
print(isinstance(wooden_chir,Chair))
print(isinstance(wooden_chir,Furniture))