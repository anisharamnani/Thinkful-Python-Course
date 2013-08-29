meal = 20 # base price of the meal 
tax = 0.15 # the tax rate for the meal 
tip = 15 # the tip for the meal 

tax_value = tax * meal # dollar value of the tax for the meal 
meal_with_tax = tax_value + meal # meal before you tip 
tip_value = meal_with_tax * tip / 100 # raw value of the tip 
total = meal_with_tax + tip_value # total cost of the meal 

print "The base cost of the meal was $%r." % meal
print "You need to pay for tax $%r."  % tax_value
print "Tipping at the rate of %r%%, you should leave $%r for a tip." % (tip, tip_value)
print "The grand total of your meal is $%r" % total