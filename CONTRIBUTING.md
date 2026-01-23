# Contributing to Analysis OS

Thank you for your interest in contributing to the Analysis & AI Consulting OS! This framework is designed to be community-driven and extensible.

## How to Contribute

### 1. Reporting Issues

If you find bugs, have questions, or want to suggest improvements:

- **Search existing issues** first to avoid duplicates
- **Open a new issue** with a clear title and description
- **Include examples** if reporting a bug (data samples, error messages, etc.)
- **Tag appropriately** (bug, enhancement, question, documentation)

### 2. Contributing Code

#### Getting Started

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/analysis-os.git
cd analysis-os

# Create a feature branch
git checkout -b feature/your-feature-name
```

#### Making Changes

1. **Follow the existing structure**
   - Place prompts in `prompts/core/` or `prompts/use_cases/`
   - Add checklists to `checklists/`
   - Include examples in `examples/`
   - Update documentation as needed

2. **Test your changes**
   - Run the quality check workflow locally if possible
   - Validate YAML files: `python -c "import yaml; yaml.safe_load(open('config.yaml'))"`
   - Check Markdown formatting
   - Ensure all links work

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add XYZ use case template"
   ```

4. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### 3. Contributing Use Cases

We especially welcome new use case templates! To add a new use case:

#### Structure

Create a new directory under `prompts/use_cases/YOUR_USE_CASE/` with:

```
prompts/use_cases/your_use_case/
├── PROMPT.md          # Main prompt template
├── README.md          # Use case overview
└── example.md         # (Optional) Real-world example
```

#### Template Requirements

Your `PROMPT.md` must include:

- **Role & Context**: Clear AI assistant persona and domain context
- **Objective**: Specific business questions and goals
- **Data Profile**: Expected data structure and sources
- **Constraints & Scope**: Limitations and focus areas
- **Output Format**: Structured response template
- **Validation Steps**: Quality checks and success criteria

#### Example Use Cases to Add

- Marketing attribution analysis
- Operations bottleneck identification  
- Product feature prioritization
- Customer segmentation
- Pricing optimization
- Sales forecasting
- A/B test analysis
- Supply chain optimization

### 4. Improving Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples or clarifications
- Improve README sections
- Create tutorials or guides
- Translate content

### 5. Enhancing Checklists

Contribute to the validation framework:

- Add new checklist items
- Improve existing validation steps
- Share lessons learned from real projects
- Add industry-specific validation rules

## Code Style Guidelines

### Markdown Files

- Use clear, concise headings (## for main sections)
- Include code blocks with syntax highlighting
- Add examples where appropriate
- Keep line length reasonable (<120 chars)
- Use bullet points for lists

### YAML Files

- Use 2-space indentation
- Add comments for complex configurations
- Follow existing naming conventions
- Validate before committing

### Prompts

- Write in clear, professional language
- Use specific, actionable instructions
- Include concrete examples
- Test with real or synthetic data
- Document assumptions

## Pull Request Process

1. **Ensure CI checks pass** (GitHub Actions will run automatically)
2. **Update documentation** to reflect your changes
3. **Add examples** if introducing new features
4. **Link related issues** in the PR description
5. **Request review** from maintainers

### PR Title Format

Use conventional commits:

- `feat: add new use case for X`
- `fix: correct calculation in recommendation table`
- `docs: improve installation instructions`
- `chore: update dependencies`
- `test: add validation for config.yaml`

## Community Guidelines

### Be Respectful

- Welcome newcomers and be patient with questions
- Provide constructive feedback
- Focus on ideas, not individuals
- Assume positive intent

### Be Collaborative

- Share knowledge and learnings
- Help others troubleshoot issues
- Review pull requests when possible
- Participate in discussions

### Be Professional

- Keep discussions on-topic
- Avoid promotional content
- Respect intellectual property
- Follow the Code of Conduct

## Getting Help

- **Questions**: Open a GitHub issue with the `question` label
- **Bugs**: Open an issue with reproduction steps
- **Feature requests**: Open an issue with the `enhancement` label
- **Security issues**: Email directly (see SECURITY.md)

## Recognition

Contributors will be:

- Listed in the repository contributors page
- Mentioned in release notes for significant contributions
- Credited in documentation for substantial additions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Quick Reference: Adding a New Use Case

```bash
# 1. Create directory structure
mkdir -p prompts/use_cases/my_use_case
cd prompts/use_cases/my_use_case

# 2. Create PROMPT.md from template
cp ../churn/PROMPT.md PROMPT.md

# 3. Customize for your use case
# Edit PROMPT.md with your content

# 4. Add README
touch README.md

# 5. (Optional) Add example
touch example.md

# 6. Update main README
# Add your use case to the "Use Cases" section

# 7. Commit and push
git add .
git commit -m "feat: add my_use_case template"
git push origin feature/my-use-case

# 8. Create pull request on GitHub
```

---

Thank you for helping make Analysis OS better! 🚀
