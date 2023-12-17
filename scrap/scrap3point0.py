import requests
from bs4 import BeautifulSoup
import json
import re

def get_page_content(url):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, 'html.parser')

def get_recirc_links(href_value):
    ziyaret_edilen_sayfa = get_page_content(href_value)
    recirc_list = ziyaret_edilen_sayfa.find(id='tax-sc__recirc-list_1-0')

    if recirc_list:
        recirc_links = recirc_list.find_all('a')
        return [recirc_link.get('href') for recirc_link in recirc_links]
    return []

def clean_file_name(file_name):
    invalid_chars = r'<>:"/\|?*'
    cleaned_name = ''.join(c if c not in invalid_chars else '_' for c in file_name)
    return cleaned_name.strip()  # Satır sonu karakterlerini temizle

def write_to_json(data, file_path):
    cleaned_file_name = clean_file_name(file_path)
    # Remove "nutrition_facts" key from the dictionary
    data.pop("nutrition_facts", None)
    with open(cleaned_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def process_full_description(full_description):
    # Varsayılan değerleri ayarla
    name = ""
    amount = "Default Amount"
    unit_of_measure = ""

    # Başındaki sayıları ve sayıları takip eden kısmı ayırmak için regex kullan
    match = re.match(r'(\d+(\.\d+)?/\d+|\d+(\.\d+)?)\s*(.*)', full_description)
    if match:
        amount = match.group(1)
        # Check if there are words after the number
        if match.group(3):
            words_after_number = match.group(3).split(maxsplit=1)
            unit_of_measure = words_after_number[0]
            if len(words_after_number) > 1:
                name = words_after_number[1]

    return name, amount, unit_of_measure

    # Varsayılan değerleri ayarla
    name = ""
    amount = "Default Amount"
    unit_of_measure = ""

    # Başındaki sayıları ve sayıları takip eden kısmı ayırmak için regex kullan
    match = re.match(r'(\d+(\.\d+)?/\d+|\d+(\.\d+)?)\s*(.*)', full_description)
    if match:
        amount = match.group(1)
        # Check if there are words after the number
        if match.group(3):
            words_after_number = match.group(3).split(maxsplit=1)
            unit_of_measure = words_after_number[0]
            if len(words_after_number) > 1:
                name = words_after_number[1]

    return name, amount, unit_of_measure

# ...

def get_recipe_info(url):
    ziyaret_edilen_sayfa = get_page_content(url)

    title = ziyaret_edilen_sayfa.find(id='article-heading_1-0').get_text()
    description = ziyaret_edilen_sayfa.find(id='article-subheading_1-0').get_text()

    # İlgili id'ye sahip elementi bulun
    ingredients_list = ziyaret_edilen_sayfa.select('.mntl-structured-ingredients__list-item p')
    ingredients = []

    # Protein, fat, and carb information from the nutrition_facts list
    nutrition_facts_table = ziyaret_edilen_sayfa.select('.mntl-nutrition-facts-summary__table-body tr')
    nutrition_facts = [row.get_text(strip=True) for row in nutrition_facts_table]

    # Extract nutritional information from the nutrition_facts list
    for fact in nutrition_facts:
        if 'Calories' in fact:
            # Extract calories from the string and convert to float
            calories = float(fact.split('Calories')[0])
        elif 'Fat' in fact:
            # Extract fat from the string and convert to float
            fat = float(fact.split('gFat')[0])
        elif 'Carbs' in fact:
            # Extract carbs from the string and convert to float
            carb = float(fact.split('gCarbs')[0])
        elif 'Protein' in fact:
            # Extract protein from the string and convert to float
            protein = float(fact.split('gProtein')[0])

    # Malzemeleri işle ve listeye ekle
    for ingredient_element in ingredients_list:
        full_description = ingredient_element.get_text(strip=True)
        name, amount, unit_of_measure = process_full_description(full_description)

        # Extract additional information from the remaining words in full_description
        remaining_words = name.split()
        unit_of_measure += " " + remaining_words[0] if remaining_words else ''
        name = ' '.join(remaining_words[1:]) if len(remaining_words) > 1 else ''

        ingredient_data = {
            "fullDescription": full_description,
            "ingredients": {
                "name": name,
                "image": "Default Image"
            },
            "measure": {
                "amount": amount,
                "unitOfMeasure": unit_of_measure
            }
        }

        ingredients.append(ingredient_data)

    # ...

    # ...

    # Malzemeleri işle ve listeye ekle
    for ingredient_element in ingredients_list:
        full_description = ingredient_element.get_text(strip=True)
        name, amount, unit_of_measure = process_full_description(full_description)

        # Extract additional information from the remaining words in full_description
        remaining_words = name.split()
        unit_of_measure += " " + remaining_words[0] if remaining_words else ''
        name = ' '.join(remaining_words[1:]) if len(remaining_words) > 1 else ''

        ingredient_data = {
            "fullDescription": full_description,
            "ingredients": {
                "name": name,
                "image": "Default Image"
            },
            "measure": {
                "amount": amount,
                "unitOfMeasure": unit_of_measure
            }
        }

        ingredients.append(ingredient_data)

    # ...
    ziyaret_edilen_sayfa = get_page_content(url)

    title = ziyaret_edilen_sayfa.find(id='article-heading_1-0').get_text()
    description = ziyaret_edilen_sayfa.find(id='article-subheading_1-0').get_text()

    # İlgili id'ye sahip elementi bulun
    ingredients_list = ziyaret_edilen_sayfa.select('.mntl-structured-ingredients__list-item p')
    ingredients = []

    # Protein, fat, and carb information from the nutrition_facts list
    nutrition_facts_table = ziyaret_edilen_sayfa.select('.mntl-nutrition-facts-summary__table-body tr')
    nutrition_facts = [row.get_text(strip=True) for row in nutrition_facts_table]

    # Extract nutritional information from the nutrition_facts list
    for fact in nutrition_facts:
        if 'Calories' in fact:
            # Extract calories from the string and convert to float
            calories = float(fact.split('Calories')[0])
        elif 'Fat' in fact:
            # Extract fat from the string and convert to float
            fat = float(fact.split('gFat')[0])
        elif 'Carbs' in fact:
            # Extract carbs from the string and convert to float
            carb = float(fact.split('gCarbs')[0])
        elif 'Protein' in fact:
            # Extract protein from the string and convert to float
            protein = float(fact.split('gProtein')[0])

    # Initialize ingredients_list as an empty list
    ingredients_list = []

    # Malzemeleri işle ve listeye ekle
    for ingredient_element in ingredients_list:
        full_description = ingredient_element.get_text(strip=True)
        name, amount, unit_of_measure = process_full_description(full_description)

        # Extract additional information from the remaining words in full_description
        remaining_words = name.split()
        unit_of_measure += remaining_words[0] if remaining_words else ''
        name = ' '.join(remaining_words[1:]) if len(remaining_words) > 1 else ''

        ingredient_data = {
            "fullDescription": full_description,
            "ingredients": {
                "name": name,
                "image": "Default Image"
            },
            "measure": {
                "amount": amount,
                "unitOfMeasure": unit_of_measure
            }
        }

        ingredients.append(ingredient_data)

    # ...

    # ...

    # Malzemeleri işle ve listeye ekle
    for ingredient_element in ingredients_list:
        full_description = ingredient_element.get_text(strip=True)
        name, amount, unit_of_measure = process_full_description(full_description)

        # Extract additional information from the remaining words in full_description
        remaining_words = name.split()
        unit_of_measure += remaining_words[0] if remaining_words else ''
        name = ' '.join(remaining_words[1:]) if len(remaining_words) > 1 else ''

        ingredient_data = {
            "fullDescription": full_description,
            "ingredients": {
                "name": name,
                "image": "Default Image"
            },
            "measure": {
                "amount": amount,
                "unitOfMeasure": unit_of_measure
            }
        }

        ingredients.append(ingredient_data)

    # ...
    ziyaret_edilen_sayfa = get_page_content(url)

    title = ziyaret_edilen_sayfa.find(id='article-heading_1-0').get_text()
    description = ziyaret_edilen_sayfa.find(id='article-subheading_1-0').get_text()

    # İlgili id'ye sahip elementi bulun
    ingredients_list = ziyaret_edilen_sayfa.select('.mntl-structured-ingredients__list-item p')
    ingredients = []

    # Protein, fat, and carb information from the nutrition_facts list
    nutrition_facts_table = ziyaret_edilen_sayfa.select('.mntl-nutrition-facts-summary__table-body tr')
    nutrition_facts = [row.get_text(strip=True) for row in nutrition_facts_table]

    # Extract nutritional information from the nutrition_facts list
    for fact in nutrition_facts:
        if 'Calories' in fact:
            # Extract calories from the string and convert to float
            calories = float(fact.split('Calories')[0])
        elif 'Fat' in fact:
            # Extract fat from the string and convert to float
            fat = float(fact.split('gFat')[0])
        elif 'Carbs' in fact:
            # Extract carbs from the string and convert to float
            carb = float(fact.split('gCarbs')[0])
        elif 'Protein' in fact:
            # Extract protein from the string and convert to float
            protein = float(fact.split('gProtein')[0])

    # İlgili id'ye sahip elementi bulun
    ingredients_list = ziyaret_edilen_sayfa.select('.mntl-structured-ingredients__list-item p')
    ingredients = []

    # Malzemeleri işle ve listeye ekle
    for ingredient_element in ingredients_list:
        full_description = ingredient_element.get_text(strip=True)
        name, amount, unit_of_measure = process_full_description(full_description)

        ingredient_data = {
            "fullDescription": full_description,
            "ingredients": {
                "name": name,
                "image": "Default Image"
            },
            "measure": {
                "amount": amount,
                "unitOfMeasure": unit_of_measure
            }
        }

        ingredients.append(ingredient_data)

    recipe_data = {
        'title': title,
        'description': description,
        'ingredientsInTheRepice': ingredients,
        'materials': [],
        'preparationTime': 0,
        'vegan': False,
        'vegetarian': False,
        'glutenFree': False,
        'ketogenic': False,
        'vitamins': [],
        'calories': calories,
        'fat': fat,
        'carb': carb,
        'protein': protein
    }

    return recipe_data

URL = 'https://www.allrecipes.com/recipes-a-z-6735880'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"}

sayfa = get_page_content(URL)

# Tüm "loc link-list" sınıfına sahip elementleri bulma
link_list_elements = sayfa.find_all(class_="loc link-list")

# Her bir elementin içindeki <a> etiketlerini bulma ve href değerlerini kullanarak sayfaları ziyaret etme
for link_list_element in link_list_elements:
    a_elements = link_list_element.find_all('a')
    for a_element in a_elements:
        href_value = a_element.get('href')
        print(f"Processing: {href_value}")

        recirc_links = get_recirc_links(href_value)
        for recirc_link in recirc_links:
            print(f"Processing recirc link: {recirc_link}")
            recipe_info = get_recipe_info(recirc_link)
            json_file_path = f"{clean_file_name(recipe_info['title'])}.json"
            write_to_json(recipe_info, json_file_path)
            print(f"Recipe info written to: {json_file_path}")
