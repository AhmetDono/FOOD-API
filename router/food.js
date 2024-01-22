const express = require('express');
const router = express.Router();
const { createFood, deleteFood, updateFood, getFood, getFoods, getFoodsByIngredients,getFoodsByNutritions, getFoodsByTitle, getFoodsByType, getFoodRandom } = require('../controller/food');
const {limitRoutes} = require('../middlewares/rateLimit')
const {paginateResults} = require('../middlewares/pagination');
const Food = require('../models/Food');


router.post('/',limitRoutes,createFood);
router.delete('/:id',limitRoutes,deleteFood);
router.put('/:id',limitRoutes,updateFood);
router.get('/:id',limitRoutes,getFood);
router.get('/',limitRoutes,paginateResults(Food),getFoods);
router.get('/search/title',limitRoutes,getFoodsByTitle);
router.get('/search/Ingredients',limitRoutes,getFoodsByIngredients);
router.get('/search/Nutritions',limitRoutes,getFoodsByNutritions); //!vitaminler dahil degil
router.get('/search/foodType',limitRoutes,getFoodsByType);
router.get('/search/random',limitRoutes,getFoodRandom);


module.exports = router