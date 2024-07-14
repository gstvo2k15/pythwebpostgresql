FROM hadolint/hadolint:latest

WORKDIR /code_checker

ENTRYPOINT ["hadolint"]
CMD ["/code_checker/Dockerfile"]

