from testapp.models import *


def run():
    english = Language(title="English")
    english.save()

    african = Language(title='African')
    african.save()

    matt = [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20]
    for count in range(0, len(matt)):
        for each_verse in range(1, int(matt[count])+1):
            chapter = Chapter.objects.get_or_create(title="Chapter " + str(count+1), book=Book.objects.get_or_create(title="Matt")[0])
            verse = Verse.objects.get_or_create (chapter=chapter[0], title="Verse " + str(each_verse))
            print(verse)


    mark = [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]
    for count in range(0, len(mark)):
        for each_verse in range(1, int(mark[count])+1):
            chapter = Chapter.objects.get_or_create(title="Chapter " + str(count+1), book=Book.objects.get_or_create(title="Mark")[0])
            verse = Verse.objects.get_or_create (chapter=chapter[0], title="Verse " + str(each_verse))
            print(verse)


    luke = [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]
    for count in range(0, len(luke)):
        for each_verse in range(1, int(luke[count])+1):
            chapter = Chapter.objects.get_or_create(title="Chapter " + str(count+1), book=Book.objects.get_or_create(title="Luke")[0])
            verse = Verse.objects.get_or_create (chapter=chapter[0], title="Verse " + str(each_verse))
            print(verse)

    john = [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]
    for count in range(0, len(john)):
        for each_verse in range(1, int(john[count])+1):
            chapter = Chapter.objects.get_or_create(title="Chapter " + str(count+1), book=Book.objects.get_or_create(title="John")[0])
            verse = Verse.objects.get_or_create (chapter=chapter[0], title="Verse " + str(each_verse))
            print(verse)
