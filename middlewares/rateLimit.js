const rateLimit = require('express-rate-limit')

const limitRoutes = rateLimit({
    windowMs: 24 * 60 * 60 * 1000,  // 24 hours
    max: 500,                       // limit of each IP
    message: "You have reached the maximum api call => 500 calls per day",
    headers: true
});

module.exports = {
    limitRoutes,
}