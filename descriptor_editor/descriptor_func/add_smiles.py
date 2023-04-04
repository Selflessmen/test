smiles = {"цена": "💰Цена", "ткань": "🧶Ткань", "материал": "🧶Ткань", "цвет": "🎨Цвет", "размер": "📐Размер", "модель": "🛍Мод.", "мод": "🛍Мод.", "арт": "🛍Мод.", "🔻": "",
          "ціна": "💰Ціна", "тканина": "🧶Тканина", "матеріал": "🧶Тканина", "колір": "🎨Колір", "кольор": "🎨Кольор", "розмір": "📐Розмір", "мод ": "🛍Мод.",


          }
forbidden_words = {"модели":"", "моделі":""}

def replace_smiles(string):
    for words in forbidden_words:
        if words in string:
            string = string.replace(words, forbidden_words[words])

    lower_case = string.lower().strip()

    for i in smiles:
        if i in lower_case:
            lower_case = lower_case.replace(i, smiles[i])
    return lower_case


if "__main__" == "__name__":
    replace_smiles(string)

