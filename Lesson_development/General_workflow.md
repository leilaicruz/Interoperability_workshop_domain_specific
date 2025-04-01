
## 🔧 1. 30-Minute Workshop Outline

### 🧠 Learning Objectives:
By the end of this session, participants will be able to:
- Explain what NetCDF files are and why they are used in research.
- Access a NetCDF file from 4TU.ResearchData via the OPeNDAP protocol using Python.
- Read and explore NetCDF metadata.
- Modify NetCDF metadata to comply with the Climate and Forecast (CF) conventions.
- Understand the role of standardized and interoperable data formats (NetCDF & IIIF) in FAIR research.

### ⏰ Time Breakdown (30 mins)
| Time | Activity |
|------|----------|
| 0–5 mins | **Introduction**: <br> - Welcome & goal of the pilot<br> - Interoperability in research (NetCDF, IIIF)<br> - Brief overview of 4TU.ResearchData |
| 5–15 mins | **Live Demo: Accessing NetCDF via OPeNDAP** <br> - Use `netCDF4.Dataset()` with an OPeNDAP URL from 4TU<br> - Navigate variables and dimensions<br> - Quick plot with `matplotlib` or `xarray.plot()` |
| 15–25 mins | **Editing Metadata to Match CF Conventions** <br> - Overview of CF metadata standard<br> - Open NetCDF file in write mode<br> - Change or add `standard_name`, `units`, `long_name` attributes<br> - Use `cfchecker` (CLI or web-based) to validate |
| 25–30 mins | **Wrap-up & Bonus IIIF Mention** <br> - Quick look at IIIF endpoints<br> - Mention microscopy image aggregation as a teaser<br> - Q&A or pointer to GitHub repo for self-exploration |

> 📝 Provide a shared notebook URL for participants to follow along or explore afterward.

---

## 🌐 2. How to Showcase Interoperability

Here are some **easy-to-grasp metaphors + visuals** to show the power of interoperable frameworks:

- **Visual Timeline Slide**: Show the evolution from proprietary → open → interoperable formats.
- **"Lego Block" Analogy**: Explain that NetCDF and IIIF are like LEGO blocks – they *click* into many tools and workflows.
- **Cross-tool compatibility**: Demonstrate how the same NetCDF file can be read in Python, MATLAB, and Panoply. Similarly, IIIF images can be displayed in Mirador, a Jupyter notebook, or a website.
- **Data Lifecycle Example**: Show a NetCDF dataset from acquisition to reuse in another research group due to standardized metadata.
- **Metadata Before/After**: Show how fixing metadata fields enables better discoverability and reuse (perhaps even machine processing via CF checker).

---

## ☁️ 3. Cloud Server Options

Binder is great for pilots, but consider these depending on future scale and stability needs:

| Platform | Pros | Cons |
|---------|------|------|
| **Binder** | Free, easy to set up from GitHub | Cold starts, no persistent storage |
| **Pangeo Binder** | Optimized for geoscience + NetCDF; uses Dask, Xarray | Still subject to Binder limits |
| **Google Colab** | Good Python support, user-friendly | Requires Google login, internet connection, limited NetCDF/OPeNDAP support |
| **Code Ocean** | Research-focused, supports reproducibility | Limited free use |
| **JupyterHub on DigitalOcean or 2i2c.org** | Fully customizable | Requires admin/setup time |
| **MyBinder + Voilà** | Convert notebooks to apps | Ideal for demos, limited for interactive coding |
| **GitHub Codespaces** | Fully configurable dev env | Requires GitHub account + might need subscription |


---

## ✅ Step-by-Step Procedure for a Code-Along via Binder

### 🛠️ 1. **Prepare Your GitHub Repository**
This is your **source-of-truth** for Binder to launch the environment.

**Must-have components:**
- `notebooks/` folder: Jupyter notebooks used in the workshop.
- `environment.yml` or `requirements.txt`: Lists packages to install (e.g., `netCDF4`, `xarray`, `cfchecker`, `matplotlib`).
- `README.md`: Clear instructions and goals.
- Optional: `postBuild` script (for shell setup), `data/` folder with small example files or links to external OPeNDAP URLs.

Binder reads the repo and builds an environment based on these files.

---

### 🔗 2. **Generate a Binder Launch Link**
Use: [https://mybinder.org](https://mybinder.org)

- Paste your GitHub repo URL.
- Optionally specify a branch or file (e.g., start with `notebooks/00-setup.ipynb`).
- Copy the generated **launch badge/link**.

💡 Example:
```
https://mybinder.org/v2/gh/<your-org>/<repo-name>/HEAD?filepath=notebooks/00-setup.ipynb
```

---

### 📤 3. **Share the Binder Link with Participants**
Before or at the start of the workshop:

- Include the Binder link in your slides or a collaborative doc (e.g., HackMD, Google Doc).
- Give them 2–3 minutes at the beginning to launch the environment.
- Let them know they **do not need to install anything**, just click and go.

---

### 🧑‍💻 4. **Facilitate the Code-Along**
As you guide the workshop:

- Work from the **same notebook** they have open.
- Pause between sections for participants to run cells.
- Ask for thumbs-up/check-in signals in Zoom/chat/in person.

Optional:
- Use an Etherpad or Google Doc where they can post issues/questions.
- Have a helper who monitors questions during the code-along.

---

### 💾 5. **Persisting Their Work (Optional Caveats)**
Binder sessions:
- Are temporary (~10 minutes idle timeout).
- Do not persist any changes unless participants download their notebook or export it to their cloud (e.g., save to GitHub or Google Drive manually).

🧩 Tip: You can add a “Download Notebook” button or instruct them to `File > Download as`.

---

### 🧪 Bonus Tips
- **Test ahead of time** with a fresh incognito window.
- Keep the example datasets small or accessed via external (e.g., OPeNDAP) links.
- Have a Plan B (e.g., static slides or demo video) in case Binder is slow or fails.

---

Would you like help creating the environment files (`environment.yml`, `requirements.txt`) or setting up the notebook structure next?