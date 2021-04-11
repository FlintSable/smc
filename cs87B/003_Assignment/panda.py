import pandas as pd

flavors = pd.DataFrame([
  [1, 'American Dream', 0.5, 4.75],
  [2, 'Karamel Sutra Core', 0.10, 4.25],
  [3, 'Phish Food', 3.00, 5.50],
  [4, 'The Tonight Dough', 2.50, 4.00],
  [5, 'Colin Kaepernicks Change the Whirled', 2.50, 8.00]

],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

flavors['Sold in quart?'] = ['Yes', 'Yes', 'No', 'No', 'Yes']

print(flavors)