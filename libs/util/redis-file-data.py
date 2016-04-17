#! /usr/bin/env python

import redis
import random


class FillData(object):

    def __init__(self, host, port, db=0):
        self.host = host
        self.port = port
        self.redis_client = redis.StrictRedis(host=self.host, port=self.port, db=db)

    def action(self):

        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 10)

            if y == 1:
                for z in xrange(1, x):
                    self.redis_client.set("Key:" + x, x)
            elif y == 2:
                for z in xrange(1, x):
                    self.redis_client.get("Key:" + x)
            elif y == 4:
                for z in xrange(1, x):
                    self.redis_client.hset("HashKey:" + x, x, x)
            elif y == 5:
                for z in xrange(1, (x / 2) + 2):
                    self.redis_client.setex("Key:" + x, 1000, x)
            elif y == 6:
                for z in xrange(1, x):
                    self.redis_client.hexists("HashKey:" + x, y)
            elif y == 7:
                for z in xrange(1, x):
                    self.redis_client.setbit("BitSet:" + x, 1, 1)
            elif y == 8:
                for z in xrange(1, x):
                    self.redis_client.getbit("BitSet:" + x, 1)
            elif y == 9:
                for z in xrange(1, x):
                    self.redis_client.expire("Key:" + x, 2000)

if __name__ == "__main__":

    fill_data = FillData(host='127.0.0.1', port=6379)
    fill_data.action()
