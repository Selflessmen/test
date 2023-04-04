import re
from descriptor_editor.descriptor_func.Remove_emoji import remove_all_emoji
from descriptor_editor.descriptor_func.Clothes_lib import clothes_items
from descriptor_editor.descriptor_func.Viber_remove_smiles import remove_viber_smiles
from descriptor_editor.descriptor_func.Telegram_remove_smiles import remove_telegram_smiles
from descriptor_editor.descriptor_func.Keywords_to_remove import remove_all_keywords
from descriptor_editor.descriptor_func.add_smiles import replace_smiles
from descriptor_editor.db import DataBase

db = DataBase("database.db")

def description_creater(description: str, manofact) -> str:
    smile = str(db.get_smile(manofact))
    smile += f"Опт, колір та розмір на вибір\n💙💛viber://chat?number=+380633602671"
    smile = smile.replace("(", "")
    smile = smile.replace(")", "")
    smile = smile.replace("'", "")
    smile = smile.replace(",", "")
    if not isinstance(description, str):
        return

    """Separate with loops string from double|tripple spaces"""
    lower_case = ""
    for i in description.split(" "):
        if i != "":
            lower_case += i + " "

    """Create the universal string 'lower_case' for comfortable using in program"""
    lower_case = lower_case.lower()
    lower_case = remove_telegram_smiles(lower_case)
    lower_case = remove_all_emoji(lower_case)
    lower_case = remove_viber_smiles(lower_case)

    """Creating variable for name of product"""
    name = clothes_items(lower_case.title()).split()
    for item in name:
        if "🔻" in item:
            name = item.strip(",!")
            break
        else:
            name = "🔻Блуза"

    """Creating variable for model of product"""
    mod = remove_all_keywords(lower_case)
    mod = replace_smiles(mod)
    for item in mod.split("\n"):
        if "🛍" in item:
            mod = item.strip()
            break
        else:
            mod = "🛍Мод: 2807"

    """Creating variable for size of product"""
    size = remove_all_keywords(lower_case)
    size = replace_smiles(size)
    for item in size.split("\n"):
        item = item.strip()
        if "📐" in item:
            size = item
            break
        else:
            size = "📐Розмір універсальний"

    """Creating variable for color of product"""
    color = replace_smiles(lower_case)
    for item in color.split("\n"):
        item = item.strip()
        if "🎨" in item and item.startswith("🎨"):
            color = item.split(",")
            color = ",".join(color).strip()
            color = color.replace("Цвета", "Цвет")
            break
        else:
            color = "🎨Колір на фото"

    """Creating variable for 'clothe' of product"""
    clothe = remove_all_keywords(lower_case)
    clothe = replace_smiles(clothe)
    for item in clothe.split("\n"):
        if "🧶" in item:
            clothe = item.strip()
            break
        else:
            clothe = "🧶Гарна якість"

    """Creating and find the price of our product"""
    price = replace_smiles(lower_case)
    for item in price.split("\n"):
        if "💰" in item:
            price = item.strip()
            break

        elif "💰" not in item:
            result = price.split("\n")
            for price in result:
                if "грн" in price:
                    result = price
                    break
                elif "гр" in price:
                    result = price

            try:
                num_res = re.findall("\d*", result)

                num_res = int("".join(num_res)) + 40
                price = f"💰Ціна: {num_res} грн"
            except:
                price = "💰Ціна в лс"
            break
        else:
            price = "💰Ціна в лс"


    """Creating the result variable for consistent main description"""
    result = f"{name}\n{mod}\n{size}\n{color}\n{clothe}\n{price}"

    """Creating other variable for additional description"""

    dop_result = remove_telegram_smiles(remove_all_keywords(result.lower().strip())).split("\n")
    some = remove_telegram_smiles(remove_all_keywords(lower_case.lower()).strip()).split("\n")
    other = ""
    for add in some:
        if add.startswith("ціна") or add.startswith("цена"):
            add = ""
        if "грн" in add:
            add = ""
        add = add.replace("модель", "мод")
        add = add.replace("матеріал", "тканина")
        if add.startswith("тканина"):
            add = ""
        add = add.strip()
        if add not in dop_result and add != "":
            other += f"▪{add.capitalize()}\n"
    if other:
        """Making the concatination of result + some additional description if we need"""

        return f"{result}\n{'-' * 20}\n💬Додатковий опис:\n{'-' * 20}\n{other}{'-' * 20}\n{smile}"
    return f"{result}\n{'-' * 20}\n{smile}"

#
# print(description_creater("""Новинка 🌷🌷🌷🌷🌷
# Сукня
# Модель № 7276-1
# ❗️ОБМЕЖЕНА КІЛЬКІСТЬ ❗️
# Ціна : 270 грн.
# ЯКІСТЬ ВІДМІННА
# Розмір : 46-48; 50-52; 54-56; 58-60
# Тканина : креп - костюмка
# ГАРНА РОЗТЯЖНІСТЬ
# Довжина сукні : 118 см.
# Довжина рукава : 66 см.
# Стильна , елегантна сукня . Тканина приємна на дотик , високої якості , не кашлатиться . Спідниця сукні пишного покрою , талія на резинці ,рукав на резинці ,пояс йде в комплекті з основної тканини"""))
