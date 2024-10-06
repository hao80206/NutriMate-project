import re


def search_data(df, keyword):
    # Make sure the column name is correct
    descs = df["food"]
    loc = []
    for item in descs:
        if re.search(keyword, item, re.IGNORECASE):
            loc.append(True)
        else:
            loc.append(False)
    return loc


def filter_nutrients(df, nutrient_name, nutrient_level, min_value_str, max_value_str):
    # Check if nutrient name is provided
    if nutrient_name in df.columns:  # Ensure nutrient name is valid
        # Check if both min and max values are provided
        if min_value_str and max_value_str:  # Both values are provided
            min_value = float(min_value_str)  # Convert to float
            max_value = float(max_value_str)  # Convert to float
            # Filter based on nutrient range
            nutrient = df[nutrient_name]
            range_filter = (nutrient >= min_value) & (nutrient <= max_value)
            df = df.loc[range_filter]
        # If min or max are not provided, filter by level
        elif nutrient_level:
            nutrient_max = df[nutrient_name].max()
            low_threshold = nutrient_max * 0.33
            mid_threshold = nutrient_max * 0.66

            if nutrient_level == 'Low':
                df = df[df[nutrient_name]] < low_threshold
            elif nutrient_level == 'Mid':
                df = (df[df[nutrient_name]] >= low_threshold) & (df[nutrient_name] <= mid_threshold)
            elif nutrient_level == 'High':
                df = df[df[nutrient_name]] > mid_threshold
    return df
