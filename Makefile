COMMIT_MESSAGE = $(github.event.head_commit.message)
ifeq ($(shell printf '%s' '$(COMMIT_MESSAGE)' | wc -c),0)
	COMMIT_MESSAGE = $(shell git log -1 --pretty=%B)
endif

.PHONY: lint
lint:
	# echo $(COMMIT_MESSAGE) > /tmp/.gitmessage
	# conventional-pre-commit /tmp/.gitmessage

	ruff check .

.PHONY: test
test:
	pytest --cov=flywheels tests/

.PHONY: changelog
changelog:
	git-changelog --style conventional \
		--sections feat,fix,revert,refactor,perf,build,ci,deps,docs,style,test \
		--template path:CHANGELOG.md.jinja \
		--bump-latest \
		-o CHANGELOG.md