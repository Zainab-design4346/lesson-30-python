class overload:
  def __init__(self,var):
    self.var=var
  def __lt__(self,other):
    if self.var<other.var:
      return "ob1 is less than ob2"
    else:
      return "ob2 is less than ob1"
  def __eq__(self, other):
    if self.var==other.var:
      return "both are equal"
    else:
      return "not equal"
    
ob1=overload(45)
ob2=overload(34)
print("passed value ",ob1.var, "and", ob2.var)
print(ob1<ob2)
ob3=overload(45)
ob4=overload(45)
print("passed value ", ob3.var, "and", ob4.var)
print(ob3==ob4)