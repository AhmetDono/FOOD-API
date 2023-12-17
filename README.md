# FOOD API

## Important
Create/Add, Delete and Update apis do not make any changes to the database.They just return data.

## How to

You can fetch data with any kind of methods you know(fetch API, Axios, jquery ajax,...)

## Web Scraping/Data
I got the data from a website using Web Scraping

### Get all foods

```js
fetch("https://food-api-9dpr.onrender.com/api/recipes/:id")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Get a single food

```js
fetch("https://food-api-9dpr.onrender.com/api/recipes")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Add new Food

```js
fetch("https://food-api-9dpr.onrender.com/api/recipes", {
  method: "POST",
  body: JSON.stringify({
    "title": "Rich Almond Milk Eggnog",
    "description": "This rich almond milk eggnog is dairy-free, and suitable for anyone who is lactose intolerant or just prefers plant-based milks. Its richness comes from the addition of a duck egg, and it has a thinner texture than commercial eggnog. ",
    "ingredientsInTheRepice": [
        {
            "fullDescription": "1 duck egg",
            "ingredients": {
                "name": "duck egg",
                "image": "ImgURL"
            },
            "measure": {
                "amount": "1",
                "unitOfMeasure": "piece"
            }
        },
        {
            "fullDescription": "1 cup vanilla almond milk",
            "ingredients": {
                "name": "almond mil",
                "image": "ImgURL"
            },
            "measure": {
                "amount": "1",
                "unitOfMeasure": "cup"
            }
        }
    ],
      "materials":[
          {
              "material":{
                  "name":"Cup",
                  "image":"ImgURL"
              }
          }
      ],
    "preparationTime": 20,
    "vegan": false,
    "vegetarian": false,
    "glutenFree": false,
    "ketogenic": false,
    "vitamins":[
            {
                "vitamin":{
                    "name":"A",
                    "description":"Vitamin A (retinol, retinoic acid) is a nutrient important to vision, growth, cell division, reproduction and immunity. Vitamin A also has antioxidant properties."
                }
            }
        ],
    "calories": 185.0,
    "fat": 9.0,
    "carb": 16.0,
    "protein": 8.0,
    "image":"Default Image"
}),
})
  .then((res) => res.json())
  .then((json) => console.log(json));

/* will return
{
    "title": "Rich Almond Milk Eggnog",
    "image": "Default Image",
    "ingredientsInTheRepice": [
        {
            "fullDescription": "1 duck egg",
            "ingredients": {
                "name": "duck egg",
                "image": "ImgURL"
            }
    ],
    ...
}
*/
```
### Updating a product

```js
fetch("https://food-api-9dpr.onrender.com/api/recipes/:id", {
  method: "PUT",
  body: JSON.stringify({
    "title": "Rich Almond Milk Eggnog",
    "description": "This rich almond milk eggnog is dairy-free, and suitable for anyone who is lactose intolerant or just prefers plant-based milks. Its richness comes from the addition of a duck egg, and it has a thinner texture than commercial eggnog. ",
    "ingredientsInTheRepice": [
        {
            "fullDescription": "1 duck egg",
            "ingredients": {
                "name": "duck egg",
                "image": "ImgURL"
            },
            "measure": {
                "amount": "1",
                "unitOfMeasure": "piece"
            }
        },
        {
            "fullDescription": "1 cup vanilla almond milk",
            "ingredients": {
                "name": "almond mil",
                "image": "ImgURL"
            },
            "measure": {
                "amount": "1",
                "unitOfMeasure": "cup"
            }
        }
    ],
      "materials":[
          {
              "material":{
                  "name":"Cup",
                  "image":"ImgURL"
              }
          }
      ],
    "preparationTime": 20,
    "vegan": false,
    "vegetarian": false,
    "glutenFree": false,
    "ketogenic": false,
    "vitamins":[
            {
                "vitamin":{
                    "name":"A",
                    "description":"Vitamin A (retinol, retinoic acid) is a nutrient important to vision, growth, cell division, reproduction and immunity. Vitamin A also has antioxidant properties."
                }
            }
        ],
    "calories": 185.0,
    "fat": 9.0,
    "carb": 16.0,
    "protein": 8.0,
    "image":"Default Image"
}),
})
  .then((res) => res.json())
  .then((json) => console.log(json));

/* will return
{
    "title": "Rich Almond Milk Eggnog",
    "image": "Default Image",
    "ingredientsInTheRepice": [
        {
            "fullDescription": "1 duck egg",
            "ingredients": {
                "name": "duck egg",
                "image": "ImgURL"
            }
    ],
    ...
}
*/
```

### Deleting a product\
```js
fetch("https://food-api-9dpr.onrender.com/api/recipes/:id", {
  method: "DELETE",
});
```

### Search By Title
#### query ==> ?title
```js
fetch("https://food-api-9dpr.onrender.com/api/search/title?title=butter")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Search By Ingredients
#### query ==> ?ingredientsName // multiple value
```js
fetch("https://food-api-9dpr.onrender.com/api/search/Ingredients?ingredientsName=salt,water")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Search By Nutritions
#### query ==> ?carb, ?fat, ?protein, ?calories
```js
fetch("https://food-api-9dpr.onrender.com/api/search/Nutritions?carb=10,calories=200")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Search By Type
#### query ==> ?vegan, ?vegetarian, ?ketogenic, ?glutenFree
#### You must enter "true" for the type of food you want to search for.
```js
fetch("https://food-api-9dpr.onrender.com/api/search/foodType?vegan=true&vegetarian=true")
  .then((res) => res.json())
  .then((json) => console.log(json));
```

### Get Random Food
```js
fetch("https://food-api-9dpr.onrender.com/api/recipes/search/random")
  .then((res) => res.json())
  .then((json) => console.log(json));
```
