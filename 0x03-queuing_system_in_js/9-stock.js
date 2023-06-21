const express = require('express');
const util = require('util');
const {createClient} = require("redis");
const {promisify} = util;
const client = createClient({});
client.connect()
    .then(r => {
      console.log('Redis client connected to the server');
    })
    .catch(err => console.log('Redis client not connected to the server:', err.message));

function getCurrentReservedStockById(itemId) {
  // this function ...
  return client.get(`item.${itemId}`).then(value=> value);
}

getCurrentReservedStockById[promisify.custom] = (itemId) => {
  /// ... we have now custom promisified it!
  /// see: https://nodejs.org/api/util.html#util_util_promisify_original
  return new Promise((resolve, reject) => {
    client.get(`item.${itemId}`).then(value=> resolve(value));
  });
};

const app = express();
const port = 1245;

const listProducts = [
  {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
  {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
  {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
  {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5},
];

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock).then(r => console.log('Stored item in redis'));
};


app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({status: 'Product not found'});
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  item.currentQuantity = currentStock !== null ? currentStock : item.initialAvailableQuantity;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({status: 'Product not found'});
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);

  if (currentStock === null) {
    currentStock = item.initialAvailableQuantity;
  }

  if (currentStock <= 0) {
    res.json({status: 'Not enough stock available', itemId});
    return;
  }

  reserveStockById(itemId, Number(currentStock) - 1);

  res.json({status: 'Reservation confirmed', itemId});
});
