from models import db, Recipe 
from app import app 
 
with app.app_context(): 
    recipes = [ 
        Recipe( 
            name="Tomato Soup", 
            cuisine="American", 
            ingredients="tomato, onion, garlic, butter,pepper", 
            instructions="1. Saute onions and garlic in butter. 2. Add tomatoes and simmer. 3. Blend and serve.", 
            prep_time="30 min", 
            image_url="Tomato Soup.jpg" 
        ), 
        Recipe( 
            name="Garlic BreaUradd", 
            cuisine="Italian", 
            ingredients="bread, garlic, butter, parsley", 
            instructions="1. Spread garlic butter on bread. \n 2. Bake until golden brown. \n 3. Garnish with parsley.", 
            prep_time="15 min", 
            image_url="Garlic Bread.jpg" 
 
 
        ), 
        Recipe( 
            name="Baby Corn Chili", 
            cuisine="Indo-Chinese", 
            ingredients="Baby corn,Bell peppers,Onion,Ginger,Soy sauce,Vinegar,Red chili sauce,Corn flour,Pepper", 
            instructions="Prepare the Vegetables: Heat oil in a wok and sauté the baby corn, bell peppers, onion, garlic, and ginger until softened. Add the Sauce: Add soy sauce, vinegar, red chili sauce, corn flour slurry, salt, and pepper to the wok. Stir well to combine.Cook the Chili: Cook the mixture until the sauce thickens and coats the vegetables.Serve: Serve hot with steamed rice or noodles.Enjoy your spicy and flavorful baby corn chili!", 
            prep_time="15 min", 
            image_url="Baby Corn Chili.jpg" 
             
 
        ), 
        Recipe( 
            name="Idli", 
            cuisine="South Indian", 
            ingredients="Urad dal,Rice,Fenugreek seeds,", 
            instructions="1.Soak the Ingredients:Wash and soak urad dal and rice separately in water for 4-5 hours.2. Grind the Batter: 3.Drain the soaked ingredients and grind them into a smooth batter.4. Add fenugreek seeds and salt.5.Ferment the Batter: Cover the batter and let it ferment for 8-10 hours in a warm place.6. Steam the Idlis:7. Grease idli molds with oil. 8. Pour the fermented batter into the molds.9.Steam: Steam the idlis for 10-12 minutes, or until they are cooked through.10.Serve hot with sambar and coconut chutney", 
            prep_time="30 min", 
            image_url="Idli.jpg" 
        ), 
        Recipe( 
            name="Omelette", 
            cuisine="American", 
            ingredients="2 eggs,Pepper,oil", 
            instructions="1.Whisk eggs,salt and pepper.2. Melt butter in a pan.3. Pour egg mixture, cook until set.4. Add fillings, fold, and cook.5. Serve hot.", 
            prep_time="10 min", 
            image_url="Omelette" 
        ), 
        Recipe( 
            name="Pasta", 
            cuisine="Italian", 
            ingredients="Pasta, Olive oil, Garlic,Red pepper flakes,Pepper", 
            instructions=" 1. Cook pasta according to package directions.2. Heat olive oil in a pan.3. Add garlic and red pepper flakes, cook until fragrant.4. Drain pasta and add to the pan.5. Add your chosen sauce and toss to coat.6. Serve hot with grated Parmesan cheese.", 
            prep_time="15 min", 
            image_url="Pasta" 
        ), 
        Recipe( 
            name="Halwa", 
            cuisine="Indian", 
            ingredients="Sooji,Ghee,Milk,Cardamom powder,Nuts", 
            instructions="1. Heat ghee in a pan.2. Add semolina and roast until golden brown.3. Add milk gradually, stirring continuously.4. Add sugar and cardamom powder, cook until the mixture thickens.5. Add nuts and cook for a few more minutes.6. Serve hot or cold.", 
            prep_time="30 min", 
            image_url="Halwa" 
        ), 
        Recipe( 
            name="French Fries", 
            cuisine="American", 
            ingredients="4 large potatoes,1/2 teaspoon black pepper,Oil for frying", 
            instructions="1.Cut potatoes into strips.2.Rinse and dry.3.Season with salt and pepper.4.Fry in hot oil until golden brown.5.Drain on paper towels.6.Serve hot with ketchup.", 
            prep_time="10 min", 
            image_url="FrenchFries" 
        ), 
        Recipe( 
            name="Egg Toast", 
            cuisine="American", 
            ingredients="2 slices bread,2 eggs,1/4 teaspoon black pepper,1 tablespoon butter", 
            instructions="1. Whisk the eggs, salt, and pepper together.2. Heat the butter in a skillet over medium heat.3. Dip the bread slices in the egg mixture, coating both sides.4. Place the bread slices in the skillet and cook until golden brown on both sides.5. Serve hot with your favorite toppings, such as butter, jam, or honey.", 
            prep_time="5 min", 
            image_url="Egg Toast" 
        ), 
        Recipe( 
            name="French Toast", 
            cuisine="American", 
            ingredients="2 slices bread,2 eggs,1/4 cup milk,1/4 teaspoon cinnamon,1 tablespoon butter", 
            instructions="1. Whisk together the eggs, milk, salt, and cinnamon.2. Dip the bread slices in the egg mixture, coating both sides.3. Heat the butter in a skillet over medium heat.4. Cook the bread slices until golden brown on both sides.5. Serve hot with syrup, powdered sugar, or fresh fruit.", 
            prep_time="5 min",  
            image_url="French Toast" 
        ), 
        Recipe( 
            name="Masala Dosa", 
            cuisine="South Indian", 
            ingredients="dal,Idli rice,Fenugreek seeds,Potato,Onion,Green chili,Ginger,Cumin seeds,Turmeric powder,Red chili powder,Garam masala,Oil", 
            instructions="1. Soak urad dal, idli rice, and fenugreek seeds overnight.2. Grind into a batter.3. Make dosa on a tawa.4. Sauté masala ingredients.5. Add mashed potato.6. Fill dosa with masala.7. Serve hot with sambar and chutney.", 
            prep_time="30 min", 
            image_url="Masala Dosa" 
        ), 
        Recipe( 
            name="Besan Chilla", 
            cuisine="Indian", 
            ingredients="Besan,Turmeric powder,Red chili powder,Cumin seeds,Baking soda,Water,Oil", 
            instructions="1. Mix ingredients into a batter.2. Heat tawa.3. Pour batter, cook until golden brown.4. Serve hot.", 
            prep_time="10 min", 
            image_url="Besan Chilla" 
 
        ), 
        Recipe( 
            name="Chocolate Shake", 
            cuisine="American", 
            ingredients="1 cup milk,1/2 cup chocolate ice cream,1 tablespoon chocolate syrup,1 teaspoon vanilla extract", 
            instructions="1. Blend all ingredients together until smooth.2. Pour into a glass and serve immediately.", 
            prep_time="5 min", 
            image_url="Chocolate Shake" 
        ), 
        Recipe( 
            name="Black Currant Shake", 
            cuisine="American", 
            ingredients="1 cup milk,1/2 cup black currants,1 teaspoon vanilla extract,Ice cubes", 
            instructions="1. Blend all ingredients together until smooth.2. Pour into a glass and serve immediately.", 
            prep_time="5 min", 
            image_url="Black Currant Shake" 
        ), 
        Recipe( 
            name="Poha", 
            cuisine="Indian", 
            ingredients="1 cup poha,1 onion (finely chopped),1 green chili (finely chopped),1 teaspoon cumin seeds,1/2 teaspoon red chili powder,2 tablespoons peanuts (roasted and ground),2 tablespoons coriander leaves (finely chopped),Ghee for tempering.", 
            instructions="1. Wash poha.2. Sauté cumin seeds, green chili, and onion.3. Add turmeric and red chili powder.4. Add poha and peanuts.5. Cook until crisp.6. Serve hot.", 
            prep_time="10 min", 
            image_url="Poha" 
        ) 
    ] 
    



    db.session.add_all(recipes)
    db.session.commit()
    db.session.bulk_save_objects(recipes)
    print("Database populated with recipes and images!")