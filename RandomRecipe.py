'''
Random recipe generator version 1.1 by Imtiaz Ahmed

Version 1.0 Feature:
1. Menu options: Generate a random recipe & Quit
2. Database: Using Dictionary, 7 recipes
3. Takes in user prompt and generates a random recipe
4. Recipe names, ingredients and instructions are tagged with an ID. Random function generates the ID number and the recipe is generated based on the ID.

Version 1.1 Update:
1. Validation - Now rejects characters or symbol entries for menu choice

'''

# Import files
import random
# End - Import files

# Variable & database declarations
userChoice = 0
recipeName = {1: 'Easy Grilled Zucchini',
              2: 'Salsa Chicken',
              3: 'Mushroom Pork Chops',
              4: 'Baked Salmon Fillet Dijon',
              5: 'Pesto Cheesy Chicken Rolls',
              6: 'Kielbasa with Peppers and Potatoes',
              7: 'Easy bake fish'}
recipeIngredients = {1: 'Olive Oil, Grill seasoning, Zucchini',
                     2: 'Chicken, taco seasoning, salsa, chedder cheese, sour cream',
                     3: 'Pork chops, salt and pepper, garlic salt, onion, fresh mushrooms, cream of mushroom soup',
                     4: 'Fillets salmon, dijon style mustard, salt and pepper, dry bread crumbs, butter, melted',
                     5: 'Skinless boneless chicken breasts, prepared basil pesto, mozzarella cheese',
                     6: 'Vegitable oil, Package smoked kielbasa sausage diced, diced red potatoes, sliced red bell peppers, sliced yellow bell pepper',
                     7: 'Honey, Dijon mustard, lemon juice, salmon steaks, pepper'}
recipeInstructions = {1: 'Preheat grill for medium heat and lightly oil the grate. Drizle zucchini slices on both sides with olive oil and season with grill seasoning. Grill zucchinis on preheated grill until tender, 3/4 minutes per side.',
                      2: 'Preheat oven to 375 degrees. Place chicken breasts in lightly greased baking dish. Sprinkle taco seasoning on both sides. Bake at 375  degrees F for 25-35 minutes. Sprinkle chicken evenly with cheese and continue baking for another 3-5 minutes',
                      3: 'Season pork chops with salt, pepper and garlic salt to taste. In a large skillet, brown the chops over medium-high heat. Add the onion and mushrooms, and saute for one minute. Pour cream of mushroom soup over chops. Cover skillet, and reduce temperature to medium-low. Simmer 20 to 30 minutes, or until chops are cooked through.',
                      4: 'Preheat oven to 400 degrees F. Place salmon skin-side down. Spread a thin layer of mustard on the top of each fillet and season with salt and pepper. Top with bread crubms. Bake in a preheated oven for 15 minutes',
                      5: 'Preheat oven to 350 degrees F. Spread 2-3 tablespoons of the pesto sauce onto each flattened chicken breast. Place one slice of cheese over the pesto. Roll up tightly and secure with toothpics. Bake uncovered for 45-50 minutes in the oven.',
                      6: 'Heat the oil in sauce-pan over medium heat. Place kielbasa and potatoes in the saucepan. Cover and cook 25 minutes, stirring occasionally, until potatoes are tender. Mix red and yellow bell pepper into the saucepan and continue cooking 5 minutes, until peppers are just tender',
                      7: 'Preheat oven 325 degrees F. Ina  small bowl, mix honey, mustard and lemon juice. Spread the mixture over the salmon steaks. Season with pepper. Arrange in baking dish. Bake 20 minutes in the oven.'}
# End variable & database declarations

# Welcome text
print('---------------------------------------------------')
print('             Welcome to Random Recipe!             ')
print('---------------------------------------------------')
# End welcome text

# Start program
while userChoice != 2:
    print('Menu:')
    print('1. Generate a random recipe')
    print('2. Quit')

    # Validation
    try:
        userChoice = int(input('Enter your choice and hit enter: '))
        if userChoice < 1 or userChoice > 2:
            print('Wrong choice. Please try again')
    except ValueError:
        print('Wrong choice. Please try again')
    # End validation

    # Generating recipe
    if userChoice == 1:
        # Generating a random number to be used as an index
        randomNumber = random.randint(1,7)
        # Generating a random number to be used as an index

        # Printing random recipe
        print('Name:' + recipeName[randomNumber])
        print('Ingredients required: ' + recipeIngredients[randomNumber])
        print('Instructions: ' + recipeInstructions[randomNumber])
        # End printing random recipe

    # End generating recipe

# End program
