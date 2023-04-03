
import json
import math

from bokeh.plotting import figure, show, output_file
from collections import Counter
from typing import NoReturn

DATA_FILE = "birthdays.json"
OUTPUT_FILE = "plot.html"
# some examples
"""
birthdays = {
  'Albert Einstein': '14 March 1879',
  'Marie Curie': '7 November 1867',
  'Pierre Curie': '15 May 1859',
  'Charlie Chaplin': '16 April 1889',
  'Franklin D. Roosevelt': '30 January 1882'
  "Pablo Picasso": "25 October 1881"
  "Francisco Goya": "30 March 1746"
}
"""

class BirthdaysDict:

  birthdays = {}
  with open(DATA_FILE, "r") as f:
    birthdays = json.load(f)

  def get_switches(self) -> NoReturn :
    while True:
      option = input(
          "What do you want to do next? you can: [A]dd, [F]ind, [L]ist, [Q]uit, [D]raw a plot\n").lower()
      match option:
        case 'a':
          self.add_entry()
          self.convert_to_readable()
        case 'f':
          self.find_entry()
        case 'l':
          self.list_entries()
        case 'd':
          self.create_plot()
        case 'q':
          break
        case _:
          print("The input is invalid.")
          break

  def list_entries(self) -> NoReturn :
    print("We have the following birthdays in our dictionary:")
    for name_dict in self.birthdays:
      print(name_dict)

  def find_entry(self) -> NoReturn :
    name = input("Who's birthday do you want to look up?\n")
    if name in self.birthdays:
      print("{}'s birthday is {}.".format(name, self.birthdays[name]))
    else:
      print("We don't have the name {} in our dictionary.".format(name))

  def add_entry(self) -> NoReturn :
    name = input("Wo's birthday do you wand to add to the dictionary?\n").title()
    birthday = input("Enter the birthday\n")
    self.birthdays[name] = birthday
    with open('birthdays.json', 'w') as filename:
      json.dump(self.birthdays, filename)

    print('{} was added to our birthday dictionary'.format(name))

  def convert_to_readable(self) :
    result = "[\n"
    add_comma = False
    for key, value in self.birthdays.items() :
      if add_comma :
        result += ",\n"

      result += "  {\n"
      result += "    \"{}\": \"{}\",\n".format(key, value)
      result += "  }"
      add_comma = True
    result += "\n]"

  # a piece of code for debugging
    with open('birthdays_readable_json.json', 'w') as filename:
      filename.write(result)

  def count_months(self) -> dict :
    result = []
    for name, birthday in self.birthdays.items():
      month = birthday.split(" ")[1]
      result.append(month)

    return Counter(result)

  def create_plot(self) -> NoReturn :
    x_months = ["January", "February", "March", "April", "May", "June",\
      "July", "August", "September", "October", "November", "December"]
    json_data = self.count_months()
    x = list(json_data.keys())
    y = list(json_data.values())

    output_file(OUTPUT_FILE)
    plot_months = figure(title = "Simple Bar Chart", x_axis_label='Months',
                  y_axis_label='Amount', x_range = x_months)
    plot_months.xaxis.major_label_orientation = math.pi/4
    plot_months.vbar(x = x, top = y, width = 0.9)
    show(plot_months)
