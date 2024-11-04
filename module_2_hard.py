def generate_password(n):
  """
  Генерирует пароль для заданного числа n.

  Args:
    n: Целое число от 3 до 20.

  Returns:
    Строка с паролем, соответствующим числу n.
  """
  result = ""
  used_pairs = set()  # Множество уже использованных пар чисел
  for i in range(1, n + 1):  # Проверяем пары от 1 до n
    for j in range(i + 1, n + 1):  # Проверяем пары от i+1 до n
      if (i, j) not in used_pairs and (j, i) not in used_pairs:
        if (i + j) % n == 0:  # Проверяем кратность
          result += str(i) + str(j)
          used_pairs.add((i, j))  # Добавляем пару в множество использованных
  return result


# Получаем число от пользователя
n = int(input("Введите число от 3 до 20: "))

# Проверяем, что число находится в допустимом диапазоне
if 3 <= n <= 20:
  # Генерируем пароль
  password = generate_password(n)
  print(f"Пароль для числа {n}: {password}")
else:
  print("Число должно быть от 3 до 20.")




