def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(years_to_add+original_date.year);
    return result;