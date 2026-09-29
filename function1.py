def convert_temperature(value, unit):
      if unit == 'C': 
           return (value * 9/5) + 32
      elif unit == 'F':
            return (value - 32) * 5/9
      else:
            print("Unit harus 'C' atau 'F'")
          
input_value = int(input("Masukkan value: "))
input_unit = input("Masukkan unit (C/F): ")
print(convert_temperature(input_value, input_unit))