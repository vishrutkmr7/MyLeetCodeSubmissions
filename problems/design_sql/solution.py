class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tab = {}
        for name in names:
            self.tab[name] = {"nextid": 1}

    def insertRow(self, name: str, row: List[str]) -> None:
        tab = self.tab[name]
        rowId = tab["nextid"]
        tab[rowId] = row
        tab["nextid"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        # tab = self.tab[name]
        # del tab[rowId]
        pass

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tab[name][rowId][columnId - 1]