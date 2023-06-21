import {createClient, print} from 'redis';

const client = createClient({});

client.connect()
    .then(r => console.log('Redis client connected to the server'))
    .catch(err => console.log('Redis client not connected to the server:', err.toString()));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print)
      .then(r => console.log(`Reply: ${r}`));
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName)
      .then((value) => console.log(value));
};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
