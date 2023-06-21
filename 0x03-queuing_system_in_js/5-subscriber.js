import {createClient} from 'redis';

const client = createClient({});

client.connect()
    .then(r => console.log('Redis client connected to the server'))
    .catch(err => console.log('Redis client not connected to the server:', err.toString()));

client.subscribe('holberton school channel', (message, channel)=>{
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe().then(r => null);
    client.quit().then(r => null);
  }
});
