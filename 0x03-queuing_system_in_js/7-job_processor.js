import {createQueue} from 'kue';

const queue = createQueue();
const queueName = 'push_notification_code_2';

const BLACKLISTED = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  const total = 100;
  job.progress(0, total);

  if (BLACKLISTED.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, total);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process(queueName, 2, (job, done) => {
  const {phoneNumber, message} = job.data;
  sendNotification(phoneNumber, message, job, done);
});
