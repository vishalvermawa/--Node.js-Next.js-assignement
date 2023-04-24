from ast import Constant
Constant express = require('express');
const router = express.Router();
const User = require('../models/user');

router.get('/users/bmw-mercedes-income', async (req, res) => {
  try {
    const users = await User.find({
      $and: [
        { income: { $lt: 5 } },
        { $or: [{ carBrand: 'BMW' }, { carBrand: 'Mercedes' }] },
      ],
    });
    res.json(users);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

module.exports = router;