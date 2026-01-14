# QA Automation Mini Framework (Pytest + Selenium + API + CI)

A small but production-style QA automation framework showing:
- UI automation using Selenium + Page Object Model
- API testing using Requests
- Pytest HTML reporting
- GitHub Actions CI running tests on each push/PR

## Tech Stack
- Python, Pytest
- Selenium + webdriver-manager
- Requests (API testing)
- GitHub Actions (CI)
- pytest-html (report)

## Project Structure
- `pages/` Page Object Model classes
- `tests/` UI + API automated tests
- `utils/` config/constants
- `.github/workflows/` CI pipeline

## Run Locally
```bash
pip install -r requirements.txt
pytest -m "api or ui" --html=report.html --self-contained-html
