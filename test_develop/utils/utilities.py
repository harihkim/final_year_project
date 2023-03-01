from fastapi import UploadFile

class PrintInfo:

    COST_PER_PAGE = 2

    def __init__(self, file: UploadFile, copies_count: int, is_double_side: bool, page_count: int) -> None:
        self.file: UploadFile = file
        self.no_of_copies: int = copies_count
        self.is_double_side: bool = is_double_side
        self.no_of_pages: int = page_count

    def calculate_cost(self) -> int:
        if(self.is_double_side == True):
            return (self.no_of_pages//2) * self.COST_PER_PAGE * self.no_of_copies
        return self.no_of_pages * self.COST_PER_PAGE

