#!/usr/bin/env python3

# lib/book.py

class Book:
    def __init__(self, title: str, page_count: int, author: str = None):
        self._title = None
        self._page_count = None
        self._author = None

        self.title = title
        self.page_count = page_count
        if author:
            self.author = author

    # ----- title -----
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise Exception("title must be a string")
        self._title = value

    # ----- page_count -----
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        # 👉 tests expect a *print* (not an exception) for non-integers
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value <= 0:
            # you can keep this guard; tests don't check it, but it's fine
            raise Exception("page_count must be > 0")
        self._page_count = value


    # ----- author -----
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str):
            raise Exception("author must be a string")
        self._author = value

    # ----- instance method -----
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __repr__(self):
        return f"Book(title={self.title!r}, pages={self.page_count}, author={self.author!r})"

    
        