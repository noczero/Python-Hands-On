def time_convert(num):
  minute = num % 60

  hour = 0
  if num > 60:
    hour = round(num / 60)

  return f"{hour}:{minute}"

print(time_convert(45)) # 0:45
print(time_convert(126)) # 2:6