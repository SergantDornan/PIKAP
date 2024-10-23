from operator import itemgetter

class Microprocessor:
 """Microprocessor"""
 def __init__(self, id, model, clock_speed, computer_id):
  self.id = id
  self.model = model
  self.clock_speed = clock_speed
  self.computer_id = computer_id

class Computer:
 """Computer"""
 def __init__(self, id, name):
  self.id = id
  self.name = name

class MicroprocessorsComputer:
 """
 'Microprocessors of a Computer' for implementing
 many-to-many relationship
 """
 def __init__(self, computer_id, microprocessor_id):
  self.computer_id = computer_id
  self.microprocessor_id = microprocessor_id

# Computers
computers = [
 Computer(1, 'Computer 1'),
 Computer(2, 'Computer 2'),
 Computer(3, 'Computer 3'),
]

# Microprocessors
microprocessors = [
 Microprocessor(1, 'Intel Core i7-12700K', 5.0, 1),
 Microprocessor(2, 'AMD Ryzen 9 5950X', 4.9, 2),
 Microprocessor(3, 'Intel Core i5-12600K', 4.9, 3),
 Microprocessor(4, 'AMD Ryzen 7 5800X', 4.7, 1),
 Microprocessor(5, 'Intel Core i3-12100', 4.3, 2),
]

microprocessors_computers = [
 MicroprocessorsComputer(1, 1),
 MicroprocessorsComputer(2, 2),
 MicroprocessorsComputer(3, 3),
 MicroprocessorsComputer(1, 4),
 MicroprocessorsComputer(2, 5),
]

def main():
 """Main function"""

 # One-to-many data connection 
 one_to_many = [(m.model, m.clock_speed, c.name) 
  for c in computers 
  for m in microprocessors 
  if m.computer_id==c.id]
 
 # Many-to-many data connection
 many_to_many_temp = [(c.name, mc.computer_id, mc.microprocessor_id) 
  for c in computers 
  for mc in microprocessors_computers 
  if c.id==mc.computer_id]
 
 many_to_many = [(m.model, m.clock_speed, c_name) 
  for c_name, c_id, m_id in many_to_many_temp
  for m in microprocessors if m.id==m_id]

 print('Task G1')
 res_11 = [ (c.name, [m.model for m in microprocessors if m.computer_id == c.id]) for c in computers if c.name[0] == 'C'] 
 print(res_11)
 
 print('\nTask G2')
 res_12_unsorted = []
 # Iterate over all computers
 for c in computers:
  # List of computer microprocessors
  c_mps = list(filter(lambda i: i[2]==c.name, one_to_many))
  # If computer is not empty  
  if len(c_mps) > 0:
   # Clock speeds of the computer's microprocessors
   c_freqs = [freq for _,freq,_ in c_mps]
   # Maximum clock speed of the computer's microprocessors
   c_max_freq = max(c_freqs)
   res_12_unsorted.append((c.name, c_max_freq))


 # Sorting by maximum clock speed
 res_12 = sorted(res_12_unsorted, key=lambda item: item[1], reverse=True)
 print(res_12)


 print('\nTask G3')
 res_13 = {}
 # Iterate over all computers
 for c in computers:
  # List of computer microprocessors
  c_mps = list(filter(lambda i: i[2]==c.name, many_to_many))
  # Only microprocessor models
  c_mps_models = [x for x,_,_ in c_mps]
  # Add the result to the dictionary
  # key - computer, value - list of microprocessor models
  res_13[c.name] = c_mps_models


 print(res_13)


if __name__ == '__main__':
 main()
