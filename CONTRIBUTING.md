# Contributing to The Google & Alphabet Mega-Ecosystem Atlas

Thank you for your interest in contributing to **The Google & Alphabet Mega-Ecosystem Atlas**! This planetary project is maintained by **Nandhakumar Murugan** (Google Student Ambassador) for the global student and developer community.

---

## 🌟 How You Can Contribute

1. **Add Missing Endpoints**: Discover a newly launched Google product, AI experiment, or local developer chapter?
2. **Verify / Update URLs**: Keep regional endpoints and docs up-to-date.
3. **Enhance the Dashboard**: Suggest UI/UX improvements, filters, or visualization features.
4. **Documentation**: Improve markdown guides in the `docs/` folder.
5. **Star & Share**: Star the repository on GitHub and share with campus GDSC chapters!

---

## 🛠️ Contribution Workflow

1. **Fork the Repository**:
   Click **Fork** on [GitHub](https://github.com/nandhakumar-murugan/google-ecosystem-atlas).

2. **Clone your Fork**:
   ```bash
   git clone https://github.com/<your-username>/google-ecosystem-atlas.git
   cd google-ecosystem-atlas
   ```

3. **Create a Feature Branch**:
   ```bash
   git checkout -b add-new-endpoints
   ```

4. **Modify Generator or Data**:
   If adding programmatic entries, edit `scripts/build_mega_ecosystem.py` and run:
   ```bash
   python scripts/build_mega_ecosystem.py
   ```
   This will automatically update `data/google_ecosystem.json`, `data/google_ecosystem.csv`, `data/google_ecosystem.js`, and the 14 category documents in `docs/`.

5. **Commit & Push**:
   ```bash
   git add .
   git commit -m "feat: Add new Google DeepMind & Cloud API endpoints"
   git push origin add-new-endpoints
   ```

6. **Submit a Pull Request**:
   Open a Pull Request against the `main` branch of `nandhakumar-murugan/google-ecosystem-atlas`.

---

## 📜 Code of Conduct
Please be respectful, collaborative, and constructive when opening issues or pull requests.
