# Say Media Interview Questions
￼
## Questions

### Prime Numbers

- Write a function to print out the first 100 prime numbers.

### DOM APIs

- Using the DOM APIs, write a routine to change every paragraph in a contenteditable div into a blockquote.

### Finding Pairs

- Write a function:
```findSumPairs(intArr, sumTotal)```
that searches an array of integers (intArr, which could have positive and/or negative values) to find pairs that add up to sumTotal.

Example 1:

```python

findSumPairs([­1, 0, 1, 2], 3) ­> [[1,2]]
findSumPairs([­1, 0, 1, 2], 1) ­> [[­1, 2], [0, 1]]

```

### Object Oriented Programming - Cargo Allocation

- Given the following types of vehicles and their respective capacities:
    1. SportsCar ­ small trunk w/100lb capacity
    2. FamilyCar ­ large trunk w/300lb capacity
    3. Truck ­ 2 doors, bed w/1500lb capacity
    4. MiniVan ­ small rear storage area w/200lb capacity
    5. CargoVan ­ large rear storage area with 800lb capacity

- Write a page/script using object oriented coding style with a text box for each each vehicle type, a text box for the cargo to be allocated, and a calculate button. When the calculate button is clicked a div on the page should have the cargo allocation written to it. Use of utilities like class.js are fine so long as they result in clean and readable js.

Example 1:

```python

INPUT:

    SportsCar: 1
    FamilyCar: 3
    Truck: 4
    MiniVan: 2
    CargoVan: 1
    Cargo: 7356

￼OUTPUT:

    allocating 7356 lbs of cargo
    a SportsCar with 100 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a Truck with 1500 lbs
    a Truck with 1500 lbs
    a Truck with 1500 lbs
    a Truck with 1500 lbs
    a MiniVan with 200 lbs
    a MiniVan with 156 lbs
    a CargoVan with 0 lbs
    we have 0 lbs of cargo left over

```

Example 2:

```python

INPUT:

    SportsCar: 1
    FamilyCar: 6
    Truck: 1
    MiniVan: 2
    CargoVan: 3
    Cargo: 7356

OUTPUT:

    allocating 7356 lbs of cargo
    a SportsCar with 100 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a FamilyCar with 300 lbs
    a Truck with 1500 lbs
    a MiniVan with 200 lbs
    a MiniVan with 200 lbs
    a CargoVan with 800 lbs
    a CargoVan with 800 lbs
    a CargoVan with 800 lbs
    we have 1156 lbs of cargo left over

```

## Cargo Allocation Usage
1. Clone the rpository from [GitHub](https://github.com/rkk09c/TrueCarInterview)
2. Spin up API:
  1. Create Python2.x Environment:
       * Make sure you have Python2.x installed, if not visit [Python installation documentation](https://www.python.org/downloads/) and download the latest version of Python2
       * Naviget to ```SayInterview``` root directory
       * Create a Python2 virtualenv:

           ```
           virtualenv -p path/to/python2.7 env
           ```

       * Start the virtual environment with:

           ```
           source env/bin/activate
           ```

       * Install application requirements to that virtual machine:

           ```
           pip install -r requirements.txt
           ```

   2. Start the application in the foreground as follows:

       ```
       python API/run.py
       ```

3. Spin up the Client:
   1. Make sure appropriate packages are installed:
       * Please see [NPM Download and Instillation Guide](https://nodejs.org) for instillation help with NPM
       * Install Bower:

           ```
           npm install bower #sudo may be necessary depending on environment
           ```

   2. In a new terminal, navigate to ```SayInterview/Client```
   3. Install all NPM dependencies:

       ```
       npm install #sudo may be necessary depending on environment
       ```

   4. Install all Bower dependencies:

       ```
       bower install
       ```

   5. Launch test server:

       ```
       grunt serve
       ```

   6. Local web server is now active, navigate to the website on the test server at ```http://localhost:9000/app/index.html```

## Scripts Usage

1. Activate aforementioned python2 virtualenv.

2. Navigate to '/SayInterview/scripts'

3. Invoke python2 repl
    - Import modules:

      ```python
      from dom_api import change_to_block_quote
      from primes import get_primes, fermat
      from pairs import get_pairs
      ```
    - Usage:

      ```python
      altered_page = change_to_block_quote('local_html_file.html')
      prime_numbers = get_primes()  # change to any amount of primes by passing in int parameter
      mostly_primes = fermat()  # uses fermat's little theorem, very fast, only partly accurate
      pairs = get_pairs([-1, 0, 1, 2], 3)  # can be any integer array and desired output
      ```

## Comments
_ Application was moved over to python2 in order to maintain a uniform version. lxml is partly broken for python3 in the tostring() method.
- Please note that the decision to use a python API as opposed to doing all logic for the object oriented question ins Javascript was done due to python/angular being the stack for Say.
- Please note special instillation instructions for the lxml package at the [lxml documentation page](http://lxml.de/installation.html)
