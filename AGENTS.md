# Repository Guidelines

## Commit messages

Use the Conventional Commits format:

```text
<type>(<optional scope>): <imperative summary>
```

- Use an appropriate lowercase type such as `feat`, `fix`, `docs`, `test`,
  `refactor`, `build`, `ci`, `perf`, `style`, `chore`, or `revert`.
- Keep the summary concise, imperative, and free of a trailing period.
- Keep each commit focused on one logical change.
- Add a body when the motivation or non-obvious tradeoffs need explanation.
- Mark breaking changes with `!` before the colon and explain them in a
  `BREAKING CHANGE:` footer.
- Review the staged diff and run relevant checks before committing.

Examples:

```text
feat(regression): add ridge regression example
fix(data): handle missing feature values
docs: clarify environment setup
build: update scikit-learn dependency
```
