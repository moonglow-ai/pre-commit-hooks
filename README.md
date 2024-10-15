![Moonglow logo](https://raw.githubusercontent.com/moonglow-ai/pre-commit-hooks/refs/heads/main/moonglow-logo.png)

# Moonglow pre-commit-hooks - autogenerate iPython notebook diffs

_This repository is is part of the [Moonglow](https://moonglow.ai) project. Moonglow makes it easy to connect iPython notebooks to powerful cloud compute._

Pre-commit hooks that autogenerate diffs for your ipython notebooks!

![Example diffs](https://raw.githubusercontent.com/moonglow-ai/pre-commit-hooks/refs/heads/main/nice-diffs.png)

These hooks assume you're using the [pre-commit package](https://pre-commit.com/). To setup and install the hooks, add this to your `.pro-commit-hooks.yaml` file:

```
 - repo: https://github.com/moonglow-ai/pre-commit-hooks
    rev: v0.1.1
    hooks:
      - id: clean-notebook
```

You can read a more in-depth guide to the hooks [here](https://blog.moonglow.ai/diffing-ipython-notebook-code-in-git/).
