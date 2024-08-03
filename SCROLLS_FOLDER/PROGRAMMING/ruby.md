<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\ruby.md -->




[Home](/index.html)

# Introduction to Ruby

## Resources

-[Official Ruby Documentation](https://www.ruby-lang.org/en/documentation/)
- [RubyGems](https://rubygems.org/)

## What is Ruby?

Ruby is a dynamic, open-source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.

Ruby was created by Yukihiro "Matz" Matsumoto, and it blends parts of his favorite languages (Perl, Smalltalk, Eiffel, Ada, and Lisp) to form a new language that balances functional programming with imperative programming.

## Why Use Ruby?

- **Ease of Use**: Ruby has a clean and readable syntax that makes it easy to understand and write.
- **Productivity**: Ruby allows for rapid development, making it a favorite among developers for prototyping and building applications quickly.
- **Community and Libraries**: A large community and a rich set of libraries (gems) make Ruby a versatile language for various applications, including web development (Ruby on Rails), data analysis, and automation.

## Installing Ruby

To start using Ruby, you need to install it on your machine. The recommended way to install Ruby is by using a version manager like `rbenv` or `RVM`.

### Using `rbenv`

1. **Install `rbenv`**:
    ```bash
    curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash
    ```

2. **Add `rbenv` to your shell**:
    ```bash
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    ```

3. **Install Ruby**:
    ```bash
    rbenv install 3.1.0
    rbenv global 3.1.0
    ```

4. **Verify the installation**:
    ```bash
    ruby -v
    ```

## Writing Your First Ruby Program

Let's write a simple Ruby program to get started.

Create a file named `hello.rb` and add the following code:

```ruby
puts 'Hello, World!'
```

To run the program, open your terminal and execute:
```bash
ruby hello.rb
```

You should see the output:
```bash
Hello, World!
```

## Basic Syntax

### Comments

Comments are ignored by the Ruby interpreter and are used to document the code.

```ruby
# This is a single-line comment

=begin
This is a
multi-line comment
=end
```

### Variables

Variables are used to store data. Ruby is dynamically typed, so you don't need to declare the type of a variable.

```ruby
name = 'Alice'
age = 25
```

### Data Types

Ruby supports several data types, including:

- Numbers: Integers and floating-point numbers
- Strings: Sequences of characters
- Arrays: Ordered collections of items
- Hashes: Key-value pairs

```ruby
# Number
num = 42

# String
greeting = "Hello, Ruby!"

# Array
colors = ['red', 'green', 'blue']

# Hash
person = { name: 'Alice', age: 25 }
```

## Control Structures

### Conditional Statements

```ruby
if age >= 18
  puts "You're an adult."
else
  puts "You're a minor."
end
```

### Loops

```ruby
# While loop
i = 0
while i < 5
  puts i
  i += 1
end

# Each loop (iterating over an array)
colors.each do |color|
  puts color
end
```

## Methods

Methods are used to encapsulate code into reusable blocks

```ruby
def greet(name)
  "Hello, #{name}!"
end

puts greet('Alice')
```

## Classes and Objects

Ruby is an object-oriented language. You can define classes and create objects.

```ruby
class Person
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def introduce
    "Hi, I'm #{@name} and I'm #{@age} years old."
  end
end

person = Person.new('Alice', 25)
puts person.introduce
```

## Exception Handling

Exceptions are used to handle errors gracefully.

```ruby
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: #{e.message}"
end
```

