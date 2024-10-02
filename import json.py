# Импорт необходимых модулей
import json
import pandas as pd

def load_anime_list():
    """
    Загружает список аниме из JSON-файла и преобразует его в DataFrame pandas.
    
    Returns:
        pandas.DataFrame: Таблица с данными о списках аниме.
    """
    try:
        # Чтение данных из JSON-файла
        with open("anime-list.json", 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Преобразование данных в DataFrame
        df = pd.DataFrame(data)
        
        return df
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    anime_df = load_anime_list()
    
    if anime_df is not None:
        # Вывод заголовков таблицы
        print("\nЗаголовки таблицы:")
        print(anime_df.columns.tolist())
        
        # Вывод информации о DataFrame
        print("\nИнформация о DataFrame:")
        print(anime_df.info())
        
        # Вывод первой строки таблицы с форматированием
        print("\nПервая строка таблицы с форматированием:")
        print(anime_df.iloc[0].apply(lambda x: f"{x:.2f}" if isinstance(x, float) else str(x)))
        
        # Вывод первых нескольких строк таблицы
        print("\nПервые несколько строк таблицы:")
        print(anime_df.head())
        
        # Вывод статистики для числовых столбцов
        print("\nСтатистика для числовых столбцов:")
        print(anime_df.describe())
        
        # Вывод всего содержимого DataFrame
        print("\nПолное содержимое DataFrame:")
        print(anime_df.to_string(index=False))
        
        # Подсчет общего количества titles
        total_titles = len(anime_df['title'])
        print(f"\nОбщее количество titles: {total_titles}")
    else:
        print("Не удалось загрузить список аниме.")

if __name__ == "__main__":
    main()