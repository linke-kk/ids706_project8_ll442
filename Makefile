install:
	rustup update &&\
		cargo build --release

test:
	cargo test

format:	
	cargo fmt

lint:
	cargo clippy

# container-lint:
# 	docker run --rm -i hadolint/hadolint < ./.devcontainer/Dockerfile

refactor: format lint

run:
	cargo run --bin database

deploy:
	cargo run --bin database

all: install lint test format refactor deploy