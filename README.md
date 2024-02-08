
- RabbitMQ broker - https://www.cloudamqp.com/

- From ```main``` directory,
```
  docker-compose db exec sh
  python manager.py db init
  python manager.py db migrate
  python manager.py db upgrade
```
   
