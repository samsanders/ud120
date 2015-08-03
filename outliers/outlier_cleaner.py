#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    errors = []

    for i in range(0, len(predictions)):
        errors.append(abs(predictions[i][0] - net_worths[i][0]))

    errors = sorted(errors)
    cutoff = errors[int(.90 * len(errors))]

    for p in range(0, len(predictions)):
        if abs(predictions[p] - net_worths[p]) < cutoff:
            cleaned_data.append((ages[p], net_worths[p], predictions[p] - net_worths[p]))

    
    return cleaned_data

