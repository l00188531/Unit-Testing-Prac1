from datetime import datetime
def is_valid_date(date_str):
    """
    Checks if the given date is valid and falls between 2020-01-01 and 2023-12-31.
    :param date_str: The date in string format (YYYY-MM-DD)
    :return: True if the date is valid and within the range, False otherwise
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        return start_date <= date <= end_date
    except ValueError:
        return False