# module calculate_store_discount() is where I am having issues. I also tried linking original_price()
# to calculate_store_discount() so I wouldn't have to have the user re-enter. The in_store_discount() 
# and calculate_store_discount() are going to be 'duplicated' with variables relating to the 
# coupon inputs and calculation ( calculate_coupon(), coupon_discount() ). Another module is going to 
# be created to calculate the final price after I figure out what my hang up is with the math. 

# Okay, so this is your `main` function. There's nothing special about it being
# called `main`, it's just done that way by convention since the beginning of
# time. It is your main "driver" for the program as a whole, which you can
# usually just assume, but you can be sure of it by seeing that at the bottom
# you have a line that consists only of `main()`. This is syntax for a function
# call. You'll also see something like the following in a lot of Python
# scripts:
# if __name__ == '__main__':
#   main()
# You can find out more here:
# http://stackoverflow.com/questions/419163/what-does-if-name-main-do

# Anyway, the Python interpreter (which is called "Python", but it's distinct
# from the language "Python" itself) will read your file and execute everything
# line by line, in order. This line defines a function called "main" and
# then actually skips over the rest of the definition, which is denoted by
# the indentation. So now Python knows there is a function called "main"
# accessible later in your program that does something (it doesn't know what
# just yet).
# Skip over to the next definitions until you get to the last line of the
# program, which calls `main`.
def main():
	# So now we're back here from the last line of the file. We're creating a
	# local variable called `welcome`, calling `welcome_message`, and assigning
	# the return value of `welcome_message` to the local variable `welcome`.
    welcome = welcome_message() # Once Python reads `welcome_message()`, it
								# jumps to the line immediately after
								# `def welcome_message():`. Go there now.
	# After we get back from calling `welcome_message`, we'll be here. We're
	# doing something similar - creating a local variable `store_discount`,
	# calling the `in_store_discount` function, and assigning the return value
	# of it to `store_discount`.
    store_discount = in_store_discount() # Now jump to the line immediately
										 # after `def in_store_discount()`.
										 
	# We've made it all the way back here! Now we're done in this function
	# and go back to the caller, which is the last line of the file.
	
# Immediately after line 28 (`def main():`), we just skip all the way down here
# to the next definition. It defines a function called `welcome_message`.
def welcome_message():
	# Now we're here. We're going to call `print "Hello! ..." and print out the
	# desired messages line by line. Great!
    print  "Hello! Calculate the final price of an item with an in-store sale and "
    print  "a coupon if they are available. First input the original price (ex. 1.00) "
    print  " follwed by the in-store discount (ex. .20), and the coupon amount. "
	# Now we're at the end of `welcome_message`. We will now jump back to line
	# 32 and assign the return value of this function to `main`s local
	# `welcome` variable (declared on line 32). However, this function doesn't
	# actually have a return value (technically all functions do - if one isn't
	# specified then functions return a special value called `None`). This
	# basically means that line 32 can just be `welcome_message()` rather than
	# `welcome = welcome_message()`. The variable `welcome` is assigned `None`
	# and never used, so we don't need it.
	# Now jump back to line 35.

# Next we skip here, define `original_item_price`.
def original_item_price():
	# Now we're here from `in_store_discount`. We're creating a new local
	# variable called `original_price` and assigning the value `0.0` to it.
    original_price = 0.0
	# Now we're calling the function `input` which takes a string, prints it
	# to the screen, and accepts input from the user. Then we pass whatever the
	# user input to the function `float` which takes whatever and tries to
	# convert it to a floating point number. Then whatever `float` returns will
	# be assigned to `original_price`.
    original_price = float(input("What is the original price of the item?"))

	# Now we return `original_price`. This means that the value of
	# `original_price` will be available to whatever called
	# `original_item_price`. Great!
    return original_price
	# Now we return back to the caller in `in_store_discount`.

