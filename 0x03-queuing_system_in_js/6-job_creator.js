import {createQueue} from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
  phoneNumber: '08061234567',
  message: 'Use 7812 as OTP to login',
});

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
}).on('failed attempt', () => {
  console.log('Notification job failed');
});
job.save();
