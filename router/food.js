const express = require('express');
const router = express.Router();
const { createFood, deleteFood, updateFood, getFood, getFoods, getFoodsByIngredients,getFoodsByNutritions, getFoodsByTitle, getFoodsByType, getFoodRandom } = require('../controller/food');
const {limitRoutes} = require('../middlewares/rateLimit')

router.post('/',limitRoutes,createFood);
router.delete('/:id',limitRoutes,deleteFood);
router.put('/:id',limitRoutes,updateFood);
router.get('/:id',limitRoutes,getFood);
router.get('/',limitRoutes,getFoods);
router.get('/search/title',limitRoutes,getFoodsByTitle);
router.get('/search/Ingredients',limitRoutes,getFoodsByIngredients);
router.get('/search/Nutritions',limitRoutes,getFoodsByNutritions); //!vitaminler dahil degil
router.get('/search/foodType',limitRoutes,getFoodsByType);
router.get('/search/random',limitRoutes,getFoodRandom);


module.exports = router