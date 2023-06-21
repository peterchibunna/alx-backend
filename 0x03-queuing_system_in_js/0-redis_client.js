import {createClient, print} from 'redis';

const client = createClient({
  // url: 'redis://127.0.0.1:6379'
});

// client.on('connect', ()=> console.log('Redis client connected to the server'));
// client.on('error', err => console.log('Redis client not connected to the server:', err.toString()));
client.connect()
    .then(r => console.log('Redis client connected to the server'))
    .catch(err => console.log('Redis client not connected to the server:', err.message));
