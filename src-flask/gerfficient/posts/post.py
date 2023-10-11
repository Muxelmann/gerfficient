import lorem
import random
import datetime

class Post:

    def __init__(self, id: str) -> None:
        self.id = id
        self.title = None
        self.summary = None
        self.date = datetime.datetime.now()
        self.body = None

    @property
    def nice_date(self) -> str:
        return self.date.strftime('%d-%m-%Y')

    @classmethod
    def lorem(cls) -> 'Post':
        post = Post('lorem')
        post.title = lorem.sentence()[:-1]
        post.title = ' '.join(post.title.split(' ')[:min(len(post.title)-1, random.randint(3, 5))])
        post.summary = lorem.paragraph()
        post.body = '\n'.join([f'<p>{lorem.paragraph()}</p>' for _ in range(random.randint(2, 4))])
        return post

    @classmethod
    def get_post_with_id(cls, id: str) -> 'Post':
        post = Post(id)

        return post