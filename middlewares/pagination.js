const paginateResults = (model) => async (req, res, next) => {
    try {
      const page = parseInt(req.query.page) || 0;
      const limit = parseInt(req.query.limit) || 0;
  
      const results = {};
  
      if (limit > 0) {
        const startIndex = (page - 1) * limit;
  
        results.results = await model.find().limit(limit).skip(startIndex).exec();
  
        if ((page - 1) * limit > 0) {
          results.previous = {
            page: page - 1,
            limit: limit,
          };
        }
  
        if (page * limit < (await model.countDocuments().exec())) {
          results.next = {
            page: page + 1,
            limit: limit,
          };
        }
      } else {
        results.results = await model.find().exec();
      }
  
      res.paginatedResults = results;
      next();
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  };
  
  module.exports = { paginateResults };
  