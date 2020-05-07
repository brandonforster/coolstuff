run:
	pip3 install --no-cache-dir -r requirements.txt
	python3 ./server.py

docker_build:
	docker build --tag coolstuff:1.0 .

docker_run:
	docker run -p 5000:5000 --name cool coolstuff:1.0

docker_clean:
	docker stop cool
	docker rm cool
