from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, Recipe, bcrypt, User
import os
from forms import LoginForm, SignupForm

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt.init_app(app)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the database
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print(f"Error initializing database: {e}")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except Exception as e:
        print(f"Error loading user: {e}")
        return None

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    try:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
            # Add user to the database
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
    except Exception as e:
        flash(f"An error occurred: {e}", 'danger')
    
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            # Fetch user from the database
            user = User.query.filter_by(email=email).first()

            # Check user existence and password validity
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                session['user_id'] = user.id  # Store user ID in session
                session['username'] = user.username  # Store username in session
                flash('Login successful! Welcome back.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
    except Exception as e:
        flash(f"Error during login: {e}", 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    try:
        logout_user()
        session.pop('user_id', None)  # Remove user_id from session
        session.pop('username', None)  # Remove username from session
        flash('You have been logged out.', 'info')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Error during logout: {e}", 'danger')
        return redirect(url_for('index'))

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('You need to log in to view your profile.', 'danger')
        return redirect(url_for('login'))

    # Fetch user details from the database
    user = User.query.get(user_id)
    if not user:
        flash('User not found. Please log in again.', 'danger')
        return redirect(url_for('logout'))

    return render_template('profile.html', user=user)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading index page: {e}"
    
@app.route("/recipes")
def recipes():
    all_recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=all_recipes)


@app.route('/search', methods=['POST'])
def search():
    try:
        user_ingredients = request.form.get('ingredients').split(',')
        user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients]

        recipes = Recipe.query.all()
        matching_recipes = []

        for recipe in recipes:
            recipe_ingredients = [ingredient.strip().lower() for ingredient in recipe.ingredients.split(',')]
            if set(user_ingredients).issubset(recipe_ingredients):
                matching_recipes.append(recipe)
            print(f"Recipe: {recipe.name}, Image URL: {recipe.image_url}")

        return render_template('results.html', recipes=matching_recipes)
    except Exception as e:
        return f"Error during search: {e}"
    

@app.route('/search_by_name', methods=['POST'])
def search_by_name():
    try:
        recipe_name = request.form.get('recipe_name', '').strip().lower()
        if recipe_name:
            # Fetch recipes matching the name
            matching_recipes = Recipe.query.filter(Recipe.name.ilike(f"%{recipe_name}%")).all()
            if matching_recipes:
                flash(f"Found {len(matching_recipes)} recipes matching '{recipe_name}'", 'success')
            else:
                flash(f"No recipes found matching '{recipe_name}'", 'info')
        else:
            matching_recipes = []
            flash("Please enter a recipe name to search.", 'warning')
        
        return render_template('results.html', recipes=matching_recipes)
    except Exception as e:
        flash(f"Error searching for recipes: {e}", 'danger')
        return redirect(url_for('index'))
        

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    try:
        if request.method == 'POST':
            name = request.form['name']
            cuisine = request.form['cuisine']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            prep_time = request.form['prep_time']

            file = request.files['image']
            if file and file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                image_url = file.filename
            else:
                image_url = None

            new_recipe = Recipe(
                name=name,
                cuisine=cuisine,
                ingredients=ingredients,
                instructions=instructions,
                prep_time=prep_time,
                image_url=image_url
            )
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added successfully!', 'success')
            return redirect(url_for('index'))

    except Exception as e:
        flash(f"Error adding recipe: {e}", 'danger')
    return render_template('add.html')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error running the app: {e}")
