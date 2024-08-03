<!-- C:\Users\razer\Desktop\walkerrh.github.io\SCROLLS_FOLDER\PROGRAMMING\rails_notes.md -->




[Home](/index.html)

rails server

### rails generate controller Home index

```sh
unix_wrh@LAPTOP-R8L6DPA5:~/myapp$ rails generate controller Home index
      create  app/controllers/home_controller.rb
       route  get 'home/index'
      invoke  erb
      create    app/views/home
      create    app/views/home/index.html.erb
      invoke  test_unit
      create    test/controllers/home_controller_test.rb
      invoke  helper
      create    app/helpers/home_helper.rb
      invoke    test_unit
```

### config/routes.rb

```rb
Rails.application.routes.draw do
  root 'home#index'
end
```

### app/views/home/index.html.erb

```html
<h1>Welcome to MyApp!</h1>
<p>Your Rails application is working!</p>
```

```sh
rails new blog
```


rails restart
rails --tasks
rails server


5. Check Routes
Ensure that you have a valid route defined for the root path ("/"). You can check your routes by running:
bin/rails routes

6. Application Logs
Check the application logs for any runtime errors. Logs can be found in log/development.log.


find . -type f -name '*_*' -print0 | xargs -0 grep -H "turbo-progress-bar"

cd /path/to/your/project
grep -r "turbo-progress-bar" .

### To show the line numbers where the phrase is found, use the -n option:
grep -rn "turbo-progress-bar" .
### To ignore case (case-insensitive search), use the -i option:
grep -ri "turbo-progress-bar" .
### If you want a count of the number of matches in each file, use the -c option:
grep -rc "turbo-progress-bar" .

grep -rl "dom_id" .




| Method | Description | Example |
| --- | ---| --- |
| `has_many` | Establishes a one-to-many relationship between models. | `has_many :posts` |
| `belongs_to` | Establishes a one-to-one connection with another model. | `belongs_to :user` |
| `validates` | Adds validations to ensure data integrity. | `validates :email, presence: true, uniqueness: true` |
| `before_validation`| A callback that runs custom code before validations are executed. | `before_validation :normalize_name` |
| `dependent` | Specifies what should happen to associated objects when the owner is destroyed. | `has_many :posts, dependent: :destroy` |

```ruby
class User < ApplicationRecord
  has_many :posts, dependent: :destroy

  validates :email, presence: true, uniqueness: true
  validates :name, presence: true

  before_validation :normalize_name

  private

  def normalize_name
    self.name = name.downcase.titleize
  end
end

class Post < ApplicationRecord
  belongs_to :user

  validates :title, presence: true
  validates :content, presence: true
end
```

ActiveRecord is designed to handle all of an application's tasks that relate to the database, including:
* establishing a connection to the database server
* retrieving data from a table
* storing new data in the database.





### In Rails, whether to create a new view or a partial depends on the use case:
* New View: Create a new view if the content is meant to be a standalone page, typically rendered via a controller action. This is suitable for full pages that are part of your application's main navigation, such as "About Us", "Contact", or a specific resource page.
* Partial: Create a partial if the content is reusable across different views or is a component of a larger view. Partials are useful for repeated UI elements like headers, footers, forms, or widgets that you want to include in multiple places.