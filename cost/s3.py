def S3_COST_STORED_AMOUNT(gigabyte_per_month,with_free_tier=True):

    def cost_until(cost,until,rest):
        if rest > until:
            total_cost = until * cost
            rest -= until
        else:
            total_cost = rest * cost
            rest = 0
        return total_cost, rest

    total_cost = 0

    if with_free_tier:
        cost,gigabyte_per_month = cost_until(0,51200,gigabyte_per_month)
        total_cost += cost
    else:
        cost,gigabyte_per_month = cost_until(0.025,51200,gigabyte_per_month)
        total_cost += cost

    cost,gigabyte_per_month = cost_until(0.024,460800,gigabyte_per_month)
    total_cost += cost

    cost,gigabyte_per_month = cost_until(0.023,gigabyte_per_month+1,gigabyte_per_month)
    total_cost += cost
    print(total_cost, "S3_COST_STORED_AMOUNT")
    return total_cost

def S3_COST_OUTBOUND_TRAFFIC(gigabyte_per_month,with_free_tier=True):

    def cost_until(cost,until,rest):
        if rest > until:
            total_cost = until * cost
            rest -= until
        else:
            total_cost = rest * cost
            rest = 0
        return total_cost, rest

    total_cost = 0

    if with_free_tier:
        gigabyte_per_month -= 15

    cost,gigabyte_per_month = cost_until(0,1,gigabyte_per_month)
    total_cost += cost

    cost,gigabyte_per_month = cost_until(0.126,10239,gigabyte_per_month)
    total_cost += cost

    cost,gigabyte_per_month = cost_until(0.122,40960,gigabyte_per_month)
    total_cost += cost

    cost,gigabyte_per_month = cost_until(0.117,102400,gigabyte_per_month)
    total_cost += cost

    cost,gigabyte_per_month = cost_until(0.108,gigabyte_per_month+1,gigabyte_per_month)
    total_cost += cost
    print(total_cost, "S3_COST_OUTBOUND_TRAFFIC")
    return total_cost

def S3_COST_PER_PUT_REQUEST(num_request,with_free_tier=True):

    if with_free_tier:
        num_request -= 2000

    if num_request >= 0:
        total_cost = (0.0045 / 1000) * num_request
        print(total_cost, "S3_COST_PER_PUT_REQUEST")
        return total_cost
    else:
        print(0, "S3_COST_PER_PUT_REQUEST")
        return 0

def S3_COST_PER_GET_REQUEST(num_request,with_free_tier=True):

    if with_free_tier:
        num_request -= 20000

    if num_request >= 0:
        total_cost = (0.00035  / 1000) * num_request
        print(total_cost, "S3_COST_PER_GET_REQUEST")
        return total_cost
    else:
        print(0, "S3_COST_PER_GET_REQUEST")
        return 0

if __name__ == '__main__':
    print(S3_COST_PER_GET_REQUEST(10000,False)+S3_COST_PER_PUT_REQUEST(10000,False))