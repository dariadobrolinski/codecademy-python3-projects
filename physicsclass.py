# Get Ready for Physics Class project from Codecademy Python 3 course.

train_mass = 22680 
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Get Force
def get_force(mass, acceleration):
  force = mass * acceleration 
  return force
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

# Get Energy
def get_energy(mass, c = (3*(10**8))):
  energy = mass * c ** 2
  return energy
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
# Get Work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work
train_work = get_work(train_mass, train_acceleration, train_distance)  
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

# Get Farenheit 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp
f100_in_celsius = f_to_c(100)
print(f"100 degrees Fahrenheit is {f100_in_celsius} degrees Celsius.")

# Get Celsius
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(f"0 degrees Celsius is {c0_in_fahrenheit} degrees Fahrenheit.")