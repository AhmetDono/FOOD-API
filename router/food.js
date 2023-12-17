const express = require('express');
const router = express.Router();
const { createFood, deleteFood, updateFood, getFood, getFoods, getFoodsByIngredients,getFoodsByNutritions, getFoodsByTitle, getFoodsByType, getFoodRandom } = require('../controller/food');

router.post('/',createFood);
router.delete('/:id',deleteFood);
router.put('/:id',updateFood);
router.get('/:id',getFood);
router.get('/',getFoods);
router.get('/search/title',getFoodsByTitle);
router.get('/search/Ingredients',getFoodsByIngredients);
router.get('/search/Nutritions',getFoodsByNutritions); //!vitaminler dahil degil onun icin sistem yap
router.get('/search/foodType',getFoodsByType);
router.get('/search/random',getFoodRandom); //TODO


module.exports = router