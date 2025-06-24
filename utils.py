def classify_stage(ef):
    if ef < 30:
        return "Severe"
    elif ef < 40:
        return "Moderate"
    elif ef < 50:
        return "Mild"
    else:
        return "Normal"
