start = 5
end = 300

result = 0
i = start

if i % 2 == 1:
   i += 1
while i <= end:
   result += i
   i  = i + 2
print("RESULT IS: " + str(result))