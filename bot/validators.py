def validateSide(side):
    if side.lower() not in ['buy','sell']:
        raise ValueError("Invalid Side. MUST be Buy or Sell")

def validateOrderType(type):
    if type.lower() not in ['market','limit','stop_limit']:
        raise ValueError("Invalid Order Type. MUST be  Market or Limit or Stop_Limit")