
import asyncio
from datetime import datetime
import random
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from book_services.app.book_config import settings
from book_services.app.book_model import Book

engine=create_async_engine(settings.DATABASE_URL,echo=False)
SessionLocal=async_sessionmaker(engine,expire_on_commit=False)

def generate_books_dataset():
    base=[
("Atomic Habits","James Clear","Self Help",499),
("Deep Work","Cal Newport","Productivity",450),
("Psychology of Money","Morgan Housel","Finance",520),
("Rich Dad Poor Dad","Robert Kiyosaki","Finance",400),
("Think and Grow Rich","Napoleon Hill","Motivation",380),
("Ikigai","Francesc Miralles","Self Help",320),
("Zero to One","Peter Thiel","Business",410),
("Lean Startup","Eric Ries","Business",460),
("Start With Why","Simon Sinek","Business",430),
("7 Habits","Stephen Covey","Self Help",540),
("Clean Code","Robert C. Martin","Programming",650),
("Pragmatic Programmer","Andrew Hunt","Programming",750),
("Python Crash Course","Eric Matthes","Programming",700),
("Fluent Python","Luciano Ramalho","Programming",980),
("Effective Python","Brett Slatkin","Programming",820),
("Intro to Algorithms","Thomas Cormen","Computer Science",1200),
("Grokking Algorithms","Aditya Bhargava","Computer Science",680),
("DDIA","Martin Kleppmann","System Design",1100),
("Hands-On ML","Aurelien Geron","AI/ML",950),
("Deep Learning","Ian Goodfellow","AI/ML",1350),
("The Alchemist","Paulo Coelho","Fiction",350),
("1984","George Orwell","Dystopian",360),
("Animal Farm","George Orwell","Satire",250),
("The Hobbit","J.R.R. Tolkien","Fantasy",480),
("Harry Potter 1","J.K. Rowling","Fantasy",550),
]
    books=[]
    for t,a,c,p in base:
        books.append(dict(title=t,author=a,category=c,price=float(p),quantity=random.randint(10,30),description=f"{t} by {a}.",book_type="hardcopy"))
        books.append(dict(title=t,author=a,category=c,price=round(p*0.45,2),quantity=random.randint(80,150),description=f"Digital edition of {t}.",book_type="softcopy"))
    return books

async def seed():
    inserted=skipped=0
    async with SessionLocal() as session:
        for b in generate_books_dataset():
            exists=await session.scalar(select(Book).where(Book.title==b["title"],Book.author==b["author"],Book.book_type==b["book_type"]))
            if exists:
                skipped+=1
                continue
            session.add(Book(**b))
            inserted+=1
        await session.commit()
    print(f"Inserted: {inserted}, Skipped: {skipped}")

if __name__=="__main__":
    asyncio.run(seed())
