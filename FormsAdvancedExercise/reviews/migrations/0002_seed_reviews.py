from django.db import migrations


REVIEWS = [
    {
        "book_isbn": "0547928220",
        "author": "Maria Petrova",
        "body": "A warm adventure with memorable characters and a perfect sense of wonder. The riddles in the dark chapter alone is worth the whole book.",
        "rating": "5.00",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0547928220",
        "author": "Alex Ivanov",
        "body": "Bilbo bargaining with Smaug and then handing the Arkenstone to the enemy camp is the moment the story stops being a children's tale.",
        "rating": "4.40",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0618346252",
        "author": "Tom Baker",
        "body": "Slow for the first hundred pages and then impossible to put down. The world feels older than the plot moving through it.",
        "rating": "4.80",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0553103547",
        "author": "Elena Marinova",
        "body": "Every chapter switches viewpoint and somehow the tension keeps rising. The political scheming is written better than the battles.",
        "rating": "4.60",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0553103547",
        "author": "Georgi Dimitrov",
        "body": "Killing Ned Stark at the end of the first book tells you exactly what kind of series this is going to be.",
        "rating": "4.20",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0747532699",
        "author": "Sara Dimitrova",
        "body": "Read it at eight and again at thirty, and the school year structure still makes the pacing feel effortless.",
        "rating": "4.90",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0747532699",
        "author": "Nikolay Ivanov",
        "body": "A gentle start to the series. The mystery is simple, but the characters carry it further than the plot does.",
        "rating": "4.10",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0756404746",
        "author": "Iva Koleva",
        "body": "The prose is gorgeous and the magic system is genuinely clever, though the frame story moves slower than I wanted.",
        "rating": "4.50",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0765311771",
        "author": "Adrian Kolev",
        "body": "A heist novel wearing a fantasy coat. The rules of the magic are explained early and then used fairly, which I appreciated.",
        "rating": "4.65",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0765311771",
        "author": "Petar Angelov",
        "body": "Finding out the Lord Ruler's real identity recontextualizes the whole first half. Worth the reread.",
        "rating": "4.35",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0451524934",
        "author": "Daniel Petroff",
        "body": "Bleak, precise, and more relevant every year. The appendix on Newspeak is the quietest and most frightening part.",
        "rating": "4.95",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0451524934",
        "author": "Kristina Vasileva",
        "body": "I expected a thriller and got a study of how language narrows thought. Not an easy read, but a necessary one.",
        "rating": "4.70",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0060850523",
        "author": "Martin Hristov",
        "body": "Less angry than 1984 and somehow more unsettling, because everyone in it is perfectly happy with the arrangement.",
        "rating": "4.45",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0061120081",
        "author": "Ana Todorova",
        "body": "The courtroom chapters are the best writing about fairness I have read. Scout's narration keeps it from ever feeling like a lecture.",
        "rating": "4.85",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0061120081",
        "author": "Viktor Stoyanov",
        "body": "Tom Robinson losing the case despite the evidence is the point of the book, and it still lands hard.",
        "rating": "4.60",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0743273567",
        "author": "Lilia Georgieva",
        "body": "Short, sharp, and beautifully written. Nick is a far less reliable narrator than he thinks he is.",
        "rating": "4.30",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0316769487",
        "author": "Boris Manev",
        "body": "Holden is exhausting on purpose, and whether that works depends entirely on the mood you bring to it.",
        "rating": "3.70",
        "is_spoiler": False,
    },
    {
        "book_isbn": "1451673310",
        "author": "Rositsa Ilieva",
        "body": "The wall-sized screens and the constant background noise read as a prediction rather than a metaphor now.",
        "rating": "4.55",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307387895",
        "author": "Stefan Nikolov",
        "body": "Sparse punctuation, almost no names, and still the most moving father-son story I have read in years.",
        "rating": "4.75",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307387895",
        "author": "Denitsa Angelova",
        "body": "The father dying on the beach and the boy being taken in by another family is the only mercy in the entire book.",
        "rating": "4.50",
        "is_spoiler": True,
    },
    {
        "book_isbn": "1400078776",
        "author": "Yana Petrova",
        "body": "Quiet and devastating. The horror is entirely in what the characters accept without argument.",
        "rating": "4.40",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0375704027",
        "author": "Emil Zhelev",
        "body": "Melancholy done well. The 1960s Tokyo setting is drawn so carefully that the plot almost does not need to move.",
        "rating": "4.25",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0062316095",
        "author": "Ivan Krastev",
        "body": "Ambitious and very readable, though it moves fast over debates that historians still argue about. Great starting point.",
        "rating": "4.50",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0062316095",
        "author": "Mila Draganova",
        "body": "The chapter on the agricultural revolution as a trap rather than a triumph changed how I think about progress.",
        "rating": "4.70",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0393317552",
        "author": "Hristo Yankov",
        "body": "A strong thesis defended over four hundred pages. Repetitive in places, but the evidence is laid out clearly.",
        "rating": "4.15",
        "is_spoiler": False,
    },
    {
        "book_isbn": "1846683807",
        "author": "Teodora Mihaylova",
        "body": "Refreshingly honest about what the sources cannot tell us. The focus on ordinary Romans is the best part.",
        "rating": "4.60",
        "is_spoiler": False,
    },
    {
        "book_isbn": "1408839970",
        "author": "Kaloyan Petkov",
        "body": "Dense but rewarding. Recentering world history away from Western Europe makes familiar events look different.",
        "rating": "4.35",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0553296981",
        "author": "Gabriela Kostova",
        "body": "What stays with you is how ordinary the entries are. Arguments about food, school work, and privacy, written in hiding.",
        "rating": "4.90",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0553380168",
        "author": "Simeon Radev",
        "body": "Still the clearest popular physics book ever written. A few chapters need a second pass, and that is fine.",
        "rating": "4.65",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0553380168",
        "author": "Nadia Ilieva",
        "body": "Read it in a weekend with no physics background and followed most of it. The imaginary time section defeated me.",
        "rating": "4.20",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0345539435",
        "author": "Vladimir Tanev",
        "body": "Part science, part argument for curiosity as a civic virtue. The final chapter is genuinely moving.",
        "rating": "4.80",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0198788606",
        "author": "Radost Hristova",
        "body": "The central idea is simple once it clicks, and then it explains a dozen behaviors you thought were unrelated.",
        "rating": "4.55",
        "is_spoiler": False,
    },
    {
        "book_isbn": "1476733503",
        "author": "Yordan Vasilev",
        "body": "Excellent on the history, careful on the ethics, and personal in a way that most science writing avoids.",
        "rating": "4.60",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0393609391",
        "author": "Desislava Petrova",
        "body": "Exactly what the title promises. Short chapters, good jokes, and no pretense that it is a complete education.",
        "rating": "4.05",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0374533555",
        "author": "Plamen Georgiev",
        "body": "The first half is outstanding. The later sections lean on studies that have aged unevenly, so read them with care.",
        "rating": "4.30",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0374533555",
        "author": "Veronika Ruseva",
        "body": "Every chapter caught me making the exact error it describes. Uncomfortable and very useful.",
        "rating": "4.70",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0735211299",
        "author": "Krasimir Dimov",
        "body": "Practical and well organized, though the ideas could fit in half the pages. The habit stacking chapter earned its place.",
        "rating": "4.00",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0399590501",
        "author": "Silvia Nikolova",
        "body": "A hard memoir told without self-pity. The sections about returning home after university are the strongest.",
        "rating": "4.75",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307352153",
        "author": "Mihail Kirilov",
        "body": "Made me rethink how we run meetings and group work. The research is solid and the examples are recognizable.",
        "rating": "4.35",
        "is_spoiler": False,
    },
    {
        "book_isbn": "1400052181",
        "author": "Antoaneta Marinova",
        "body": "Two stories braided together, the science and the family, and the book never lets you forget which one was ignored.",
        "rating": "4.65",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307454541",
        "author": "Ivo Stanchev",
        "body": "The financial subplot drags, but Lisbeth is one of the best characters in modern crime fiction.",
        "rating": "4.20",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307454541",
        "author": "Magdalena Koleva",
        "body": "Harriet being alive and hidden abroad the whole time is a satisfying answer to a forty-year-old disappearance.",
        "rating": "4.00",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0307588378",
        "author": "Tsvetan Yordanov",
        "body": "The midpoint twist is famous for a reason, and the second half is a much stranger book than the first.",
        "rating": "4.45",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0307588378",
        "author": "Zornitsa Tasheva",
        "body": "Amy staging her own murder and then coming back to the marriage is a bleaker ending than any conviction would have been.",
        "rating": "4.25",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0007527526",
        "author": "Lyubomir Panov",
        "body": "The fairest unfair mystery ever written. Every clue is on the page and I still missed all of them.",
        "rating": "4.85",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0062073486",
        "author": "Neda Bozhilova",
        "body": "Tightly plotted and genuinely tense. Ten suspects, no detective, and a solution that holds up under rereading.",
        "rating": "4.70",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0062073486",
        "author": "Rumen Aleksiev",
        "body": "The judge faking his own death to keep killing is the cleverest use of an unreliable body count I know.",
        "rating": "4.50",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0394758285",
        "author": "Christina Lazarova",
        "body": "The plot is famously tangled and it does not matter at all. Read it for the dialogue and the atmosphere.",
        "rating": "4.30",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0140437863",
        "author": "Dimitar Vulkov",
        "body": "Great use of the moor as a setting. Watson carries most of the investigation and is better company for it.",
        "rating": "4.40",
        "is_spoiler": False,
    },
    {
        "book_isbn": "0140437863",
        "author": "Polina Grozdanova",
        "body": "The hound turns out to be an ordinary dog with phosphorus paint, which is somehow more sinister than a curse.",
        "rating": "4.10",
        "is_spoiler": True,
    },
    {
        "book_isbn": "0618346252",
        "author": "Ognyan Ivanov",
        "body": "Best read slowly. The songs and long descriptions are the point, not an obstacle to the plot.",
        "rating": "4.55",
        "is_spoiler": False,
    },
]


def seed_reviews(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Review = apps.get_model("reviews", "Review")

    books_by_isbn = {
        book.isbn: book
        for book in Book.objects.filter(
            isbn__in=[review["book_isbn"] for review in REVIEWS],
        )
    }

    for review in REVIEWS:
        book = books_by_isbn.get(review["book_isbn"])

        if not book:
            continue

        Review.objects.update_or_create(
            book=book,
            author=review["author"],
            defaults={
                "body": review["body"],
                "rating": review["rating"],
                "is_spoiler": review["is_spoiler"],
            },
        )


def remove_seeded_reviews(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Review = apps.get_model("reviews", "Review")

    books_by_isbn = {
        book.isbn: book
        for book in Book.objects.filter(
            isbn__in=[review["book_isbn"] for review in REVIEWS],
        )
    }

    for review in REVIEWS:
        book = books_by_isbn.get(review["book_isbn"])

        if book:
            Review.objects.filter(
                book=book,
                author=review["author"],
            ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_seed_books"),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_reviews, remove_seeded_reviews),
    ]
