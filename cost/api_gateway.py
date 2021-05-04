

def API_GATEWAY_REST_REQUEST(requests,with_free_tier=True):

    if with_free_tier:
        requests -= 1000000

    def cost_until(cost,until,rest):
        if rest > until:
            total_cost = until * cost
            rest -= until
        else:
            total_cost = rest * cost
            rest = 0

        return total_cost, rest

    total_cost = 0


    cost,requests = cost_until((3.50/1000000),333000000,requests)
    total_cost += cost

    cost,requests = cost_until((3.19/1000000),667000000,requests)
    total_cost += cost

    cost,requests = cost_until((2.71/1000000),19000000000,requests)
    total_cost += cost

    cost,requests = cost_until((1.72/1000000),requests+1,requests)
    total_cost += cost

    print(total_cost,"API_GATEWAY_REST_REQUEST")
    return total_cost


if __name__ == '__main__':
    print(API_GATEWAY_REST_REQUEST(5000000,with_free_tier=False))