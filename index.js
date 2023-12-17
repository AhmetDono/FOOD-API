const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const dotenv = require('dotenv')
const food = require('./router/food');
const app = express();
dotenv.config();


mongoose.connect(process.env.MONGO_URI)
.then(()=>console.log("Db connection is successfull"))
.catch((err)=>{console.log(err)});

app.use(express.json());
app.use(cors());
//app.use('/api/auth',auth);


app.use('/api/recipes',food);

app.listen(process.env.PORT || 5000,()=>{
    console.log(`server is running on port: ${process.env.PORT}`)
})