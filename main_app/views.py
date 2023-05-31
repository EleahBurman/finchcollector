from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })

# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

finches = [
  Finch('CooCoo', 'Blue Finch', 'Chirpy in the morning', 3),
  Finch('Margaret', 'Star Finch', 'Thinks she is a star', 1),
]