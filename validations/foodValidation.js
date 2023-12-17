const Joi = require('joi');

const foodValidationSchema = Joi.object({
    title: Joi.string().min(5).max(50).required(),
    image: Joi.string().required(),
    description: Joi.string().min(5).max(500).required(),
    preparationTime:Joi.number().min(0).max(9999).required(),
    protein:Joi.number().min(0).max(9999).required(),
    calories:Joi.number().min(0).max(9999).required(),
    fat:Joi.number().min(0).max(9999).required(),
    carb:Joi.number().min(0).max(9999).required(),
    vegan:Joi.boolean().required(),
    vegetarian:Joi.boolean().required(),
    glutenFree:Joi.boolean().required(),
    ketogenic:Joi.boolean().required(),
    ingredientsInTheRepice: Joi.array().items(
        Joi.object({
            fullDescription: Joi.string().min(1).max(500).required(),
            ingredients: Joi.object({
                name: Joi.string().min(1).max(100).required(),
                image: Joi.string(),
            }).required(),
            measure: Joi.object({
                amount: Joi.string().min(1).max(100).required(),
                unitOfMeasure: Joi.string().required(),
            }).required(),
        })
    ),
    materials: Joi.array().items(
        Joi.object({
            material: Joi.object({
                name: Joi.string().min(1).max(100),
                image: Joi.string(),
            })
        })
    ),
    vitamins: Joi.array().items(
        Joi.object({
            vitamin: Joi.object({
                name: Joi.string().min(1).max(100),
                description: Joi.string().min(1).max(500),
            })
        })
    ),
  });
  
module.exports = foodValidationSchema;