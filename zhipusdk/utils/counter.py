class Counter:
    def __init__(self) -> None:
        self._count = 0

    def add_one(self) -> None:
        self._count += 1

    def where_to_add_line_break(self) -> str:
        if self._count % 2 == 0:
            return "after"
        elif self._count % 2 == 1:
            return "before"
        else:
            return ""

    def get_count(self) -> int:
        return self._count
