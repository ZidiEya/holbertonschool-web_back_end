const request = require('supertest');
const app = require('./api');
const { expect } = require('chai');

describe('API tests', () => {
  describe('GET /available_payments', () => {
    it('should return correct payment methods', (done) => {
      request(app)
        .get('/available_payments')
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).to.deep.equal({
            payment_methods: {
              credit_cards: true,
              paypal: false
            }
          });
          done();
        });
    });
  });

  describe('POST /login', () => {
    it('should return welcome message with username', (done) => {
      request(app)
        .post('/login')
        .send({ userName: 'Betty' })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.text).to.equal('Welcome Betty');
          done();
        });
    });

    it('should return 400 if no username is sent', (done) => {
      request(app)
        .post('/login')
        .send({})
        .expect(400)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.text).to.equal('Missing userName');
          done();
        });
    });
  });
});
