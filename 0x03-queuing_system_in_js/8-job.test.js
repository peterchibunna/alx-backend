import { createQueue } from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('if jobs is an empty', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });
  
  it('if jobs is not an array but Number', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('if jobs is not an array but Object', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('if jobs is not an array but String', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    queue.createJob('job_01', {item: 'Basket'}).save();
    queue.createJob('job_02', {item: 'Shirt'}).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('job_01');
    expect(queue.testMode.jobs[0].data).to.deep.equal({item: 'Basket'});
    expect(queue.testMode.jobs[1].type).to.equal('job_02');
    expect(queue.testMode.jobs[1].data).to.deep.equal({item: 'Shirt'});
  });
});
