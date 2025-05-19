import sys
def check_age(age):
  return int(age) > 18

if __name__ == "__main__":
  name = sys.argv[1]
  age = sys.argv[2]
  country = sys.argv[3]

is_adult = check_age(age)

with open("result.txt", "w")as f:
  f.write(f"{name},{is_adult},{country}")
