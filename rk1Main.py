from operator import itemgetter

class Schoolboy:
  """Schoolboy"""
  def __init__(self, id, surname, mark, class_id):
    self.id = id
    self.surname = surname
    self.mark = mark
    self.class_id = class_id

class Class:
  """Class"""
  def __init__(self, id, name):
    self.id = id
    self.name = name

class SchoolboyClass:
  """
  'Schoolboys of a Class' for implementing
  many-to-many relationship
  """
  def __init__(self, class_id, schoolboy_id):
    self.class_id = class_id
    self.schoolboy_id = schoolboy_id

classes = [
  Class(1, '9A'),
  Class(2, '10Б'),
  Class(3, '11В'),
  Class(4, '9Г'),
  Class(5, '10Д'),
]

schoolboys = [
  Schoolboy(1, 'Иванов', 5, 1),
  Schoolboy(2, 'Петров', 4, 2),
  Schoolboy(3, 'Сидоров', 3, 3),
  Schoolboy(4, 'Кузнецов', 5, 4),
  Schoolboy(5, 'Смирнов', 4, 5),
]

schoolboys_classes = [
  SchoolboyClass(1, 1),
  SchoolboyClass(2, 2),
  SchoolboyClass(3, 3),
  SchoolboyClass(4, 4),
  SchoolboyClass(5, 5),
  SchoolboyClass(1, 2),
  SchoolboyClass(2, 3),
  SchoolboyClass(3, 4),
  SchoolboyClass(4, 5),
  SchoolboyClass(5, 1),
]

def main():
  """Main function"""

  one_to_many = [(s.surname, s.mark, c.name) 
    for c in classes 
    for s in schoolboys 
    if s.class_id == c.id]

  many_to_many_temp = [(c.name, sc.class_id, sc.schoolboy_id) 
    for c in classes 
    for sc in schoolboys_classes 
    if c.id == sc.class_id]

  many_to_many = [(s.surname, s.mark, c_name) 
    for c_name, c_id, s_id in many_to_many_temp
    for s in schoolboys if s.id == s_id]

  print('Task B1')
  res_11 = [ (s.surname, c.name) for c in classes for s in schoolboys if s.class_id == c.id and s.surname.endswith('ов')] 
  print(res_11)
  
  print('\nTask B2')
  res_12_unsorted = []
  for c in classes:
    c_schoolboys = list(filter(lambda i: i[2] == c.name, one_to_many))
    if len(c_schoolboys) > 0:
      c_marks = [mark for _, mark, _ in c_schoolboys]
      c_avg_mark = sum(c_marks) / len(c_marks)
      res_12_unsorted.append((c.name, c_avg_mark))

  res_12 = sorted(res_12_unsorted, key=itemgetter(1))
  print(res_12)

  print('\nTask B3')
  res_13 = sorted(many_to_many, key=itemgetter(0)) # Sort by schoolboy surname
  print(res_13)

if __name__ == '__main__':
  main()

