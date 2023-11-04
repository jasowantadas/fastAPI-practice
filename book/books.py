from fastapi import FastAPI

app = FastAPI()
# bookss = [{'title': 'Title one', 'author': 'author one', 'category': 'math'}, {'title': 'Title two', 'author': 'author two', 'category': 'math'}, {'title': 'Title three',
#                                                                                                                                                    'author': 'author three', 'category': 'math'}, {'title': 'Title four', 'author': 'author four', 'category': 'math'}, {'title': 'Title five', 'author': 'author five', 'category': 'math'}]


class Book:
    id: str
    title: str
    author: str
    discription: str
    rating: str

    def __init__(self, id, title, author, discription, rating):
        self.id = id
        self.author = author
        self.discription = discription
        self.rating = rating
        self.title = title


BOOKS = [Book(1, "Coomputer Science Pro",
              "Codding with Jaso", "A very nice book", 5), Book(2, "Coomputer Science Pro II",
                                                                "Codding with Jaso", "A greatbook", 4), Book(3, "JAVA",
                                                                                                             "Codding with Jaso", "Ok Book", 3), Book(4, "Abra ka dabra",
                                                                                                                                                      "ZEUS", "G book", 5)]


@app.get('/books')
async def first_api():
    return BOOKS
