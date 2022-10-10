# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print(all(((not (x or y or z)) == (not x and not y and not z))
      for x, y, z in range(2)*3))
