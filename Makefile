code := $(wildcard code/*.ipynb) $(wildcard code/**/*.ipynb)
md_pages := $(patsubst code/%.ipynb,docs/tutorials/%.md,$(code))

build.site: $(md_pages)

docs/tutorials/%.md: code/%.ipynb
	jupyter nbconvert\
		--to markdown $<\
		--output-dir $(dir $@)\
		--template=src/to_markdown.tpl