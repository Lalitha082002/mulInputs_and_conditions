def test_check_result():
  with open("result.txt", "r") as f:
    name, is_adult, country = f.read().strip().split(",")
  assert is_adult == "True", f"{name} is not an adult"
