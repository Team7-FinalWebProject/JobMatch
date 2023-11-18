def apply_salary_threshold(min_salary, max_salary, threshold):
    try:
        min_salary,max_salary, threshold = float(min_salary),float(max_salary), float(threshold)
    except:
        try:
            min_salary,max_salary, threshold = sum(map(ord, min_salary)),sum(map(ord, max_salary)), sum(map(ord, threshold))
        except:
            return 0, 0

    fraction = threshold / 100
    multiplyer = fraction + 1

    swap = lambda mi,ma : (ma,mi) if mi > ma else (mi,ma)
    min_salary, max_salary = swap(min_salary, max_salary)

    def decay(min_salary, multi):
        decayed_salary = (min_salary / multi) if multi > 0 else 0
        return max(0,min(2147483647,int(round(decayed_salary))))

    def growth(max_salary, multi):
        growed_salary = (max_salary * multi) if multi < 2147483647 else 2147483647
        return max(0,min(2147483647,int(round(growed_salary))))

    modified_min_salary = decay(min_salary, multiplyer) 
    modified_max_salary = growth(max_salary, multiplyer)

    modified_min_salary, modified_max_salary = swap(modified_min_salary, modified_max_salary)

    return modified_min_salary, modified_max_salary