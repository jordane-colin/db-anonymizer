.PHONY: install build-requirements

.PHONY: build
build:
	docker build -t app .

# Launch this to ...install ?
.PHONY: install
install:
	pip3 install -Ur requirements.txt

.PHONY: launch
launch:
	 docker-compose build anonymizer && docker-compose up -d anonymizer
