# Usage
```bash
source env/bin/activate
```
```bash
docker-compose up -d --build
```
--or--
```bash
docker run -d -p 6379:6379 --name redis redis
python app/src/main.py
```
```bash
curl http://localhost:5000/tasks
```
# Running tests
python -m unittest discover -s ./app/tests -p "when*" -v