# Ditto, `in_store_discount`.
def in_store_discount():
	# Now we're here from `main`. We're creating three local variables,
	# `store_discount_choice`, `original_price`, and
	# `store_discount_percentage`, and assigning `0.0` to each of them.
    store_discount_choice = 0.0
    original_price = 0.0
    store_discount_percentage = 0.0

	# Now we're going to call `original_item_price()` and assign the value
	# returned by that function to `orig_price`.
	# NOTE: The variable here is called `orig_price`, which is a new local
	# variable being created right now. Python will just create a new variable
	# if you use one that doesn't exist, which can lead to confusing
	# situations.
    orig_price = original_item_price() # Jump to the line immediately after
									   # `def original_item_price():`.
	# We've just come back from `original_item_price` and assign the return
	# value to `orig_price`. What this means in human-terms is that the user
	# has been asked what the original price of the item was, they put in a
	# number (hopefully), and now the local variable `orig_price` knows that
	# number.

	# Now we're prompting the user for input again in the same way as in
	# `original_item_price()`. The only difference is what we do with the value
	# that `input` returns - in this case we convert it to an integer with the
	# `int` function rather than converting it to a floating point number with
	# `float`. Great. Then we assign that value to `store_discount_choice`.
    store_discount_choice = int(input("Is there an in-store discount? Enter 1 for Yes, 2 for No."))

	# Now we compare `store_discount_choice` with the integer `1`. If they are
	# equal, we call `calculate_store_discount()`.
	# This is a "branch", which means that there are now two different code
	# paths that can be followed, depending upon the value of
	# `store_discount_choice`. You can go to either function definition below.
	# I'll assume both happen (which is impossible in a single run, but we'll
	# assume the user runs the program twice).
    if store_discount_choice == 1:
        calculate_store_discount() # If they entered "1", jump to the line
								   # immediately after
								   # `def calculate_store_discount():`
	# We're now done with the call, which will end up being the last thing this
	# function does. We would now jump back to the caller of this function,
	# which is line 39 in the function `main`.
	
	# Otherwise, if `store_discount_choice` equals `2`, we call
	# `original_price_remains` (which doesn't actually exist).
    elif store_discount_choice == 2:
        original_price_remains() # If this function existed, you would jump to
								 # it's definition.

# Finally, define `calculate_store_discount`.
def calculate_store_discount():
	# If the user entered "1", we'll be here. We create four local variables,
	# `original_price`, `in_store_discount`, `discount_amount`, and
	# `final_store_discount`. We assign the value `0.0` to all of them.
    original_price = 0.0
    in_store_discount = 0.0
    discount_amount = 0.0
    final_store_discount = 0.0 

	# Here we are asking the user to re-enter the original price. We actually
	# don't need to do this, because we already asked! In `in_store_discount`,
	# we have a variable with the value they input. We can use this for
	# whatever we want. The most common (and best) way to have functions work
	# with each other is to pass values to functions using parameters. You'll
	# need to do this if you want to have multiple functions doing the work
	# (which you do!). You're already using this functionality in your calls to
	# `input()`. You're passing a value (in all these cases, a string) to
	# `input()`, which returns a value (which is whatever the user entered),
	# which is then passed to the function `int()` which THEN returns a value
	# which is assigned to the variable `original_price`, in this case. You can
	# use this for whatever, like passing it to functions.
    original_price = int(input("Re-Enter the original price."))

	# Now we do a similar thing to what you did above with `original_price`.
	# One important thing to note is that, based on the usage, you're expecting
	# a floating point number (e.g., .2), but you're passing whatever the user
	# inputs to the `int` function, which converts things to integers (whole
	# numbers). What this means is that it will take something that looks like
	# a number and convert it to a whole number based on a few rules. The most
	# relevant one for your situation right now is that floating point to
	# integer conversions truncate. So 0.2 turns to 0, 0.8 turns to 0, 1.4
	# turns to 1, 1234.56789 turns to 1234 - it will simply cut off everything
	# after the decimal point and doesn't bother rounding. 0.999999 -> 0.
	# This is the main issue you're experiencing. By changing the call from
	# `int` to `float` (i.e., `float(input("..."))`), you'll get the output you
	# expect.
    in_store_discount = int(input("What is the in_store discount? (ex. .20)"))

	# We now calculate some values and assign them to variables. These work as
	# expected.
    discount_amount = original_price * in_store_discount
    final_store_discount = original_price - discount_amount

	# Finally, print out the information to the user.
    print "The in_store savings amount is ", discount_amount
    print "Your new price is ", final_store_discount
	
	# Again, here we implicitly return `None` and would jump back to the caller
	# (line 119).

# Now we're here. We've defined five functions, `main`, `welcome_message`,
# `original_item_price`, `in_store_discount`, and `calculate_store_discount`.
# The next line, `main()` will call the function `main()`. So execution now
# jumps back up to the line immediately after `def main():`.
main()

# Finally we've finished main, we reach the end of the file, and the Python
# intepreter says "I'm done!" and the program is over.