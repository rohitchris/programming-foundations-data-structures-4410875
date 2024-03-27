user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    update_preferences_cleaned = {}

    # using python list comprehension 
    update_preferences_cleaned = {key: value for key, value in user_pref.items() if value is not None}


    # for key, value in user_preferences.items():
    #     if value is not None: 
    #         update_preferences_cleaned[key] = value

    return update_preferences_cleaned


print(update_preferences(user_preferences))
