# class Note:
#       def __init__(self, text):
#           self.text = text
#           self.count = 0
#       def upcount(self):
#           self.count += 1
#
#
# note1 = Note('Задача 1')
# note2 = Note('Задача 2')

class NoteTwo:
    def __init__(self, text, iscompleted):
         self.text = text
         self.count = 0
         self.iscompleted = iscompleted

    def UpCount(self, num):
         self.count += num

    def ResetCount(self):
         self.count = 0

note1 = NoteTwo('Текст', True)

print(note1.__dict__)
note1.UpCount(5)
print(note1.__dict__)
