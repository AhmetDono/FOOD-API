const Food = require('../models/Food');
const foodValidationSchema = require('../validations/foodValidation');


const createFood = async(req,res,next)=>{
    const { error } = foodValidationSchema.validate(req.body);

    if (error) {
        return res.status(400).json({ error: error.details[0].message });
    }
    const newFood = new Food(req.body)
    try{
        const fakeSavedFoodData = req.body; 
        res.status(200).json(fakeSavedFoodData);
        // const savedFood = await newFood.save();
        // res.status(200).json(savedFood)
    }catch(err){
        return res.status(500).json(err)
    }
}

const deleteFood = async(req,res,next)=>{
    try{
        // await Food.findByIdAndDelete(req.params.id);
        res.status(200).json("Food has been deleted");
    }catch(err){
        return res.status(500).json(err)
    }
}

const updateFood = async(req,res,next)=>{
    const { error } = foodValidationSchema.validate(req.body);

    if (error) {
        return res.status(400).json({ error: error.details[0].message });
    }

    try {
        // const updatedFood = await Food.findByIdAndUpdate(
        //   req.params.id,{
        //     $set: req.body,
        //   },{ new: true }
        // );
        // res.status(200).json(updatedFood);
        const updatedFood = req.body;
        res.status(200).json(updatedFood);
      } catch (err) {
        return res.status(500).json(err)
      }
}

const getFood = async(req,res,next)=>{
    try{
        const food = await Food.findById(req.params.id);
        res.status(200).json(food);
    }catch(err){
        return res.status(500).json(err)
    }
}

const getFoods = async(req,res,next)=>{
    try {
        const foods = await Food.find()
        res.status(200).json(foods);
    } catch (err) {
        return res.status(500).json(err)
    }
}

const getFoodsByIngredients = async (req, res,next) => {
    try {
        const ingredientsName = req.query.ingredientsName ? req.query.ingredientsName.split(',') : [];
        const foods = await Food.find({
            'ingredientsInTheRepice.ingredients.name': {
                $all: ingredientsName.map(ingredient => new RegExp(ingredient, 'i'))
            }
        });
        res.status(200).json(foods);
    } catch (err) {
        return res.status(500).json(err)
    }
};

const getFoodsByNutritions = async(req,res,next)=>{
    try {
        const carb = req.query.carb ? parseFloat(req.query.carb) : null;
        const fat = req.query.fat ? parseFloat(req.query.fat) : null;
        const protein = req.query.protein ? parseFloat(req.query.protein) : null;
        const calories = req.query.calories ? parseFloat(req.query.calories) : null;

        const queryFilters = {};

        if (carb !== null) {
            queryFilters['carb'] = { $lte: carb };
        }

        if (fat !== null) {
            queryFilters['fat'] = { $lte: fat };
        }

        if (protein !== null) {
            queryFilters['protein'] = { $lte: protein };
        }

        if (calories !== null) {
            // Calories 300 ve altında olanları filtrele
            queryFilters['calories'] = { $lte: calories };
        }

        // Foods collection'ından verileri çek
        const foods = await Food.find(queryFilters);
        res.status(200).json(foods);

    } catch (err) {
        return res.status(500).json(err)
    }
}

const getFoodsByTitle = async(req,res,next)=>{
    try {
        const title = req.query.title ? req.query.title.split(' ') : [];

        // Şimdi title dizisini istediğiniz şekilde kullanabilirsiniz
        // Örneğin, title dizisiyle MongoDB sorgusu oluşturabilir ve filtreleme yapabilirsiniz

        const foods = await Food.find({
            'title': { $regex: new RegExp(title, 'i') }
        });
        res.status(200).json(foods);

    } catch (err) {
        return res.status(500).json(err)
    }
}

const getFoodsByType = async (req, res,next) => {

    try {
        const vegan = req.query.vegan === "true" || false;
        const vegetarian = req.query.vegetarian === "true" || false;
        const ketogenic = req.query.ketogenic === "true" || false;
        const glutenFree = req.query.glutenFree === "true" || false;

        const queryFilters = {};

        if (vegan) {
            queryFilters['vegan'] = true;
        }

        if (vegetarian) {
            queryFilters['vegetarian'] = true;
        }

        if (ketogenic) {
            queryFilters['ketogenic'] = true;
        }

        if (glutenFree) {
            queryFilters['glutenFree'] = true;
        }

        // MongoDB sorgusu oluştur
        const foods = await Food.find({
            $or: [
                { 'vegan': queryFilters['vegan'] },
                { 'vegetarian': queryFilters['vegetarian'] },
                { 'ketogenic': queryFilters['ketogenic'] },
                { 'glutenFree': queryFilters['glutenFree'] }
            ]
        });

        res.status(200).json(foods);

    } catch (err) {
        return res.status(500).json(err)
    }
};

const getFoodRandom = async(req,res,next)=>{
    try {
        // Collection'daki indexleri listele
        const totalCount = await Food.countDocuments()
        //const rand = Math.floor(Math.random(0,totalCount)); random() argumansiz olarak kullaniliyormus normalde o yuzden 0 donduruyor surekli bu kodda
        const rand = Math.floor(Math.random() * totalCount);
        const food = await Food.findOne().skip(rand)
        console.log(rand)
        res.status(200).json(food);

    } catch (err) {
        return res.status(500).json(err)
    }
}

module.exports = {
    createFood,
    deleteFood,
    updateFood,
    getFood,
    getFoods,
    getFoodsByTitle,
    getFoodsByIngredients,
    getFoodsByNutritions,
    getFoodsByType,
    getFoodRandom,
}