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

@When('a preset is entered')
def step_impl(context):
    context.calc.use_preset(preset='Ferrari')

@Then('preset values replace current values')
def step_impl(context):
    assert context.calc.speed == 100

@When('a new city is entered')
def step_impl(context):
    assert context.calc.get_city('Test Input', city_distance=200) == 'Test Input'

@Then('write the data to a file')
def step_impl(context):
    assert context.calc.write_to_file() is True

@When('a new route is entered')
def step_impl(context):
    context.calc.create_route()

@Then('return total distance')
def step_impl(context):
    assert context.calc.route_distance == 150

@When('a starting city is entered')
def step_impl(context):
    context.calc.get_city('Salem')

@Then('store that city')
def step_impl(context):
    assert context.calc.city_name == 'Salem'

@When('an expected latency is entered')
def step_impl(context):
    context.calc.get_latency()

@Then('needed values are changed')
def step_impl(context):
    assert context.calc.latency == 2

@Then('get drive speed')
def step_impl(context):
    assert context.calc.drive_speed == 3