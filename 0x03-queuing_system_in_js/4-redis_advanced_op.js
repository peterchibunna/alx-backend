import {createClient, print} from 'redis';

const client = createClient();

client.connect()
    .then(r => {
      console.log('Redis client connected to the server');
      const hashObj = {
        'Portland': 50,
        'Seattle': 80,
        'New York': 20,
        'Bogota': 20,
        'Cali': 40,
        'Paris': 2,
      };
      for (const [field, value] of Object.entries(hashObj)) {
        setHashTableData('HolbertonSchools', field, value);
      }
      displayHashTableData('HolbertonSchools');
    })
    .catch(err => console.log('Redis client not connected to the server:', err.toString()));

const setHashTableData = (hashName, fieldName, fieldValue) => {
  client.hSet(hashName, fieldName, fieldValue, print)
      .then(r => console.log(`Reply: ${r}`));
};

const displayHashTableData = (name) => {
  client.hGetAll(name)
      .then(r => console.log(JSON.parse(JSON.stringify(r))));
};
