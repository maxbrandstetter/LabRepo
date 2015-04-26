from behave import given, when, then

from source.BDD_Source import Calculator

@Given('the user is researching speeds')
def step_impl(context):
    context.calc = Calculator()

@When('a file name is entered')
def step_impl(context):
    context.calc.read_file(filename='source/Test.txt')

@Then('the cities, distances, and speeds will be read')
def step_impl(context):
    assert context.calc.readSuccess is True

@When('an estimated speed is entered')
def step_impl(context):
    assert context.calc.get_speed() == 60

@When('a hard drive size is entered')
def step_impl(context):
    assert context.calc.get_size() == 1000

@When('a city is entered')
def step_impl(context):
    assert context.calc.get_city() == 'Portland'

@Then('the user can see which would be faster')
def step_impl(context):
    assert context.calc.compare_speeds() == 'Hard Drive'

@Then('the user can see the time difference')
def step_impl(context):
    assert context.calc.get_time_difference() == 5900
