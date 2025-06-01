# 🧾 PDF Editor GUI with Python & PyMuPDF

**A lightweight PDF merging and (soon-to-be) splitting tool built using PyQt6 and PyMuPDF (fitz).**
Perfect for quick PDF tasks with a clean interface and minimal overhead.

## 🚀 Features

✅ Merge multiple PDF files into one
⏳ Split functionality coming soon
🖱️ GUI-based, no command-line needed
🎨 Built using PyQt6 for a native desktop feel
📂 File dialogs for easy input/output paths

---

## 🛠️ Requirements

* Python 3.10+
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`)
* [PyQt6](https://pypi.org/project/PyQt6/)

Install dependencies:

```bash
pip install PyQt6 PyMuPDF
```

---

## 📁 File Structure

| File        | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| `UI-qt.py`  | Core GUI app with functional "Merge PDF" & placeholder for split |
| `main.py`   | CLI starter (WIP) – basic input-based PDF tools                  |
| `withUI.py` | Experimental UI – mix of button actions and raw input methods    |

---

## 🎮 How to Run

Just want the GUI?

```bash
python UI-qt.py
```

Wanna play around with experiments?

```bash
python withUI.py
```

---

## 📌 Sample Usage (Merge)

1. Click **"Merge PDFs"**
2. Select 2+ PDFs via file dialog
3. Save your merged output when prompted

> Output PDF will be saved wherever you choose in the dialog.

---

## ⚠️ Known Issues / TODOs

* `split_pdf()` not implemented yet
* `input_pdf()` logic in `main.py`/`withUI.py` is buggy (indexing before assignment)
* Refactor duplicated logic across files
* Remove unused or placeholder buttons (e.g., `abc()`)

---

## 💡 Roadmap Ideas

* [ ] Add PDF splitting UI
* [ ] Drag-and-drop support
* [ ] Page selection (merge only selected pages)
* [ ] Dark mode toggle
* [ ] Export settings / preferences

---

## 📷 Screenshots

Coming soon

---

## 🤝 Contributing

Open to PRs, especially if you can:

* Fix bugs in `main.py`
* Improve UX/UI
* Add PDF preview
---
## 📜 License

MIT — Do what you want, but don’t sue me. Or worse, push to main without testing.
---

## 👑 Author

Made with 💼 by [MrSaltyFish](https://github.com/MrSaltyFish)
