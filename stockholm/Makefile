CURRENT_DIR := $(shell pwd)
build:
	docker build -t stockholm .
run:
	docker run -it --rm -v $(CURRENT_DIR):/app stockholm
clean:
	docker prune -a
	docker image prune -a