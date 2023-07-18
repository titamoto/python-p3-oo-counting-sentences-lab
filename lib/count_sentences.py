
class MyString:
  def __init__(self, value=None):
    if type(value) != str:
      print("The value must be a string.")
      self.value = ""
    else:
      self.value = value
  
  def is_sentence(self):
    if self.value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else:
      return False
    
  def count_sentences(self):
    if self.value == "":
      return 0
    else:
      calm_down = self.value.replace("...", ".").replace("!", ".").replace("!!", ".").replace("?", ".").replace("??", ".")
      return calm_down.count(". ") + 1