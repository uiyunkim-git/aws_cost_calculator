

def LAMBDA_COST(requests,ram_usage_in_megabyte,runtime_in_millisecond,with_free_tier=True):
    total_cost = (runtime_in_millisecond/1000)*requests * (ram_usage_in_megabyte/1024)

    if with_free_tier:
        total_cost -= 400000
        if total_cost < 0:
            total_cost = 0
        requests -= 1000000
        if requests < 0:
            requests = 0


    total_cost = total_cost * 0.00001667
    total_cost += requests * (0.2 / 1000000)

    print(round(total_cost,2),"LAMBDA_COST")
    return round(total_cost,2)



if __name__ == '__main__':
    print(LAMBDA_COST(3000000,512,1000,with_free_tier=False))