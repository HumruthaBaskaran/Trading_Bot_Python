import argparse
from bot.client import BybitClient
from bot.orders import place_limit_order,place_market_order,place_stop_limit_order
from bot.validators import validateOrderType,validateSide


API_KEY = "P9jkyWcol8jVdmIanR"
API_SECRET = "0x6UGS6KVtoKrZtoqixCCkUISnXsQJ00Xz2a"

def print_order_summery(args):
    print("\n========ORDER SUMMERY========")
    print("SYMBOL     :",args.symbol)
    print("SIDE       :",args.side)
    print("ORDER TYPE :",args.type)
    print("QUANTITY   :",args.qty)
    if args.type.lower() == "limit":
        print("PRICE   :",args.price)
    print("================================\n")

def print_order_responce(orderId,data):
    
    # print(data)
    status = data["orderStatus"]
    executedQty = data["cumExecQty"]
    avgPrice = data["avgPrice"]

    print("\n========ORDER RESPONCE========")
    print("ORDER ID       :",orderId)
    print("ORDER STATUS   :",status)
    print("ORDER QUANTITY :",executedQty)
    if avgPrice:
        print("AVERAGE PRICE  :",avgPrice)
    print("================================\n")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol",required=True)
    parser.add_argument("--side",required=True)
    parser.add_argument("--type",required=True)
    parser.add_argument("--qty",type=float,required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stopPrice", type=float)


    args = parser.parse_args()
    client = BybitClient(API_KEY,API_SECRET).getClient()

    try:
        validateSide(args.side)
        validateOrderType(args.type)
        print_order_summery(args)
        if args.type.lower() == "market":
            responce = place_market_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                qty=args.qty
            )
        elif args.type.lower() == "limit":
            responce = place_limit_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                qty=args.qty,
                price=args.price
            )
        elif args.type.lower() == "stop_limit":
            responce = place_stop_limit_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                qty=args.qty,
                price=args.price,
                stopPrice = args.stopPrice
            )
        
        orderId = responce['result']['orderId']

        order_info = client.get_open_orders(
            category = "linear",
            symbol = args.symbol,
            orderId=orderId

        )
        print_order_responce(orderId,order_info['result']['list'][0])

        print("✅ Order placed successfully")
    except ValueError as v:
        print("\u274c Invalid Input")
        print(v)
    except Exception as e:
        print("\n❌ Order failed")
        print("Error: ",e)

if __name__ == "__main__":
    main()

