import {createClient, print} from 'redis';

import {promisify}  from 'util';

const client = createClient({});

client.connect()
    .then(async(r) => {
      console.log('Redis client connected to the server');
      await func();
    })
    .catch(err => console.log('Redis client not connected to the server:', err.message));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print)
      .then(r => console.log(`Reply: ${r}`));
};

const displaySchoolValue = promisify(
    (schoolName) => client.get(schoolName)
        .then((value) => {
          console.log(value);
        })
);

const func = () => {
  displaySchoolValue('Holberton').then(r => null);
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco').then(r => null);
}
