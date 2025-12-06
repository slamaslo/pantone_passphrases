# 🎨 Pantone Passphrases

Generate **memorable**, **beautiful**, and **secure** passwords using Pantone-style color names.

This tool produces semantic passphrases like:

```
Bluewash-Tropical-Peach-340
Saffron-Silver-Ocean-712
Mint-Coral-Sand-981
```

These are easier to remember than random character strings and harder to guess than common dictionary passwords.

---

## 🚀 Features

* Uses a prebuilt JSON of Pantone-style semantic categories
* Weighted category selection for balanced variety
* Distinct category pairing to avoid repetition
* Simple Python code, no external libraries
* Passphrase format: `color-color-number`

---

## 📦 Project Structure

```
builder/
  build_categories.py        # one-time category builder
  pantone-colors.json        # original Pantone-like dataset

generator/
  password_generator.py      # main password generator
  pantone_semantic_categories.json  # generated categories JSON

README.md
```

---

## 🧪 Usage

### Generate passwords

```bash
python3 generator/password_generator.py
```

Example output:

```
Dusty-Yellow-Classic-Blue-697
Tender-Greens-Silver-428
Pink-Icing-Rio-Red-371
```

### Build / rebuild category JSON (optional)

```bash
python3 builder/build_categories.py
```

This is only needed if you change the source Pantone file.

---

## 🔐 Security Notes

* Designed for **master passwords**, **device passwords**, and **daily-use passphrases**
* Semantic structure increases memorability
* Random numeric suffix increases entropy
* For added strength, append a symbol:

```
Tropical-Blue-Gold-392!
```

---

## 📝 License

MIT License.

---

## 💡 Inspiration

Inspired by **Diceware passphrases**, adapted to color vocabulary for human-friendly security. Semantic passwords are proven easier to remember and harder to brute-force than typical weak patterns.

---

## 🙏 Credits

Color name data originally sourced from  
**https://github.com/Margaret2/pantone-colors**

Pantone® is a trademark of Pantone LLC.  
This project is not affiliated with or endorsed by Pantone.

